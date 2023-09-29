# **La Posada**
Developed by Michael Roberts

![Am I Responsive](docs/am-i-responsive.png)

💻 [Visit live website](https://pp4-la-posada-a7d4e62f5c13.herokuapp.com/)  
(Ctrl + click to open in new tab)

## Introduction
La Posada is a fictional tapas restaurant in Brighton, England. This website aims to give users an overview of the restaurant and the food and drink available, provide contact details for customers to give feedback and a booking system for users to make reservations, and run a blog where users can stay updated and interact with the restaurant and other users.

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
        * [Website Pages](#website-pages)
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
4.	As a user I want to view the opening hours and details on how to contact the restaurant via email, phone and socials.
5.  As a user I want to create an account so I can make bookings and enquiries and interact with the restaurants blog page.
6.	As a user I want to be able to make a booking at the restaurant quickly and easily.
7.  As a user I want to see clear prompts and confirmation when making a booking or contacting the restaurant.
8.	As a user I want to be able to view all of my bookings, both active and expired.
9.	As a user I want to be able to change or cancel my booking without a long process.
10.  As a user I want to view the site's blog for updates on the restaurant or related articles.


### Admin/Authorised User
11.	As an admin/authorised user I want to be able to log in to the back end admin page.
12.	As an admin/authorised user I want to be able to manually add or amend a booking. 
13.	As an admin/authorised user I want to be able to confirm or reject bookings.
14.	As an admin/authorised user I want to be able to add, edit or remove items from the menus.
15.	As an admin/authorised user I want to be able to add, edit or remove blog posts.
16.	As an admin/authorised user I want to be able to moderate blog post comments before approving them.
17.	As an admin/authorised user I want to be able to search and filter through bookings, blog posts and customer messages.

### Site Owner
18.	As an site owner I want to provide clearly presented contact and booking details to maximise customer interaction.
19.	As an site owner I want validated data entered into my site so that to keep my databases accurate and efficient.


## Design
### Colours
The website was designed to be simple but stylish, the site implements multiple images and forms so use of fonting and color was kept minimal so as not to overload the pages.
Dark grey themes were used for the header and footer with a white background set to the main body of the page. White font color was used against the grey backgrounds and black against the white backgrounds. All pages were tested and validated for contrast.

### Fonts
The fonts selected were Josefin Sans with sans-serif as a backup, sourced from Google Fonts.

### Structure
#### Website Pages
The site was designed to be clearly presented and easy to navigate with a uniform header containing navigation links and footer containing social media links.

- The site consists of the following pages:
  - Homepage featuring images of the restaurant and food available, and a short introduction.
  - Tapas Menu and Drinks Menu pages featuring all menu items with descriptions and prices.
  - Blog page with a list view of blog posts.
  - Expanded blog view displays a post the user has selected so they can read the blog, if they are logged in they can also like and leave a comment which will then need to be approved before it is displayed.
  - Booking page with a booking form that can be submitted by signed in users.
  - View Bookings displays all bookings associated with the users account.
  - Amend Booking allows the user to change their booking details.
  - Cancel Booking allows the user to cancel their booking.
  - Contact Us allows the user to send us a message or enquiry to the restaurant if they are signed in, or can contact us from the displayed email and phone number or visit the address listed.
  - Sign In/Sign Out allows users to access their account to make bookings, make enquiries and interact with the restaurant blog.
  - Sign Up allows the user to register an account with the restaurant.
  - 404 error page to display if a 404 error is raised

#### Database
Built with Python and the Django framework with a Postgres database for the deployed Heroku app.
<hr>
<details><summary>Show Diagram</summary>
    <img src="docs/database-schema.png">
</details>
<hr>

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
Wireframes were created using Balsamiq
<details><summary>Home</summary>
    <img src="docs/wireframes/wireframe-homepage.png">
</details>

<details><summary>Tapas Menu</summary>
    <img src="docs/wireframes/wireframe-tapas-menu.png">
</details>

<details><summary>Drinks Menu</summary>
    <img src="docs/wireframes/wireframe-drink-menu.png">
</details>

<details><summary>Blog</summary>
    <img src="docs/wireframes/wireframe-blog.png">
</details>

<details><summary>Blog Detail</summary>
    <img src="docs/wireframes/wireframe-blog-detail.png">
</details>

<details><summary>Contact Us</summary>
    <img src="docs/wireframes/wireframe-contact.png">
</details>

<details><summary>Booking</summary>
    <img src="docs/wireframes/wireframe-booking.png">
</details>

<details><summary>My Bookings</summary>
    <img src="docs/wireframes/wireframe-my-bookings.png">
</details>

<details><summary>Amend Booking</summary>
    <img src="docs/wireframes/wireframe-amend-booking.png">
</details>

<details><summary>Cancel Booking</summary>
    <img src="docs/wireframes/wireframe-cancel-booking.png">
</details>

<details><summary>Sign Up</summary>
    <img src="docs/wireframes/wireframe-signup.png">
</details>

<details><summary>Sign In</summary>
    <img src="docs/wireframes/wireframe-sign-in.png">
</details>

<details><summary>Sign Out</summary>
    <img src="docs/wireframes/wireframe-sign-out.png">
</details>


## Technologies Used
### Languages & Frameworks
- HTML
- CSS
- Javascript
- Python
- Django

### Libraries & Tools
- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)

## Features
### Header & Navigation
- Page header is fixed at the top of every page
- Includes a navigation bar which collapses to a burger icon with a dropdown menu on small screen sizes
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-navbar.png">
    <img src="docs/features/feature-navbar-collapsed.png">
</details>
<hr>

### Home Page
- Home page includes an image carousel and an introduction section
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-homepage-carousel.png">
    <img src="docs/features/feature-homepage-introduction.png">
</details>
<hr>

### Footer
- At the bottom of every page
- Contains social media links
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-footer.png">
</details>
<hr>

### Sign Up
- A page for users to sign up for an account
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-signup.png">
</details>
<hr>

### Sign In 
- A page for users to login to their account
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-signin.png">
</details>
<hr>

### Sign Out
- A page for users to log out
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-signout.png">
</details>
<hr>

### Booking
- Displays a form for the user to make a booking
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-booking.png">
</details>
<hr>

### My Bookings
- Displays a paginated list of the users bookings
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-my-bookings.png">
</details>
<hr>

### Amend Booking
- Display a form for the user to change their booking details
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-amend-booking.png">
</details>
<hr>

### Cancel Booking
- Allows the user to cancel their booking
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-cancel-booking.png">
</details>
<hr>

### Tapas Menu
- Displays a menu of food items
- Categorised into Salads & Cold Cuts, Hot Dishes, Sides and Desserts
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-tapas-menu-01.png">
    <img src="docs/features/feature-tapas-menu-02.png">
    <img src="docs/features/feature-tapas-menu-03.png">
    <img src="docs/features/feature-tapas-menu-04.png">
    <img src="docs/features/feature-tapas-menu-05.png">
</details>
<hr>

### Drinks Menu
- Displays a menu of drink items
- Categorised into Beers & Ciders, Wines & Sparlking, Cocktails and Spirits
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-drinks-menu-01.png">
    <img src="docs/features/feature-drinks-menu-02.png">
    <img src="docs/features/feature-drinks-menu-03.png">
    <img src="docs/features/feature-drinks-menu-04.png">
</details>
<hr>

### Blog
- Displays a paginated list of blog posts
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-blog.png">
</details>
<hr>

### Blog Detail
- Displays a detailed view of the selected blog post
- Allows the user to like and comment on the post
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-blog-detail-01.png">
    <img src="docs/features/feature-blog-detail-02.png">
    <img src="docs/features/feature-blog-detail-03.png">
</details>
<hr>

### Contact Us
- Displays an embedded Google map with the restaurants address, opening times and phone number
- Displays a form for users to message the restaurant
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-contact-us-01.png">
    <img src="docs/features/feature-contact-us-02.png">
</details>
<hr>

### Footer
- At the bottom of every page
- Contains social media links
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-footer.png">
</details>
<hr>

### Pagination
- Site contains pagination on the blog page and my bookings page
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/features/feature-pagination-blog.png">
    <img src="docs/features/feature-pagination-my-bookings.png">
</details>
<hr>

## Validation
### HTML Validation
The W3C Markup Validation Service
<details><summary>Home</summary>
<img src="docs/validation/validation-html-home.png">
</details>

<details><summary>Tapas Menu</summary>
<img src="docs/validation/validation-html-tapas-menu.png">
</details>

<details><summary>Drink Menu</summary>
<img src="docs/validation/validation-html-drink-menu.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/validation-html-blog.png">
</details>

<details><summary>Contact Us</summary>
<img src="docs/validation/validation-html-contact.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/validation-html-make-booking.png">
</details>

<details><summary>Amend Booking</summary>
<img src="docs/validation/validation-html-amend-booking.png">
</details>

<details><summary>Cancel Booking</summary>
<img src="docs/validation/validation-html-cancel-booking.png">
</details>

<details><summary>Sign Up</summary>
<img src="docs/validation/validation-html-sign-up.png">
</details>

<details><summary>Sign In</summary>
<img src="docs/validation/validation-html-sign-in.png">
</details>

<details><summary>Sign Out</summary>
<img src="docs/validation/validation-html-signout.png">
</details>

### CSS Validation
The W3C Jigsaw CSS Validation Service
<details><summary>style.css</summary>
<img src="docs/validation/validation-css.png">
</details>

### PEP8 Validation
Code Institute's own Python Linter pep8 was used to validate all Python code in this project. All code passed with no errors.

<hr><summary>La Posada</summary><hr>

<details><summary>urls.py</summary>
<img src="docs/validation/pep8-validation-la-posada-urls.png">
</details><hr>

<hr><summary>Home</summary><hr>

<details><summary>urls.py</summary>
<img src="docs/validation/pep8-validation-home-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8-validation-home-views.png">
</details><hr>

<hr><summary>Menus</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/validation/pep8-validation-menus-admin.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8-validation-menus-models.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8-validation-menus-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8-validation-menus-views.png">
</details>
<details><summary>test_models.py</summary>
<img src="docs/validation/pep8-validation-menus-test-models.png">
</details>
<details><summary>test_views.py</summary>
<img src="docs/validation/pep8-validation-menus-test-views.png">
</details>
<details><summary>test_urls.py</summary>
<img src="docs/validation/pep8-validation-menus-test-urls.png">
</details>


<hr><summary>Booking</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/validation/pep8-validation-booking-admin.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8-validation-booking-models.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8-validation-booking-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8-validation-booking-views.png">
</details>
<details><summary>test_models.py</summary>
<img src="docs/validation/pep8-validation-booking-test-models.png">
</details>
<details><summary>test_urls.py</summary>
<img src="docs/validation/pep8-validation-booking-test-urls.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/pep8-validation-booking-forms.png">
</details>


<hr><summary>Blog</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/validation/pep8-validation-blog-admin.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8-validation-blog-models.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8-validation-blog-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8-validation-blog-views.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/pep8-validation-blog-forms.png">
</details>


<hr><summary>Contact</summary><hr>

<details><summary>Admin.py</summary>
<img src="docs/validation/pep8-validation-contact-admin.png">
</details>
<details><summary>models.py</summary>
<img src="docs/validation/pep8-validation-contact-models.png">
</details>
<details><summary>urls.py</summary>
<img src="docs/validation/pep8-validation-contact-urls.png">
</details>
<details><summary>views.py</summary>
<img src="docs/validation/pep8-validation-contact-views.png">
</details>
<details><summary>forms.py</summary>
<img src="docs/validation/pep8-validation-contact-forms.png">
</details>

### Lighthouse
Performance, best practices and SEO was tested using Lighthouse.
<details><summary>Home</summary>
<img src="docs/validation/lighthouse-home.png">
</details>

<details><summary>Tapas Menu</summary>
<img src="docs/validation/lighthouse-tapas-menu.png">
</details>

<details><summary>Drink Menu</summary>
<img src="docs/validation/lighthouse-drink-menu.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/lighthouse-blog.png">
</details>

<details><summary>Blog Detail</summary>
<img src="docs/validation/lighthouse-blog-detail.png">
</details>

<details><summary>Contact Us</summary>
<img src="docs/validation/lighthouse-contact.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/lighthouse-booking.png">
</details>

<details><summary>My Bookings</summary>
<img src="docs/validation/lighthouse-my-bookings.png">
</details>

<details><summary>Amend Booking</summary>
<img src="docs/validation/lighthouse-amend-booking.png">
</details>

<details><summary>Cancel Booking</summary>
<img src="docs/validation/lighthouse-cancel-booking.png">
</details>

<details><summary>Sign Up</summary>
<img src="docs/validation/lighthouse-signup.png">
</details>

<details><summary>Sign In</summary>
<img src="docs/validation/lighthouse-sign-in.png">
</details>

<details><summary>Sign Out</summary>
<img src="docs/validation/lighthouse-sign-out.png">
</details>

### Wave
WAVE was used to test the websites accessibility.

<details><summary>Home</summary>
<img src="docs/validation/validation-wave-home.png">
</details>

<details><summary>Sign Up</summary>
<img src="docs/validation/validation-wave-signup.png">
</details>

<details><summary>Sign In</summary>
<img src="docs/validation/validation-wave-signin.png">
</details>

<details><summary>Tapas Menu</summary>
<img src="docs/validation/validation-wave-tapas-menu.png">
</details>

<details><summary>Drinks Menu</summary>
<img src="docs/validation/validation-wave-drinks-menu.png">
</details>

<details><summary>Booking</summary>
<img src="docs/validation/validation-wave-booking.png">
</details>

<details><summary>Amend Booking</summary>
<img src="docs/validation/validation-wave-amend-booking.png">
</details>

<details><summary>Cancel Booking</summary>
<img src="docs/validation/validation-wave-cancel-booking.png">
</details>

<details><summary>Blog</summary>
<img src="docs/validation/validation-wave-blog.png">
</details>

<details><summary>Blog Expanded</summary>
<img src="docs/validation/validation-wave-blog-expanded.png">
</details>

<details><summary>Contact Us</summary>
<img src="docs/validation/validation-wave-contact.png">
</details>


## Testing
### Manual Testing
1.	As a user I want to know more about the restaurant and get a quick overview.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Home | Enter the site or click the home button or logo to go back to the home page | View the home page with images of the restaurant and food. | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-01-01.png">
    <img src="docs/testing/user-story-testing-01-02.png">
</details>
<hr>

2.	As a user I want to navigate through the sites pages easily to get more information.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Header & Navigation | Click throught the navigation links | Navigation is clear and simple and each page loads correctly | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-02-01.png">
</details>
<hr>

3. As a user I want to view the food and drink menu before I decide to make a booking or not.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Menus | Navigate to the menus dropdown in the nav bar | Find up to date food and drink menus with descriptions and prices | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-03-01.png">
    <img src="docs/testing/user-story-testing-03-02.png">
    <img src="docs/testing/user-story-testing-03-03.png">
    <img src="docs/testing/user-story-testing-03-04.png">
    <img src="docs/testing/user-story-testing-03-05.png">
    <img src="docs/testing/user-story-testing-03-06.png">
</details>
<hr>

4.	As a user I want to view the opening hours and details on how to contact the restaurant via email, phone and socials.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Us | Click on the 'Contact Us' link in the navigation bar and scroll to bottom of page | Find opening hours, contact details and social links in the page footers | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-04-01.png">
</details>
<hr>

5. As a user I want to create an account so I can make bookings and enquiries and interact with the restaurants blog page.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Sign Up | Navigate to the sign up page and enter a username and password | Access previously unavailable features such as table booking, contact form and blog commenting  | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-05-01.png">
</details>
<hr>

6.	As a user I want to be able to make a booking at the restaurant quickly and easily.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Booking | Navigate to the booking page when logged in | Complete the short booking form, and click submit | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-06-01.png">
</details>
<hr>

7. As a user I want to be see clear prompts and confirmation when making a booking.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Booking Confirmed | Make a booking in the Booking page | Submit your booking request and automatically redirect to confirm booking page | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-07-01.png">
    <img src="docs/testing/user-story-testing-07-02.png">
    <img src="docs/testing/user-story-testing-07-03.png">
</details>
<hr>

8.	As a user I want to be able to view all of my bookings, both active and expired.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| View Booking | Navigate to the View Bookings page | See a list view of all bookings associated with your account | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-08-01.png">
</details>
<hr>

9.	As a user I want to be able to change or cancel my booking without a long process.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Amend Booking | Click the Amend or Cancel buttons in the relevant booking | Amend or cancel booking and recieve confirmation | Works as expected |
| Cancel Booking | Click the Amend or Cancel buttons in the relevant booking | Amend or cancel booking and recieve confirmation | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-09-01.png">
    <img src="docs/testing/user-story-testing-09-02.png">
</details>
<hr>

10. As a user I want to view the site's blog for updates on the restaurant or related articles.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Blog | Navigate to the blog page | See a list of blog posts which can be clicked to see full details | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-10-01.png">
    <img src="docs/testing/user-story-testing-10-02.png">
    <img src="docs/testing/user-story-testing-10-03.png">
</details>
<hr>

11.	As an admin/authorised user I want to be able to log in to the back end admin page.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin | Use /admin url extension to access admin login page | Enter admin login details to access the admin hub | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-11-01.png">
</details>
<hr>

12.	As an admin/authorised user I want to be able to manually add or amend a booking.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin | Click on the bookings section in the admin hub | See a list of bookings that can be edited and the option to create a new booking | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-12-01.png">
    <img src="docs/testing/user-story-testing-12-02.png">
    <img src="docs/testing/user-story-testing-12-03.png">
</details>
<hr>

13.	As an admin/authorised user I want to be able to confirm or reject bookings.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin | Click on the relevant booking in the bookings list | See options to confirm or reject booking | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-13-01.png">
    <img src="docs/testing/user-story-testing-13-02.png">
</details>
<hr>

14.	As an admin/authorised user I want to be able to add, edit or remove items from the menus.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin | Go to the tapas menu or drink menu sections in the admin hub | See each menu item that can be edited or removed and the option to create new menu item | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-14-01.png">
    <img src="docs/testing/user-story-testing-14-02.png">
    <img src="docs/testing/user-story-testing-14-03.png">
    <img src="docs/testing/user-story-testing-14-04.png">
    <img src="docs/testing/user-story-testing-14-05.png">
</details>
<hr>

15.	As an admin/authorised user I want to be able to add, edit or remove blog posts.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin | Go to the blog posts section in the admin hub | See a list of blog posts which can be edited or removed and the option to create a new blog post | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-15-01.png">
    <img src="docs/testing/user-story-testing-15-02.png">
    <img src="docs/testing/user-story-testing-15-03.png">
    <img src="docs/testing/user-story-testing-15-04.png">
    <img src="docs/testing/user-story-testing-15-05.png">
    <img src="docs/testing/user-story-testing-15-06.png">
    <img src="docs/testing/user-story-testing-15-07.png">
</details>
<hr>

16.	As an admin/authorised user I want to be able to moderate blog post comments before approving them.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin | Go to blog comments section in admin hub | See a list of blog post comments which can be reviewed before approving | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-16-01.png">
</details>
<hr>

17.	As an admin/authorised user I want to be able to search and filter through bookings, blog posts and customer messages.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Admin | Go to the relevant section in admin hub | See options to filter entries from the booking, blog and contact apps as well as users and accounts  | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-17-01.png">
    <img src="docs/testing/user-story-testing-17-02.png">
    <img src="docs/testing/user-story-testing-17-03.png">
</details>
<hr>

18.	As a site owner I want to provide clearly presented contact and booking details to maximise customer interaction.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Booking | Navigate to the booking page when signed in | See a simple and clearly presented booking form  | Works as expected |
| Contact Us | Navigate to the contact us page | See a map with the restaurants location, opening hours, contact details and a contact form  | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-18-01.png">
    <img src="docs/testing/user-story-testing-18-02.png">
    <img src="docs/testing/user-story-testing-18-03.png">
</details>
<hr>

19.	As a site owner I want validated data entered into my site to keep my databases accurate and efficient.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Booking | Navigate to the booking page | See prompts to reenter information if phone number or email is incorrect or if the booking slot is already filled  | Works as expected |
| Contact | Navigate to the booking page | See prompts to reenter information if phone number or email is incorrect  | Works as expected |
<hr>
<details><summary>Screenshots</summary>
    <img src="docs/testing/user-story-testing-19-01.png">
    <img src="docs/testing/user-story-testing-19-02.png">
    <img src="docs/testing/user-story-testing-19-03.png">
    <img src="docs/testing/user-story-testing-19-04.png">
    <img src="docs/testing/user-story-testing-19-05.png">
</details>
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
The website was tested on the following devices:
- Google Pixel 7
- Samsung Galaxy A7 Lite Tab
- HP Laptop 14
- Apple iMac

The website was tested on the following browsers:
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Safari

## Bugs
| **Bug** | **Fix** |
| ----------- | ----------- |
| Blog page not linking from navigation bar | Correct url pattern by adding 'blog/' to the path |
| Pagination not working on blog page | Change post_list to page_obj |
<hr>

## Heroku Deployment
[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Sign in to heroku.com
<details>
<img src="docs/heroku/heroku-deployment-01.png">
</details>

2. Create an app, give it a name and select a region
<details>
<img src="docs/heroku/heroku-deployment-02.png">
</details>

3. Under resources search for postgres, and add a Postgres database to the app
<details>
<img src="docs/heroku/heroku-deployment-03.png">
</details>

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
<details>
<img src="docs/heroku/heroku-deployment-04.png">
<img src="docs/heroku/heroku-deployment-05.png">
</details>

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
<details>
<img src="docs/heroku/heroku-deployment-06.png">
</details>

4. Create a Procfile
<details>
<img src="docs/heroku/heroku-deployment-07.png">
</details>

5. In settings.py ensure the connection is to the Heroku postgres database unless you are using a test database, store in the env.py file
<details>
<img src="docs/heroku/heroku-deployment-08.png">
<img src="docs/heroku/heroku-deployment-09.png">
</details>

6. Ensure debug is set to false in the settings.py file
<details>
<img src="docs/heroku/heroku-deployment-10.png">
</details>

7. Add localhost, and the herokuapp to the ALLOWED_HOSTS variable in settings.py

8. Run "python3 manage.py showmigrations" to check the status of the migrations

9. Run "python3 manage.py migrate" to migrate the database

10. Run "python3 manage.py createsuperuser" to create a super/admin user

11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories

12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products

13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

14. Disable collectstatic in Heroku before any code is pushed

15. Ensure the following environment variables are set in Heroku
<details>
<img src="docs/heroku/heroku-deployment-11.png">
</details>

16. Connect the app to GitHub
<details>
<img src="docs/heroku/heroku-deployment-12.png">
<img src="docs/heroku/heroku-deployment-13.png">
</details>

17. Click deploy to deploy your application to Heroku for the first time

18. Click on the link provided to access the application

19. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue
<hr>

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

## Credits
### Images
Images used were sourced from Pexels.com and the logo was generated at Looka.com.

### Code
Bootstrap dark navigation theme was used alongside boostrap classes and carousel

## Acknowledgements
- My Code Institute Mentor Mo Shami for his guidance and advice.
- Code Institute learning modules and tutor support.