from nlp import preprocess as preproc
from worddoc import wdf as w
#from SVM import SVMProcess1 as svm
#from sentiment import senti as sent
import os
import glob
from collections import Counter

def Train():
    
    print("EnteredTrain")
    preprocessed = [] 
    wordcount = 0
    categoryId =0
    path = ('./dataset/input/')
    #string =[ "Hello this is it;","Hi How are you","This is Congratulations:"]
    
    for filename in glob.glob(os.path.join(path, '*.txt')):
      categoryId += 1
      with open(filename) as f:
           tweets = [x.strip() for x in f] 
           preprocessed = preproc.tweet_mains(tweets)
           wordcount = w.generatewordset(preprocessed,categoryId)
           #svm.create_trainfile() "not complete" 
    
    '''for pre in preprocessed:
        print pre'''

    print("Leaving Train")


def Test():
    print("Entered Test")
    wordcount = 0
    path = ('./dataset/Test/input/bse.txt')
    with open(path) as f:
           tweets = [x.strip() for x in f] 
           preprocessed = preproc.tweet_mains(tweets)
           wordcount = w.generatetestset(preprocessed)
    print("Leaving Test") 


             
 
       

if __name__=='__main__':
    
    inpu = input("1.User's Interest \t2.Sentiment")
    if(inpu ==1):
       case = input("1.Train\t 2.Test")

       if(case==1):

           Train()
       else:

           Test()
    else:
      #sent.main()
      pass

