# Investment Simulator
### Scraping of prices of the S&P 500 index and simulation of the result of an investment in it.

## Industry
Finance

## Problem
There is a necessity for a tool to simulate the result of a diversified investment in the US capital market in a personalized way. To perform a simulation such us, the data needed are:

1. Rate offered by the market
2. Initial capital
3. Amount of periodic contributions
4. Investment horizon

Parameters from 2 to 4 are defined by the user. Meanwhile, the rate offered by the United States market for a diversified and passive investment[^1] is generally represented by the compound interest rate of the S&P 500 index.

## Project objective
Extract the daily closing prices of the S&P 500 index and make it available in a centralized database, which serves as a supply for the calculation of the annualized rate of return, defined as a compound interest rate [^2]. This outcome, processed in a python script together with the parameters entered by the user, determines the estimated result (final capital) of the investment.

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
* Historical data of the S&P 500 index with incremental loading every 24 hours, centralized in a CSV file
* Calculation of interest rate up to date
* S&P 500 investment simulator 
* Error handling and alerts

## Side projects
* Tableau dashboard of S&P 500 index prices[^3]

## Notes
[^1]: Passive investment is the one that requires the minimum effort on the part of the user or no management by third parties. 
[^2]: Compound interest is the interest on a deposit calculated based on both the initial principal and the accumulated interest from previous periods. [More Information](https://www.investopedia.com/terms/c/compoundinterest.asp) 
[^3]: A brief analysis and viz of S&P 500 index prices can be seen on this [Tableau dashboard](https://public.tableau.com/app/profile/agostina.granja#!/) I made
