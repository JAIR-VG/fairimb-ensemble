import numpy as np
import math
import os
#from sklearn.ensemble import RandomForestClassifier
#from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score


def load_dataset(nfile):
    df = np.loadtxt(nfile,dtype='str')
    return np.asarray(df[:,0:-1],dtype=float), np.asarray(df[:,-1],dtype=int)


nfolds=10

#fname=['yeast1','wisconsinImb']

fname=['yeast1','wisconsinImb']

for element in fname:
    print(element)
    rmat = np.zeros((nfolds,6))
    i =0
    for folds in range(1,(nfolds+1)):
        #ftra = 'datasets/Real/3/'+element+'/'+element+'-'+str(nfolds)+'-'+str(folds)+'tra.prn'
        #ftst = 'datasets/Real/3/'+element+'/'+element+'-'+str(nfolds)+'-'+str(folds)+'tst.prn'
        ftra = 'datasets/Real/3/'+element+'/'+element+'-'+str(nfolds)+'dobscv-'+str(folds)+'tra.prn'
        ftst = 'datasets/Real/3/'+element+'/'+element+'-'+str(nfolds)+'dobscv-'+str(folds)+'tst.prn'
        
        X_tra,y_tra = load_dataset(ftra)
        
        X_tst,y_tst = load_dataset(ftst)

        #clf = XGBClassifier(n_estimators=100,objective='binary:logistic')

       # clf = RandomForestClassifier(random_state=0)
        
        clf = CatBoostClassifier(n_estimators=100)

        clf.fit(X_tra,y_tra)

        ypred = clf.predict(X_tst)

        tpr,tnr=recall_score(y_tst,ypred,average = None)
        print(tpr)
        print(tnr)
        prec = precision_score(y_tst,ypred, pos_label=0)
        f1=f1_score(y_tst,ypred, pos_label=0)
        gmean = math.sqrt(tpr*tnr)
        acc = accuracy_score(y_tst,ypred)
        rmat[i][0]=tpr
        rmat[i][1]=tnr
        rmat[i][2]=prec
        rmat[i][3]=f1
        rmat[i][4]=gmean
        rmat[i][5]=acc
        i=i+1

    avgrmat = np.mean(rmat,axis=0)
    #ficherotxt = 'datasets/Real/3/'+element+'-'+str(nfolds)+'dobscv-XGB.avg.txt'
    ficherotxt = 'datasets/Real/3/'+element+'-'+str(nfolds)+'dobscv-Cat.avg.txt'
    if os.path.exists(ficherotxt):
        os.remove(ficherotxt)

    textfile = open(ficherotxt, "a")
    for listelement in avgrmat:
        textfile.write(str(listelement) + " ")
    textfile.write("\n")
    
    textfile.close()
