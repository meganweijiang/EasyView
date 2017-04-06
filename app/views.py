from flask import Flask, render_template, request, redirect, url_for, flash
from app import app
import urllib.request
import json
import datetime
import string
from .helper import *
from flask_wtf import Form
from wtforms import TextField, SubmitField, validators, ValidationError

app.secret_key = 'development key'
dataDict = {'name': "", 'state': "", 'city': ""}


class InfoForm(Form):
	name = TextField("Name: ", [validators.required()])
	state = TextField("State or Country: ", [validators.required(), validators.length(max=2)])
	city = TextField("City: ", [validators.required()])
	submit = SubmitField("Submit")
	cancel = SubmitField("Cancel")

@app.route('/', methods=['POST', 'GET'])

def index(*form):

	name = dataDict['name']
	state = dataDict['state']
	city = dataDict['city']
	cityQuery = city

	if city != "" and name != "" and state != "":
		city = string.capwords(city)
		name = string.capwords(name)
		state = state.upper()
		cityQuery = city.replace(" ", "_")

	else:
		return redirect(url_for('form'))

	today = datetime.datetime.now()

	conditionsURL = createConditionsURL(cityQuery, state)
	conditionsData = createData(conditionsURL)

	forecastURL = createForecastURL(cityQuery, state)
	forecastData = createData(forecastURL)

	degree_sign= u'\N{DEGREE SIGN}'
	try:
		temperature = str(conditionsData['current_observation']['temp_f']) + str(degree_sign)
		precipitation = str(forecastData['forecast']['txt_forecast']['forecastday'][0]['pop']) + '%'
		weather = str(conditionsData['current_observation']['weather']).lower()
	except KeyError:
		temperature = ''
		precipitation = ''
		weather = ''

	if int(today.strftime("%H")) >= 19 and int(today.strftime("%H")) < 4:
		greeting = 'Good Night'
	elif int(today.strftime("%H")) >= 4 and int(today.strftime("%H")) <= 12:
		greeting = 'Good Morning'
	else:
		greeting = 'Good Afternoon'

	if 'rain' in weather:
		symbol = str(u'\u26C6')
	elif 'cloud' in weather and 'part' in weather:
		symbol = str(u'\u26C5')
	elif 'cloud' in weather:
		symbol = str(u'\u2601')
	elif 'storm' in weather:
		symcol = str(u'\u26A1')
	else:
		symbol = str(u'\u2600')		

	currentDate = today.strftime("%A %B %d, %Y")
	currentTime = today.strftime("%I:%M %p")
	return render_template('index.html', name=name, currentDate=currentDate, currentTime=currentTime, temperature=temperature, city=city, state=state, precipitation=precipitation, greeting=greeting, symbol=symbol)

@app.route('/form', methods=['GET', 'POST'])
def form():
	form = InfoForm()
	if request.method == 'POST':
		if 'submit' in request.form:
			dataDict['name'] = request.form['name']
			dataDict['state'] = request.form['state']
			dataDict['city'] = request.form['city']
			return redirect(url_for('index'))	

		elif 'cancel' in request.form:
			return redirect(url_for('index'))

	return render_template('form.html', form=form)



