# Dominican Lottery Scraper

A Python script that scrapes lottery results from conectate.com.do. The script collects data from various Dominican lottery games and saves the results in a structured JSON format.

## Project Structure
```
LoteriaNacionalScaper/
├── scraper.py          # Main scraping script
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## Requirements
- Python 3.6 or higher
- Google Chrome browser installed
- Internet connection

## Dependencies
The script uses the following Python packages:
- beautifulsoup4 - For HTML parsing
- selenium - For browser automation
- webdriver-manager - For Chrome WebDriver management

## Setup Instructions

1. Clone the repository:
```bash
git clone git@github.com:kylodelgado/LoteriaNacionalScaper.git
cd LoteriaNacionalScaper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
Run the script to get today's results:
```bash
python scraper.py
```

The script will:
1. Launch a headless Chrome browser
2. Fetch the lottery website content
3. Parse all lottery data
4. Save results to `lottery_results.json`

### Output Format
The data is saved in JSON format with the following structure:
```json
{
    "date": "YYYY-MM-DD",
    "lotteries": {
        "Nacional": {
            "name": "Nacional",
            "games": [
                {
                    "name": "Game Name",
                    "time": "DD-MM",
                    "numbers": [
                        {
                            "value": "XX",
                            "type": "regular|special1|special2|bonus"
                        }
                    ],
                    "logo_url": "https://example.com/logo.png"
                }
            ]
        }
    }
}
```

### Data Fields
- `date`: The date of the results
- `lotteries`: Dictionary of lottery companies
  - `name`: Lottery company name
  - `games`: List of games for this lottery
    - `name`: Game name
    - `time`: Time of the draw
    - `numbers`: List of drawn numbers with their types
    - `logo_url`: URL of the game's logo

## Development Notes

### Project Files
- `scraper.py`: Contains the main scraping logic using Selenium and BeautifulSoup
- `requirements.txt`: Lists all Python package dependencies
- `.gitignore`: Configured to ignore Python artifacts, logs, and environment-specific files

### Chrome WebDriver
The script uses `webdriver-manager` to automatically handle Chrome WebDriver installation and updates. No manual WebDriver installation is needed.

### Error Handling
The script includes basic error handling for:
- Network issues
- HTML parsing errors
- Browser automation problems

## Future Improvements
- Add command-line arguments for date selection
- Implement historical data scraping
- Add data validation
- Include more detailed error logging
- Add retry mechanisms for failed requests

## Troubleshooting
1. If Chrome fails to start:
   - Ensure Google Chrome is installed
   - Try running without headless mode (remove '--headless' option)
   - Check Chrome version compatibility

2. If parsing fails:
   - Check internet connection
   - Verify the website structure hasn't changed
   - Check console for specific error messages

## Contributing
Feel free to fork the repository and submit pull requests for any improvements.

## License
This project is open-source and available under the MIT License. 