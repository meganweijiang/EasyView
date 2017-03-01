import urllib.request
import json

def createConditionsURL(city, state):
	api_key = '0a2e7496ef93abf1'
	url = 'http://api.wunderground.com/api/' + api_key + "/conditions/q/" + state + '/' + city + '.json'
	return url

def createForecastURL(city, state):
	api_key = '0a2e7496ef93abf1'
	url = 'http://api.wunderground.com/api/' + api_key + "/forecast/q/" + state + '/' + city + '.json'
	print (url)
	return url

def createData(url):
	f = urllib.request.urlopen(url)
	json_string = f.read().decode('utf-8')
	parsed_json = json.loads(json_string)
	return parsed_json