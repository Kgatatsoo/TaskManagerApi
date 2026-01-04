**TaskManager API**

A simple task management API built with Django & Django REST Framework.

**The Api contains Features such as**
User registration & login (token-based)
CRUD tasks (create, read, update, delete)
Mark tasks complete/incomplete
Only accessible by authenticated users

**Tech Stack used to build the Api**
Python 
Django 
Django REST Framework 
Djoser 
SQLite 

**How to Setup?**
git clone https://github.com/Kgatatsoo/TaskManagerAPI.git
cd TaskManagerAPI
python -m venv venv
source venv/Scripts/activate 
pip install django djangorestframework djoser django-cors-headers
python manage.py migrate
python manage.py runserver

**Authentication**
Register: POST /auth/users/
Login for token: POST /auth/token/login/
Add token to headers for protected endpoints.

**Task Endpoints**
GET /api/tasks/ – List tasks
POST /api/tasks/ – Create task
GET /api/tasks/1/ – View task
PUT / PATCH /api/tasks/2/ – Update task
DELETE /api/tasks/1/ – Delete task