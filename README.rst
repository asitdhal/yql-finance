Yahoo Finance
===========

**Python module - retrieve stock quote data from Yahoo Finance**

 * Created by: Asit Dhal(asit.dhal@hotmail.com)
 * License: GNU LGPLv2+
 * Dev Home: https://github.com/lipun4u/YahooFinance


Dependency
-------------
  * Python 2.7

Install
-------------
  * Copy utility.py and yql.py
  * Import yql.py

Example Usage
-------------
import yql

def make_field_list():
    fields = []
    fields.append('Symbol')
    fields.append('Name')
    fields.append('StockExchange')
    fields.append('Ask')
    fields.append('Bid')
    fields.append('Change')
    fields.append('ChangeinPercent')
    fields.append('Open')
    fields.append('TradeDate')
    fields.append('PreviousClose')
    fields.append('PercentChange')
    fields.append('LastTradeDate')
    fields.append('LastTradeTime')
    fields.append('LastTradePriceOnly')
    fields.append('DaysRange')
    fields.append('DaysHigh')
    fields.append('DaysLow')
    fields.append('YearLow')
    fields.append('YearHigh')
    fields.append('PercebtChangeFromYearHigh')
    fields.append('PercentChangeFromYearLow')
    fields.append('ChangeFromYearHigh')
    fields.append('ChangeFromYearLow')
    return fields
    
if __name__ == '__main__':
    
        fields = make_field_list()
        lis= []
        lis.append("TCS.NS")
        lis.append("HINDALCO.NS")
        lis.append("GOOG")
        yql_ob = yql.Yql(lis, fields )
        yql_res =  yql_ob.query_yql()
        for company, quotes in yql_res.iteritems():
            print company, " => ", quotes

Output :- 

GOOG  =>  {'YearLow': '556.52', 'Name': 'Google Inc.', 'Symbol': 'GOOG', 'DaysLow': '902.01', 'LastTradeTime': '2:36pm', 'Ask': '910.35', 'ChangeFromYearHigh': '+66.18', 'LastTradePriceOnly': '910.18', 'DaysRange': '902.01 - 919.9799', 'ChangeinPercent': '-0.62%', 'LastTradeDate': '5/16/2013', 'DaysHigh': '919.9799', 'PercentChangeFromYearLow': '+63.55%', 'TradeDate': None, 'PercebtChangeFromYearHigh': '+7.84%', 'Bid': '910.10', 'PreviousClose': '915.89', 'ChangeFromYearLow': '+353.66', 'PercentChange': '-0.62%', 'StockExchange': 'NasdaqNM', 'Open': '919.00', 'YearHigh': '844.00', 'Change': '-5.71'}
HINDALCO.NS  =>  {'YearLow': '86.90', 'Name': None, 'Symbol': 'HINDALCO.NS', 'DaysLow': '115.25', 'LastTradeTime': '6:24am', 'Ask': '118.40', 'ChangeFromYearHigh': '-18.70', 'LastTradePriceOnly': '118.40', 'DaysRange': '115.25 - 119.50', 'ChangeinPercent': '+1.72%', 'LastTradeDate': '1/28/2013', 'DaysHigh': '119.50', 'PercentChangeFromYearLow': '+36.25%', 'TradeDate': None, 'PercebtChangeFromYearHigh': '-13.64%', 'Bid': '118.40', 'PreviousClose': '116.40', 'ChangeFromYearLow': '+31.50', 'PercentChange': '+1.72%', 'StockExchange': 'NSE', 'Open': '117.40', 'YearHigh': '137.10', 'Change': '+2.00'}
TCS.NS  =>  {'YearLow': '1020.50', 'Name': 'TATA CONSULTANCY', 'Symbol': 'TCS.NS', 'DaysLow': '1447.45', 'LastTradeTime': '5:59am', 'Ask': '1454.05', 'ChangeFromYearHigh': '+14.25', 'LastTradePriceOnly': '1454.05', 'DaysRange': '1447.45 - 1469.00', 'ChangeinPercent': '-1.19%', 'LastTradeDate': '5/16/2013', 'DaysHigh': '1469.00', 'PercentChangeFromYearLow': '+42.48%', 'TradeDate': None, 'PercebtChangeFromYearHigh': '+0.99%', 'Bid': None, 'PreviousClose': '1471.55', 'ChangeFromYearLow': '+433.55', 'PercentChange': '-1.19%', 'StockExchange': 'NSE', 'Open': '1469.00', 'YearHigh': '1439.80', 'Change': '-17.50'}


To Do
-------------
  * XmlDictConfig and XmlListConfig are terribly unstable. These components need to be replaced.
   * Stock Exchange Specific wrapper needs to be dedeveloped
   * Database Support(mysql and sqlite) needs to be added
   * Django Example needs to be added