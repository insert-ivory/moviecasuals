# MovieCasuals

MovieCasuals is a web application that allows users to manage movies, directors, and their personal interactions with films. Users can add movies, associate them with directors, rate and review them, and track their movie statuses (e.g., Watched, Want to Watch, Interested, etc.). The platform also enables users to organize their movie collections and engage with others through comments and ratings.

---

## Features

- **Manage Movies & Directors**: Add, update, and view movies and their associated directors.
- **Rating & Reviews**: Rate movies and provide feedback through reviews.
- **Movie Status Tracking**: Track movie statuses such as "Watched", "Want to Watch", and "Interested".
- **Organize Collections**: Organize and manage movie collections with an intuitive interface.
- **Comments & Ratings**: Engage with other users through comments and ratings on movies.
- **Minimal API**: A minimal RESTful API built with Django REST Framework for certain tasks.

---

## Setup and Installation Guide

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

Clone the repository to your local system using the following command:


git clone https://github.com/yourusername/moviecasuals.git
cd moviecasuals

2. Create a Virtual Environment
Create a virtual environment to isolate project dependencies:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate

3. Install Project Dependencies
Install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
4. Set Up Environment Variables
Create a .env file in the root of the project directory and add the following environment variables:

ini
Copy code
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
5. Prepare the Database
Run the following commands to set up the database:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
6. Create an Admin User
To access the Django admin panel, create a staff account:

bash
Copy code
python manage.py createsuperuser
7. Run the Development Server
Start the local development server:

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to view the application.

---

## Admin Panel  
Permissions and Groups:
The application has a role-based access control system with four distinct admin roles/groups:

User : Standard access for regular users, allowing interaction with core platform features, such as browsing movies, leaving ratings, and comments.

Admin: Elevated permissions for managing entities such as movies, directors, comments, and user accounts. Admins can add, edit, or remove content as needed.

Content Approver: A specialized role focused on reviewing and approving movies and directors before they are publicly listed, ensuring that only verified content is featured.

Superuser: Full administrative rights across the platform, granting access to all settings, user management, and system configuration. Only the superuser can perform critical tasks like managing the database and system settings.
Each role is carefully defined to provide the appropriate level of access, ensuring efficient delegation of tasks without compromising security.

Staff: To access the admin panel make sure to be registered as staff before superuser!

##  Technical Stack
Backend: Django 5.1.3, Django REST Framework
Database: PostgreSQL
Frontend: HTML/CSS (Django templates), JavaScript, Bootstrap


