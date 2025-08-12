# Premier League Stats Scraper

This Python script scrapes Premier League match and shooting statistics from the FBref website for the 2024-2025 season. The collected data is saved as a CSV file for further analysis.

---

## Features

- Scrapes match stats and shooting stats for all Premier League teams.
- Combines match and shooting data based on date, competition, and round.
- Saves the cleaned dataset into a CSV file for easy use in analysis or modeling.

---

## Requirements

- Python 3.x
- Google Chrome browser installed (required by ChromeDriver)
- Python packages:
  - selenium
  - beautifulsoup4
  - pandas
  - webdriver-manager
  - lxml
  - html5lib

---

## Installation

1. Clone this repository or download the script to your local machine.

2. Install the required Python dependencies with:

   ```bash
   pip install -r requirements.txt

## Running Scraper

   python scraper.py


---

## How It Works

The core function scrape_premier_league_stats() performs the following:

Navigates to the Premier League stats page on FBref.

Extracts all team URLs from the main table.

## For each team:

Scrapes match stats.

Scrapes shooting stats.

Merges both datasets on Date, Comp, and Round.

Adds Season and Team information.

Combines all team data into a single DataFrame.

Saves the combined data as a CSV file.

---


## Notes
Ensure a stable internet connection during scraping.

The script relies on the FBref page structure — if the website changes, the scraper may need updating.

ChromeDriver is automatically managed by webdriver-manager.
