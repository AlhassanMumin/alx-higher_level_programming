-- create user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' 
IDENTIFIED WITH caching_sha2_password 
BY 'user_0d_1_pwd';
GRANT SELECT 
ON *.* 
TO 'user_0d_1'@localhost;
