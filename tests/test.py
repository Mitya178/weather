import json

st = """{"cod": "200", "message": 0, "cnt": 3, "list": [{"dt": 1632085200, "main": {"temp": 17.13, "feels_like": 17.09, "temp_min": 17.13, "temp_max": 17.57, "pressure": 1016, "sea_level": 1016, "grnd_level": 1013, "humidity": 84, "temp_kf": -0.44}, "weather": [{"id": 500, "main": "Rain", "description": "небольшой дождь", "icon": "10n"}], "clouds": {"all": 60}, "wind": {"speed": 1.89, "deg": 340, "gust": 5.43}, "visibility": 10000, "pop": 0.32, "rain": {"3h": 0.3}, "sys": {"pod": "n"}, "dt_txt": "2021-09-19 21:00:00"}, {"dt": 1632096000, "main": {"temp": 16.5, "feels_like": 16.29, "temp_min": 16.29, "temp_max": 16.5, "pressure": 1017, "sea_level": 1017, "grnd_level": 1014, "humidity": 80, "temp_kf": 0.21}, "weather": [{"id": 803, "main": "Clouds", "description": "облачно с прояснениями", "icon": "04n"}], "clouds": {"all": 80}, "wind": {"speed": 3.37, "deg": 350, "gust": 8.43}, "visibility": 10000, "pop": 0.2, "sys": {"pod": "n"}, "dt_txt": "2021-09-20 00:00:00"}, {"dt": 1632106800, "main": {"temp": 15.46, "feels_like": 14.89, "temp_min": 15.46, "temp_max": 15.46, "pressure": 1018, "sea_level": 1018, "grnd_level": 1015, "humidity": 70, "temp_kf": 0}, "weather": [{"id": 804, "main": "Clouds", "description": "пасмурно", "icon": "04n"}], "clouds": {"all": 100}, "wind": {"speed": 3.37, "deg": 346, "gust": 9.53}, "visibility": 10000, "pop": 0.06, "sys": {"pod": "n"}, "dt_txt": "2021-09-20 03:00:00"}], "city": {"id": 2643743, "name": "Лондон", "coord": {"lat": 51.5085, "lon": -0.1257}, "country": "GB", "population": 1000000, "timezone": 3600, "sunrise": 1632030116, "sunset": 1632074805}}"""
todo = json.loads(st)

#print(todo["list"])
temp=[]
pressure=[]
humidity=[]
for l in todo["list"]:
  t = (l["main"]["temp"])
  p = (l["main"]["pressure"])
  h = (l["main"]["humidity"])
  temp.append(t)
  pressure.append(p)
  humidity.append(h)


print(temp)
print(pressure)
print(humidity)
