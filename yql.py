import urllib2
import httplib
#from elementtree import ElementTree
import types

from utility import *
#
#class XmlListConfig(list):
#    def __init__(self, aList):
#        for element in aList:
#            if element:
#                # treat like dict
#                if len(element) == 1 or element[0].tag != element[1].tag:
#                    self.append(XmlDictConfig(element))
#                # treat like list
#                elif element[0].tag == element[1].tag:
#                    self.append(XmlListConfig(element))
#            elif element.text:
#                text = element.text.strip()
#                if text:
#                    self.append(text)
#
#
#class XmlDictConfig(dict):
#    def __init__(self, parent_element):
#        if parent_element.items():
#            self.update(dict(parent_element.items()))
#        for element in parent_element:
#            if element:
#                # treat like dict - we assume that if the first two tags
#                # in a series are different, then they are all different.
#                if len(element) == 1 or element[0].tag != element[1].tag:
#                    aDict = XmlDictConfig(element)
#                # treat like list - we assume that if the first two tags
#                # in a series are the same, then the rest are the same.
#                else:
#                    # here, we put the list in dictionary; the key is the
#                    # tag name the list elements all share in common, and
#                    # the value is the list itself
#                    aDict = {element[0].tag: XmlListConfig(element)}
#                # if the tag has attributes, add those to the dict
#                if element.items():
#                    aDict.update(dict(element.items()))
#                self.update({element.tag: aDict})
#            # this assumes that if you've got an attribute in a tag,
#            # you won't be having any text. This may or may not be a
#            # good idea -- time will tell. It works for the way we are
#            # currently doing XML configuration files...
#            elif element.items():
#                self.update({element.tag: dict(element.items())})
#            # finally, if there are no child tags and no attributes, extract
#            # the text
#            else:
#                self.update({element.tag: element.text})
#
#
#class UrlFetch(object):
#
#    def __init__(self, url, debug=False):
#        self.response_data =''
#        try:
#            response = urllib2.urlopen(url)
#            if  debug == True:
#                print "Url : ", url
#                print "Response : ", response
#            self.response_data = response.read()
#            response.close()
#        except urllib2.URLError, e:
#            print "URL Error >> ", str(e.reason)
#        except urllib2.HTTPError, e:
#            print "HTTP Error >> ", str(e.code)
#        except httplib.HTTPException, e:
#            print "HTTP Exception"
#        except Exception:
#            import traceback
#            print traceback.format_exc()
#
#    def Get(self):
#        return self.response_data

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
        self.res_quotes = {}
        root = ElementTree.XML(self.res_data)
        xmldict = XmlDictConfig(root)
        #print self.res_data
        for quote in xmldict["results"]["quote"]:
            self.res_quotes[quote['Symbol']] = quote
        return self.res_quotes

