#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      asit
#
# Created:
# Copyright:   (c) asit
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import yql
import store_db

def create_field_list():
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

def create_symbol_list():
    symbols = []
    symbols.append("TCS.NS")
    symbols.append("HINDALCO.NS")
    return symbols

def main():
    fields = create_field_list()
    symbols = create_symbol_list()
    db_hand = store_db.DbDailyQuotes()
    for i in range(0,2000):
        yql_ob = yql.Yql(symbols, fields )
        yql_res = yql_ob.query_yql()
        for key, val in yql_res.items():
            print "Fetched for ... ", key
            db_hand.Insert(val)




if __name__ == '__main__':
    main()
