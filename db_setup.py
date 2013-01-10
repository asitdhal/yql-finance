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

from sqlalchemy import *

class DbSetup(object):

    def __init__(self, db_echo=False, engine_name = 'stock_quote.db'):
        self.db = create_engine('sqlite:///' + engine_name)
        self.db_echo = db_echo
        self.metadata = MetaData(self.db)

    def _create_daily_quotes_table(self):
        daily_quotes = Table('DAILY_QUOTES', self.metadata,
            Column('Symbol', String),
            Column('Name', String),
            Column('StockExchange', String),
            Column('Ask', String),
            Column('Bid', String),
            Column('Change', String),
            Column('ChangeinPercent', String),
            Column('Open', String),
            Column('TradeDate', String),
            Column('PreviousClose', String),
            Column('PercentChange', String),
            Column('LastTradeDate', String),
            Column('LastTradeTime', String),
            Column('LastTradePriceOnly', String),
            Column('DaysRange', String),
            Column('DaysHigh', String),
            Column('DaysLow', String),
            Column('YearLow', String),
            Column('YearHigh', String),
            Column('PercebtChangeFromYearHigh', String),
            Column('PercentChangeFromYearLow', String),
            Column('ChangeFromYearHigh', String),
            Column('ChangeFromYearLow', String),
        )
        daily_quotes.create()

    def _create_symbols_table(self):
        symbols = Table('SYMBOLS', self.metadata,
            Column('Symbol', String, primary_key=True),
            Column('Exchange', String(40), primary_key=True),
            Column('Name', String),
            Column('Status', String),
        )
        symbols.create()




def main():
    setup = DbSetup()
    #setup._create_daily_quotes_table()
    setup._create_symbols_table()

if __name__ == '__main__':
    main()
