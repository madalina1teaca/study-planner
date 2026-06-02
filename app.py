# importarea funcțiilor și claselor necesare din Flask

## Flask - creează aplicația web

### render_template - afișează paginile HTML
### request - preia datele trimise prin formulare
### redirect - redirectționează către altă pagină
### session - reține datele utilizatorului autentificat

from flask import Flask, render_template, request, redirect, session


# importarea pymysql pentru conectarea aplicației la baza de date mysql
import pymysql

# inițializează  aplicația Flask
app = Flask(__name__)

# cheia folosită pentru gestionarea sesiunilor
app.secret_key = "cheie_secreta_proiect"

# realizează conexiunea la baza de date
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Madalina1",
        database="study_planner",
        cursorclass=pymysql.cursors.DictCursor
    )

# ruta principală - pagina de start
@app.route("/")
def home():
    return render_template("index.html")

# ruta de înregistrare 
# GET - afișează formularul
@app.route("/register", methods=["GET", "POST"])
def register():

    # POST - salvează datale în baza de date
    if request.method == "POST":
        
        # preia datele introduse în formular
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # deschide conexiunea  la baza de date
        connection = get_db_connection()
        cursor = connection.cursor()

        # SQL - inserarea unui utlizator nou
        sql = """
        INSERT INTO users (username, email, password)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (username, email, password))

        # salvează modificările în baza de date
        connection.commit()

        # închide conexiunea
        cursor.close()
        connection.close()

        # redirecționează către pagina de login
        return redirect("/login")

    return render_template("register.html")

# ruta de autentificare
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # preia emailul și parola din formularul de login
        email = request.form["email"]
        password = request.form["password"]

        # deschide conexiunea la baza de date
        connection = get_db_connection()
        cursor = connection.cursor()

        # caută utilizatorul ce se potrivește cu emailul și parola introdusă 
        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )

        # returnează primul utilizator gășit, dacă acesta există
        ### dacă nu - None
        user = cursor.fetchone()

        
        # închide conexiunea
        cursor.close()
        connection.close()

        if user:
            # dacă utilizatorul există salvează în sesiune id-ul și username-ul
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            
            # după autentificarea reușită redirecționează la pagina de start
            return redirect("/dashboard")
        else:
            # afișează un mesaj dacă datele sunt greșite
            return "Email sau parolă greșită!"

    # dacă metoda este GET -  se afișează pagina de login
    return render_template("login.html")

# ruta pentru dashboard
@app.route("/dashboard")
def dashboard():

    # utilizator nelogat - redirecționează la pagina de login
    if "user_id" not in session:
        return redirect("/login")

    # deschide conexiunea la baza de date
    connection = get_db_connection()
    cursor = connection.cursor()

    # selectează task-urile utilizatorului
    cursor.execute(
        "SELECT * FROM tasks WHERE user_id = %s",
        (session["user_id"],)
    )

    # preia toate taskurile găsite
    tasks = cursor.fetchall()

    # închide conexiunea
    cursor.close()
    connection.close()

    # trimite lista taskurilor către pagina de start - dashboard
    return render_template("dashboard.html", tasks=tasks)

# ruta de adăugare a unui task nou
@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    # verifică dacă utilizatorul este autentificat
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        
        # preia datele introduse în formulare de adăugare a unui task nou
        title = request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        status = request.form["status"]

        # deschide conexiunea cu baza de date
        connection = get_db_connection()
        cursor = connection.cursor()

        # inserează taskul în baza de date
        cursor.execute(
            """
            INSERT INTO tasks (user_id, title, description, deadline, status)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (session["user_id"], title, description, deadline, status)
        )

        # salvează modificările
        connection.commit()

        # închide conexiunea
        cursor.close()
        connection.close()

        # revine la dashboard după adăugare
        return redirect("/dashboard")

    # dacă metoda este GET - afișează formularul de adăugare a unui task
    return render_template("add_task.html")


# ruta de ștergere a unui task
@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):

    # verifică dacă utilizatorul este autentificat
    if "user_id" not in session:
        return redirect("/login")

    # deschide conexiunea la baza de date
    connection = get_db_connection()
    cursor = connection.cursor()

    # șterge taskul doar dacă aparține utilizatorului logat
    cursor.execute(
        "DELETE FROM tasks WHERE id = %s AND user_id = %s",
        (task_id, session["user_id"])
    )

    # salvează modificările
    connection.commit()
    
    # închide conexiunea
    cursor.close()
    connection.close()

    # redirecionează la bashboard
    return redirect("/dashboard")

# ruta pentru editarea taskurilor
@app.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):

    # verifică dacă utilizatorul este autentificat
    if "user_id" not in session:
        return redirect("/login")

    # deschide conexiunea la baza de date
    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == "POST":
        
        # preia noile date ale taskului introduse în formular
        title = request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]
        status = request.form["status"]

        # actualizează taskul selectat în baza de bate
        cursor.execute(
            """
            UPDATE tasks
            SET title = %s, description = %s, deadline = %s, status = %s
            WHERE id = %s AND user_id = %s
            """,
            (title, description, deadline, status, task_id, session["user_id"])
        )

        # salvează modificările
        connection.commit()

        # închide conexiunea
        cursor.close()
        connection.close()

        # redirecționează către dashboard după terminarea editării
        return redirect("/dashboard")

    # metoda GET - caută taskul care trebuie editat
    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s AND user_id = %s",
        (task_id, session["user_id"])
    )

    # preia taskul găsit
    task = cursor.fetchone()

    # închide conexiunea
    cursor.close()
    connection.close()

    # trimite taskul către pagina de editare a taskului
    return render_template("edit_task.html", task=task)

# ruta de logout
# șterege toate datele sesiunii și trimite la pagina de login 
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ruta de testare pentru verificarea conexiunii la baza de date
@app.route("/test-db")
def test_db():
    connection = get_db_connection()
    connection.close()
    return "Conexiunea la baza de date funcționează!"


# pornește aplicația Flask în modul debug
if __name__ == "__main__":
    app.run(debug=True)