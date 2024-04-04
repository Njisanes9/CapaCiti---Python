
import csv
import random
from  urllib import request
import json
import datetime
import tweepy


def get_random_quote(quotes_file = 'quotes.csv'):
    try:
        with open(quotes_file) as csvfile:
            quotes = [{
                'author' : line[0],
                'quote' : line[1]
            } for line in csv.reader(csvfile, delimiter='|')]
    except Exception as e:
        quotes = [{
            'author' : 'Eric Idle',
            'quote' : 'Always Look on the bright side of Life.'
        }]

    return random.choice(quotes)

def get_weather_forecast(coords={'lat': 33.55, 'lon': 18.25}):
    try:
        api_key = '644bed12aecaaf39e94824f69bbd2ab2'
        url = f'api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}'
        data = json.load(request.urlopen(url))

        forecast = {
            'city' : data['city']['name'],
            'country': data['city']['country'],
            'periods' : list(),
        }

        for period in data['list'][0:9]:
            forecast['periods'].append({
                'timestamp' : datetime.datetime.fromtimestamp(period['dt']),
                'temp' : round(period['main']['temp']),
                'description': period['weather'][0]['description'].title(),
                'icon':f'http://openweathermap.org/img/wn/{period["weather"]}',
            })

        return forecast
    except Exception as e:
        print(e) 
    
    

def get_twitter_trends(woeid = 23424977):
    try:
        api_key = 'jmSfE6ocHT61S0JNA4XUrLzlB'
        api_secret_key ='y4tIsXPSEACzxKCSPQuBmLQ9LMXfofrjvznsAV2zDVtXJsqyUK'
        auth = tweepy.AppAuthHandler(api_key, api_secret_key)
        return tweepy.API(auth).get_place_trends(woeid)[0]['trends']
    except Exception as e:
        print(e)

def get_wikipedia_article():
    try:
        data = json.load(request.urlopen('https://en.wikipedia.org/api/rest_v1/page/page/random/summary'))
        return {
            'title':data['title'],
            'extract':data['extract'],
            'url':data['content_urls']['desktop']['page'],
        }
    except Exception as e:
        print(e)

if  __name__ == '__main__':
    
    print('\nTesting quote generation...')

    quote = get_random_quote()
    print(f' -  Random quote is "{quote["quote"]}" -  {quote["author"]}')

    quote = get_random_quote(quotes_file=None)
    print(f' -  Default quote is "{quote["quote"]} " -  {quote["author"]}')

    print('\nTesting weather forecast...')

    forecast = get_weather_forecast()
    print(f'{forecast["city"]} - {forecast["country"]} - {forecast["description"]}')
