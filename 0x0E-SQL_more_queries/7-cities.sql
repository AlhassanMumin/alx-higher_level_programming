-- create a table states in database hbtn_0d_usa
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE
	IF NOT EXISTS hbtn_0d_usa.cities (
		id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
		state_id INT NOT NULL,
		name  VARCHAR(256) NOT NULL,
		FOREIGN KEY(state_id)
		REFERENCES hbtn_0d_usa.states (id) 
		);
