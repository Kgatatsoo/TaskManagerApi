Task Management API

A simple Django REST Framework API for managing tasks.
Users can register, authenticate using tokens, and perform CRUD operations on their own tasks.

Features

User registration and authentication (Token-based)

Create, read, update, and delete tasks

Mark tasks as complete or incomplete

Each user can only access their own tasks

Built using Django ORM

Ready for deployment (Heroku / PythonAnywhere)

Tech Stack

Python

Django

Django REST Framework

Djoser (Authentication)

SQLite (development database)

Project Structure
TaskManagerAPI/
│
├── taskmanager/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── taskmanagerapp/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md

Setup Instructions
Clone the repository
git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api

Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate

Install dependencies
pip install django djangorestframework djoser django-cors-headers

Run migrations
python manage.py makemigrations
python manage.py migrate

Start development server
python manage.py runserver

Authentication (Token-Based)
Register a user

POST

/auth/users/


Request body:

{
  "username": "testuser",
  "password": "testpassword123"
}

Login and get token

POST

/auth/token/login/


Request body:

{
  "username": "testuser",
  "password": "testpassword123"
}


Response:

{
  "auth_token": "your_token_here"
}

Use token in requests

Add this header in Postman:

Authorization: Token your_token_here

API Endpoints
Tasks
Method	Endpoint	Description
GET	/api/tasks/	List tasks
POST	/api/tasks/	Create task
GET	/api/tasks/{id}/	Retrieve task
PUT	/api/tasks/{id}/	Update task
PATCH	/api/tasks/{id}/	Mark complete/incomplete
DELETE	/api/tasks/{id}/	Delete task
Example: Create a Task

POST /api/tasks/

{
  "title": "Learn Django REST",
  "description": "Build my first API",
  "completed": false
}
