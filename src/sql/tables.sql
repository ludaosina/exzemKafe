CREATE TABLE IF NOT EXISTS beauty_salon (
customer_id INTEGER PRIMARY KEY,
FIO_customers VARCHAR(50) NOT NULL,
quantity INTEGER,
service VARCHAR(50));

CREATE TABLE IF NOT EXISTS employee (
id INTEGER PRIMARY KEY,
FIO VARCHAR(50) NOT NULL,
Address VARCHAR(50),
sale_of_cosmetics  INTEGER NOT NULL,
number INTEGER UNIQUE,
experience INTEGER);

CREATE TABLE IF NOT EXISTS customers (
id INTEGER PRIMARY KEY,
FIO VARCHAR(50) NOT NULL,
Address VARCHAR(50),
number INTEGER UNIQUE);

CREATE TABLE IF NOT EXISTS sale_of_cosmetics (
id INTEGER PRIMARY KEY,
client VARCHAR(50),
date_of_purchase DATE,
quantity INTEGER,
cost_per_piece INTEGER NOT NULL,
total_cost INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS cosmetic (
id INTEGER PRIMARY KEY,
title VARCHAR(50) NOT NULL,
cost INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS category_of_employees (
id INTEGER PRIMARY KEY,
chart VARCHAR(50),
post VARCHAR(50));

CREATE TABLE IF NOT EXISTS procedures (
id INTEGER PRIMARY KEY,
title VARCHAR(100) NOT NULL,
cost INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS services (
id INTEGER PRIMARY KEY,
cost REAL,
date TEXT,
masters VARCHAR(50) NOT NULL);

CREATE TABLE IF NOT EXISTS records (
id INTEGER PRIMARY KEY,
client_id INTEGER NOT NULL,
employee_id INTEGER NOT NULL,
service_id INTEGER NOT NULL,
appointmentDate DATE,
appointmentTime TEXT,
FOREIGN KEY(client_id)
    REFERENCES customers(id)
    ON DELETE CASCADE ON UPDATE NO ACTION,
FOREIGN KEY(employee_id)
    REFERENCES employee(id)
    ON DELETE CASCADE ON UPDATE NO ACTION,
FOREIGN KEY(service_id)
    REFERENCES services(id)
    ON DELETE CASCADE ON UPDATE NO ACTION);

CREATE TABLE IF NOT EXISTS reviews (
id INTEGER PRIMARY KEY,
client_id INTEGER NOT NULL,
employee_id INTEGER NOT NULL,
rating INTEGER NOT NULL,
comment VARCHAR(50),
FOREIGN KEY(client_id)
    REFERENCES customers(id)
    ON DELETE CASCADE ON UPDATE NO ACTION,
FOREIGN KEY(employee_id)
    REFERENCES employee(id)
    ON DELETE CASCADE ON UPDATE NO ACTION);