**TaskManager API**

A simple and secure Task Management REST API built with Django and Django REST Framework.

**Features:**
- User registration & authentication (Token-based)
- Create, read, update, and delete tasks
- Mark tasks as complete or incomplete
- Tasks accessible only to authenticated users
- Secure API endpoints

**Tech Stack:**
- Python
- Django
- Django REST Framework
- Djoser
- SQLite
-PostMan

**Running the project locally follow these steps.**
**1. Clone Repository**
git clone https://github.com/Kgatatsoo/TaskManagerAPI.git
cd TaskManagerAPI

**2. Create Virtual Environment**
python -m venv venv
source venv/Scripts/activate

**3. Install Dependencies**
pip install django djangorestframework djoser django-cors-headers

**4. Run Migrations**
python manage.py migrate

**5. Run Server**
python manage.py runserver

**Authentication:**
POST /auth/users/
POST /auth/token/login/

**Task Endpoints:**
GET /api/tasks/
POST /api/tasks/
GET /api/tasks/1/
PUT /api/tasks/1/
PATCH /api/tasks/1/
DELETE /api/tasks/1/
**N.B Postman was used to verify the code functionality**
