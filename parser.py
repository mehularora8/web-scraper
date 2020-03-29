import json

with open("JFtweets.json") as fin:
	tweet_data = json.load(fin)

jimmyCounter = 0

for tweet in tweet_data:
	if "obama" in tweet['tweet'].lower():
		jimmyCounter += 1

print(jimmyCounter)