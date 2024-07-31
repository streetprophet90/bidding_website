# Bidding Website

This is a bidding website built using Django. Users can create auctions, place bids, and manage their accounts. The project is designed to be a fully functional bidding platform with user authentication, auction management, and bid tracking.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- User authentication and account management
- Create, view, and manage auctions
- Place bids on auctions
- Track bid history and auction status
- Notifications for winning and losing bids

## Technologies Used
- Python 3.8+
- Django 3.2+
- SQLite (default database, can be replaced with PostgreSQL or MySQL)
- HTML, CSS, JavaScript for frontend

## Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/bidding-website.git
   cd biddingwebsite
   ```
2. **Set up a virutal environment(recommended)**
   ```bash
   python -m venv env
   ```
3. **Activate the virtual environment**
   ```bash
   .\env\Scripts\activate #OnWindows
   source env/bin/activate #onMac_Linux
   ```
4. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python mangage.py migrate
   ```

6. Creat a superuser
   ```bash
   python manage.py createsuperuser
   ```
8. Run the development server
   ```bash
   python manage.py runserver
   ```
## Running the Project

Once the development server is running, you can access the application by navigating to http://127.0.0.1:8000/ in your web browser.
```
Admin interface: http://127.0.0.1:8000/admin/
Home page: http://127.0.0.1:8000/
Register a new user: http://127.0.0.1:8000/accounts/register/
Login: http://127.0.0.1:8000/accounts/login/
Profile page: http://127.0.0.1:8000/bidding/profile/
Create a new auction: http://127.0.0.1:8000/bidding/auction/new/
```
   


