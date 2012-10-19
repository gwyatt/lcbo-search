import json
import urllib2
import string
import time

#Set up global variables - LCBO API
lcboapi = "http://lcboapi.com/products"

request = urllib2.Request(lcboapi)
request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_1; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
result = urllib2.urlopen(request).read()
result_json = json.loads(result)
for key in result_json.iterkeys():
	print key


time.sleep(15)