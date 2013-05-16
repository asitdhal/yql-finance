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