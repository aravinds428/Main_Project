import os
import sys
from collections import Counter
sys.path.insert(0, '../libsvm/python')
from svmutil import * 

def create_trainfile(flow):
  
    print("\nIn train:\n\n")
    
    
    os.getcwd()   
    if flow==1:                                         # os.getcwd is used if the py file is used to be called from another main file 
      files1 = os.path.abspath('../dataset/Trained/docset.txt') 
      files = ['../dataset/Trained/trainingfiles/sportstrainfile.txt','../dataset/Trained/trainingfiles/financetrainfile.txt']
    else:
      files1 = os.path.abspath('../dataset/Test/testdocset.txt')     # Here when we  all this py file docset.txt should be absolute path                 
      files = ['../dataset/Test/liblinear/testf.txt']                          #add training files when necessary
    N=2                                                    #explicit declaration of no. of training files to be created
    
                                                          
    
    doc =[]
    tweetidchecklist=[]
    documentwords =[] 
    catId = {}
    countId =str(1)

   
    for index in range(0,N,1):                          #No. of files
      print(index)
      if flow==1:
         cat = index+1
         currentcat = str(cat)
      else:                            #Be careful with str.when you get from the txt file obtained value is str.
         currentcat = str(0)
      filesk = os.path.abspath(files[0])#index for training and '0' for testing
      tf = open(filesk,'a+')

      df=open(files1,'r+')

      for entry in df:
       
         docset = entry.split()
         categoryId = docset[0]
                                               #categoryId
         tweetId = docset[1]
                                               #tweetId
         wordId = docset[2]
                                               #wordId
         i = 0
         if(categoryId !=  currentcat):        #if not current category != obtained categoryid then not the needed field
               
               categoryId = str(-1)
               
             
               
         
           
         

         if(tweetId == countId):            #Check if the word is in the same tweetId
            
               doc.append(long(wordId))     #then add to an array 
   
         else:
      
               tf.write(str(categoryId)+"\t")    #write to the specified files the category id(id / -1)
               for docs in doc:
                  tf.write(str(docs)+":"+str(1)+"\t") #write the tweet and the its wt.
               tf.write("\n") 
               
               doc = []
               doc.append(wordId)                     #because the first word of the tweet will not be added in other case

         countId = tweetId                             #change tweet Id
   
         
    #tf.close()
    df.close()        
    print("Leaving creating train")



def train_models():

    '''labels,features=svm_read_problem('../dataset/Trained/trainingfiles/sportstrainfile.txt')
    options='-s 0  -t 1 -c 4 -v 5'
    m1=svm_train(labels,features,str(options))
    p_label, p_acc, p_val = svm_predict(labels, features, m1)
    svm_save_model('../dataset/Trained/models/sports.model',m1)'''

    labels,features=svm_read_problem('../dataset/Trained/trainingfiles/financetrainfile.txt')
    #options='-s 0  -t 1 -c 4 -v 5'
    options='-s 0  -t 1 -c 0.03125 '
    m1=svm_train(labels,features,str(options))
    p_label, p_acc, p_val = svm_predict(labels, features, m1)
    svm_save_model('../dataset/Trained/models/finance.model',m1)



def testSVM():
    m=svm_load_model('../dataset/Trained/models/sports.model')
    labelsS,featuresS=svm_read_problem('../dataset/Test/liblinear/testf.txt')
    s_label, p_acc, p_val = svm_predict(labelsS, featuresS, m)
    print "Sports:  "+str(s_label)
    c = Counter(s_label)
    print c

    m1=svm_load_model('../dataset/Trained/models/finance.model')
    labelsF,featuresF=svm_read_problem('../dataset/Test/liblinear/testf.txt')
    f_label, p_acc, p_val = svm_predict(labelsF, featuresF, m1)
    print "Finance:  "+str(f_label)
    c = Counter(f_label)
    print c

   
if __name__=='__main__':
    #create_trainfile(2)   # 1 for train and 2 for test
    #train_models()
    testSVM()
