CREATE TABLE users (
	id VARCHAR(20) PRIMARY KEY,
	password_hash TEXT NOT NULL,
	role VARCHAR(20) NOT NULL DEFAULT 'user'
);

INSERT INTO users (id,password_hash,role)
VALUES ('admin','123456789','admin');

SELECT * FROM users;