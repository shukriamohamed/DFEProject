CREATE TABLE doctor  (
doc_id INT PRIMARY KEY,
doc_forname VARCHAR(20),
doc_surname VARCHAR(20),
);


CREATE TABLE owner  (
own_id INT PRIMARY KEY,
own_forname VARCHAR(20),
own_surname VARCHAR(20),
);

CREATE TABLE pet  (
pet_id INT PRIMARY KEY,
pet_name VARCHAR(20),
FOREIGN KEY(own_id) REFERENCES owner(own_id) ON DELETE CASCADE,
FOREIGN KEY(doc_id) REFERENCES doctor(doc_id) ON DELETE CASCADE
);