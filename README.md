# **La Posada**
Developed by Michael Roberts

💻 [Visit live website]()  
(Ctrl + click to open in new tab)

## Introduction

## Table of Contents
* [Project Goals](#project-goals)
    * [User Goals](#user-goals)
    * [Site Owner Goals](#site-owner-goals)
* [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Requirements](#user-requirements)
* [User Stories](#user-stories)
    * [User](#user)
    * [Admin/Authorised User](#admin/authorised_user)
    * [Site Owner](#site_owner)
* [Design](#design)
    * [Colours](#colours)
    * [Fonts](#fonts)
    * [Structure](#structure)
        * [Website pages](#website-pages)
        * [Database](#database)
    * [Wireframes](#wireframes)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Validation](#validation)
* [Testing](#testing)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Device Testing & Browser Compatibility](#device-testing--browser-compatibility)
* [Bugs](#bugs)
* [Heroku Deployment](#heroku-deployment)
    * [Fork Repository](#fork-repository)
    * [Clone Repository](#clone-repository)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)


## Project Goals
### User Goals
- To create a table booking
- To be able to view edit and cancel bookings
- To view menus, a blog and contact info

### Site Owner Goals
- To provide a solution to allow users to book a table online
- To attract more business with a well crafted site
- Provide a modern application with an easy navigation
- Fully responsive and accessible

## User Experience
### Target Audience

### User Requirements

## User Stories
### User
1.	As a user I want to know more about the restaurant and get a quick overview.
2.	As a user I want to navigate through the sites pages easily to get more information.
3.	As a user I want to view the opening hours and details on how to contact the restaurant via email, phone and socials.
4.	As a user I want to be able to make a booking at the restaurant quickly and easily.
5.	As a user I want to be able to change or cancel my booking without a long process.
6.	As a user I want to be able to view all of my bookings, both active and expired.
7. As a user I want to be see clear prompts and confirmation when making a booking or contacting the restaurant.
8. As a user I want to create an account so I can make bookings and enquiries and interact with the restaurants blog page.
9. As a user I want to view the site's blog for updates on the restaurant or related articles.
10. As a user I want to view the food and drink menu before I decide to make a booking or not.

### Admin/Authorised User
11.	As an admin/authorised user I want to be able to log in to the back end admin page.
12.	As an admin/authorised user I want to be able to manually add or amend a booking. 
13.	As an admin/authorised user I want to be able to confirm or reject bookings.
14.	As an admin/authorised user I want to be able to add, edit or remove items from the menus.
15.	As an admin/authorised user I want to be able to add, edit or remove blog posts.
16.	As an admin/authorised user I want to be able to moderate blog post comments before approving them.
17.	As an admin/authorised user I want to be able to search and filter through bookings, menus, blog posts and customer messages.

### Site Owner
16.	As an site owner I want to provide a fully responsive site to ensure a good user experience for my customers and admin.
16.	As an site owner I want validated data entered into my site so that to keep my databases accurate and efficient.
16.	As an site owner I want to provide clearly presented contact and booking details to maximise customer interaction.


## Design
### Colours

### Fonts

### Structure
#### Website Pages

#### Database
Built with Python and the Django framework with a Postgres database for the deployed Heroku app.
##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

##### TapasItem Model
The TapasItem Model contains the following:
- tapas_id
- tapas_name
- description
- tapas_price
- plato_price
- sides_price
- dessert_price
- tapas_type

##### DrinkItem Model
The DrinkItem Model contains the following:
- drink_id
- drink_name
- description
- glass_price
- bottle_price
- drink_price
- drink_type

##### Table Model
The Table Model contains the following:
- table_id (PrimaryKey)
- table_number
- seats

##### Booking Model
The Booking Model contains the following:
- booking_id (PrimaryKey)
- created_on
- booking_date
- booking_time
- table (ForeignKey)
- user (ForeignKey)
- name
- email
- phone
- status
- seats
- party_of

##### Post Model
The Post Model contains the following:
- title
- slug
- post_id (PrimaryKey)
- author (ForeignKey)
- created_on
- updated_on
- content
- image
- excerpt
- status
- likes

##### Comment Model
The Comment Model contains the following:
- post (ForeignKey)
- name
- email
- body
- created_on
- approved

##### ContactUs Model
The ContactUs Model contains the following:
- message_id (PrimaryKey)
- message_date
- user (ForeignKey)
- name
- email
- phone
- message

### Wireframes

## Technologies Used
### Languages & Frameworks

### Libraries & Tools

## Features
### Home Page

### Header & Navigation

### Footer

### Sign Up

### Sign In 

### Sign Out

### Booking

### My Bookings

### Amend Booking

### Cancel Booking

### Tapas Menu

### Drinks Menu

### Blog

### Blog Detail

### Comments

### Contact Us

### Pagination

## Validation
### CSS Validation

### JavaScript Validation

### PEP8 Validation

### Lighthouse

### Wave

## Testing
### Manual Testing


### Automated Testing
- Testing was done using the built in Django module, unittest.

<details><summary>Menu App, test_models.py</summary>
<img src="docs/testing/unittest_menus_test_models.png" alt="A screenshot of menu app models testing">
</details>

<details><summary>Menu App, test_views.py</summary>
<img src="docs/testing/unittest_menus_test_views.png" alt="A screenshot of menu app views testing">
</details>

<details><summary>Menu App, test_urls.py</summary>
<img src="docs/testing/unittest_menus_test_urls.png" alt="A screenshot of menu app urls testing">
</details>

<details><summary>Booking App, test_models.py</summary>
<img src="docs/testing/unittest_booking_test_models.png" alt="A screenshot of booking app models testing">
</details>

<details><summary>Booking App, test_urls.py</summary>
<img src="docs/testing/unittest_booking_test_urls.png" alt="A screenshot of booking app urls testing">
</details>

### Device Testing & Browser Compatibility

## Bugs

## Heroku Deployment
### Fork Repository

### Clone Repository

## Credits
### Images

### Code

## Acknowledgements
