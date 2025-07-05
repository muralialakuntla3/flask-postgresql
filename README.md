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
![image](https://github.com/user-attachments/assets/7bc3bfa8-ced0-4278-85be-e3573166ad69)

### check the table and table data
```
\dt
SELECT * FROM users:
exit
```
<img width="272" alt="image" src="https://github.com/user-attachments/assets/8e1ab403-53ca-4007-88c4-55579e8745b7" />

## download the code into server and run the application
```
ls
git clone https://github.com/muralialakuntla3/flask-postgresql.git
cd flask-postgresql
ls
```
<img width="575" alt="image" src="https://github.com/user-attachments/assets/7ac84dcd-2080-4167-959a-948c4e6c4de4" />

## Install dependencies
```
sudo apt install python3-flask -y 
sudo apt install python3-psycopg2 -y
```
![image](https://github.com/user-attachments/assets/e78d6905-5525-4ea2-8443-6a4597455d00)
![image](https://github.com/user-attachments/assets/292ce48a-5c79-40b8-a284-a018586bcd75)
## update database details in app.py file
```
vi app.py
```
![image](https://github.com/user-attachments/assets/ab4ab24c-6c93-4c69-bacb-882eafd63b09)

## run application
```
python3 app.py 
```
![image](https://github.com/user-attachments/assets/1dfc3716-5405-4572-9cd1-0d987dfb3a62)

## check the application
- update the network security group to allow port 5000
<img width="946" alt="image" src="https://github.com/user-attachments/assets/7c4af6d4-2a15-4be9-9cf0-cbe8c68b5819" />
- browse the application
  - public-ip:5000
![image](https://github.com/user-attachments/assets/b1c14f42-373e-40b4-93f1-0968ae38b8d9)

## check the database
- connect the database and verify the data
```
psql -h myappdatabase.postgres.database.azure.com -p 5432 -U adminuser demo_app
\dt
SELECT * FROM users;
```

<img width="694" alt="image" src="https://github.com/user-attachments/assets/ffdb1934-90c2-4b5a-975b-add34a132748" />



