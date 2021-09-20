import requests
city = "London"
cnt = "3"
response = requests.get(f'https://pro.openweathermap.org/data/2.5/forecast/climate?q={city}&appid=7ace9452d6c407830023ad484d1decae&lang=ru&cnt={cnt}&units=metric')
print (response.json())
