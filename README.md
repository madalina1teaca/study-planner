# Study Planner

> **Study Planner** este o aplicație web dezvoltată pentru gestionarea și organizarea taskurilor personale.

> Utlizatorii își pot crea un cont, se pot autentifica și își pot administra propriile activități prin operații de tip CRUD (Create, Read, Update, Delete).

> Aplicația a fost realizată în cadrul proiectului pentru disciplina **Tehnologii Web**

## Funcționalități
* Înregistrarea utilizatorului
* Autentificarea utilizatorului
* Gestionarea sesiunilor
* Vizualizarea taskurilor
* Adăugarea unui task nou
* Editarea taskurilor
* Ștergerea taskurilor
* De-logarea
* Interfață 'responsive'
* Funcționalități JavaScript și jQuery

## Tehnologii utilizate
* HTML
* CSS3
* JavaScript
* jQuery
* Python Flask
* MySQL
* Railway (Deployment)
* Github

## Structura proiectului
```text
study-planner/
|
|- app.py
|- database.sql
|- requirements.txt
|- Procfile
|
|- static/
|   |- css/
|   |   |- style.css
|   |
|   |- js/
|       |- script.js
|
|- templates/
|   |- index.html
|   |- dashboard.html
|   |- register.html
|   |- login.html
|   |- add_task.html
|   |- edit_task.html
|
|- README.md
```

## Baza de date
Aplicația utilizează două tabele:

### users
| Câmp          | Tip           |
| ------------- |:-------------:|
| id            | `INT`         |
| username      | `VARCHAR(100)`|
| email         | `VARCHAR(100)`|
| password      | `VARCHAR(255)`|


### tasks
| Câmp          | Tip           |
| ------------- |:-------------:|
| id            | `INT`         |
| user_id       | `INT`         |
| titke         | `VARCHAR(100)`|
| description   | `TEXT`        |
| deadline      | `DATE`        |
| status        | `VARCHAR(50)` |

Relația dintre tabele este de tip **One-to-Many (1)**.


## Instalare locală
1. Clonează repository-ul:
``` git clone <rhttps://github.com/madalina1teaca/study-planner.git>```
2. Creează și activează mediul virtual;
``` 
python -m venv venv 
source venv/bin/activate 
```
3. Instalează dependențele:
``` pip install -r requirements.txt ```
4. Creează baza de data folosind fișierul:
``` database.sql```
5. Rulează aplicația:
``` python app.py```

## Deployment
Aplicația este publicată online folosind **Railway** și poate fi accesată prin linkul:
[Study Planner](https://web-production-d55a6.up.railway.app)

Repository **GitHub**:
[Git Repo](https://github.com/madalina1teaca/study-planner)


## Autor

**Madalina Teaca**

Proiect realizat pentru disciplina **Tehnologii Web**.