Tasks for KeyUA

## Production 
- set production configuration in .env file

``docker-compose up -d``

## Set up project for local development
- Required system packages
```
sudo apt install python3-dev mysql-server libmysqlclient-dev
```

- For set up MySQL use this guide:
[How to install MySQL on Ubuntu](https://www.digitalocean.com/community/tutorials/mysql-ubuntu-18-04-ru)
  
- Create venv
```
python3 -m  venv venv
```

- Install libs and apply migrations

````
source venv/bin/activate/
pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python manage.py runserver
````



- Redis setup
``sudo apt install redis-server``
  
### define additional settings in .env
Run server python manage.py runserver