DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    surname TEXT,
    date_of_birth DATETIME,
    current_location TEXT
);
