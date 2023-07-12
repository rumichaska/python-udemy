-- Para usar una base de datos
USE udemy_db;

CREATE TABLE Usuario(
	id INT,
    email VARCHAR(255),
    username VARCHAR(50)
);

-- Para eliminar una tabla
-- DROP TABLE Usuario;

-- Para agregar un campo
ALTER TABLE Usuario ADD edad INT;

-- Para eliminar un campo
-- ALTER TABLE Usuario DROP COLUMN edad;

-- Para modificar una columna
ALTER TABLE Usuario MODIFY COLUMN email VARCHAR(50);

-- Ingresar registros, puede ocurrir error cuando no se tiene llave primaria como autoincremental
INSERT INTO Usuario(email, username) VALUES ("nicolas@correo.com", "Ricolas");

-- Eliminar registros, LIMIT 1 se usa cuando no se ha establecido una llave primaria
DELETE FROM Usuario WHERE email = "nicolas@correo.com" LIMIT 1;

-- Agregar llave primaria
ALTER TABLE Usuario ADD PRIMARY KEY (id);

-- Indicar que la columna id es autoincremental
ALTER TABLE Usuario MODIFY COLUMN id INT AUTO_INCREMENT;

-- Mostrar table, * indica todas las columnas
SELECT * FROM Usuario;

-- Agregar otro usuario
INSERT INTO Usuario(email, username, edad) VALUES ("castrogda@gmail.com", "Diego", 33);
INSERT INTO Usuario(email, username, edad) VALUES ("dcastro@gmail.com", "Arturo", 28);
INSERT INTO Usuario(email, username, edad) VALUES ("acg.castro@gmail.com", "Juan", 12);

-- Filtrar información a mostrar
SELECT * FROM Usuario WHERE email = "castrogda@gmail.com";
SELECT * FROM Usuario WHERE edad > 30;

-- Actualizar información de registros
UPDATE Usuario SET edad = 32 WHERE id = "3";

-- Eliminar registros
DELETE FROM Usuario WHERE id = "2";