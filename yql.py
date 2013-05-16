import urllib2
import httplib
import types

from utility import *


BASE_URL = "http://query.yahooapis.com/v1/public/yql"
APPEND_URL = "&diagnostics=true&env=http%3A%2F%2Fdatatables.org%2Falltables.env"
QUERY = "select %s from yahoo.finance.quotes where symbol in "
RESPONSE_FORMAT = "xml"

class Yql(object):

    def __init__(self, symbols, fields='*'):
        self.base_url = BASE_URL
        self.append_url = APPEND_URL
        self.query = QUERY
        self.format= RESPONSE_FORMAT
        self.url = ''
        self.symbols = symbols
        self.fields = fields
        self.encoded_url = ''
        self.res_data = ''

    def _make_url(self):
        
        #only specific fields are required
        if isinstance(self.fields, types.ListType):
            #Field 'Symbol' is required in the response for further processing
            if 'Symbol' not in self.fields:
                self.fields.append('Symbol')
            #All fields should be separated by ','
            field_str = ",".join(self.fields)
            #print field_str
            self.query = self.query % (field_str)
           
        #all fields are required 
        elif self.fields == '*':
            self.query = self.query % (self.fields)
        
        #only one field required    
        else:
            if self.fields != 'Symbol':
                field_str = self.fields + ", " + 'Symbol'
            else:
                field_str = self.fields
            self.query = self.query % (self.fields)
            
        if isinstance(self.symbols, types.ListType):
            for index, symbol in enumerate(self.symbols):
                self.symbols[index] = '\"' + symbol +'\"'
            self.url = ','.join(self.symbols) 
            #print self.url           
        else:
            self.url = '\"' + self.symbols + '\"'
            
        encoded_url=urllib2.quote((self.query + "(" + self.url + ")").encode('utf8'))
        #print encoded_url
        self.encoded_url= self.base_url + "?q=" + encoded_url + self.append_url + "&format=" + self.format
        #print "**************************************"
        #print self.encoded_url

    def query_yql(self):
        self._make_url()
        res = UrlFetch(self.encoded_url)
        self.res_data = res.Get()
        #print self.res_data        
        self.res_quotes = {}
        root = ElementTree.XML(self.res_data)
        xmldict = XmlDictConfig(root)
 
        for quote in xmldict["results"]["quote"]:
            self.res_quotes[quote['Symbol']] = quote
        return self.res_quotes

