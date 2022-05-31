# Investment Simulator

## Overview
This is a tool to simulate the result of a diversified investment in the USA market, using the compound interest rate related to the S&P 500 Index. It consists of:
* Calculation of the market rate with updated values on a daily basis, and 
* Calculation of the final capital by means of the financial capitalization formula. 

All of this was created using _Python._

## Project goal
Calculate the final capital that would be obtained from the investment of a capital composed by an initial capital and/or successive contributions. 

## Approach
To achieve the stated objective, we start modeling the financial capitalization formula in a python script, which requires 4 parameters:
* Principal: the initial capital. This is a parameter entered by the user.
* Contributions: the successive capital additions. This is also a parameter entered by the user. 
* Investment horizon: the time period where one expects to hold an investment for a specific goal. User parameter too.
* Compound interest rate: the annual compound interest rate currently offered by the market. This parameter is calculated based on S&P 500 index prices.

_Note: If it is of your interest, I recommend you investigate the formula of financial capitalization and compound interest._

#### 1) Yahoo Finance Scraper
This python script automatically:
* Downloads from Yahoo Finance web the value of the S&P 500 index
* Update a csv file to store current date, value and daily change
* It is settle to automatically do the task every day at USA market closing time (17 P.M.)

This values are then used to calculate the _Compound Interest Rate._

#### 2) Compound Interest Rate Calculator
This python script contains a function that returns the compound interest rate, using historical prices of the S&P 500 index from the csv file created as a result of the Yahoo Finance Scraper. 

#### 3) Final Capital Calculator
The final capital is calculated within a function that, as mentioned, takes 4 parameters:
* Principal
* Contributions
* Investment horizon
* Compound interest rate: returned in the Compound Interest Rate Calculator function. 

This parameters are processed through capitalization formula, using two loops, whose flow charts are below:


As a result, this function 
1. Returns the final capital and the effect of compound interest on principal
2. Create a csv file with inputs and output
3. Update this csv file every time a simulation is run

###### 

