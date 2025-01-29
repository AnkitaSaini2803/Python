''' 25/1/2025
Use the NewsAPI and the requests module to fetch the daily news related to 
different topics. Go to: https://newsapi.org/ and explore the various options 
to build you application
'''
import requests
import json
query=input("What type of news are you interested In : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-12-25&sortBy=publishedAt&apiKey=6e5f02dd14724469988c80b8b59f017a"
detail=requests.get(url)
# print(detail.text)         #as a text dega
news=json.loads(detail.text)
print(news,type(news))

