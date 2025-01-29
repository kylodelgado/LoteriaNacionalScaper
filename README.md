# Lottery Scraper

A Python script to scrape lottery results from conectate.com.do. The script collects data for various Dominican lottery games and saves the results in JSON format.

## Features
- Scrapes current day lottery results
- Supports historical data retrieval
- Saves data in organized JSON format
- Handles multiple lottery companies and games

## Installation
1. Clone this repository
2. Create a virtual environment:
```python
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install dependencies:
```python
pip install -r requirements.txt
```

## Usage
Run the script:
```python
python scraper.py
```

For historical data, specify a date:
```python
python scraper.py --date YYYY-MM-DD
```

## Data Structure
The data is saved in JSON format with the following structure:
```json
{
    "date": "YYYY-MM-DD",
    "companies": [
        {
            "name": "Company Name",
            "games": [
                {
                    "name": "Game Name",
                    "numbers": ["XX", "YY", "ZZ"],
                    "time": "HH:MM"
                }
            ]
        }
    ]
}
``` 