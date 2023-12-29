# E-Commerce Platform

This project implements a basic e-commerce platform using Django, enabling user authentication, product management, and shopping cart functionality.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/AvazovOgabek/E-Commerce.git
    ```

2. **Setup Virtual Environment:**
    ```bash
    cd e-commerce
    virtualenv env
    source env/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create Superuser (Admin):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```

## Usage

- Access the admin panel by going to `http://localhost:8000/admin/` and log in using the superuser credentials created earlier.
- Use the provided Django views and templates for user sign-up, sign-in, viewing products, adding/removing products from the cart, and managing user accounts.
- Customize and expand functionality as needed for your e-commerce requirements.

## Folder Structure

- `users/`: Contains user-related models and authentication views.
- `products/`: Manages product-related models and views.
- `templates/`: Includes HTML templates for different views.
- `static/`: Stores static files like CSS, JavaScript, and images.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or create a pull request.

