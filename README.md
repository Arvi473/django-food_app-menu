Django commands for food_menu_app:
$ conda create --name myDjangoEnv django
$ n

$ conda create --name myDjangoEnv python=3.12.0
#python latest version.
$ y

# To activate this environment, use
#     $ conda activate myDjangoEnv
# To deactivate an active environment, use
#     $ conda deactivate

$ conda info --envs

$ activate myDjangoEnv
(myDjangoEnv)$ conda install django
(myDjangoEnv) $ y

(myDjangoEnv) $ python         #To check the python version
>>>quit()

(myDjangoEnv) $ deactivate    #Back to the terminal/CMD.

$ python
#To check the python version
>>>quit()
***Example of new project in Django....!***

$ cd Downloads\Django Portfolio
#to make a path for the Django project.

$ mkdir Food

$ cd Food

$ activate myDjangoEnv

(myDjangoEnv) $ django-admin startproject food_project

(myDjangoEnv) $ cd food_project

(myDjangoEnv) $ python manage.py runserver

***Example of new Application in Django...!***

(myDjangoEnv) $ python manage.py startapp food_app

(myDjangoEnv) $ python manage.py runserver

(myDjangoEnv) $ python manage.py migrate

(myDjangoEnv) $ python manage.py makemigrations food_app

(myDjangoEnv) $ python manage.py sqlmigrate food_app 0001

(myDjangoEnv) $ python manage.py migrate

(myDjangoEnv) $ python manage.py runserver
