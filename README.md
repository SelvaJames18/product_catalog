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
![screencapture-product-catlog-onrender-2025-05-08-13_45_19](https://github.com/user-attachments/assets/7acbf36f-c1e8-412f-90ce-c6b3a12d7c66)

– Product section displaying all available products with images, prices, and categories
![screencapture-product-catlog-onrender-products-2025-05-08-13_45_39](https://github.com/user-attachments/assets/e28584fb-8f87-454e-8371-7bc9e6977523)

– Products can be filtered by category
![screencapture-product-catlog-onrender-products-2025-05-08-13_46_00](https://github.com/user-attachments/assets/2d4a1ae2-f6d2-474a-b96c-38a238d62521)

– Products can be searched by their name
![Screenshot 2025-05-08 134642](https://github.com/user-attachments/assets/de1ac65f-ce98-4ac5-ae34-fe6491a97964)

– Cart section to view selected products and their quantities
![screencapture-product-catlog-onrender-cart-2025-05-08-13_47_16](https://github.com/user-attachments/assets/047fa8c0-3878-4d5a-8ba0-442a5be552bb)

– Checkout section to enter customer details and place orders
![screencapture-product-catlog-onrender-checkout-2025-05-08-13_47_56](https://github.com/user-attachments/assets/79712dff-0152-430b-9443-4087ad62b379)

– Order confirmation page
![screencapture-product-catlog-onrender-order-confirm-2025-05-08-13_48_15](https://github.com/user-attachments/assets/b9db4be8-64ba-4048-bd99-debc1c9bc040)

– Admin panel login page for managing products and orders
![screencapture-product-catlog-onrender-admin-login-2025-05-08-13_51_07](https://github.com/user-attachments/assets/8b3a5289-2ca3-4c6e-b92c-d7f27e31cfc3)
![screencapture-product-catlog-onrender-admin-2025-05-08-13_48_45](https://github.com/user-attachments/assets/cf9056f4-0252-493f-ae4b-deca4a2bc286)

– Admin view to see customer orders with product details and quantities
![screencapture-product-catlog-onrender-admin-catalog-order-66-change-2025-05-08-13_49_17](https://github.com/user-attachments/assets/00069b1f-2a33-4598-94e4-aaaa27288147)

– Customer receives an order confirmation email with order details
![screencapture-mail-google-mail-u-0-2025-05-08-13_50_33](https://github.com/user-attachments/assets/95e1971b-9d47-40a0-966c-74619ecfde6d)

– Admin can add and remove products from the product list
![screencapture-product-catlog-onrender-admin-catalog-product-add-2025-05-08-14_29_58](https://github.com/user-attachments/assets/4e42a8ad-711f-4614-b214-f0785314fc3a)
![screencapture-product-catlog-onrender-products-2025-05-08-14_32_27](https://github.com/user-attachments/assets/288238e6-a2f2-48a6-a49f-df22fb7d8384)

## Live Demo

Check out the live demo of the project at the following link:

[Live Demo](https://product-catlog.onrender.com/)
