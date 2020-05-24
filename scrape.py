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
cates = []

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
    
    for i in range(n_articles):
        cates.append(category)

n_data = len(titles)

data = []

for i in range(n_data):
    temp = (titles[i], descriptions[i], cates[i], publishedAts[i], urls[i], urlToImages[i])
    data.append(temp)


connection = MySQLdb.connect(
    host='localhost',
    user='tsutsutaku',
    passwd='P0c0i224.',
    db='news',
# テーブル内部で日本語を扱うために追加
    charset='utf8'
)

cursor = connection.cursor()

sql = 'insert into articles (title, description, category, publishedAt, link, linkToImage) values (%s, %s, %s, %s, %s, %s)'

cursor.executemany(sql, data)

connection.commit()
connection.close()




