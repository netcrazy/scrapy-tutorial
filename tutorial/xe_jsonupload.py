#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Created on 2014. 12. 2.

@author: IKCHOI
"""
import os
import pycurl
import sys

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode
    
    
args = ' {masterqna|jobkorea}'

if len(sys.argv) != 2:
    print 'usage : ' + sys.argv[0] + args
    exit()

#첫번째 인수값
arg1 = sys.argv[1]

#인수 체크
if( arg1 != 'masterqna' and
    arg1 != 'jobkorea' ):
    print 'usage : ' + sys.argv[0] + args
    exit()

json_path = ''
curl_url = ''
if arg1 == 'masterqna':
    json_path = '../masterqna.json'
    curl_url = 'http://nonstop.pe.kr/api/xe.php'
elif arg1 == 'jobkorea':
    json_path = '../jobkorea.json'
    curl_url = 'http://nonstop.pe.kr/api/jobkorea.php'

try :
    c = pycurl.Curl()
    c.setopt(c.POST, 1)
    c.setopt(c.URL, curl_url)
    c.setopt(c.HTTPPOST, [('sort', arg1),('file1', (c.FORM_FILE, json_path))])
    #c.setopt(c.VERBOSE, 1)
    c.perform()
    c.close()    
    
    #전송 후 삭제
    os.unlink(json_path)
    
except IOError, e:
    print e
    print 'There is no "%s" file' % json_path
    
except Exception, e:
    print e
    

