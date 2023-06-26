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



fname=['03subcl5-600-5-0-bi','03subcl5-600-5-30-bi', '03subcl5-600-5-50-bi', '03subcl5-600-5-60-bi',
        '03subcl5-600-5-70-bi', '04clover5z-600-5-0-bi', '04clover5z-600-5-30-bi', '04clover5z-600-5-50-bi', 
        '04clover5z-600-5-60-bi', '04clover5z-600-5-70-bi', 'paw02a-600-5-0-bi', 'paw02a-600-5-30-bi',
        'paw02a-600-5-50-bi', 'paw02a-600-5-60-bi', 'paw02a-600-5-70-bi', '03subcl5-800-7-0-bi', 
        '03subcl5-800-7-30-bi', '03subcl5-800-7-50-bi', '03subcl5-800-7-60-bi', '03subcl5-800-7-70-bi', 
        '04clover5z-800-7-0-bi', '04clover5z-800-7-30-bi', '04clover5z-800-7-50-bi', '04clover5z-800-7-60-bi', 
        '04clover5z-800-7-70-bi', 'paw02a-800-7-0-bi', 'paw02a-800-7-30-bi', 'paw02a-800-7-50-bi', 
        'paw02a-800-7-60-bi', 'paw02a-800-7-70-bi']

nfolds=5

for element in fname:
    print(element)

    ficherotxt = 'datasets/'+element+'.txt'
    if os.path.exists(ficherotxt):
        os.remove(ficherotxt)

    textfile = open(ficherotxt, "a")

    
    fichero = 'datasets/'+element+'/'+element+'.prn'
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