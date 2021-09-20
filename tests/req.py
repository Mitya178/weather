import os
import requests
city = "London"
cnt = "3"
API_KEY = os.environ['API_KEY']

#print(f"API = {API_KEY}")

#r=API_KEY
#print(r)
response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&lang=ru&cnt={cnt}&units=metric')
print (response.json())
