from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from datetime import datetime

# Launch Chrome Browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# Open CoinMarketCap
driver.get("https://coinmarketcap.com/")

# Wait for page load
time.sleep(5)

# Get table rows
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

# Store data
crypto_data = []

# Extract Top 10 Coins
for row in rows[:10]:
    try:
        name = row.find_element(By.XPATH, ".//td[3]").text
        price = row.find_element(By.XPATH, ".//td[4]").text
        change_24h = row.find_element(By.XPATH, ".//td[5]").text
        market_cap = row.find_element(By.XPATH, ".//td[8]").text

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        crypto_data.append([
            name,
            price,
            change_24h,
            market_cap,
            timestamp
        ])

    except Exception as e:
        print("Error:", e)

# Create DataFrame
df = pd.DataFrame(
    crypto_data,
    columns=[
        "Coin Name",
        "Price",
        "24H Change",
        "Market Cap",
        "Timestamp"
    ]
)

# Display data
print("\nTop 10 Cryptocurrency Data:\n")
print(df)

# Save CSV File
df.to_csv("crypto_prices.csv", index=False)

print("\nData saved successfully to crypto_prices.csv")

# Browser open ஆக இருக்கும்
input("\nPress Enter to close browser...")

# Browser close
driver.quit()