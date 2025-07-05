# flask-postgresql Deployment
## Install PostgreSql 
```
sudo apt update
sudo apt install curl ca-certificates
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
. /etc/os-release
sudo sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list"
sudo apt update
sudo apt -y install postgresql-16
```
## Connect to Database
```
psql -h azure2501db.postgres.database.azure.com -p 5432 -U adminuser postgres
```
<img width="602" alt="image" src="https://github.com/user-attachments/assets/efe3b911-4a6f-4cab-b5b6-b186070378ef" />

## Create database and Table for application
```
CREATE DATABASE demo_app;
\c demo_app
\dt
```
<img width="501" alt="image" src="https://github.com/user-attachments/assets/76c16bf1-ed0b-4529-a67d-959080a35c4e" />

### Create Table
```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    number VARCHAR(20)
);
```
## download the code into server anfd run the application
```
git clone https://github.com/muralialakuntla3/flask-postgresql.git
cd flask-postgresql
```
## Install dependencies
```
sudo apt install python3-flask
sudo apt install python3-psycopg2
```
## run application
```
python3 app.py 
```
![image](https://github.com/user-attachments/assets/b1c14f42-373e-40b4-93f1-0968ae38b8d9)






