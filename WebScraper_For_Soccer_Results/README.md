Premier League Stats Scraper
This Python script scrapes Premier League match and shooting statistics from the FBref website for the 2024-2025 season. The data is then saved into a CSV file for further analysis.

Requirements
Python 3.x

Selenium

BeautifulSoup

pandas

webdriver-manager

You can install the required dependencies using the following:

bash
Copy
Edit
pip install selenium beautifulsoup4 pandas webdriver-manager
How to Use
Clone this repository (or save the script to your local machine).

Install the required dependencies by running:

bash
Copy
Edit
pip install -r requirements.txt
Make sure you have Google Chrome installed on your machine, as the script uses ChromeDriver.

Run the script:

bash
Copy
Edit
python premier_league_scraper.py
The script will scrape match and shooting stats for all Premier League teams in the 2024-2025 season.

After completion, a CSV file named premier_league_2024_2025_team_stats.csv will be saved in your working directory.

Code Overview
scrape_premier_league_stats()
This function performs the following steps:

Navigates to the Premier League stats page on FBref.

Extracts the team URLs from the table containing the team links.

For each team, it:

Scrapes the team’s match stats.

Scrapes the team's shooting stats.

Merges both datasets on the date, competition, and round columns.

Adds season and team name information.

The final data is saved into a CSV file.

Dependencies:
Selenium is used for web scraping dynamic content (i.e., pages rendered by JavaScript).

BeautifulSoup is used for parsing the HTML content.

Pandas is used for handling and saving the data into a CSV file.

webdriver-manager automatically handles ChromeDriver installation.

Notes
Make sure to have a stable internet connection as the script fetches data from external sources.

If you encounter any errors due to webpage structure changes, please check if FBref has updated the page structure.

License
This script is open-source and available under the MIT License. Feel free to fork or modify it!