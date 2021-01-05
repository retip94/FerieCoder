import requests, json
from datetime import datetime
import random
import pytz
from bs4 import BeautifulSoup

# get current weather for given city
API_KEY='6f3fd6fce29c2928050252e99609a1c6'
city = 'Warszawa'
r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=pl&appid={API_KEY}')
if r.status_code == 200:
    r = json.loads(r.content)
    print(f'Prognoza dla miasta {city} o godzinie: {datetime.fromtimestamp(r["dt"])}')
    print(f'{r["weather"][-1]["description"]}\n'
          f'temperatura: {r["main"]["temp"]}°C\n'
          f'ciśnienie: {r["main"]["pressure"]}hPa\n'
          f'wilgotność: {r["main"]["humidity"]}%')
else:
    print(f'Błąd pobierania pogody: {r.status_code}')

# get random quote
r = requests.get('https://type.fit/api/quotes')
if r.status_code == 200:
    random_quote = random.choice(json.loads(r.content))
    print(f'\n\"{random_quote["text"]}\"\n{random_quote["author"]}')
else:
    print(f'Błąd pobierania cytatu: {r.status_code}')

# get current time in Washington, Sydney and Pekin
print(f'\nWashington: {datetime.now(pytz.timezone("US/Pacific")).strftime("%H:%M:%S")}\n'
      f'Sydney: {datetime.now(pytz.timezone("Australia/Sydney")).strftime("%H:%M:%S")}\n'
      f'Shanghai: {datetime.now(pytz.timezone("Asia/Shanghai")).strftime("%H:%M:%S")}')

# find whose name day is today
r = requests.get('https://imienniczek.pl/widget/js')
if r.status_code==200:
    soup = BeautifulSoup(r.content, features='lxml').find_all('a')
    names = [x.text for x in soup if x.text != "Imieniny"]
    print(f'\nDzisiaj imieniny: {", ".join(names)}')
else:
    print(f'Błąd pobierania imienin: {r.status_code}')


