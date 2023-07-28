from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

import numpy as np

from sklearn.metrics import recall_score

def load_dataset(nfile):
    df = np.loadtxt(nfile,dtype='str')
    return np.asarray(df[:,0:-1],dtype=float), np.asarray(df[:,-1],dtype=int)


def get_labels(ylabel,indx):
    return(ylabel[indx])

def get_uniquelabels(ylabel):
    return np.unique(ylabel)


fname=['03subcl5-600-5-0-bi','03subcl5-600-5-30-bi', '03subcl5-600-5-50-bi', '03subcl5-600-5-60-bi',
        '03subcl5-600-5-70-bi', '04clover5z-600-5-0-bi', '04clover5z-600-5-30-bi', '04clover5z-600-5-50-bi', 
        '04clover5z-600-5-60-bi', '04clover5z-600-5-70-bi', 'paw02a-600-5-0-bi', 'paw02a-600-5-30-bi',
        'paw02a-600-5-50-bi', 'paw02a-600-5-60-bi', 'paw02a-600-5-70-bi', '03subcl5-800-7-0-bi', 
        '03subcl5-800-7-30-bi', '03subcl5-800-7-50-bi', '03subcl5-800-7-60-bi', '03subcl5-800-7-70-bi', 
        '04clover5z-800-7-0-bi', '04clover5z-800-7-30-bi', '04clover5z-800-7-50-bi', '04clover5z-800-7-60-bi', 
        '04clover5z-800-7-70-bi', 'paw02a-800-7-0-bi', 'paw02a-800-7-30-bi', 'paw02a-800-7-50-bi', 
        'paw02a-800-7-60-bi', 'paw02a-800-7-70-bi']



nfolds=5

for folds in range(1,(nfolds+1)):
    #ftra = 'datasets/'+element+'/'+element+'-5x2-'+str(folds)+'tst.prn'
   # ftra = 'datasets/03subcl5-600-5-50-bi/03subcl5-600-5-50-bi-5x2-'+str(folds)+'tra.prn'
    #ftst = 'datasets/03subcl5-600-5-50-bi/03subcl5-600-5-50-bi-5x2-'+str(folds)+'tst.prn'

    

    ftra = 'datasets/03subcl5-600-5-50-bi/03subcl5-600-5-50-bi-'+str(nfolds)+'dobscv-'+str(folds)+'tra.prn'
    ftst = 'datasets/03subcl5-600-5-50-bi/03subcl5-600-5-50-bi-'+str(nfolds)+'dobscv-'+str(folds)+'tst.prn'

    Xtra,ytra = load_dataset(ftra)
    
    Xtst,ytst = load_dataset(ftst)

   # tree = DecisionTreeClassifier(random_state=0).fit(Xtra, ytra)

   # tree = LogisticRegression(random_state=0).fit(Xtra, ytra)

    tree = MLPClassifier(random_state=1, max_iter=1000).fit(Xtra,ytra)

    #tree.fit(Xtra,ytra)

    #ree = GaussianNB().fit(Xtra, ytra)

    ypred = tree.predict(Xtst)

    print(recall_score(ytst,ypred,average = None))

    ypred = tree.predict(Xtra)

    tp1,tp2=recall_score(ytra,ypred,average = None)

    print(tp1,tp2)