-- crează baza de date a aplicației dacă nu există deja
CREATE DATABASE IF NOT EXISTS study_planner;

-- selectează baza de date pentru a fi utilizată
USE study_planner;

-- creează tabelul utlizatorilor dacă acesta nu există deja
CREATE TABLE IF NOT EXISTS users (
    -- identificatorul unic
    id INT AUTO_INCREMENT PRIMARY KEY,

    -- username-ul utilizatorului
    username VARCHAR(100) NOT NULL,

    -- adresa de email a utilizatorului - unică pentru a nu exista mai mulți utilizatori cu aceeași adresă
    email VARCHAR(100) NOT NULL UNIQUE,
    
    -- parola utilizatorului
    password VARCHAR(255) NOT NULL
);


-- creează tabelul cu taskuri dacă acesta nu există deja
CREATE TABLE IF NOT EXISTS tasks (
    
    -- identificatorul unic pentru fiecare task
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- identificatorul către utilizatorul care a creat taskul
    user_id INT,
    
    -- titlul taskului
    title VARCHAR(100) NOT NULL,
    
    -- descrierea taskului
    description TEXT,
    
    -- data limită / deadline-ul taskului
    deadline DATE,
    
    -- statusul taskului: To Do | În lucru | Finalizat
    status VARCHAR(50),
    
    -- cheia externă pentru legătura task - utilizator
    FOREIGN KEY (user_id) REFERENCES users(id)
);