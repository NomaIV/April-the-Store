# April, the Store

## Project Overview
April, the Store is a Django capstone project, designed as an online secure shopping store specialising in affordable socks and mugs.

## Technologies Used
- Python
- HTML
- CSS
- Django
- SQLite
- Bootsrap
- Heroku (for deployment)

## Repository Link
[Link to repository](https://github.com/NomaIV/April-the-Store)

## Features
Product Catalog:
- Showcase a diverse range of socks and mugs in an organized catalog.
  
Secure Shopping Cart:
- Allow users to easily add products to their shopping cart for a seamless shopping experience.
  
User Accounts:
- Provide user registration and login features for personalized experiences.
  
Checkout and Payment:
- Smooth checkout process with secure payment options for customer convenience.
  
Contact Options:
- Multiple ways to connect with the store, including a physical address, social media links, a newsletter subscription, and a contact number.
  
Product Reviews:
- Allow customers to leave reviews and ratings for products, enhancing trust and transparency.
  
Newsletter Subscription:
- Enable users to subscribe to newsletters for updates on new products, promotions, and store news.
  
Social Media Integration:
- Connect the website with social media platforms to expand reach and engage with the audience.
  
Order History:
- Provide users with access to their order history and order tracking.
  
Responsive Design:
- Ensure the website is accessible and user-friendly on various devices, including desktops, tablets, and smartphones.


### Prerequisites
- Python 3.8
- Docker

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/NomaIV/April-the-Store.git
   ```
2. Navigate to the project directory:
   ```sh
   cd store
   ```
3. Create and activate virtual environment (Optional):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```
5. Running the Django application:
   - Activate the virtual environment (if not already active):
     ```sh
     source venv/bin/activate  # On Windows, use venv\Scripts\activate
     ```
   - Run Dajngo development server:
     ```sh
     python3 manage.py runserver
     ```
6. Building and running with Docker:
   ```sh
   # Build Docker image
   docker build -t april-the-store .

   # Run Docker container
   docker run -p 80:80 april-the-store
   ```

## Usage
To use April, the Store, visit the deployed website and explore the catalog of mugs and socks. Use the shopping cart to add items, register or log in for a personalised shopping experience and use the checkout process. Interact with product reviews, subscribe to the newsletter and engage with the other avaliable contact options.

## Limitations
Please note that this project was developed as part of a capstone, and while it demonstrates many core functionalities, some features are not fully implemented:
- Buy buttons are non-functional.
- Unsuubscribe link is not operational.
- "Connect with us" links (email, newsletter) are not active.
- "Follow us" links (Facebook, Twitter, Instagram) do not function.
- Send us a message submit link is non-functional.
- Search functionality on the website is not operational.

These limitations are part of the project's current state and were included for demonstration purposes.

## Deployment
This project is deployed on Heroku.
[Visit April, the Store](https://aprilthestore-3fb3852f6979.herokuapp.com)

## Licence
This project is lincensed under MIT License. 




