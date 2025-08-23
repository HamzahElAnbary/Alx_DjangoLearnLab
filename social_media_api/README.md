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

### Feed
GET /api/feed/
Headers: Authorization: Token <token>
Response: Paginated list of posts ordered by -created_at
