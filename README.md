# GitHub Profile Image Scraper

## Overview

This Flask web application is a simple tool that allows users to retrieve the profile image of a GitHub user. Users can input a GitHub username, and the application will scrape the user's GitHub page to find and display the profile image.

## Features

- User Input: Users can provide a GitHub username via a form.
- Web Scraping: The application utilizes web scraping techniques to extract the profile image from the specified GitHub user's page.
- Display: The retrieved profile image is displayed on the web page.

## Technologies Used

- Flask: The web framework used for building the application.
- Requests: A library for making HTTP requests to fetch the GitHub user's page.
- Beautiful Soup: A library for pulling data out of HTML, used here for parsing the GitHub user's page.

## How to Use

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/tusharpamnani/GitHub-WebScrapper.git

2. Install the required dependencies.
   ```bash
   pip install -r requirements.txt

3. Run the Flask application.
   ```bash
   python app.py

4. Open your web browser and go to http://127.0.0.1:5000/ to access the application.

5. Enter a GitHub username in the provided form and submit to see the profile image. 

## Notes

The application uses web scraping, which may be subject to changes on the GitHub website. It's advised to review and update the scraping logic if GitHub's HTML structure changes.

## Acknowledgments

This application is a simple demonstration of web scraping and using Flask for web development.
