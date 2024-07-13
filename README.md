# WorkoutHub

The Live App can be found at:

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

### Features


***

### Testing


***

### Bugs

#### Bug 1
The first issue which I encountered was being unable to build my database.

This issue was rectified by using: psql -h 127.0.0.1 in the terminal, forcing psql to connect on the port, as it was trying to connect via something else.

#### Bug 2
The second issue I encountered was when trying to edit/delete a workout, this was taking me to the url with undefined at the end.

