import urllib.request
import json
import os

def createConditionsURL(city, state):
	api_key = os.environ.get('WU_API_KEY')
	url = 'http://api.wunderground.com/api/' + api_key + "/conditions/q/" + state + '/' + city + '.json'
	return url

def createForecastURL(city, state):
	api_key = os.environ.get('WU_API_KEY')
	url = 'http://api.wunderground.com/api/' + api_key + "/forecast/q/" + state + '/' + city + '.json'
	return url

def createData(url):
	f = urllib.request.urlopen(url)
	json_string = f.read().decode('utf-8')
	parsed_json = json.loads(json_string)
	return parsed_json
