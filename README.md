# WorkoutHub

The Live App can be found at: https://workouthub-2144cdf5941f.herokuapp.com/

WorkoutHub is a place to keep, change and add new workouts all in one place. It allows you to easily access all of your planned workouts.

## Project Goals and User Experience

### Project Goals
- Create a fully functioning web app that allows you to view your workouts.
- Keeps your workouts secure from other users.
- Keeping the application easy to use, update and delete workouts.
- Continuously improve the app through updates, bug fixes and feedback.

Ultimately the goal of the app is to create a secure and easy way to edit and keep a record of all your workouts.


### User Stories
#### First Time User
|Story No.|Story|
| ------------- | ------------- |
|1|As a first time user , <br> I want to be able to know how to easily sign up <br> so that I can access the app.  <br><br>I know I am done, when there is clear signposting to sign up.|
|2|As a first time user, <br> I want to be able to login <br> so that I asm able to use the app <br><br>I know this has been achieved when the user can sign in. |
|3|As a first time user, <br> I want to be able to add workouts <br>so that i can use the app <br><br>I know I am done there is the ability to add workouts. |

#### All Users
|Story No.|Story|
| ------------- | ------------- |
|1|As a user, <br> I want to be able to make changes to my workouts  <br><br>I know I am done, when users are able to edit their workouts. |
|2|As a user, <br> I want to be able to delete existing workouts.  <br><br>I know this has been achieved there is the ability to delete workouts |

***

## Design
### Wireframes
Below are the designs that were used as a reference point to build the project, these designs were build while keeping in mind the needs of the above used stories.
#### Home Page
![Image of homepage.html](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/New%20Wireframe%201.png)

#### Workout Page
![Image of homepage.html](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/New%20Wireframe%201%20(3).png)

#### Edit Workout Page
![Image of homepage.html](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/New%20Wireframe%201%20(1).png)

***

### Database Schema
![Image of database schema](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/schema.png)


***

### Colour Choices

![Image of colour schema](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/colour-palette.png)

***

### Font Selection
Google fonts was used for all fonts on the website, I chose google fonts as it is simple and provides clean refined fonts.

#### Monofett
Used for the "logo" or main title on the navbar
![Image of colour schema](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/monofett.png)


#### Red Hat Mono
Used for the rest of the text throughout the website
![Image of colour schema](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/red-hat-mono.png)
***

### Features

#### Log in
The page where a user is able to log into their already existing account, which allows them to access their dashboard.

![Login](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/login-function.png)

#### Register
The register button takes the user to a page to register a new account if one doesn't currently exist.

![Register](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/signup-function.png)

#### Dashboard
The users dashboard displaying all of your workouts and functionality to update, create and delete workouts.

![Dashboard](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/delete-workout.png)

#### Add Workout Page
Page allowing you to add workouts, increase the number of exercises within a workout.

![Gameboard Screenshot](assets/media/howtoplay-ss.png)

#### Edit Workout
Page allowing you to change currently existing workouts.

![Edit Workout](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/edit-workout.png)

***

### Future Implementations
* A feature that I would like to add in the future would be metrics to the dashboard, showing possibibly the total number of workouts you have saved, the percentages of categories.
* A feature that I would also like to add in the future would be the ability to actually log individual sessions and compare them every time you do the same session.
* A final feature I would like to add in the future would be an admin user who is able to view all users and delete users.

***

### Testing

#### W3 HTML Validator

##### Home/Login Page
https://validator.w3.org/nu/?doc=https%3A%2F%2Fworkouthub-2144cdf5941f.herokuapp.com%2F
No errors were returned

#### Register Page
https://validator.w3.org/nu/?doc=https%3A%2F%2Fworkouthub-2144cdf5941f.herokuapp.com%2Fregister

#### Jigsaw CSS Validator
https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fworkouthub-2144cdf5941f.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
No errors were returned

#### JS
There were no errors when passing the js through the official JSHint Validator.
The below metrics were returned:
* There are 11 functions in this file.
* The function with the largest signature takes 2 arguments, the median is 1.
* The largest function has 19 statements in it, the median is 5
* The most complex function has a cyclomatic complexity value of 5 with the median being 1.

#### Code Institute Python Linter
#### Models.py
![models](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/models-linter.png)

#### _init_.py
![init](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/init-pep8.png)

#### routes.py
![routes](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/routes-pep8.png)


#### User Story Testing
#### First Time User
|Story No.|Result|Story/ Evidence|
| ------------- | ------------- | ------------- |
|1|Test Pass |As a first time user , <br> I want to be able to know how to easily sign up <br> so that I can access the app.  <br><br>I know I am done, when there is clear signposting to sign up. <br><br>Evidence:<br>There is clear signposting to the register page in the navbar.<br> ![Signup Function](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/signup-function.png)|
|2|Test Pass |As a first time user, <br> I want to be able to login <br> so that I asm able to use the app <br><br>I know this has been achieved when the user can sign in. <br><br>Evidence:<br>There is clear signposting to login, the login function is working correctly.<br> ![Login Function](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/login-function.png)|
|3|Test Pass |As a first time user, <br> I want to be able to add workouts <br>so that i can use the app <br><br>I know I am done there is the ability to add workouts. <br><br>Evidence:<br>The Add Workout function is working as expected.<br> ![Add Workout Function](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/add-workout.png)|

