# Tweet Mood Analyzer

Using IBM Watson's Tone Analyzer, this simple Python script analyzes a Tweet for it's mood, such as anger, sadness, etc.

## Prerequisites

### Python 3.X
With the following packages:
```bash
pip install watson_developer_cloud
pip install python-twitter
```

### IBM Watson Bluemix & Tone Analyzer Setup
1. Create an account on [IBM Watson's Bluemix](https://www.ibm.com/watson/developercloud/tone-analyzer.html) website.
2. After logging in, click on *Catalog* (top-right)
3. On the left-hand side, click on three-horizontal menu accordion and select **Services** > **Watson**.
4. Click on **Create Watson Service** button.
5. Select **Tone Analyzer**.
6. Copy the `username` and `password`. We'll use that to make calls to the service in our Python script.

### Twitter Developer Account Setup
1. If you don't already, create a regular Twitter account.
2. Then, go to https://dev.twitter.com/resources/signup and fill out the form.
3. After you've gone through the registration process, navigate to https://apps.twitter.com/app/new and create a new app.
4. Copy down the following:
	- Consumer Key (API Key)
	- Consume Secret (API Secret)
	- Access Token
	- Access Token Secret

## Running the Script

You'll need to pass in the following **required** environment variables when calling the Python script.

| Environment Variable 	| Description                                                                                    	|
|----------------------	|------------------------------------------------------------------------------------------------	|
| `tck`                	| Twitter Consumer Key                                                                           	|
| `tcs`                	| Twitter Consumer Secret                                                                        	|
| `tat`                	| Twitter Access Token                                                                           	|
| `ttc`                	| Number of Tweets to analyze (recommend around 10)                                              	|
| `tats`               	| Twitter Access Token Secret                                                                    	|
| `tun`                	| Twitter Username -- the username of Twitter user you want Tweets analyzed (e.g., `twitterapi`) 	|
| `watson_tau`         	| Watson Tone Analyzer Username                                                                  	|
| `watson_tap`         	| Watson Tone Analyzer Password                                                                  	|

### Sample Input
```python
tck="<twitter-consumer-key>" tcs="<twitter-consumer-secret>" tat="<twitter-access-token>" tats="twitter-access-token-secret" watson_tau="<tone-analyzer-username>" watson_tap="<tone-analyzer-password>" ttc=<tweet-count> tun=<twitter-username> python twitter-mood-analyzer.py
```

### Sample Output
```
TWEET #1
Great meeting with the @RepublicanStudy Committee this morning at the @WhiteHouse! https://t.co/8Y2UoHoYaY
Anger: 1.72
Disgust: 3.04
Fear: 1.7
Joy: 68.48
Sadness: 11.89
---------------
TWEET #2
"The President Changed. So Has Small Businesses' Confidence"
https://t.co/daTGjPmYeJ
Anger: 1.41
Disgust: 11.91
Fear: 4.22
Joy: 66.56
Sadness: 5.04
---------------
TWEET #3
North Korea is behaving very badly. They have been "playing" the United States for years. China has done little to help!
Anger: 13.57
Disgust: 52.64
Fear: 6.52
Joy: 1.07
Sadness: 41.74
---------------
```

## Known Bugs & Planned Improvements

 - **String parsing error** -- some strings cause the Tone Analyzer SDK to crash. It's likely due to unsupported characters. More investigation is needed.
 - **Simpler UX** -- the current implementation isn't very user-friendly with having to pass in credentials via environment variables. A simpler initialization (maybe step-by-step) might be better.
 - **Free *Tone Analyzer* alternative** -- although the IBM Watson Tone Analyzer works as expected, the 30-day free trial isn't ideal for long-term usage. I'll need to investigate equivalent free alternative services.
