# Restaurant Web Application

## Overview

This is a full-stack web application developed using **Python** and **Django** for the backend and **HTML**, **CSS** and **Bootstrap** for the frontend. The application is designed for restaurant owners and their customers. It allows restaurant owners to manage the menu dynamically through an admin interface, and customers can view available and unavailable dishes along with their details and price via a QR code or the website URL.

Customers can easily scan a QR code generated by the app to access the restaurant's website and view the menu, including dish descriptions, ingredients, and prices. The website is updated in real-time based on the status of the dishes in the database. Additionally, restaurant owners and cooks have admin access to add, edit, and delete dishes through the backend interface.

## Features

### Customer Interface

- **QR Code Access**: Customers can scan a QR code to access the restaurant's website on their mobile devices or desktop browsers.
- **Menu Overview**: Customers can view a list of available and unavailable dishes with:
  - Dish name.
  - Description (ingredients).
  - Price.
  - A line-through effect for unavailable dishes to indicate their status.
- **Dish Details**: By clicking on a dish, customers can navigate to a detailed page showing additional information about the selected dish.
- **Navigation**: 
  - **Home Page**: Displays the list of all dishes.
  - **About Page**: Provides information about the restaurant.

### Admin Interface (Restaurant Owner & Cooks)

- **User Roles**:
  - Restaurant owners can create user accounts for cooks with access to the admin panel.
  - Cooks can log in and manage the menu.
  
- **Admin Dashboard**:
  - Add, edit, and delete dishes directly from the admin interface.
  - Manage dish attributes such as:
    - Name
    - Description (ingredients)
    - Price
    - Type of dish
    - Availability status (available/unavailable)
    - Cook name
  - Automatic handling of `date created` and `date updated` fields for each dish in the SQL database.

- **Real-time Updates**: Any changes made to the database (add, edit, or delete dishes) are instantly reflected on the customer-facing website.

### Backend

- **Django Framework**: Powered by Django using class-based views for routing and handling web requests.
- **SQL Database**: Stores dish data including name, description, price, availability status, type, cook name, and timestamps for creation and updates.

### QR Code Integration

- **QR Code Generation**: The application uses a Python library to generate QR codes that link to the restaurant's website.

## Technologies Used

- **Python**: Core programming language.
- **Django**: Web framework for building the backend.
- **Jinja2**: Templating engine used for rendering dynamic content in HTML.
- **HTML/CSS**: Frontend technologies for building the web interface.
- **Bootstrap**: CSS framework for responsive design.
- **SQL Database**: Backend database storing food data and user information.
- **QR Code Library**: For generating QR codes linking to the website.
- **Class-Based Views**: Django's class-based views are used to handle different routes such as the home page, about page, and detail views for dishes.

## URLs

- **Main Page**: `/` - Displays all available and unavailable dishes.
- **About Page**: `/about/` - Provides information about the restaurant.
- **Dish Details**: `/detail<primary key>/` - Displays detailed information about a selected dish.
- **Admin Interface**: `/admin/` - Allows owners and cooks to manage dishes and user accounts.

## Installation

### Prerequisites

- Python 3.x installed.
- Django installed.
- SQL Database (e.g., SQLite by default).

### Steps to Run the Application

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Mahdi-Meyghani/Restaurant-Web-Application.git
    cd Restaurant-Web-Application
    ```

2. **Install Requirements**:
    Install the dependencies listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run Migrations**:
    Set up the database by running the migrations:
    ```bash
    python manage.py migrate
    ```

4. **Run the Development Server**:
    Start the Django development server:
    ```bash
    python manage.py runserver
    ```

5. **Access the Website**:
    - Customer Interface: Visit `http://127.0.0.1:8000/` in a browser.
    - Admin Interface: Visit `http://127.0.0.1:8000/admin/` and log in with admin credentials.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contact

For any inquiries, please contact me :)