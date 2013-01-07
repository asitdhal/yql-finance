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

    def __init__(self, db_echo=False):
        self.db_echo = db_echo


def main():
    pass

if __name__ == '__main__':
    main()
