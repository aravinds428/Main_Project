from nlp import preprocess as preproc
import os
import glob
from gensim.models import Word2Vec
def Train():
    
    print("EnteredTrain")
    preprocessed = [] 
    wordcount = 0
    categoryId =0
    
    #string =[ "Hello this is it;","Hi How are you","This is Congratulations:"]
    
    path = ('./dataset/input/')
    #string =[ "Hello this is it;","Hi How are you","This is Congratulations:"]
    
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open('./dataset/test.txt','r+') as f:
            tweets = [x.strip() for x in f] 
            preprocessed = preproc.tweet_mains(tweets)
    m = Word2Vec(preprocessed)
    print m.vocab
    m.most_similar('SunRisers', topn=5)
   
    
    '''for tweet in preprocessed:
       for word in tweet: 
           print word
           m = Word2Vec(word)
           print m'''

if __name__=='__main__':
  
    Train()
