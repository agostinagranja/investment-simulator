# Investment Simulator

## Overview
This is a tool to simulate the result of a diversified investment in the US market, using the compound interest rate related to the S&P 500 Index. It consists of:
* Calculation of the market rate with updated values on a daily basis, and 
* Calculation of the final capital by means of the financial capitalization formula. 
All of this was created using **Python**. 

## Project goal
Calculate the final capital that would be obtained from the investment of a capital composed by an initial capital (principal) and/or successive contributions. 

## Approach
To achieve the stated objective, we start modeling the financial capitalization formula in a python script, which requires 4 parameters:
* Principal: the initial capital. This is a parameter entered by the user.
* Contributions: the successive capital additions. This is also a parameter entered by the user. 
* Investment horizon: the time period where one expects to hold an investment for a specific goal. User parameter too.
* Compound interest rate: the annual compound interest rate currently offered by the market. This parameter is calculated based on S&P 500 index prices.

_Note: If it is of your interest, I recommend you investigate the formula of financial capitalization and compound interest._


#### 1) Yahoo Finance Scraper
A Python script was developed to automatically download once a day, from Yahoo Finance web, the value of the S&P 500 index. 
It’s then used to calculate the annualized return. 

#### 2) Compound Interest Rate Calculator
A function was designed in a python script to calculate the annual compound interest rate.
