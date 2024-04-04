import dd_Content
import datetime


class DailyDigestEmail:

    def __init__(self):
        self.content = {
            'quote' : {'include' : True, 'content' : dd_Content.get_random_quote()},
            'weather' : {'include' : True, 'content' : dd_Content.get_weather_forecast()},
            'twitter' : {'include' : True, 'content' : dd_Content.get_twitter_trends()},
            'wikipedia' : {'include' : True, 'content' : dd_Content.get_wikipedia_article()}
        }

    def send_email(self):
        pass

    def format_message(self):

        #Generate Plain Text

        text = f'*~*~*~*~* Daily Digest - {datetime.date.today().strftime("%d %b %y")} *~*~*~*~*\n\n'

        # Format random quote

        if self.content['quote']['include'] and self.content['quote']['content']:
            text += '*~*~* Quote of the Day *~*~*\n\n'
            text += f'"{self.content["quote"]["content"]["quote"] }" -  {self.content["quote"]["content"]["author"]}\n\n' 

        # Format Weather Forecast
            
        if self.content['weather']['include'] and self.content['weather']['weather']:
            text += f'*~*~* Forecast for {self.content["weather"]["content"]["city"]}, {self.content["weather"]["content"]["country"]} *~*~*\n\n'

            for forecast in self.content['weather']['content']['periods']:
                text += f'{forecast["timestamp"].strftime("%d %m %H%M")} - {forecast["temp"]}\u000c | {forecast["description"]} \n'

        
        # Format Twitter Trends 
                
        if self.content['twitter']['include']  and self.content['twitter']['content']:
            text += '*~*~* Top Tend Twitter Trends *~*~*'

            for trend in self.content['content']['content'][0:10]:
                text += f'{trend["name"]}\n'
            text += '\n'

        # Format Wikipedia Article

        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            text +=  '*~*~* Daily Random Learning *~*~* \n\n'
            text += f'{self.content["wikipedia"]["content"]["title"]} \n {self.content["wikipedia"]["content"]["extract"]}'


        html = f'''<html>
            <body>
                <h1>Daily Digest {datetime.date.today().strftime("%d %m %y")}</h1>
            </body>
        
        </html>'''
    

