<p align="center"><img src="project_title.png"> 

​

# <p style="text-align: center;"> **Project 1 - Portfolio Analysis**

​

### Investors: Jada Williams, Rajiv Shrestha, Andrew Park, Marius Nsamou, and Lynette Cary

#

### This project focused on creating an optimum investment portfolio using an analysis of stock data and an analysis of crypto data

#

​

## **Stock Portfolio Analysis**

The first analysis looked at investing $20,000 in the financial market and analyzing selected historical stock data using Monte Carlo simulations to generate the highest return for the lowest risk to answer the question: 

### ***"Should we invest?"*** and ***"What is the risk?"*** 

​

The portfolio included all available historical stock data from Alpaca Stock Trading API from January 2008 to November 2020 *(approximately 13 years)* for the following stocks: Procter & Gamble (PG), Walmart (WMT), Intel (INTC), Microsoft (MSFT), Intuit (INTU), and the S&P 500 Index (SPY).

​

The analysis ran 50 Monte Carlo simulations with assigned weights to model the likelihood of generating a high return with low risk over 3 years, 5 years, and 10 years.

​

The findings of the analysis based on an investment of $20,000 and a 95% confidence interval shows that we can expect approximately 95% of the simulations to project a portfolio return within the following ranges:

​

​

| Forecast (years)  | Portfolio Return (range)

|------------------ | ------------------------------|

|       3 years     | $21,106 and $40,682 (rounded) |

|       5 years     | $28,499 and $52,558 (rounded) |

|      10 years     | $38,670 and $119,721 (rounded)|

### **Result: Good Investment**

​

#

![image.png](https://github.com/apark19/team004_project001/blob/main/Resources/MC_3yrs_sim_plot.png)

​

![image.png](https://github.com/apark19/team004_project001/blob/main/Resources/MC_5yrs_sim_plot.png)

​

![image.png](https://github.com/apark19/team004_project001/blob/main/Resources/MC_10yrs_sim_plot.png)

​

​

The simulations show that the stocks selected are less volatile compared against the market with a small variance between the cumulative return and the mean, but the risk increases over longer periods of projections. 

​

*Please note that the stock analysis can be modified using different stock tickers to pull data for various companies and assign different weights across the portfolio.* 

​

#

## **Crypto Portfolio Analysis**

The second analysis looked at investing in four selected cryptocurrencies and analyzing the performance of the crypto price data compared to two selected Indexes to answer the question:

### ***Should we invest?*** 

​

The portfolio included a benchmark analysis to look at trends in the data and compare the performance of the cryptocurrencies price data against the Indexes.  The four selected cryptocurrencies included: Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC), and Ripple (XRP) compared against the S&P 500 Index (SPY) and the Dow Jones Index (DJI). The cryptocurrency data was collected using CryptoCompare API.  The historical data was available for *approximately 5 years (2015 - 2020).*

​

The findings of the analysis ...


