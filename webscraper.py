from bs4 import BeautifulSoup
import requests
import json

url = "http://ethans_fake_twitter_site.surge.sh/"
response = requests.get(url, timeout = 5)
content = BeautifulSoup(response.content, "html.parser")

tweets = content.findAll('div', attrs = {"class" : "tweetcontainer"})
jsonArray = []

for tweet in tweets:
	tweet_obj = {
		"author" : tweet.find('h2', attrs = {"class" : "author"}).text,
		"tweet" : tweet.find('p', attrs = {"class" : "content"}).text,
		"date" : tweet.find('h5', attrs = {"class" : "dateTime"}).text
	}
	jsonArray.append(tweet_obj)
	
with open('JFtweets.json', 'w') as fout:
	json.dump(jsonArray, fout)
