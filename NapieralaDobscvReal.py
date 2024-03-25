import numpy as np
import os

def mydist2(vctr, mtrx):
    return np.linalg.norm(mtrx-vctr,axis=1)


def load_dataset(nfile):
    df = np.loadtxt(nfile,dtype='str')
    return np.asarray(df[:,0:-1],dtype=float), np.asarray(df[:,-1],dtype=int)

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
#       'winequality-red-8_vs_6', 'winequality-red-8_vs_6-7','winequality-white-3-9_vs_5','winequality-white-9_vs_4', 'yeast-1-2-8-9_vs_7',
 #       'yeast4','yeast6']

fname=['ecoli-0_vs_1']

nfolds=10
#tipeir=30
tipeir=3


for element in fname:
    print(element)
    #Para usar el test se debe de cambiar "tra" por "tst"
    #para procesar cv se debe de quitar dobscv. Revisar el archivo original

    #ficherotxt = 'datasets/Real/'+str(tipeir)+'/'+element+'/'+element+'-'+str(nfolds)+'-dobscv-tra.txt'
    ficherotxt = 'datasets/Real/'+str(tipeir)+'/'+element+'/'+element+'-'+str(nfolds)+'-dobscv-tst.txt'
    
    #ficherotxt = 'datasets/'+element+'-'+str(nfolds)+'dobscv-tra.txt'
    if os.path.exists(ficherotxt):
        os.remove(ficherotxt)

    textfile = open(ficherotxt, "a")

    for folds in range(1,(nfolds+1)):
        #Para usar el test se debe de cambiar "tra" por "tst"
        #fichero = 'datasets/Real/'+str(tipeir)+'/'+element+'/'+element+'-'+str(nfolds)+'dobscv-'+str(folds)+'tra.prn'
        fichero = 'datasets/Real/'+str(tipeir)+'/'+element+'/'+element+'-'+str(nfolds)+'dobscv-'+str(folds)+'tst.prn'
        #fichero = 'datasets/'+element+'/'+element+'-'+str(nfolds)+'dobscv-'+str(folds)+'tra.prn'
        print(fichero)
        
        X,y = load_dataset(fichero)
        
        typeclass0=[]
        typeclass1=[]

        labelsdataset=get_uniquelabels(y)

        for i in range(len(y)):
            xv = X[i,:]
            yv = y[i]
            xm =np.delete(X,i,0)
            ym = np.delete(y,i)
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
    
    textfile.close()





#textfile = open("items.txt", "a")
#for element in ksample:
#    textfile.write(str(element) + " ")
#textfile.write("\n")    
#textfile.close()