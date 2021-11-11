import requests
import os
import json

from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
API_KEY = os.environ['API_KEY']


@app.route("/weather", methods=['GET'])
def index():
    city = request.args.get('city')
    days = request.args.get('days')
    days = (int(days)*8)
    r = req(city, days)
    out={}
    date_arr=[]
    temp=[]
    pressure=[]
    humidity=[]
    for l in r["list"]:
        dt = (l["dt"])
        t = (l["main"]["temp"])
        p = (l["main"]["pressure"])
        h = (l["main"]["humidity"])
        date_arr.append(dt)
        temp.append(t)
        pressure.append(p)
        humidity.append(h)
    date_sort=sorted(date_arr, reverse=True)
    date_to=datetime.fromtimestamp(date_sort[0]).strftime("%Y-%m-%d")
    date_from=datetime.fromtimestamp(date_sort[int(days)-1]).strftime("%Y-%m-%d")

    out["city"] = city
    out["from"] = date_from
    out["to"] = date_to
    w = ["temperature_c", "pressure_mb", "humidity"]
    for put_out in w:
      if put_out == "temperature_c":
        array=temp
      elif put_out == "pressure_mb":
        array=pressure
      elif put_out == "humidity":
        array=humidity

      out[put_out]={}
      out[put_out]["average"] = average(array)
      out[put_out]["median"] = median(array)
      out[put_out]["min"] = minv(array)
      out[put_out]["max"] = maxv(array)

    json_string = json.dumps(out)
    return json_string


def req(city, days):
    city = city
    cnt = days
    response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&lang=ru&cnt={cnt}&units=metric')
    return response.json()

def median(sample):
    n = len(sample)
    if n%2:
        sarr=(sorted(sample, reverse=True))
        m = (n+1)/2
        return f"{sarr[int(m)-1]}"
    else:
        sarr=(sorted(sample, reverse=True))
        m1 = n/2
        m2 = m1 -1
        m = (sarr[int(m2)] + sarr[int(m1)])/2
        return f"{round(m, 2)}"


def average(sample):
    n = len(sample)
    a = sum(sample)/n
    return f"{round(a, 2)}"


def maxv(sample):
    n = len(sample)
    sarr=(sorted(sample, reverse=True))
    return f"{sarr[0]}"


def minv(sample):
    n = len(sample)
    sarr=(sorted(sample, reverse=True))
    return f"{sarr[n-1]}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
