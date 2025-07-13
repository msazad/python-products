# 🛍️ Product Review API (Django REST Framework)

A simple RESTful API for managing products and product reviews. Built using Django and Django REST Framework (DRF). This project supports token-based authentication, user registration/login, and nested review handling.

---

## 📦 Features

- Token-based Authentication (`rest_framework.authtoken`)
- User Registration & Login
- Product CRUD (Admin-only for creation)
- One review per user per product
- Nested Reviews under Products
- DRF Browsable API for easy debugging and testing

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- pip
- Virtualenv (recommended)
- SQLite (default)

---

### 🧪 Setup Instructions

```bash
# 1. Clone the project
git clone https://github.com/msazad/python-products.git
cd python-products

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies

pip freeze > requirements.txt
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser (for admin access)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver


🔑 API Endpoints
✅ Authentication

    POST /api/register/ → Register a new user

    POST /api/login/ → Obtain an authentication token

🛍️ Products

    GET /api/products/ → List all products

    POST /api/products/ → Create a new product (admin only)

    GET /api/products/<id>/ → Retrieve a single product and its details

📝 Reviews (nested under products)

    GET /api/products/<product_id>/reviews/ → List all reviews for a product

    POST /api/products/<product_id>/reviews/ → Create a review (authenticated users only)

        ⛔ Each user can only review a product once

🔐 Auth Header Format

For protected endpoints (like creating reviews or products), include the token in the request header:

Authorization: Token <your_token_here>

Example:

Authorization: Token 9b0a3f7348cb4ec9a8f9e2a5e1ee3c8d9a0a1d6f
