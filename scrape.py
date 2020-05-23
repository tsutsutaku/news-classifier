from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='e1690ca5e0c44073bafe2137ef150b5b')

headlines = newsapi.get_top_headlines(country='jp',
                                      category='technology')
                        

titles = []
for i in range(20):
   titles.append(headlines['articles'][i]['title'])

urls = []
for i in range(20):
    urls.append(headlines['articles'][i]['url'])