from newsapi import NewsApiClient
import datetime
import MySQLdb

newsapi = NewsApiClient(api_key='e1690ca5e0c44073bafe2137ef150b5b')


categories = ['business', 'entertainment', 'health', 'science', 'sports', 'technology']

titles = []
urls = []
descriptions = []
urlToImages = []
publishedAts = []

for category in categories:

    headlines = newsapi.get_top_headlines(country='jp',
                                        category=category)
                
    n_articles = len(headlines['articles'])

    for i in range(n_articles):
        titles.append(headlines['articles'][i]['title'])


    for i in range(n_articles):
        urls.append(headlines['articles'][i]['url'])


    for i in range(n_articles):
        descriptions.append(headlines['articles'][i]['description'])


    for i in range(n_articles):
        urlToImages.append(headlines['articles'][i]['urlToImage'])


    for i in range(n_articles):
        temp = headlines['articles'][i]['publishedAt']
        temp = temp.replace('T', ' ')
        temp = temp.replace('Z', '')
        publishedAts.append(temp)

n_data = len(titles)

data = [[None]*5 for _ in range(n_data)]

for i in range(n_data):
    data[i][0] = titles[i]
    data[i][1] = descriptions[i]
    data[i][2] = publishedAts[i]
    data[i][3] = urls[i]
    data[i][4] = urlToImages[i]

"""
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='ルートのパスワード',
    db='python_db',
# テーブル内部で日本語を扱うために追加
    charset='utf8'
)

cursor = connection.cursor()

sql = 'insert into articles articles (title, description, publishedAt, link, linkToImage) values (?. ?, ?, ?, ?)'
"""

print(data[0])



