import json
import csv, xlrd, codecs, xlwt
import requests
import mechanize
import cookielib
import re
import time, random
import datetime

def leaf_value(obj, prefix=''):
     if isinstance(obj, dict):
         for k, v in obj.items():
             for res in leaf_value(v, str(v)):
                 yield res
     elif isinstance(obj, list):
         for i, v in enumerate(obj):
             for res in leaf_value(v, '['+str(v)+']'):
                 yield res
     else:
         yield prefix



def dot_notation(obj, prefix=''):
     if isinstance(obj, dict):
         if prefix: prefix += '.'
         for k, v in obj.items():
             for res in dot_notation(v, prefix+str(k)):
                 yield res
     elif isinstance(obj, list):
         for i, v in enumerate(obj):
             for res in dot_notation(v, prefix+'['+str(i)+']'):
                 yield res
     else:
         yield prefix

def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

url = 'http://www.masters.com/en_US/scores/feeds/scores.json'

wb = xlwt.Workbook(encoding="utf-8")
sh = wb.add_sheet('Page1')


count = 0

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

r = requests.get(url).text

data = json.loads(r)

data = convert(data)

#print data

y = list(dot_notation(data))
x = list(leaf_value(data))

for i in range(len(y)):
	sh.write(i,0,y[i])
	sh.write(i,1,x[i])

wb.save("Masters.xls")