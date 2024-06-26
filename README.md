# Ecommerce

Welcome to my Ecommerce project!

This project is my personal creation designed to demonstrate my web development skills. It is a complete ecommerce system, with a solid backend developed in Django and a dynamic frontend using JavaScript to provide an exceptional user experience.

## Key features

- **Powerful backend with Django:** The heart of this project is its backend, built with Django, a robust and highly flexible framework that enables the rapid creation of secure and scalable web applications.

- **Fluid interaction between frontend and backend:** Although the main focus of JavaScript is on the frontend for a smooth and interactive user experience, vital connections are also established between the frontend and backend through the use of AJAX, especially in areas such as the shopping cart.

- **Full functionality for administrators:** Administrators have at their disposal a number of powerful tools to manage the site, such as the ability to create products, product categories, promotional banners, coupons and have a robust DashBoard that allows descriptive data analysis on sales and spending.

- For end users, the shopping experience is intuitive and convenient. They can manage their personal information, track their purchases, explore the store with ease, get all product details.

## What will you find in this repository?

- **Well structured and documented code:** All code is organized in a clean and well structured way, with clear comments for easy understanding and collaboration.

- **Easy setup and simple deployment:** I include detailed instructions for setting up the project in your local environment, so you can start exploring and customizing quickly.

## Why is this project special?
This project not only demonstrates my technical skills in web development, but also my ability to create a complete and functional application that spans all stages of the software development process, from initial planning to final deployment. I am excited to share my work with you and hope you find this project as exciting and useful as I have found developing it.


## System requirements

In order to use this project in your local environment, the following requirements must be met:

- **Python 3.8 or higher:** Make sure you have a version of Python equal to or higher than 3.8 installed on your system.

- **MySQL:** This project uses MySQL as database. Make sure you have MySQL installed on your system.

Once you have installed Python and MySQL, you can configure and run the project in your local environment by following the instructions provided below.

## Import or clone repository

**Clone the repository from GitHub:** 

   Use the following command to clone the repository to your local machine:
```bash
git clone https://github.com/DanielFPerezG/ecommerce.git
```

## Project configuration

1. **Create a virtual environment for the project in Python:**.

Enter the project directory and run the following commands to create and activate a virtual environment:

```bash
cd your_project
python3 -m venv venv
```

for Linux/MacOS:
```bash
source venv/bin/activate
```
for Windows:
```bash
venv/scripts/activate
```
This will create a virtual environment in the project directory and activate it.

2. **Install the project's dependencies:**
Once you have the virtual environment activated, you can install the project dependencies by running:
```bash
pip install -r requirements.txt
```
This will install all the libraries and packages needed to run the project in your local environment.

3. **Update database credentials:**
In the project folder go to the file in the path "ecommerce/ecommerce/settings.py" in line 118 you find the content to update the database name, user, password, host and port. Example:
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourDBName',
        'USER': 'yourUser',
        'PASSWORD': 'yourUserPassword',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```
3. **Update email credentials:**
For the email functionalities to work you need to update the credentials in the file in the folder "ecommerce/ecommerce/settings.py" in row 47 and 48. This is necessary for the welcome, password recovery, order in progress and promotional emails to be sent correctly. Please note that if you do not update this information, errors will be generated as these are merely examples.

4. **Perform migrations:**"
It is necessary to perform migrations so that the database creates the necessary tables for the correct operation of the project. You can perform them with the following commands in the terminal in the main path of the project:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

5. **Create super user**:

You need to create a user with the super user attribute to be able to start using the project, you can do this with the following command:

```bash
python3 manage.py createsuperuser
```

5. **Start project**:

Once completed the previous steps you can start the project, keep in mind that the section of the store can be seen in the address "http://127.0.0.1:8000/" and the administrator section can be found in "base.localhost:8000", the administrator can only enter with the credentials of a user with super user permissions, once logged in and you can create in the menu the different products, categories, banners, coupons and email campaigns.