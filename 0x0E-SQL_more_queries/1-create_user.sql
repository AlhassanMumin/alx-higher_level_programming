-- create the user user_od_1 with all privileges.

CREATE USER
   IF NOT EXISTS 'user_od_1'@'localhost'
   IDENTIFIED BY 'user_od_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_od_1'@'localhost';
