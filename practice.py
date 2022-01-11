# モジュールをインストール
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

with urlopen("https://gsacademy.jp/mentor/") as res:
  html = res.read().decode("utf-8")
  
soup = BeautifulSoup(html, "html.parser")

titles = soup.select(".col_prof h3")
# img = soup.select(".col_prof img")
titles = [t.string for t in titles]


pprint(titles)