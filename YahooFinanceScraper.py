# WEB SCRAPER
# It consists of downloading S&P500 index price data, once a day, from yahoo finance web. Then, store it in a csv file.

# Tags: beautifulSoup, web scraping, datetime, csv, pandas, file handling, incremental ETL, html, function

# Create function to get_data

def get_data(symbol):
    # Import libraries
    from bs4 import BeautifulSoup
    import requests
    import datetime
    import csv 
    import pandas as pd

    # Connect to website
    url = f'https://finance.yahoo.com/quote/{symbol}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Extract price and change
    price = soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
    change = soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
    change_percentage = soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    change_percentage = change_percentage.strip('()')

    # Create date stamp
    today = datetime.date.today()

    # Create data list
    data = [today,price,change,change_percentage]

    # Read csv file already created
    pd.read_csv(r'[C:\Users\User\OneDrive\Projects\web scrapping\investment-simulator\SnpPrices.csv]')
    
    # Append new data
    with open('SnpPrices.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Run
stock = '^GSPC'
get_data(stock)

# Schedule code running once a day
#while(True):
#    get_data(stock)
#    seconds_per_day = 24*60*60
#    time.sleep(seconds_per_day)


 