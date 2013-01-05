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

import urllib2
import urllib
import types
import json
from elementtree import ElementTree

##http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22MSFT%22)&diagnostics=true&env=http%3A%2F%2Fdatatables.org%2Falltables.env
debug=False
base_url = "http://query.yahooapis.com/v1/public/yql"
append_url = "&diagnostics=true&env=http%3A%2F%2Fdatatables.org%2Falltables.env"
query = "select * from yahoo.finance.quotes where symbol in "
format="xml"

def fetch(url):
    response = urllib2.urlopen(url)
    if  debug == True:
        print "Url : ", url
        print "Response : ", response
    response_data = response.read()
    response.close()
    return response_data

def make_url(symbols):
    symbol_url=""
    if isinstance(symbols, types.ListType):
        for symbol in symbols:
            if len(symbol_url) == 0:
                symbol_url ='\"' + symbol + '\"'
            else:
                symbol_url += ",\"" + symbol + '\"'
    else:
        symbol_url = '\"' + symbols + '\"'
    encoded_url=urllib2.quote((query + "(" + symbol_url + ")").encode('utf8'))
    final_url = base_url + "?q=" + encoded_url + append_url + "&format=" + format
    return final_url

class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)


class XmlDictConfig(dict):
    '''
    Example usage:

    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)

    Or, if you want to use an XML string:

    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)

    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})

def print_symbol(quote):
    print 'YearLow' , " :: ",  quote[ 'YearLow' ]
    print 'OneyrTargetPrice' , " :: ",  quote[ 'OneyrTargetPrice' ]
    print 'DividendShare' , " :: ",  quote[ 'DividendShare' ]
    print 'ChangeFromFiftydayMovingAverage' , " :: ",  quote[ 'ChangeFromFiftydayMovingAverage' ]
    print 'ExDividendDate' , " :: ",  quote[ 'ExDividendDate' ]
    print 'SharesOwned' , " :: ",  quote[ 'SharesOwned' ]
    print 'PercentChangeFromTwoHundreddayMovingAverage' , " :: ",  quote[ 'PercentChangeFromTwoHundreddayMovingAverage' ]
    print 'PricePaid' , " :: ",  quote[ 'PricePaid' ]
    print 'DaysLow' , " :: ",  quote[ 'DaysLow' ]
    print 'DividendYield' , " :: ",  quote[ 'DividendYield' ]
    print 'Commission' , " :: ",  quote[ 'Commission' ]
    print 'EPSEstimateNextQuarter' , " :: ",  quote[ 'EPSEstimateNextQuarter' ]
    print 'HoldingsGainRealtime' , " :: ",  quote[ 'HoldingsGainRealtime' ]
    print 'FiftydayMovingAverage' , " :: ",  quote[ 'FiftydayMovingAverage' ]
    print 'EarningsShare' , " :: ",  quote[ 'EarningsShare' ]
    print 'AverageDailyVolume' , " :: ",  quote[ 'AverageDailyVolume' ]
    print 'LastTradePriceOnly' , " :: ",  quote[ 'LastTradePriceOnly' ]
    print 'YearHigh' , " :: ",  quote[ 'YearHigh' ]
    print 'EBITDA' , " :: ",  quote[ 'EBITDA' ]
    print 'ErrorIndicationreturnedforsymbolchangedinvalid' , " :: ",  quote[ 'ErrorIndicationreturnedforsymbolchangedinvalid' ]
    print 'AnnualizedGain' , " :: ",  quote[ 'AnnualizedGain' ]
    print 'ShortRatio' , " :: ",  quote[ 'ShortRatio' ]
    print 'LastTradeDate' , " :: ",  quote[ 'LastTradeDate' ]
    print 'PriceSales' , " :: ",  quote[ 'PriceSales' ]
    print 'EPSEstimateCurrentYear' , " :: ",  quote[ 'EPSEstimateCurrentYear' ]
    print 'BookValue' , " :: ",  quote[ 'BookValue' ]
    print 'Bid' , " :: ",  quote[ 'Bid' ]
    print 'AskRealtime' , " :: ",  quote[ 'AskRealtime' ]
    print 'PreviousClose' , " :: ",  quote[ 'PreviousClose' ]
    print 'DaysRangeRealtime' , " :: ",  quote[ 'DaysRangeRealtime' ]
    print 'EPSEstimateNextYear' , " :: ",  quote[ 'EPSEstimateNextYear' ]
    print 'Volume' , " :: ",  quote[ 'Volume' ]
    print 'HoldingsGainPercent' , " :: ",  quote[ 'HoldingsGainPercent' ]
    print 'Change_PercentChange' , " :: ",  quote[ 'Change_PercentChange' ]
    print 'PercentChange' , " :: ",  quote[ 'PercentChange' ]
    print 'TickerTrend' , " :: ",  quote[ 'TickerTrend' ]
    print 'Ask' , " :: ",  quote[ 'Ask' ]
    print 'ChangeRealtime' , " :: ",  quote[ 'ChangeRealtime' ]
    print 'PriceEPSEstimateNextYear' , " :: ",  quote[ 'PriceEPSEstimateNextYear' ]
    print 'HoldingsGain' , " :: ",  quote[ 'HoldingsGain' ]
    print 'Change' , " :: ",  quote[ 'Change' ]
    print 'MarketCapitalization' , " :: ",  quote[ 'MarketCapitalization' ]
    print 'Name' , " :: ",  quote[ 'Name' ]
    print 'HoldingsValue' , " :: ",  quote[ 'HoldingsValue' ]
    print 'DaysRange' , " :: ",  quote[ 'DaysRange' ]
    print 'AfterHoursChangeRealtime' , " :: ",  quote[ 'AfterHoursChangeRealtime' ]
    print 'symbol' , " :: ",  quote[ 'symbol' ]
    print 'ChangePercentRealtime' , " :: ",  quote[ 'ChangePercentRealtime' ]
    print 'DaysValueChange' , " :: ",  quote[ 'DaysValueChange' ]
    print 'LastTradeTime' , " :: ",  quote[ 'LastTradeTime' ]
    print 'StockExchange' , " :: ",  quote[ 'StockExchange' ]
    print 'DividendPayDate' , " :: ",  quote[ 'DividendPayDate' ]
    print 'LastTradeRealtimeWithTime' , " :: ",  quote[ 'LastTradeRealtimeWithTime' ]
    print 'Notes' , " :: ",  quote[ 'Notes' ]
    print 'MarketCapRealtime' , " :: ",  quote[ 'MarketCapRealtime' ]
    print 'PERatio' , " :: ",  quote[ 'PERatio' ]
    print 'DaysValueChangeRealtime' , " :: ",  quote[ 'DaysValueChangeRealtime' ]
    print 'ChangeFromYearHigh' , " :: ",  quote[ 'ChangeFromYearHigh' ]
    print 'ChangeinPercent' , " :: ",  quote[ 'ChangeinPercent' ]
    print 'HoldingsValueRealtime' , " :: ",  quote[ 'HoldingsValueRealtime' ]
    print 'PercentChangeFromFiftydayMovingAverage' , " :: ",  quote[ 'PercentChangeFromFiftydayMovingAverage' ]
    print 'PEGRatio' , " :: ",  quote[ 'PEGRatio' ]
    print 'ChangeFromTwoHundreddayMovingAverage' , " :: ",  quote[ 'ChangeFromTwoHundreddayMovingAverage' ]
    print 'DaysHigh' , " :: ",  quote[ 'DaysHigh' ]
    print 'PercentChangeFromYearLow' , " :: ",  quote[ 'PercentChangeFromYearLow' ]
    print 'TradeDate' , " :: ",  quote[ 'TradeDate' ]
    print 'LastTradeWithTime' , " :: ",  quote[ 'LastTradeWithTime' ]
    print 'BidRealtime' , " :: ",  quote[ 'BidRealtime' ]
    print 'YearRange' , " :: ",  quote[ 'YearRange' ]
    print 'HighLimit' , " :: ",  quote[ 'HighLimit' ]
    print 'OrderBookRealtime' , " :: ",  quote[ 'OrderBookRealtime' ]
    print 'ChangeFromYearLow' , " :: ",  quote[ 'ChangeFromYearLow' ]
    print 'PriceBook' , " :: ",  quote[ 'PriceBook' ]
    print 'LowLimit' , " :: ",  quote[ 'LowLimit' ]
    print 'HoldingsGainPercentRealtime' , " :: ",  quote[ 'HoldingsGainPercentRealtime' ]
    print 'TwoHundreddayMovingAverage' , " :: ",  quote[ 'TwoHundreddayMovingAverage' ]
    print 'PERatioRealtime' , " :: ",  quote[ 'PERatioRealtime' ]
    print 'PercebtChangeFromYearHigh' , " :: ",  quote[ 'PercebtChangeFromYearHigh' ]
    print 'Open' , " :: ",  quote[ 'Open' ]
    print 'PriceEPSEstimateCurrentYear' , " :: ",  quote[ 'PriceEPSEstimateCurrentYear' ]
    print 'MoreInfo' , " :: ",  quote[ 'MoreInfo' ]


def parse_yql_response(data):
    root = ElementTree.XML(data)
    xmldict = XmlDictConfig(root)
    for quote in xmldict["results"]["quote"]:
        print "################################################################"
        print_symbol(quote)
        print "################################################################"




##print fetch("http://kodeyard.blogspot.in")
#print fetch("http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22MSFT%22)&diagnostics=true&env=http%3A%2F%2Fdatatables.org%2Falltables.env")

lis = []
lis.append("TCS.NS")
lis.append("HINDALCO.NS")

url = make_url(lis)
##url = urllib2.quote(url.encode('utf8'))
print url
res = fetch(url)
print res
parse_yql_response(res)

