import json

# Get JSON data from file
with open("JFtweets.json") as fin:
	tweet_data = json.load(fin)

# Counter
jimmyCounter = 0

# Find words
for tweet in tweet_data:
	if "obama" in tweet['tweet'].lower():
		jimmyCounter += 1

print(jimmyCounter)
