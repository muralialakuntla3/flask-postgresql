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
## Create database and Table for application
```
CREATE DATABASE demo_app
\c demo_app
\dt
```
### Create Table
```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    number VARCHAR(20)
);
```
## Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
## Install required Python packages
```
pip install flask psycopg2
```
## Run app
```
python3 app.py 
```
![image](https://github.com/user-attachments/assets/b1c14f42-373e-40b4-93f1-0968ae38b8d9)






