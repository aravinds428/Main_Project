import re
import tweepy
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob
#from nltk.stem.porter import PorterStemmer
#from stopwords import get_stopwords
from gensim import corpora, models
from nltk.tokenize import RegexpTokenizer

def init():
    consumer_key = "IfuKYq60y957g3BgofJbYrHUz"
    consumer_secret = "lWAiJ9rTNvVMSjNJymiAqrZX4CsZouL8ZTWdWxPDzJThTL2iBz"
    access_key = "948230321660502017-SWKah1yrR5R5z0b5COfqTZXTqIKJh6Q"
    access_secret = "zBUj0kX4WsWHNbiKEYxGi62zvzyWd2aXKeHoXDPvNd3Cg"
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    return auth

def get_tweets(username,auths):
    # Calling api

    api = tweepy.API(auths)

    tweets= api.search( q='cricket', tweet_mode='extended',count=400, lang='en', )

    #number_of_tweets = 200 only 126 can be obtained

   # tweets = api.user_timeline(screen_name=username, count=20, tweet_mode='extended', lang='en')

     #search for particular product code is:
    #tweets = api.search(q='iphonex',count=200,tweet_mode='extended',lang='en')
    return tweets


def clean_tweet(tweet):

        #Utility function to clean tweet text by removing links, special characters
        #using simple regex statements.

        # This is old fuction
        # return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])  | (\w +:\ / \ / \S +)", " ", tweet).split())

        #removelists includes characters to be considered exceptions

        removelist1 = "@"
        removelist2="#"
        rm_ls = r'[0-9]+'
        return ' '.join(re.sub(r'[^\w]'and r'http:\/\/.*[\r\n]*' and r'https?:\/\/.*[\r\n]*' and r'^RT' and rm_ls, " ", tweet).split())

    # replaces non alphanumeric characters by space and splits and joins with space


regex_str = [

    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    #
    # r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]


'''def tokenize(t):
    tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)

    return tokens_re.findall(t)'''


def preprocess(t, lowercase=False):

    # tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
    # emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(t)

    if lowercase:
        tokens = [token.lower() for token in tokens]
    return tokens

def checktxt(checkword,enstop):
    flag=0
    # print(checkword.lower())
    for word in enstop:

         if(word==checkword.lower()):    # if the word is number or stop word return 1 (ignore)
            #print(word ,",",checkword)
            flag=1

    return flag




def tweet_mains():
    #
    auths=init()

    #tweets = get_tweets("@narendramodi",auths)
    inp = raw_input("Enter the name of the user  ")
    tweets = get_tweets(inp, auths)             # inp is user name 

    '''
    friend list get function not complete
    friend_list = get_user("akki47kishore")
    for friend in friend_list:
        print friend.screen_name
        print '\n'''

    # nltk.download('stopwords') do in terminal for stopwords
    #    english_stops = set(stopwords.words('english'))
    tweet_count  = 0
    count=0
    preprocessed = []
    #text_file = open("stopwords.txt", "r")
    with open('stopwords.txt') as f:
        en_stop = [word.strip() for word in f]  # to cut /n
    #en_stop =[x.rstrip('\n') for x in text_file.readline().split(',')]

    # p_stemmer = PorterStemmer()
    for tweet in tweets:

        tweet_count = tweet_count + 1
        print("tweet number=", tweet_count)
        print(tweet.full_text)

        analysis = clean_tweet(tweet.full_text)
        print("cleaning:")
        print(analysis)
        print("tokenize:")
        t = preprocess(analysis)
        words = t
        print(t)
        print("stopwords:")

        texts = [word for word in words if (checktxt(word,en_stop))==0] # if not in stop word list(en_stop)
        #s = [word for word in words if word not in en_stop]
        #print(s)
        #print("stemmed:")
        #texts = [p_stemmer.stem(i) for i in s]
        print(texts)
        preprocessed.append(texts) #= [val for val in texts]
        count=count+1
        print('\n')

    print("final preproceses set")
    for i in range(0,count,1):
        print(preprocessed[i])
        print('\n')

    #final = [val for val in preprocessed]
    #print(final)
'''    dictionary = corpora.Dictionary(final)
    #corpus = [dictionary.doc2bow(val) for val in final]
    corpus = [dictionary.doc2bow(val) for val in final]
    print(corpus[0])

    ldamodel = models.ldamodel.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=500)
    print('\n''\n')
    print("PRINTING RESULTS")
    print('\n''\n')
    print(ldamodel.print_topics(num_topics=9, num_words=10))
'''


if __name__ == '__main__':

    #Main function call
    tweet_mains()
