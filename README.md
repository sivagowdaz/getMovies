# getMovies
## About the project
### This is a web application where a user can search and download the movies. The website features effective search and filtering options. 
### This is done by scraping the data from the website “www.2movierulz.com”. 
### The intention is to provide an easy and good user interface and user experience by prohibiting the dummy clicks(the user is redirected to random pages where lot of ads come up)

## Prerequisites 
1. python must be installed

## Project Setup
1. Install all the dependencies listed in the requirements.txt file(It is recommended to install dependencies inside the virtual environment, instead of installing globally.)
2. Make migrations by running bellow commands
```
python manage.py migrate
python manage.py makemigrations
```
3. Run bellow command to run the server
```
python manage.py runserver
```
