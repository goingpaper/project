beers and boys
===============

To run the application an installation of Django is required, the latest one can be found at https://www.djangoproject.com/download/. Now to run the app go to the project/project directory in terminal. To initialise the database type 'python manage.py syncdb' (The SQL code which creates the tables can be accessed by the terminal command 'python manage.py sqlall barreviews') and to import the data type 'export DJANGO_SETTINGS_MODULE=project.settings' and 'python import.py', now type 'python manage.py runserver' to run the application.

From here the admin site can be accessed at http://127.0.0.1:8000/admin/ or the main site can be accessed at http://127.0.0.1:8000/index.html. It is necessary to login into the main site to access anything, an example login for a user with superuser privileges is the account with username 'admin' and password 'admin'. A regular users login for testing is account with username 'GoingPaper' and password 'goingpaper_123'. All other test accounts can be found in the project/project/users.json file.

After login on the main site a few different html pages can be accessed from hyperlinks in the navigation bar. The linked pages are as follows
•	Bars: Displays a list of bars in the database with links to their websites and individual bar detail page.
•	Users: Displays a list of users that are signed up and are stored in the databass, as well as links to their individual user page.
•	Drinks: Displays a list of all the drinks in the database along with a link to their respective drink detail page.
•	Reviews: Displays a list of all the reviews that are in the database with links to the user, bar and review detail page.
•	Breweries: Displays a list of all the breweries in the database and a link to their detail page.
•	User Home (user page of logged in user): Takes you to the current users detail page allowing them to modify their own data.
•	Logout: Logs current user out.
•	Signup (only if not logged in): Allows the registration of a new user.

The application provides functionality for a logged in general user to review bars, like drinks and comment on other users pages. How to do each of these is detailed below
•	Review Bars: To review a bar, click its link to its detail page. Then type in the comment text field a 300 or less character review of the bar. Add a rating from 1 – 5 and click submit to post the review. To edit or delete the view click the date hyperlink to look at the individual review and click the corresponding option.
•	Like Drinks: To like a drink click the link to its detail page. Then click like to add it to your likes or dislike to remove it. You are unable to like a drink more than once so repeat clicks do nothing.
•	Comment on users: This works much the same as reviewing bars except that comments are done from a users detail page. The comment can be submitted onto someone’s page and the creator can delete it.

The admin site allows a superuser to edit any database entry that is stored in the database. It uses the django default admin interface to display the easy to use adding and changing of all parts of the website. Staff users can also be assigned to allow them to add, edit and delete Bars, Drinks and Breweries.