#### All Users
|Story No.|Result|Story/ Evidence|
| ------------- | ------------- | ------------- |
|1|Test Pass |As a user, <br> I want to be able to make changes to my workouts  <br><br>I know I am done, when users are able to edit their workouts.<br><br>Evidence:<br>There is functionality to edit workouts<br> ![edit-workout](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/edit-workout.png)|
|2|Test Pass |As a user, <br> I want to be able to delete existing workouts.  <br><br>I know this has been achieved there is the ability to delete workouts <br><br>Evidence:<br>The functionality to delete workouts works correctly<br> ![delete workout](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/delete-workout.png)|

#### Accessibility Testing

| Login Page |
| ------- |
| ![lighthouse result login page](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/login-page-lighthouse%20copy.png) |

| Register |
| ------- |
| ![lighthouse result register page](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/register-page-lighthouse.png) |

| Edit Workout |
| ------- |
| ![lighthouse result edit workout page](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/edit-workout-page-lighthouse.png) |

| Dashboard |
| ------- |
| ![lighthouse resultdashboard page](https://github.com/darrenrob25/workoutHub-Project/blob/main/media/dashboard-page-lighthouse.png) |


### Manual Testing
* I have tested that the project works in different web browsers.
* I have tested that the project is responsive and works with different device sizes and it looks good and functions correctly.
* I have tested all links and they work correctly.
* I have tested that register function works correctly.
* I have tested that the login function works correctly.
* I have tested the Add workouts function works correctly.
* I have tested the Editing Workouts function works correctly.
* I have tested the Delete workouts function works correctly.

***

### Bugs

#### Bug 1
The first issue which I encountered was being unable to build my database.

This issue was rectified by using: psql -h 127.0.0.1 in the terminal, forcing psql to connect on the port, as it was trying to connect via something else.

#### Bug 2
The second issue I encountered was when trying to edit/delete a workout, this was taking me to the url with undefined at the end.

This issue was rectified by moving a lot of functionality away from the javascript file and into the html file, allowing me to use JS to handle the replication and jinja in the html to link correctly.

#### Bug 3
The third issue which I encountered was that the live version hosted on heroku maxed out the possible connections.

This issue was likely caused by to much interaction having happened for the database to handle. This was rectified by restarting all dyno's in heroku.

***

### Cloning & Forking
#### Fork
1. On GitHub.com, navigate to the [WorkoutHub](https://github.com/darrenrob25/workoutHub-project) repository.
2. In the top-right corner of the page, click Fork.
3. By default, forks are named the same as their parent repositories. You can change the name of the fork to distinguish it further.
4. Add a description to your fork.
5. Click Create fork.

#### Clone
1. Above the list of files click the button that says 'Code'.
2. Copy the URL for the repository.
3. Open Terminal. Change the directory to the location where you want the cloned directory.
4. Type git clone, and then paste the URL
5. Press Enter.

#### Local Deployment
1. Sign up to [Gitpod](https://gitpod.io/)
2. Download the Gitpod browser extension.
3. On GitHub.com, navigate to the [WorkoutHub](https://github.com/darrenrob25/workoutHub) repository.
4. Above the list of files click the button that says 'Gitpod'.

#### Remote Deployment
1. Log in to Heroku
2. Click on the 'Create new app' button.
3. Give your application a name that hasn't been previously used, select the closest region to you and click the 'Create app' button.
4. You can use an external database for example postgresql.
5. Go to settings section and click 'Reveal Config Vars' in the Config variable section.
6. Set DATABASE_URL to your external database link.
7. Set DEBUG to False
8. Set IP to 0.0.0.0
9. Set port to 5000
10. Set SECRET_KEY to your chosen secret key
11. Navigate to the 'Deploy' page
12. Select 'GitHub' from the 'Deployment method' section
13. Enter your github account details and select the forked/ clone repository.
14. Select 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.
15. Once built, click the 'View' button to load the URL and it should be done.

#### Database
The Database for this project was provided by CodeInstitute, you can obtain a postgresql server from many vendors including Heroku it's self. Once you have your Postgres server you should follow the below steps:
1. Navigate to your app in heroku
2. Click on the settings tab.
3. Click reveal config vars
4. Update the DATABASE_URL to be your database link.
5. To migrate your models to the new database use the heroku terminal and select a 'Python3' terminal
6. Use the below codes in the terminal to create your database:
7. 'From Workouthub import db'
8. 'db.create_all()'
9. Your database should now be created.
10. 
***

 ## Credits

 ### Content
 - Processes from the CI Task Manager project was used to help create this website - [CI Task Manager](https://github.com/Code-Institute-Solutions/flask-sqlalchemy-task-manager/tree/main)

- HTML, CSS, Python and Javascript code help was taken from w3schools - [W3Schools](https://www.w3schools.com/)

- Bootstrap was used to help with the CSS [Bootstrap](https://getbootstrap.com/)

- Various [Stack Overflow](https://stackoverflow.com) articles were used for guidance, most notably:
 
- [Flask Jsonify](https://tedboy.github.io/flask/generated/flask.jsonify.html)
  
- [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/)



### Media
* Background Photo taken from [pexels](https://www.pexels.com/)



