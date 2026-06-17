# cryptocurrency_price_tracker
A Python Selenium-based web scraping project that extracts real-time cryptocurrency prices, 24-hour changes, and market capitalization from CoinMarketCap and stores the data in CSV format for analysis and tracking.
# Cryptocurrency Price Tracker

## Project Overview

The Cryptocurrency Price Tracker is a Python-based web scraping project that uses Selenium to collect real-time cryptocurrency market data from CoinMarketCap. The application automatically extracts information such as coin name, current price, 24-hour price change, and market capitalization for the top cryptocurrencies.

The collected data is stored in CSV format for analysis, monitoring, and historical tracking.

## Features

- Live cryptocurrency price scraping
- Dynamic page handling using Selenium WebDriver
- Top 10 cryptocurrency data extraction
- CSV data export
- Headless browser support
- Historical data logging with timestamps
- Custom filtering for price and percentage changes

## Technologies Used

- Python
- Selenium
- Pandas
- WebDriver Manager
- Google Chrome
- ChromeDriver

## Project Structure

```text
Cryptocurrency-Price-Tracker/
│
├── cryptocurrency_price_tracker.py
├── requirements.txt
├── README.md
└── crypto_prices.csv
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Cryptocurrency-Price-Tracker.git
cd Cryptocurrency-Price-Tracker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the project using:

```bash
python cryptocurrency_price_tracker.py
```

## Sample Output

| Coin | Price | 24h Change | Market Cap |
|--------|--------|------------|------------|
| Bitcoin | $108,000 | +2.5% | $2.1T |
| Ethereum | $5,800 | +3.1% | $700B |

## Outcomes

- Real-time market monitoring
- Historical trend analysis
- Automated cryptocurrency tracking
- Dashboard-ready CSV data
- Portfolio monitoring support

## Future Enhancements

- Email alerts
- Telegram notifications
- Streamlit dashboard
- Database integration
- Scheduled scraping

## Author

Santhiya MUniyandi
