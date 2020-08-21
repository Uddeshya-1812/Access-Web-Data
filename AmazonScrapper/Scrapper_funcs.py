import re
import requests 
import json
from selectorlib import Extractor
from urllib.request import Request,urlopen
 

e = Extractor.from_yaml_file('AmazonReviews.yml')#Extracts css-selectors from yml file for the web pages

def scrape(url,user_agent):
	headers = {
	'authority': 'www.amazon.in',
	'pragma': 'no-cache',
	'cache-control': 'no-cache',
	'dnt': '1',
	'upgrade-insecure-requests': '1',
	'user-agent':user_agent,
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
	}#http headers  
	r = requests.get(url, headers=headers)
	if r.status_code > 500:
		if "To discuss automated access to Amazon data please contact" in r.text:
		   print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
		else:
		   print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
		return None
	return e.extract(r.text)#return dictionary	
