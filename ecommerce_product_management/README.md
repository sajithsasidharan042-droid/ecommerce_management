# E-commerce Product Management System

A simple Django Product Management System created for the Junior Python/Django Developer Development Test.

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap 5
- JavaScript (Bootstrap bundle)
- Pillow for image uploads

## Features

- User login and logout
- Dashboard with:
  - Total Products
  - Active Products
  - Inactive Products
  - Low Stock Products
- Product CRUD
- Category relationship
- Product image upload
- Search by product name or SKU
- Category filter
- Active/Inactive filter
- Pagination
- Product details
- Form validation
- Unique SKU
- Low stock indication when stock is 5 or below
- Delete confirmation
- Login protection for product management

## Installation

### 1. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create database tables

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create an admin/login user

```bash
python manage.py createsuperuser
```

Enter a username, email (optional), and password.

### 5. Run the server

```bash
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

## Add Categories

Go to:

http://127.0.0.1:8000/admin/

Login with the superuser account and create categories.

Example:

- Clothing
- Electronics
- Footwear
- Accessories

Then use the main Product Management page to add products.

## Git workflow

Suggested meaningful commits:

```bash
git init
git add .
git commit -m "Initial Django setup"

git add .
git commit -m "Create product and category models"

git add .
git commit -m "Add product CRUD"

git add .
git commit -m "Create product listing UI"

git add .
git commit -m "Add search and filters"

git add .
git commit -m "Add authentication"

git add .
git commit -m "Fix validation"
```

## Important

The project uses SQLite as requested by the assessment. For production, replace the development secret key, configure allowed hosts, and use a production database/server.
