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

class ConfigTable(object):

    def __init__(self, file_name = 'nsesymbols.txt', table_name = 'config.db', db_echo = False, create_new=False):
        self.table_name = 'SYMBOLS'
        self.create_new = False
        self.db = create_engine('sqlite:///' + table_name)
        self.file_name = file_name
        self.db_echo = db_echo
        self.metadata = MetaData(self.db)
        self.symbols = None

    def _create_table(self):
        self.symbols = Table('SYMBOLS', metadata,
            Column('symbol', String, primary_key=True),
            Column('exchange', String(40), primary_key=True),
            Column('name', String),
            Column('status', String),
        )
        self.symbols.create()

    def _load_table(self):
        self.symbols = Table('SYMBOLS', metadata, autoload=True)

    def insert(self, symbol_field, symbol_exchange, symbol_name, symbol_status):
        ins = self.symbols.insert()
        ins.execute(symbol=symbol_field, exchange=symbol_exchange, name=symbol_name, status= symbol_status)

    def get_symbols(self):
        sel = symbols.select()
        rs = sel.execute()
        symbols_list = []
        for row in rs:
            symbols_list.append(symbols_list)

