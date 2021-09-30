

# App Weather
Application to call weather forecast

## Linux
```
# python3 -m pip install -r requirements.txt
# export API_KEY=<your api key>
# Please get api key from https://openweathermap.org/api/forecast30#data
# python3 main.py
```

## Docker
```

# docker pull mitya178/task2_dell:v1

# docker run -p 8080:8080 --rm -e API_KEY='Your_API_KEY' mitya178/task2_dell:v1
```

## How to check
```

# curl 127.0.0.1:8080/weather?city=London\&days=4
```
