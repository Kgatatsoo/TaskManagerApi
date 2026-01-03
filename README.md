📝 Task Management API

This is a Task Management API built using Django and Django REST Framework.

The API allows users to:

👤 Register and log in using token authentication

✅ Create, view, update, and delete tasks

✔️ Mark tasks as complete or incomplete

🔒 Access only their own tasks

This project was built for learning and portfolio purposes.

✨ Features

🔑 Token-based authentication

🧑‍💻 User registration and login

🗂️ CRUD operations for tasks

🗒️ Tasks belong to individual users

🐍 Uses Django ORM for database management

💻 Technologies Used

Python 🐍

Django 🌐

Django REST Framework ⚡

Djoser 🔐

SQLite (development database) 💾

📂 Project Structure
TaskManagerAPI
│
├── taskmanager/       # Project settings
├── taskmanagerapp/    # Tasks application
├── manage.py
├── db.sqlite3
└── README.md

🚀 Installation and Setup

Clone the repository:

git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api


Create a virtual environment:

python -m venv venv
source venv/Scripts/activate   # Windows
# OR
source venv/bin/activate       # Linux / Mac


Install dependencies:

pip install django djangorestframework djoser django-cors-headers


Run migrations:

python manage.py makemigrations
python manage.py migrate


Start the development server:

python manage.py runserver

🔐 Authentication
Register a user

POST /auth/users/

Request body:

{
  "username": "testuser",
  "password": "testpassword123"
}

Login and get token

POST /auth/token/login/

Request body:

{
  "username": "testuser",
  "password": "testpassword123"
}


Response:

{
  "auth_token": "your_token_here"
}

Using the token

For all protected endpoints, add this header:

Authorization: Token your_token_here

🗂️ Task Endpoints

GET /api/tasks/ – Returns all tasks for the logged-in user

POST /api/tasks/ – Creates a new task

GET /api/tasks/id/ – Returns a single task

PUT / PATCH /api/tasks/id/ – Updates a task or marks it complete/incomplete

DELETE /api/tasks/id/ – Deletes a task

📝 Example: Create Task

POST /api/tasks/

{
  "title": "Learn Django REST",
  "description": "Build a task manager API",
  "completed": false
}

🗄️ Database Model

Task model fields:

👤 user

🏷️ title

📝 description

✅ completed

🕒 created_at

🕒 updated_at

🌐 Deployment

This project can be deployed on:

PythonAnywhere 🐍

Heroku ☁️

Deployment configuration is not included in this repository.

👨‍💻 Author

Vibration Banda
Backend / API Developer (Django REST Framework)

⚠️ Notes

🔒 Authentication is required for all task endpoints

👤 Each user can only access their own tasks