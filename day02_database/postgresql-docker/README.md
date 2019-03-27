# BEM-workshop
PostgreSQL Docker by Wisit Tipchuen

## Install Docker on Windows
* https://docs.docker.com/docker-for-windows/install/?fbclid=IwAR2rnhapojanHBsAuKgfhEmm7uBwsizlfLaFmKXRNbBB7aFfvPAAnxLUoUE
* https://www.smarthomebeginner.com/install-docker-on-windows-10/?fbclid=IwAR0e0Tz4PNWvdevd4F8ulKCE9bIf7mzoBZkX2zWaQJ0T1vrAcWRbjCeZBEo

## Start container
```
docker-compose up -d
```

Connect to localhost
Port 5432 สำหรับ db ครับ 
User: postgres
Password: password


## Stop container
```
docker-compose down
```

## Add External Data
Put files in `data` folder. These files will be included in the container. Use `docker-compose exec <name-in-yml> sh` to enter shell inside the container.
Create database, type: `psql -U postgres -W -c "CREATE DATABASE \"Adventureworks\";"`
Import data, type: `psql -d Adventureworks < install.sql`

## Access Adminer
Go to localhost port 8080
Enter 
Database: postgres
User: postgres
Password: password
