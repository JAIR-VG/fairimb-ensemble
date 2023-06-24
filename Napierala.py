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
       return 0
    else:
        if (numknn/kvalue) >= 0.4:
            return 1
        else:
            if (numknn/kvalue) >= 0.2:
                return 2
            else:
                return 3


X,y = load_dataset('prueba.prn')


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

print(typeclass0)
print(len(typeclass0))
print(typeclass1)
print(len(typeclass1))

print((np.array(typeclass1) == 3).sum())
