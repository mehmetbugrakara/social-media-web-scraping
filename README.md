****Web Scraping Application****

This project is a web scraping application developed in Python for extracting data from LinkedIn, Instagram, and a news website. This application utilizes libraries such as Instaloader, Selenium, and BeautifulSoup.

**Installation Packages**

pip install -r requirements.txt

**Installing Drivers**

Selenium WebDriver

As we'll be automating web browsers using Selenium WebDriver, we need to download the appropriate WebDriver for the browser we'll be using. 

For Chrome users:

Download the latest version of[ ChromeDriver](https://chromedriver.chromium.org/downloads) and place it in an appropriate location on your system.

For Moziila users:

Download the latest version of[ Geckodriver](https://github.com/mozilla/geckodriver/releases) and place it in an appropriate location on your system.

**Usage**

1. LinkedIn Data Extraction
   1. Run the “**linkedin\_scraping.py**” file
   1. Sace the relevant data to a CSV file
1. Instagram Data Extraction
   1. Run the “**instagram\_scraping.py**” file
   1. Sace the relevant data to a CSV file
1. News Website Data Extraction
   1. Run the “**news\_scraping.py**” file
   1. Sace the relevant data to a CSV file

The data obtained after running each file will be stored in CSV format within the data folder.

**General Purpose**

This web scraping application is used to collect data from a specific LinkedIn profile, Instagram user, or a news website. It extracts profile information and media content from LinkedIn and Instagram, while extracting article titles and texts from the news website.

**Notes**

- No login credentials or authentication processes are required for scraping LinkedIn or Instagram. 
- For scraping the news website, data is extracted using BeautifulSoup from specific HTML tags, so specific adjustments may be required for each news website. 

Please be sure to adhere to the terms of use of the target websites while using this project and utilize data extraction methods permitted by them.





