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
        #self.session = create_session()
        #self.transaction = self.session.create_transaction()

    def Insert(self, data):
        if data is None:
            return
        else:
            try:
                if isinstance(data, types.ListType):
                    for ele in data:
                        self.execute(ele)
                        #session.flush()
                elif isinstance(data, types.DictType):
                    self.ins.execute(data)
                    #session.flush()
                else:
                    print "Invalid Data ", data
                    return
                #self.transaction.commit()
            except:
                transaction.rollback()
                raise
