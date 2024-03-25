import numpy as np
import os
from sklearn.model_selection import train_test_split


def load_dataset(nfile):
    df = np.loadtxt(nfile,dtype='str')
    return np.asarray(df[:,0:-1],dtype=float), np.asarray(df[:,-1],dtype=int)

def mydist2(vctr, mtrx):
    return np.linalg.norm(mtrx-vctr,axis=1)


def get_indxknn(dstnc,k):
    return dstnc.argsort()[:k]

def get_labels(ylabel,indx):
    return(ylabel[indx])

def get_uniquelabels(ylabel):
    return np.unique(ylabel)

def count_labels(zlabel,ylabel):
    for x in zlabel:
        print((ylabel==zlabel[x]).sum())

def count_label(thelabel,ylabel):
    return (ylabel==thelabel).sum()

def kind_sample(xvector, yvector,xmatrix,ymatrix,kvalue):
    distancia = mydist2(xvector,xmatrix)
    indx_k = get_indxknn(distancia,kvalue)
    klabels = get_labels(ymatrix,indx_k)
    numknn = count_label(yvector,klabels)
    if (numknn/kvalue) >= 0.8:
       return 0
    else:
        if (numknn/kvalue) >= 0.4:
            return 1
        else:
            if (numknn/kvalue) >= 0.2:
                return 2
            else:
                return 3



#fname=['ecoli-0_vs_1', 'glass0', 'glass1', 'habermanImb', 'iris0', 'pimaImb', 'vehicle1', 'vehicle2', 'vehicle3', 'wisconsinImb', 'yeast1']

#fname=['ecoli-0-1-3-7_vs_2-6', 'poker-8_vs_6', 'poker-8-9_vs_5', 'poker-8-9_vs_6', 'shuttle-2_vs_5', 'winequality-red-3_vs_5',
 #      'winequality-red-8_vs_6', 'winequality-red-8_vs_6-7','winequality-white-3-9_vs_5','winequality-white-9_vs_4', 'yeast-1-2-8-9_vs_7',
  #      'yeast4','yeast6']

fname=['ecoli-0_vs_1']

nfolds=5
#tipeir=30
tipeir=3

for elements in fname:
    print(elements)

    fichero = 'datasets/Real/'+str(tipeir)+'/'+elements+'/'+elements+'.prn'
    #fichero = 'datasets/'+elements+'/'+elements+'.prn'
    
    print(fichero)
    #ficherotxt = 'datasets/Real/'+str(tipeir)+'/'+elements+'/'+elements+'-5050-holdout5-tra.txt'
    ficherotxt = 'datasets/Real/'+str(tipeir)+'/'+elements+'/'+elements+'-8020-holdout5-tra.txt'
    #ficherotxt = 'datasets/'+elements+'-5050-holdout5-tra.txt'
    if os.path.exists(ficherotxt):
        os.remove(ficherotxt)

    textfile = open(ficherotxt, "a")

    #ficherotxt2 = 'datasets/Real/'+str(tipeir)+'/'+elements+'/'+elements+'-5050-holdout5-tst.txt'
    ficherotxt2 = 'datasets/Real/'+str(tipeir)+'/'+elements+'/'+elements+'-8020-holdout5-tst.txt'
    #ficherotxt2 = 'datasets/'+elements+'-5050-holdout5-tst.txt'
    if os.path.exists(ficherotxt2):
        os.remove(ficherotxt2)

    textfile2 = open(ficherotxt2, "a")


    X,y = load_dataset(fichero)


    rs = 42

    for folds in range(1,(nfolds+1)):
        
        #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=rs+folds, stratify=y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=rs+folds, stratify=y)
        

        #Procesar el conjunto de entrenamiento
        typeclass0=[]
        typeclass1=[]

        labelsdataset=get_uniquelabels(y_train)

        for i in range(len(y_train)):
            xv = X_train[i,:]
            yv = y_train[i]
            xm =np.delete(X_train,i,0)
            ym = np.delete(y_train,i)
            if (yv == labelsdataset[0]):
                typeclass0.append(kind_sample(xv,yv,xm,ym,5))
            else:
                typeclass1.append(kind_sample(xv,yv,xm,ym,5))

        ksample=[]

        ksample.append((np.array(typeclass0) == 0).sum())
        ksample.append((np.array(typeclass0) == 1).sum())
        ksample.append((np.array(typeclass0) == 2).sum())
        ksample.append((np.array(typeclass0) == 3).sum())
        ksample.append(len(typeclass0))
        #print(ksample)

        ksample.append(ksample[0]/ksample[4])
        ksample.append(ksample[1]/ksample[4])
        ksample.append(ksample[2]/ksample[4])
        ksample.append(ksample[3]/ksample[4])

        ksample.append((np.array(typeclass1) == 0).sum())
        ksample.append((np.array(typeclass1) == 1).sum())
        ksample.append((np.array(typeclass1) == 2).sum())
        ksample.append((np.array(typeclass1) == 3).sum())
        ksample.append(len(typeclass1))

        #print(ksample)

        ksample.append(ksample[9]/ksample[13])
        ksample.append(ksample[10]/ksample[13])
        ksample.append(ksample[11]/ksample[13])
        ksample.append(ksample[12]/ksample[13])
        print(ksample)

        for listelement in ksample:
            textfile.write(str(listelement) + " ")
        textfile.write("\n")

        print('-----------Processing test dataset------------')
    
        typeclass0=[]
        typeclass1=[]

        labelsdataset=get_uniquelabels(y_test)
        for i in range(len(y_test)):
            xv = X_test[i,:]
            yv = y_test[i]
            xm =np.delete(X_test,i,0)
            ym = np.delete(y_test,i)
            if (yv == labelsdataset[0]):
                typeclass0.append(kind_sample(xv,yv,xm,ym,5))
            else:
                typeclass1.append(kind_sample(xv,yv,xm,ym,5))
        
        ksample=[]
        ksample.append((np.array(typeclass0) == 0).sum())
        ksample.append((np.array(typeclass0) == 1).sum())
        ksample.append((np.array(typeclass0) == 2).sum())
        ksample.append((np.array(typeclass0) == 3).sum())
        ksample.append(len(typeclass0))
        #print(ksample)

        ksample.append(ksample[0]/ksample[4])
        ksample.append(ksample[1]/ksample[4])
        ksample.append(ksample[2]/ksample[4])
        ksample.append(ksample[3]/ksample[4])

        ksample.append((np.array(typeclass1) == 0).sum())
        ksample.append((np.array(typeclass1) == 1).sum())
        ksample.append((np.array(typeclass1) == 2).sum())
        ksample.append((np.array(typeclass1) == 3).sum())
        ksample.append(len(typeclass1))

        #print(ksample)

        ksample.append(ksample[9]/ksample[13])
        ksample.append(ksample[10]/ksample[13])
        ksample.append(ksample[11]/ksample[13])
        ksample.append(ksample[12]/ksample[13])
        print(ksample)

        for listelement in ksample:
            textfile2.write(str(listelement) + " ")
        textfile2.write("\n")

    textfile.close()
    textfile2.close()
