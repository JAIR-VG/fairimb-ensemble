#from sklearn import neighbors,tree
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import math
import os
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score
from sklearn.model_selection import train_test_split


def load_dataset(nfile):
    df = np.loadtxt(nfile,dtype='str')
    return np.asarray(df[:,0:-1],dtype=float), np.asarray(df[:,-1],dtype=int)

fname=['03subcl5-600-5-0-bi','03subcl5-600-5-30-bi', '03subcl5-600-5-50-bi', '03subcl5-600-5-60-bi',
        '03subcl5-600-5-70-bi', '04clover5z-600-5-0-bi', '04clover5z-600-5-30-bi', '04clover5z-600-5-50-bi', 
        '04clover5z-600-5-60-bi', '04clover5z-600-5-70-bi', 'paw02a-600-5-0-bi', 'paw02a-600-5-30-bi',
        'paw02a-600-5-50-bi', 'paw02a-600-5-60-bi', 'paw02a-600-5-70-bi', '03subcl5-800-7-0-bi', 
        '03subcl5-800-7-30-bi', '03subcl5-800-7-50-bi', '03subcl5-800-7-60-bi', '03subcl5-800-7-70-bi', 
        '04clover5z-800-7-0-bi', '04clover5z-800-7-30-bi', '04clover5z-800-7-50-bi', '04clover5z-800-7-60-bi', 
        '04clover5z-800-7-70-bi', 'paw02a-800-7-0-bi', 'paw02a-800-7-30-bi', 'paw02a-800-7-50-bi', 
        'paw02a-800-7-60-bi', 'paw02a-800-7-70-bi']


nfolds=5
#k_neighbors=3

for element in fname:
    
    fichero = 'datasets/'+element+'/'+element+'.prn'
    
    X,y = load_dataset(fichero)

    rs = 42
    
    rmat = np.zeros((nfolds,6))
    i =0
    for folds in range(1,(nfolds+1)):

        X_tra, X_tst, y_tra, y_tst = train_test_split(X, y, test_size=0.20, random_state=rs+folds, stratify=y)
        
        #clf = neighbors.KNeighborsClassifier(k_neighbors,weights='uniform')
        clf = RandomForestClassifier(random_state=0)
        #clf = tree.DecisionTreeClassifier()
        clf.fit(X_tra,y_tra)

        ypred = clf.predict(X_tst)

        tpr,tnr=recall_score(y_tst,ypred,average = None)
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
    ficherotxt = 'datasets/Holdout8020/'+element+'-'+str(nfolds)+'-8020-RF.avg.txt'
    #ficherotxt = 'datasets/Bias/'+element+'-'+str(nfolds)+'-3NN-100-9010-dt.avg.txt'
    if os.path.exists(ficherotxt):
        os.remove(ficherotxt)

    textfile = open(ficherotxt, "a")
    for listelement in avgrmat:
        textfile.write(str(listelement) + " ")
    textfile.write("\n")
    
    textfile.close()