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


#single_point = [3, 4]
#points = np.arange(20).reshape((10,2))


#b = mydist2(single_point,points)
#print(b)

#knnids=b.argsort()[:5]
#print(knnids)

X,y = load_dataset('prueba.prn')

#print(X)
#print(X.shape)
print(X[0,:])
distancia = mydist2(X[0,:],X[1:,:])
#print(distancia)
print(distancia.shape)

print(get_indxknn(distancia,7))
print(y[get_indxknn(distancia,7)])
yetiquetas= get_labels(y,get_indxknn(distancia,7))
print(yetiquetas)
zetiquetas = get_uniquelabels(y)
print(zetiquetas)

count_labels(zetiquetas,yetiquetas)


