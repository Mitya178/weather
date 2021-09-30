

# App Weather
Application to call weather forecast

### Linux
```
# python3 -m pip install -r requirements.txt
# export API_KEY=<your api key>
# Please get api key from https://openweathermap.org/api/forecast30#data
# python3 main.py
```

## Docker
```

# pulling image from dockerhub

# docker pull mitya178/task2_dell:v1

# running your service

# docker run -p 8080:8080 --rm -e API_KEY='Your_API_KEY' mitya178/task2_dell:v1
```

## How to check
```
# sudo apt-get

# sudo apt install -y docker.io

# curl 127.0.0.1:8080/weather?city=London\&days=4
```
