# Final capital consists of two functions: first, determine de current annual rate (according to SP 500 yield)
# Then, determine de amount of final capital expected from annual rate, principal, contributions and compounding 
# periods

# Tags: datetime, functions, csv files, convert str to date, difference between dates, aritmetic operations like addition, subtraction, multiplication, division and power, compound interest, finance, file handling, unittest, error handling, exceptions handling
    
def get_annual_rate():

    # Import libraries
    import datetime as dt
    import pandas

    #1 Read file with S&P 500 historical prices
    file = pandas.read_csv(r'C:\Users\User\OneDrive\Projects\web scrapping\scraping\snp-prices.csv')

    #2 Get latest and oldest date

    first_row = file.head(1).values.tolist()[0]
    last_row = file.tail(1).values.tolist()[0]

    oldest_date = (first_row[0])
    oldest_date = dt.datetime.strptime(oldest_date,'%m/%d/%Y')

    latest_date = (last_row[0]) 
    latest_date = dt.datetime.strptime(latest_date,'%m/%d/%Y')

    #3 Get latest and oldest price
    oldest_price = float(first_row[1])
    latest_price = float(last_row[1])

    #4 Calculate rate of return on a single compounding
    total_rate = latest_price/oldest_price

    #5 Calculate total period corresponding to the total_rate
    total_time = (latest_date - oldest_date).days/365

    #6 Calculate expected_rate
    annual_rate = (total_rate ** (1/total_time) - 1) * 100

    #7 Return expected_rate
    return annual_rate 
        
def get_final_capital(principal,contribution,compounding_periods):
    
    import datetime
    import pandas
    import csv

    parameters = [principal,contribution,compounding_periods]
    
    # Flow control
    for p in parameters:
        if type(p) != int or (p < 0):   
            raise ValueError('Enter integer numbers greaters than zero')
      
    # Inputs 
    annual_rate = get_annual_rate()
    monthly_rate = ((1 + annual_rate/100) ** (1/12) - 1) * 100
    
    # Outputs

    # From principal
    fc_principal = principal * ((1 + annual_rate/100) ** (compounding_periods))
    try:
        principal_growth = round(fc_principal/principal,2)
    except ZeroDivisionError:
        principal_growth = 0
    
    # From contributions
    year = compounding_periods
    fc_contribution = 0
    
    while year > 0:
        month = 11
        capital_first_year = 0
        while month >= 0: 
            month_capitalized = contribution * ((1 + monthly_rate/100) ** (12 - month))
            capital_first_year += month_capitalized
            month -= 1
        year_capitalized = capital_first_year * (1 + annual_rate/100) ** (10 - year)
        fc_contribution += year_capitalized
        year -= 1
    
    final_capital = fc_principal + fc_contribution

    # Export data into csv
    # Create date stamp
    today = datetime.date.today()

    # Create headers and data list
    data = [today,principal,contribution,compounding_periods,annual_rate,final_capital,principal_growth]
    headers = ['date','principal','contributions','n','annual rate','final capital','principal growth']

    # Create file
    #with open('final-capital.csv','w',newline= '',encoding='UTF8') as f:
    #    writer = csv.writer(f)
    #    writer.writerow(headers)
    #   writer.writerow(data)
    
    # Read csv file already created
    pandas.read_csv(r'C:\Users\User\OneDrive\Projects\web scrapping\interest rate\final-capital.csv')
    
    # Append new data
    with open('final-capital.csv','a+',newline='',encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

    return round(final_capital,2), principal_growth

print(get_final_capital(1000,0,5))