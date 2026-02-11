# Cab Booking System

A Django-based application for managing riders, cabs, and location-based bookings, following OOD and LLD principles including SOLID.

## Features
- Rider and cab management with location updates.
- Trip initiation and completion.
- Nearest available cab booking based on location.
- RESTful APIs via Django Rest Framework.

## Technologies
- Python
- Django 5.2.11
- Django Rest Framework 3.16.1

## Setup
1. Clone the repo: `git clone https://github.com/AkshatGit00/cab-booking-system.git`
2. Create virtual env: `python -m venv env`
3. Activate: `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)
4. Install deps: `pip install -r requirements.txt`
5. Migrate: `python manage.py makemigrations` then `python manage.py migrate`
6. Run: `python manage.py runserver`

## Changes in Refactoring
- Fixed method inconsistencies and bugs (e.g., manager calls, end_trip arguments).
- Optimized methods with @staticmethod and @classmethod.
- Improved code readability with docstrings and Pythonic practices.
- No new features added; suggestions for integrations in next step.

## API Endpoints
- /api/riders/ (GET/POST)
- /api/cabs/ (GET/POST)
- /api/trips/ (GET)
- /api/book-ride/ (POST) { "rider_id": <id> }
- /api/end-trip/<id>/ (PUT)