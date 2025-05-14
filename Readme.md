# Patient Portal – Spring 2025 Project  

## CS 520 - UMass Amherst

### Team Name: The Chefs

- **Steven Tang**  
- **Isha Bang** — `ibang@umass.edu`  
- **Juhi Manish Jain** — `juhimanishjain`  
- **Anthony Rozet** — `AnthonyRoze`

---

## Project Overview

This project aims to build a **digital patient portal** designed to improve the accessibility, accuracy, and efficiency of managing healthcare data. The portal supports essential patient information, medical records, appointment tracking, and prescription viewing, all within a clean and user-friendly interface.

---

## Why This Matters

The importance of digitized patient information management stems from the need for:

- **Efficiency & Accessibility:**  
  Eliminating manual paperwork streamlines the process of storing, updating, and accessing patient records.

- **Real-Time Updates:**  
  Medical histories and treatment records can be updated instantly, ensuring accuracy across providers.

- **Patient Safety:**  
  Digital systems reduce the likelihood of human error, such as medication mix-ups or missing information.

- **Telehealth Support:**  
  Enables remote access to medical records and consultations, increasing care accessibility regardless of location.

---

## Key Features

- Patient profile management (contact, emergency, insurance)
- Medical history tracking (diagnoses, surgeries, allergies)
- Medication and lab report organization
- Upcoming appointment overview
- Interactive **Prescription Viewer** page
- Downloadable or printable summaries



python
Always show details

Copy
from pathlib import Path

readme_content = """
# Healthcare Management System

This is a web-based Healthcare Management System built with Django. It allows patients to register, log in, manage their health data, schedule appointments, view prescriptions, and update personal settings.

## Features

- Patient registration and login
- View and update profile details
- Schedule appointments via modal interface
- View and manage prescriptions
- Access to lab reports and past medical records
- Mobile-friendly and responsive UI

## Technologies Used

- Django (Python)
- HTML, CSS, JavaScript
- PostgreSQL
- Bootstrap Icons / Font Awesome

## Setup Instructions

1. **Clone the repository**

git clone https://github.com/your-username/healthcare-management-system.git
cd healthcare-management-system

2. **Create and activate a virtual environment**

python3 -m venv env
source env/bin/activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Configure environment variables**

Create a `.env` file in the root directory with the following content:

DBNAME=your_db_name
DBUSER=your_db_user
DBPASS=your_db_password
DBHOST=localhost
DBPORT=5432
SECRET_KEY=your_django_secret_key

5. **Apply migrations and run the server**

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

6. **Access the App**

Visit `http://127.0.0.1:8000/` in your browser.
