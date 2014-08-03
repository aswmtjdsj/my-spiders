#!/usr/bin/python
import BeautifulSoup as bs4
from BeautifulSoup import BeautifulSoup as bs
import requests
callurl = 'http://community.topcoder.com/tc?module=ActiveContests&pt=39'
r=requests.post(callurl)
print r.status_code
print ''
a = bs(r.content)
cnt = 0
cItem=[]
for i in a.findAll('table', {"class": "stat"}):
    for j in i.findAll('tr'):
        if len(j.attrs) >0 and u'class' in j.attrs[0]:
            print "Contest #{}: ".format(cnt),
            cnt += 1
            for k in j.findAll('td'):
                print map(lambda x: x.strip() if type(x) != bs4.Tag else x.contents, k.contents), " | ",
            print ""
        else:
            print j.contents
