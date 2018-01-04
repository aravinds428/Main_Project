from nltk.tokenize import TweetTokenizer
from  nltk.corpus import stopwords
import string

import requests
from requests_oauthlib import OAuth1

consumer_key =  '9M3mv6QKuEZN1o74voiZXqHyC'
consumer_secret = 'vygMZiBKxVlTq1iyAkN8q3cBUGMZQWpTLc41xEvBQzR93G5Dtb'

acess_token =  '914350353805709312-AX6KU6LGNoxuTGTdck6W7wlQxFT1oue'
acess_token_secret =  'dJJ35wMvSRTrhu7UVzcFqPgORgGNXLmIxvsEA21Wqi9HG'

q = 'iphonex - filter:retweets AND -filter:replace'

url = 'https://api.Twitter.com/1.1/search/tweets.json'
pms = {'q': q,'count':100,'lang':'en','result_type':'recent'}

auth = OAuth1(consumer_key, consumer_secret, acess_token, acess_token_secret)

res = requests.get(url,params=pms,auth=auth)

tweets = res.json()

for i in range(0,10):
    print (tweets['statuses'][i]['text'])
    print ('\n')




