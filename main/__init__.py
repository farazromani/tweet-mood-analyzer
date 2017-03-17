import twitter
import os
import json
from watson_developer_cloud import ToneAnalyzerV3
from _codecs import encode
import re

# Assign environment variables to local variables
twitter_consumer_key = os.environ['tck']
twitter_consumer_secret = os.environ['tcs']
twitter_access_token = os.environ['tat']
twitter_access_token_secret = os.environ['tats']
twitter_username = os.environ['tun']
twitter_tweet_count = os.environ['ttc']
ta_username = os.environ['watson_tau']
ta_password = os.environ['watson_tap']

# Initialize Twitter SDK
api = twitter.Api(consumer_key=twitter_consumer_key,
                    consumer_secret=twitter_consumer_secret,
                    access_token_key=twitter_access_token,
                    access_token_secret=twitter_access_token_secret)

# Make Twitter SDK call to retrieve Tweets
statuses = api.GetUserTimeline(screen_name=twitter_username, count=twitter_tweet_count)

# Initialize Tone Analyzer SDK
tone_analyzer = ToneAnalyzerV3(
    username=ta_username,
    password=ta_password,
    version='2016-02-11')

# Remove emoticons from Tweet
emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
    u"\U0001F680-\U0001F6FF"  # transport & map symbols
    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       "]+", flags=re.UNICODE)

# Iterate through each Tweet
for index, s in enumerate(statuses):
  
    # Analyize the Tweet string
    tone_analyzer_result = tone_analyzer.tone(text=s.text)
    
    print("Tweet #" + str(index + 1) + ": " + str(emoji_pattern.sub(r'', s.text.strip())))
    
    document_tone = tone_analyzer_result["document_tone"]
    for tone_categories in document_tone["tone_categories"]:

        # Store emotional attributes
        emotions = {}
        
        if tone_categories["category_id"] == "emotion_tone":
            for tone in tone_categories["tones"]:
                emotions[tone["tone_name"]] = tone["score"] * 100
    
            result = "".join(str(key) + ": " + str(round(value, 2)) + " " for key, value in emotions.items())
            print(result + "\n")
