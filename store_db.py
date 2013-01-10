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
import types

class DbDailyQuotes(object):

    def __init__(self, db_echo=False, engine_name = 'stock_quote.db'):
        self.db = create_engine('sqlite:///' + engine_name)
        self.db_echo = db_echo
        self.metadata = MetaData(self.db)
        self.table = Table('DAILY_QUOTES', self.metadata, autoload=True)
        self.ins = self.table.insert()

    def Insert(self, data):
        if data is None:
            return
        else:
            if isinstance(data, types.ListType):
                for ele in data:
                    self.execute(ele)
            elif isinstance(data, types.DictType):
                self.ins.execute(data)
            else:
                print "Invalid Data ", data
                return
