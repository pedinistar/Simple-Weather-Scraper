# Simple Weather Scraper

## Description

This project is a simple weather scraper built using Python and Selenium. It demonstrates basic web automation skills by fetching current weather information for a user-specified city using Google search results.

The script does the following:
1. Prompts the user to enter a city name
2. Opens Google in a Chrome browser
3. Searches for the weather in the specified city
4. Extract the current temperature and weather condition
5. Displays the results to the user

This project is a basic example of using Selenium for web scraping and automation tasks.

## Requirements

- Python 3.x
- Selenium WebDriver
- ChromeDriver

## Installation

1. Ensure you have Python installed on your system.
2. Install Selenium using pip:
   ```
   pip install selenium
   ```
3. Download ChromeDriver and add it to your system PATH.

## Usage

Run the script using Python:
```
python scraper.py
```


When prompted, enter the city name where you want to check the weather.

## Note

This project is for educational purposes only and demonstrates basic Selenium usage. It relies on Google's search results format, which may change over time. For production use or more reliable weather data, consider using a dedicated weather API.
