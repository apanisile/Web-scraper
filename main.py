from bs4 import BeautifulSoup
import requests
import json

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

tweettArr = []

for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}),
        "tweet": tweet.find('p', attrs={"class": "content"}),
        "dateTime": tweet.find('h5', attrs={"class": "dateTime"})
    }

    print(tweetObject)



