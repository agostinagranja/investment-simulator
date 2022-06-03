# Investment Simulator
### Scraping of prices of the S&P 500 index and simulation of the result of an investment in it.

## Industry
Finance

## Problem
There is a need for a tool that allows the result of a diversified investment in the US capital market to be simulated in a personalized way. The data needed to simulate this result are:

1. Rate offered by the market
2. Initial capital and/or 
3. Amount of periodic contributions
4. Investment horizon

Parameters from 2 to 4 are defined by the user, while the rate offered by the United States market for a diversified and passive investment, that is, one that requires minimum effort on the part of the user or none management by third parties, is generally represented by the compound interest rate of the S&P 500 index.

## Project objective
Extract the daily closing prices of the S&P 500 index and make it available in a centralized database, which serves as a supply for the calculation of the annualized rate of return, defined as a compound interest rate. Then, that allows, together with the parameters entered by the user, to determine the estimated result (final capital) of the investment.

## Implementation process
1. Obtaining data from external sources:
   * S&P 500 price (Source: Yahoo Finance)
2. Python script development
   * Incremental ETL
   * Automation: frequency -> once a day
   * Calculation of compound interest rate
   * Calculation of final capital
   * Storage of simulations carried out in csv file
3. Script testing
   * Black Box Tests

### Diagram

<img src="https://github.com/agostinagranja/investment-simulator/blob/main/diagram.jpg" width="700"> 

## Results
* Historical data of the S&P 500 index with incremental loading every 24 hours, centralized in database in csv file
* Calculation of interest rate up to date
* S&P 500 investment simulator 
* Error handling and alerts
