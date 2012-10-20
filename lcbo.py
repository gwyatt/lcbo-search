import json
import urllib2
import pprint
import sys

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


def keyitr(dump, currentpage=1):
	"""Iterate through data, look for item"""
	maxpage = dump['pager']['final_page']
	while currentpage < maxpage:
		for i in xrange(19):
			print dump['result'][i]['name']
		currentpage += 1
		keyitr(JsonConvert(GetURL(currentpage)),currentpage)	

keyitr(JsonConvert(GetURL()))

