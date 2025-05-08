# Product Catalog with Checkout System

This is a Django-based e-commerce application that features a product catalog, shopping cart, and checkout system. It allows customers to browse products by category, add items to their cart, proceed to checkout, and place orders. The application also includes an admin panel for managing products and orders.

## Features

- **Product Catalog**: View and filter products by category and search by name.
- **Shopping Cart**: Add products to the cart with adjustable quantities. Cart data is stored in the session.
- **Checkout Process**: Enter customer details (name, email, address, phone) to place an order. The total price is calculated, including a fixed delivery fee.
- **Order Confirmation**: Once an order is placed, the customer receives an order confirmation email with the details of the order.
- **Admin Panel**: Admins can manage products and view detailed information about customer orders, including the list of items ordered.

## Technologies Used

- **Django**: The web framework used to build the backend.
- **HTML/CSS**: For the frontend design of the product catalog, cart, and checkout pages.
- **JavaScript**: To handle dynamic behavior like updating the cart via AJAX.
- **Email**: Uses Django’s email system to send order confirmation emails to customers.

## Setup Instructions

### Prerequisites
Make sure you have the following installed on your machine:
- Python 3.x
- Django
- A mail server configuration (for sending order confirmation emails)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/product-catalog.git
   cd product-catalog

2. **Install dependencies**:
Install the required Python packages.
   ```bash
   pip install -r requirements.txt

3. **Set up the database**:
Run migrations to create the necessary database tables.
   ```bash
   python manage.py migrate

4. **Create a superuser**:
To access the Django admin panel, create a superuser account.
   ```bash
   python manage.py createsuperuser

5. **Run the server**:
Start the development server.
   ```bash
   python manage.py runserver

## Screenshots
– Home page with a welcome message or introduction to the shop
![screencapture-product-catlog-onrender-2025-05-08-13_45_19](https://github.com/user-attachments/assets/f40f05cb-c247-4f6c-ad36-82002d94817e)

– Product section displaying all available products with images, prices, and categories
![screencapture-product-catlog-onrender-products-2025-05-08-13_45_39](https://github.com/user-attachments/assets/7c5a3ab5-5451-491d-bd16-4479788cbd7e)

– Products can be filtered by category
![screencapture-product-catlog-onrender-products-2025-05-08-13_46_00](https://github.com/user-attachments/assets/d42f607e-5bef-4152-9ab1-1dbc0f72aca6)

– Products can be searched by their name
![Screenshot 2025-05-08 134642](https://github.com/user-attachments/assets/9b39a82b-8873-47c0-8225-18c36503c5f4)

– Cart section to view selected products and their quantities
![screencapture-product-catlog-onrender-cart-2025-05-08-13_47_16](https://github.com/user-attachments/assets/57bb7f2e-2587-4a5e-98c0-479f9e1819cc)

– Checkout section to enter customer details and place orders
![screencapture-product-catlog-onrender-checkout-2025-05-08-13_47_56](https://github.com/user-attachments/assets/47f66731-22f2-4608-906b-9bbba58cd442)

– Order confirmation page
![screencapture-product-catlog-onrender-order-confirm-2025-05-08-13_48_15](https://github.com/user-attachments/assets/9cf424a5-15dd-426d-82d3-480c4d39fdfe)

– Admin panel login page for managing products and orders
![screencapture-product-catlog-onrender-admin-login-2025-05-08-13_51_07](https://github.com/user-attachments/assets/e866ffb5-5041-4a5a-a765-6ee13fd9461f)
![screencapture-product-catlog-onrender-admin-2025-05-08-13_48_45](https://github.com/user-attachments/assets/f4dd6c1d-8a23-4d22-ab1b-aa8c67f27c26)

– Admin view to see customer orders with product details and quantities
![screencapture-product-catlog-onrender-admin-catalog-order-66-change-2025-05-08-13_49_17](https://github.com/user-attachments/assets/ea37980c-2bab-47fb-9ba2-791cbd3e72f5)

– Customer receives an order confirmation email with order details
![screencapture-mail-google-mail-u-0-2025-05-08-13_50_33](https://github.com/user-attachments/assets/f73b34b8-879c-4d0b-a43d-9505826c50a4)

– Admin can add and remove products from the product list
![screencapture-product-catlog-onrender-admin-catalog-product-add-2025-05-08-14_29_58](https://github.com/user-attachments/assets/ac9164ef-24dd-4026-8d76-8e4e5c333e11)
![screencapture-product-catlog-onrender-products-2025-05-08-14_32_27](https://github.com/user-attachments/assets/d0be2c49-fe73-4f0c-b3e1-995eaeba4435)

## Live Demo

Check out the live demo of the project at the following link:

[Live Demo](https://product-catlog.onrender.com/)
