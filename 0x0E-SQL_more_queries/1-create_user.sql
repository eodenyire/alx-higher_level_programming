<<<<<<< HEAD
--This script creates the MySQL server user user_0d_1
=======
-- Creates the mysql useruser_0d_1
>>>>>>> 09272d6854d0b75b429a7f3041ac9dcee26222ac
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
