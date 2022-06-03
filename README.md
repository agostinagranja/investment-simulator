# Investment Simulator
### Scraping of prices of the S&P 500 index and simulation of the result of an investment in it.

## Industry
Finance

## Problem
There is a need for a tool that allows the result of a diversified investment in the US capital market to be simulated in a personalized way. The data needed to simulate this result are:
• Rate offered by the market
• Initial capital and/or the amount of periodic contributions
• Investment horizon

Parameters 2 and 3 are defined by the user, while the rate offered by the United States market for a diversified and passive investment, that is, one that does not require effort on the part of the user or management by third parties, is generally represented by the compound interest rate of the S&P 500 index.

## Project objective
Extract the daily closing prices of the S&P 500 index and make it available in a centralized database, which serves as a supply for the calculation of the annualized rate of return, defined as a compound interest rate. Then, that allows, together with the parameters entered by the user, to determine the estimated result (final capital) of the investment.

## Implementation process
1. Obtaining data from external sources:
* S&P 500 price (Source: Yahoo Finance)
* User parameters
2. Python script development
* Incremental ETL
* Automation: frequency -> once a day
* Rate of return calculation
* Calculation of final capital
* Storage of simulations carried out in csv file
3. Script testing
* Black Box Tests

##### Diagram

/assets/images/electrocat.png

## Results
* Historical data of the S&P 500 index with incremental loading every 24 hours, centralized in database in csv file
* Calculation of interest rate updated daily
* S&P 500 investment simulator 
* Error handling and alerts
