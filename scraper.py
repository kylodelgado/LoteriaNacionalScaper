#!/usr/bin/env python3
"""
Simple Lottery Scraper
---------------------
Scrapes lottery results from conectate.com.do and saves to JSON
"""

import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def setup_browser():
    """Setup Chrome browser in headless mode"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def get_lottery_data(date=None):
    """Get lottery data from website"""
    browser = setup_browser()
    try:
        # Get page content
        url = "https://www.conectate.com.do/loterias/"
        if date:
            url += f"?date={date}"
        browser.get(url)
        html = browser.page_source
        
        # Parse content
        soup = BeautifulSoup(html, 'html.parser')
        data = {
            "date": date or datetime.now().strftime("%Y-%m-%d"),
            "lotteries": {}  # Changed to dictionary for better organization
        }
        
        # Find all sections that contain lottery data
        sections = soup.find_all("section", class_="col-content")
        for section in sections:
            parse_lottery_sections(section, data["lotteries"])
        
        return data
    finally:
        browser.quit()

def parse_lottery_sections(section, lotteries):
    """Parse each lottery section"""
    current_lottery = None
    
    # Iterate through all elements in the section
    for element in section.children:
        if not hasattr(element, 'get'):  # Skip non-tag elements
            continue
            
        # Check if this is a lottery company header
        if "company-block" in element.get("class", []) and "company-title" not in element.get("class", []):
            title = element.find("div", class_="company-title")
            if title and title.find("a"):
                current_lottery = title.find("a").text.strip()
                lotteries[current_lottery] = {
                    "name": current_lottery,
                    "games": []
                }
        
        # If we have a current lottery and this is a game block, parse it
        elif current_lottery and "game-block" in element.get("class", []):
            game_data = parse_game(element)
            if game_data:
                lotteries[current_lottery]["games"].append(game_data)

def parse_game(game_block):
    """Parse game data"""
    title = game_block.find("a", class_="game-title")
    if not title:
        return None
    
    # Get the game time
    session_date = game_block.find("span", class_="session-date")
    time = session_date.text.strip() if session_date else ""
    
    # Get all numbers/scores
    scores = game_block.find_all("span", class_="score")
    numbers = []
    for score in scores:
        score_type = "regular"
        if "special1" in score.get("class", []):
            score_type = "special1"
        elif "special2" in score.get("class", []):
            score_type = "special2"
        elif "bonus" in score.get("class", []):
            score_type = "bonus"
            
        numbers.append({
            "value": score.text.strip(),
            "type": score_type
        })
    
    # Get the game logo URL
    logo_img = game_block.find("div", class_="game-logo").find("img")
    logo_url = ""
    if logo_img:
        # Try to get the src first, if not available use data-src
        logo_url = logo_img.get("src") or logo_img.get("data-src", "")
    
    return {
        "name": title.text.strip(),
        "time": time,
        "numbers": numbers,
        "logo_url": logo_url
    }

def save_results(data, filename="lottery_results.json"):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    try:
        print("Getting lottery results...")
        data = get_lottery_data()
        save_results(data)
        print(f"Results saved to lottery_results.json")
        
        # Print a sample of the data structure
        print("\nSample of saved data:")
        for lottery_name, lottery_data in list(data["lotteries"].items())[:1]:
            print(f"\n{lottery_name}:")
            for game in lottery_data["games"][:1]:
                print(f"  {game['name']}:")
                print(f"    Time: {game['time']}")
                print(f"    Numbers: {[n['value'] for n in game['numbers']]}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 