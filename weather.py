from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint


with urlopen("https://weather.yahoo.co.jp/weather/jp/40/8210.html") as res:
  html = res.read().decode("utf-8")
  
  soup = BeautifulSoup(html, "html.parser")
  date = soup.select(".forecastCity td .date span")
  weater = soup.select(".forecastCity td img")
  
  date = [d.string for d in date]
  weater = [w["alt"] for w in weater]
  
  pprint(weater)
  
  pprint('福岡の天気' + date[0] + date[1] + weater[0] + date[2] + date[3] + weater[1])
  

