import time
import re
from io import StringIO
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_premier_league_stats():
    base_url = "https://fbref.com"
    all_matches = pd.DataFrame()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://fbref.com/en/comps/9/2024-2025/Premier-League-Stats")
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    teams_table = soup.find("table", {"id": "results2024-202591_overall"})

    if not teams_table:
        print("Table not found.")
        driver.quit()
        return

    links = [l for l in teams_table.find_all("a", href=True) if '/squads/' in l["href"]]
    team_urls = [base_url + link["href"] for link in links]

    for team_url in team_urls:
        driver.get(team_url)
        time.sleep(1)
        html = driver.page_source
        matches = pd.read_html(StringIO(html), match="Scores & Fixtures")

        soup = BeautifulSoup(html, "html.parser")
        teams_shooting_table = soup.find("a", string="Shooting")

        if not teams_shooting_table or not teams_shooting_table.has_attr("href"):
            print("Shooting link not found.")
            continue

        shooting_url = base_url + teams_shooting_table["href"]
        driver.get(shooting_url)
        time.sleep(1)
        html = driver.page_source
        shooting = pd.read_html(StringIO(html), match=re.compile(r"2024-2025.*: All Competitions"))
        shoot = shooting[0]
        shoot.columns = shoot.columns.droplevel()

        try:
            match_df = matches[0]
            match_df = match_df.merge(
                shoot[["Date", "Comp", "Round", "Sh", "SoT", "Dist", "FK", "PK"]],
                on=["Date", "Comp", "Round"],
                how="left"
            )
        except (ValueError, KeyError, IndexError):
            print(f"Error processing matches for {team_url}. Skipping.")
            continue

        team_data = match_df[match_df["Comp"] == "Premier League"].copy()
        team_data["Season"] = "2024-2025"
        team_data["Team"] = team_url.split("/")[-1].replace("-Stats", " ").replace("-", " ")

        all_matches = pd.concat([all_matches, team_data], ignore_index=True)

    driver.quit()

    all_matches.to_csv("premier_league_2024_2025_team_stats.csv", index=False)
    print("Data saved to premier_league_2024_2025_team_stats.csv")

if __name__ == "__main__":
    scrape_premier_league_stats()
