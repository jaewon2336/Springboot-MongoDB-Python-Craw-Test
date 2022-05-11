from operator import truediv
# 몽고 DB 연결
from pymongo import MongoClient
from pymongo.cursor import CursorType
# html 다운
import requests
# html 파싱
from bs4 import BeautifulSoup
# 날짜 타입
import datetime

# Mongo 연결
mongo = MongoClient("localhost", 20000)


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


# sid = 100 (정치) oid = 005 (국민일보)
html = requests.get(
    "https://n.news.naver.com/mnews/article/005/0000000002?sid=100")

soup = BeautifulSoup(html.text, 'html.parser')

title = soup.select_one(".media_end_head_headline").text
company = soup.select(".media_end_head_top_logo_img")[0]["alt"]
createdAt = datetime.datetime.now()

print(title)

navers = [{"title": title, "company": company, "createdAt": createdAt}, {
    "title": "제목1", "company": "회사1", "createdAt": createdAt}]
print(type(navers))

aaa = mongo_save(mongo, navers, "greendb", "navers")  # List안에 dict을 넣어야 함
print(aaa)
