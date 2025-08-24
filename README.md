HEAD
# LibraryProject

This is a basic Django project created for the ALX Introduction to Django task.

## Overview

This project serves as a foundation for learning Django. It includes the default project structure and a working development server.

## Setup Instructions

1. Make sure Python and Django are installed.
2. Apply database migrations:
3. Run the development server:
4. Open your browser and visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the default Django welcome page.

## Project Structure

- `LibraryProject/`: Main Django project folder.
- `manage.py`: Django project management script.
- `LibraryProject/settings.py`: Django project settings.
- `LibraryProject/urls.py`: URL configuration.

## Notes

This project is part of the ALX Django learning labs.

# Social Media API - ALX Django LearnLab

## Setup Instructions
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/social_media_api
Install dependencies:

bash
Copy
Edit
pip install django djangorestframework djangorestframework-simplejwt
Run migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Start server:

bash
Copy
Edit
python manage.py runserver
API Endpoints
POST /api/accounts/register/ → Register new user (returns token)

POST /api/accounts/login/ → Login user (returns token)

GET/PUT /api/accounts/profile/ → View or update user profile (requires authentication)

User Model
username

email

bio

profile_picture

followers

### Follow / Unfollow
POST /api/accounts/follow/{user_id}/
POST /api/accounts/unfollow/{user_id}/
Headers: Authorization: Token <token>

e40048e (Ready for deployment)
