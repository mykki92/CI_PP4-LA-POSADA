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
- Find information on a local tapas restaurant and be able to see a menu.
- Be able to make a booking at the restaurant which I can later change or cancel.
- Be able to contact the restaurant with any other enquiries.
- Be able to view and interact with the restaurants blog.

### Site Owner Goals
- To attract more business and generate bookings with a well crafted site.
- Provide clear information and easy navigation throughout the site.
- Make the site fully responsive and accessible.

## User Experience
### Target Audience
- People who want to book a table at a tapas restaurant for a meal or a party.
- Tourists visiting the area that are looking for a tapas restaurant.
- People employed in the area to eat and drink after work.

### User Requirements
- Fully responsive
- Accessible
- Clear and simple navigation and site interaction
- Contact information

## User Stories
### User
1.	As a user I want to know more about the restaurant and get a quick overview.
2.	As a user I want to navigate through the sites pages easily to get more information.
3.  As a user I want to view the food and drink menu before I decide to make a booking or not.
3.	As a user I want to view the opening hours and details on how to contact the restaurant via email, phone and socials.
8.  As a user I want to create an account so I can make bookings and enquiries and interact with the restaurants blog page.
4.	As a user I want to be able to make a booking at the restaurant quickly and easily.
7.  As a user I want to be see clear prompts and confirmation when making a booking or contacting the restaurant.
6.	As a user I want to be able to view all of my bookings, both active and expired.
5.	As a user I want to be able to change or cancel my booking without a long process.
9.  As a user I want to view the site's blog for updates on the restaurant or related articles.


### Admin/Authorised User
11.	As an admin/authorised user I want to be able to log in to the back end admin page.
12.	As an admin/authorised user I want to be able to manually add or amend a booking. 
13.	As an admin/authorised user I want to be able to confirm or reject bookings.
14.	As an admin/authorised user I want to be able to add, edit or remove items from the menus.
15.	As an admin/authorised user I want to be able to add, edit or remove blog posts.
16.	As an admin/authorised user I want to be able to moderate blog post comments before approving them.
17.	As an admin/authorised user I want to be able to search and filter through bookings, menus, blog posts and customer messages.

### Site Owner
18.	As an site owner I want to provide a fully responsive site to ensure a good user experience for my customers and admin.
19.	As an site owner I want validated data entered into my site so that to keep my databases accurate and efficient.
20.	As an site owner I want to provide clearly presented contact and booking details to maximise customer interaction.


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
1.	As a user I want to know more about the restaurant and get a quick overview.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Home | Enter the site or click the home button or logo to go back to the home page | View the home page with images of the restaurant and food. | Works as expected |
<hr>


2.	As a user I want to navigate through the sites pages easily to get more information.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Header & Navigation | Click throught the navigation links | Navigation is clear and simple and each page loads correctly | Works as expected |
<hr>

3. As a user I want to view the food and drink menu before I decide to make a booking or not.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Menus | Navigate to the menus dropdown in the nav bar | Find up to date food and drink menus with descriptions and prices | Works as expected |
<hr>

4.	As a user I want to view the opening hours and details on how to contact the restaurant via email, phone and socials.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Us | Click on the 'Contact Us' link in the navigation bar and scroll to bottom of page | Find opening hours, contact details and social links in the page footers | Works as expected |
<hr>

5. As a user I want to create an account so I can make bookings and enquiries and interact with the restaurants blog page.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Sign Up | Navigate to the sign up page and enter a username and password | Access previously unavailable features such as table booking, contact form and blog commenting  | Works as expected |
<hr>

6.	As a user I want to be able to make a booking at the restaurant quickly and easily.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Booking | Navigate to the booking page when logged in | Complete the short booking form, submit and recieve confirmation | Works as expected |
<hr>

7. As a user I want to be see clear prompts and confirmation when making a booking.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Booking Confirmed | Make a booking in the Booking page | Submit your booking request and automatically redirect to confirm booking page | Works as expected |
<hr>

8.	As a user I want to be able to view all of my bookings, both active and expired.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| View Booking | Navigate to the View Bookings page | See a list view of all bookings associated with your account | Works as expected |
<hr>

9.	As a user I want to be able to change or cancel my booking without a long process.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Amend Booking | Click the Amend or Cancel buttons in the relevant booking | Amend or cancel booking and recieve confirmation | Works as expected |
| Cancel Booking | Click the Amend or Cancel buttons in the relevant booking | Amend or cancel booking and recieve confirmation | Works as expected |
<hr>

10. As a user I want to view the site's blog for updates on the restaurant or related articles.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Blog | Navigate to the blog page | See a list of blog posts which can be clicked to see full details | Works as expected |
<hr>

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
