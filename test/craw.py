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


navers = []
aid = 1  # 얘를 ++해서 "0000000002"로 변환한 후 url에 넣어야함 # for문의 i가 대신함
result = 0

# sid = 100 (정치) oid = 005 (국민일보)


# # 1번글
# html = requests.get(
#     "https://n.news.naver.com/mnews/article/005/0000000001?sid=100")

# soup = BeautifulSoup(html.text, 'html.parser')

# title = soup.select_one(".media_end_head_headline").text
# company = soup.select(".media_end_head_top_logo_img")[0]["alt"]
# createdAt = datetime.datetime.now()

# naver_dict = {"title": title, "company": company, "createdAt": createdAt}

# navers.append(naver_dict)
# print(len(navers))


# 2번글부터 클래스 이름 달라짐
while True:

    aid_string = format(aid, '010')

    # sid = 100 (정치) oid = 005 (국민일보)
    try:
        html = requests.get(
            f"https://entertain.naver.com/read?oid=005&aid={aid_string}&sid=100")

        if html.status_code == 200:

            soup = BeautifulSoup(html.text, 'html.parser')

            title = soup.select_one(".end_tit").text
            company = soup.select(".press_logo > img")[0]["alt"]
            createdAt = datetime.datetime.now()

            dict = {"title": title, "company": company, "createdAt": createdAt}
            navers.append(dict)
            print(len(navers))

            result += 1

        if result == 20:
            print("끝")
            break

        aid += 1

    except Exception as e:
        print("뭔가 잘못됨")
        pass

aaa = mongo_save(mongo, navers, "greendb", "navers")  # List안에 dict을 넣어야 함
print(aaa)
