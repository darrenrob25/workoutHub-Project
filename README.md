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


***

### Testing

#### W3 HTML Validator

##### Home/Login Page
https://validator.w3.org/nu/?doc=https%3A%2F%2Fworkouthub-2144cdf5941f.herokuapp.com%2F
No errors were returned

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

