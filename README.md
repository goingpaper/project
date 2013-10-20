beers and boys
===============

To run the application an installation of Django is required, the latest one can be found at
https://www.djangoproject.com/download/ . Now to run the app in the project directory go to 
project/project in terminal. To initialise the database type 'python manage.py syncdb'(The SQL code which creates 
the tables can be accessed by the terminal command 'python manage.py sqlall barreviews') and to import the 
data type 'export DJANGO_SETTINGS_MODULE=project.settings' and 'python import.py', now type
'python manage.py runserver' to run the application.

From here the admin site can be accessed at http://127.0.0.1:8000/admin/ or the main site can
be accessed at http://127.0.0.1:8000/index.html . It is necessary to login into the main site to access anything,
to the list of users in project/project/users.json login access is currently granted with superuser status given
to one account with username 'admin' and password 'admin'. An example non-superuser account to login with has username 
'GoingPaper' and password 'goingpaper_123'.

After login on the main site a few different html pages can be accessed from hyperlinks in the header bar.
The linked pages are the Index page, Bars, Users, Drinks, Reviews, Breweries, Current User and a logout option. From each 
of those pages individual detailed views of those objects can be accessed. Users have
the ability to add reviews on any bar which can be edited, like or unlike any listed drink and comment on or 
edit their own comments any non-superusers page.

On the admin site superusers can create new objects of any model in models.py this includes Users and Groups
while being able to edit everything.

