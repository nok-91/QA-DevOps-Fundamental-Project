# QA-DevOps-Fundamental-Project
This repository contains my deliverable for the QA DevOps Fundamental Project.

## Contents
* [Project Brief](#Project-Brief)  
* [Design](#App-Design) 
* [CI Pipeline](#CI-Pipeline)
* [Risks](#Task-App)
* [Task App](#Task-App)
* [Testing](#Testing)
* [Issues](#Known-Issues)
* [Future Sprints](#Future-Sprints)

## Project Brief:
For this project, I had to create a web application with CRUD (create, read, update, delete) functionality. I had to use a Flask micro web framework (a framework for developing web application in python) and a MySQL database to store information. The database had to have at least 2 tables sharing a one-to-many relationship. 

## Design:
As this was a short first sprint, I decided to create a basic task application. The MVP for this project consists of 2 tables - Category and Task, which have a one to many relationship (One category can have many tasks). Using a Category PK (primary key) as a FK (foreign key) attribute within the Task table allowed for querying by category.
The web app itself, through the rendered UI, allows a user to take a note / task and assign it some attributes in addition to a category - such as a due date and an option to mark it as complete (Create Functionality). The user's tasks are displayed to them on the home page (Read Functionality), where they have the option of update a task (Update functionality) or delete a task (Delete Functionality). 
This is the first ERD for my project:

![ERD](https://github.com/nok911/QA-DevOps-Fundamental-Project/blob/main/DevOps_images/db_schema.png)

## CI Pipeline: 
For tracking the progress of this project I used Trello. I created a project scope / backlog that included the requirements and user stories. From that, I was able to create a sprint backlog with cards I prioritised using MoSCoW acceptance criteria. 
I used git for version control after creating a project repository on github. I was able to stage changes and push them to a development branch of the project repo as the project evolved on my local machine (local development branch).  
The project was developed in a py3 virtual environment where I could install project specific requiements.
This is the Trello board for my project:

![Trello](https://github.com/nok911/QA-DevOps-Fundamental-Project/blob/main/DevOps_images/trello.png)

## Risks
To keep sensitive data secure their were a few measures that had to be implemented. I created a file with environment variables to store the database URI and Secret key. I imported SQLAlchemy so that commands couldn't be sent directly to the database, and I put validators on WTForms so that the expected input types would be received - before creating the model objects and routes (mapping URL's to functions). Finally, I added files that I did not want tracked to a gitignore file.

## Task App
This is the application home / read page with a menu for adding tasks or categories: 

![Home](https://github.com/nok911/QA-DevOps-Fundamental-Project/blob/main/DevOps_images/TaskApp_Home.png)

This is where a user can add a task and be redirected back to the read page:

![Add Task](https://github.com/nok911/QA-DevOps-Fundamental-Project/blob/main/DevOps_images/TaskApp_AddTask.png)

This is an example of tasks where one has been updated.

![Update Task](https://github.com/nok911/QA-DevOps-Fundamental-Project/blob/main/DevOps_images/TaskApp_Addtask2.png)

Here a task has been deleted from the list:

![Delete Task](https://github.com/nok911/QA-DevOps-Fundamental-Project/blob/main/DevOps_images/TaskApp_Delete.png)

## Unit Testing
I tested the functionality (create, read, update, delete) of the application by creating a test environment and running pytest (a software framework for finding and testing code). Within this environment I created an SQLite database to store sample data that would be used when testing the functions. This would be dropped afer each test.
Here are the coverage results:
![Coverage](https://github.com/nok911/QA-DevOps-Fundamental-Project/blob/main/DevOps_images/Coverage_report.png)

## Future Sprints
* Handle duplicate data with a message and redirect
* Add a user table with login authentication 
* Add Update and Delete Category functionality 
* Create a styling template for the application's UX/UI design