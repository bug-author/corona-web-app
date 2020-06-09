from flask import Flask, render_template
import requests
app = Flask(__name__)


# print('last updated at '+ time[0] +':' +time[1] +' ' +response['abbreviation'])

''' ##############################################

    SET FLASK_APP='appname'.py
    SET FLASK_DEBUG=1

###############################################'''


@app.route('/')
def index():
    time_url = 'http://api.timezonedb.com/v2.1/get-time-zone?key=BUFVLD01W6M6&format=json&by=zone&zone=Asia/Karachi'

    r = requests.get(time_url)
    response = r.json()
    # print('last updated at:',response['formatted'],response['abbreviation'])
    time = str(response['formatted'])
    time = time.split()  # makes a list
    time = str(time[1])
    time = time.split(':')

    hours = time[0]
    minutes = time[1]
    seconds = time[2]
    country_code = response['abbreviation']

    corona_url = 'http://corona-api.com/countries/pk'

    response = requests.get(corona_url).json()

    today_deaths = response['data']['today']['deaths']  # new deaths
    today_confirmed = response['data']['today']['confirmed']  # new cases
    today_update_time = response['data']['updated_at']

    # total
    total_cases = response['data']['latest_data']['confirmed']
    total_deaths = response['data']['latest_data']['deaths']
    total_recovered = response['data']['latest_data']['recovered']

    return render_template('index.html', hours=hours, minutes=minutes,
                           country_code=country_code, seconds=seconds,
                           total_cases=total_cases, total_deaths=total_deaths,
                           total_recovered=total_recovered,
                           today_confirmed=today_confirmed,
                           today_deaths=today_deaths,
                           today_update_time=today_update_time,
                           )
