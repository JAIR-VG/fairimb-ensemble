import numpy as np

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
        print('Safe')
    else:
        if (numknn/kvalue) >= 0.4:
            print('Borderline')
        else:
            if (numknn/kvalue) >= 0.2:
                print('Rare')
            else:
                print('Outlier')


X,y = load_dataset('prueba.prn')



for i in range(len(y)):
    xv = X[i,:]
    yv = y[i]
    xm =np.delete(X,i,0)
    ym = np.delete(y,i)
    kind_sample(xv,yv,xm,ym,5)
