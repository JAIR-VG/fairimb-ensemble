import numpy as np





def mydist2(vctr, mtrx):
    return np.linalg.norm(mtrx-vctr,axis=1)


def load_dataset(nfile):
    df = np.loadtxt(nfile,dtype='str')
    return np.asarray(df[:,0:-1],dtype=float), np.asarray(df[:,-1],dtype=int)


single_point = [3, 4]
points = np.arange(20).reshape((10,2))


b = mydist2(single_point,points)
print(b)

knnids=b.argsort()[:5]
print(knnids)

X,y = load_dataset('prueba.prn')

print(X)
print(X.shape)

