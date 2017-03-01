from flask import render_template
from app import app
import urllib.request
import json
import datetime
from .helper import *

@app.route('/')
@app.route('/index')

def index():
	city = 'Austin'
	state = 'TX'
	today = datetime.datetime.now()

	conditionsURL = createConditionsURL(city, state)
	conditionsData = createData(conditionsURL)

	forecastURL = createForecastURL(city, state)
	forecastData = createData(forecastURL)

	degree_sign= u'\N{DEGREE SIGN}'
	temperature = str(conditionsData['current_observation']['temp_f']) + str(degree_sign)
	precipitation = str(forecastData['forecast']['txt_forecast']['forecastday'][0]['pop']) + '%'
	print (precipitation)


	user = {'nickname': 'Megan'}
	currentDate = today.strftime("%A %B %d, %Y")
	currentTime = today.strftime("%I:%M %p")
	return render_template('index.html', user=user, currentDate=currentDate, currentTime=currentTime, temperature=temperature, city=city, state=state, precipitation=precipitation)




