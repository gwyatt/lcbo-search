import json
import urllib2
import pprint

#Set up global variables - LCBO API
def GetURL(page=1):
	"""Grab the URL from LCBO API"""
	lcboapi = "http://lcboapi.com/products"
	
	if page == 1:
		request = urllib2.Request(lcboapi)
		request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_1; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
		result = urllib2.urlopen(request).read()
		return result
	else: #Append page number
		lcboapi += '?page=%s' % page
		request = urllib2.Request(lcboapi)
		request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_1; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
		result = urllib2.urlopen(request).read()
		return result

def JsonConvert(rawdump):
	"""Convert API result into python dict"""
	dump = json.loads(rawdump)
	return dump

def keyitr(dump):
	"""Iterate through data, look for item"""
	i = 0
	while True:
		print dump['result'][i]['name']
		i += 1
		if i == 19:
			break
		else:
			pass

keyitr(JsonConvert(GetURL(485)))

