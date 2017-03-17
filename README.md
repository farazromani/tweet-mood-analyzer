# Twitter Mood Analyzer

Using IBM Watson's Tone Analyzer, this simple Python script analyzes a Tweet for it's mood, such as anger, sadness, etc.

## How to Build

### Prerequisites

#### Python 3.X
With the following packages:
```bash
pip install watson_developer_cloud
pip install python-twitter
```

#### IBM Watson Bluemix & Tone Analyzer Setup
1. Create an account on [IBM Watson's Bluemix](https://www.ibm.com/watson/developercloud/tone-analyzer.html) website.
2. After logging in, click on *Catalog* (top-right)
3. On the left-hand side, click on three-horizontal menu accordion and select **Services** > **Watson**.
4. Click on **Create Watson Service** button.
5. Select **Tone Analyzer**.
6. Copy the `username` and `password`. We'll use that to make calls to the service in our Python script.

#### Twitter Developer Account Setup
1. If you don't already, create a regular Twitter account.
2. Then, go to https://dev.twitter.com/resources/signup and fill out the form.
3. After you've gone through the registration process, navigate to https://apps.twitter.com/app/new and create a new app.
4. Copy down the following:
	- Consumer Key (API Key)
	- Consume Secret (API Secret)
	- Access Token
	- Access Token Secret

### Running the Script

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

#### Sample Input
```python
tck="stMjbgJDPJq6g9sLK66lf3FOOBAR" tcs="req79u8cBSryBMzyc7juDCwOrw9eBaNNhms76gshRPrS6ToFOOBAR" tat="14684320-IJuCE47ckjQbl6EzrFyKpo3XQrgmgbFPjPjIxUFOOBAR" tats="ij50IGYtMPcBnA7ESyCiAqHrPjC3KyUBDiVvUMYl6gFOOBAR" watson_tau="5c9028eb-1328-4924-a298-c737c6e9dFOOBAR" watson_tap="wZiIA2t2aFOOBAR" ttc=10 tun=realdonaldtrump python __init__.py
```

#### Sample Output
```
Tweet #1: My representatives had a great meeting w/ the Hispanic Chamber of Commerce at the WH today. Look forward to tremendous growth &amp; future mtgs!
Anger: 2.69 Disgust: 1.15 Fear: 2.61 Joy: 76.03 Sadness: 7.2 

Tweet #2: Great progress on healthcare. Improvements being made - Republicans coming together!
Anger: 5.88 Disgust: 8.98 Fear: 1.35 Joy: 72.01 Sadness: 3.01 

Tweet #3: RT @USHCC: USHCC was delighted to host @IvankaTrump for a roundtable discussion w/ Hispanic women biz owners today in Washington #USHCCLegi…
Anger: 5.26 Disgust: 25.48 Fear: 2.72 Joy: 44.62 Sadness: 11.12 

Tweet #4: An honor to welcome the Taoiseach of Ireland, @EndaKennyTD to the @WhiteHouse today with @VP Pence.  https://t.co/J3iTl2iSiQ
Anger: 0.29 Disgust: 10.77 Fear: 1.37 Joy: 71.5 Sadness: 5.83 

Tweet #5: A budget that puts #AmericaFirst must make safety its no. 1 priority—without safety there can be no prosperity: https://t.co/9lxx1iQo7m
Anger: 6.52 Disgust: 48.21 Fear: 9.53 Joy: 11.94 Sadness: 26.82 
```
