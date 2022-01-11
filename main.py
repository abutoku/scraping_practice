# モジュールをインストール
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint

#1.Get a html. htmlをサーバーからインストールする
with urlopen("http://www.yoheim.net") as res:
  #res.read()でバイナリ型で受け取る,.decodeでutf-8に戻す
  html = res.read().decode("utf-8")

# 2. Load a html by BeautifulSoup. 解析できる状態にする
soup = BeautifulSoup(html, "html.parser")

# 3. Get items you want.必要な情報を受け取る
titles = soup.select(".articleListItem h2")
titles = [t.string for t in titles]

# Check results.
#pprint =>綺麗な状態で取得
pprint(titles[:4])


#----selectors in BeautifulSoup-------------------------

##select CSSのセレクターでアクセス

#soup.select(".articleListItem h2")

##select_one

#soup.select_one(“.articleListItem h2")

##find 該当する要素を一つだけ取得

# soup.find("h1")
# soup.find(id="header_subtitle")
# soup.find(class_="articleListItem")


##find_all すべて該当する要素を一つだけ取得

# soup.find_all("h1")
# soup.find_all(id="header_subtitle")
# soup.find_all(class_="articleListItem")


# -----extractors in BeautifulSoup---------------------

##text
# <h1>My Special App</h1>
# タグの中の文字列を取得

# elm.string

##attribute
# <img src="/my_secret.png"/>
# 属性の中身を取得

# elm["src"]
