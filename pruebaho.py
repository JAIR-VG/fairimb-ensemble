import numpy as np
from sklearn.model_selection import train_test_split

X = np.arange(25)
rs = 42
train, test = train_test_split(X,
                               test_size=0.3,
                               random_state=rs)
for i in range(10):
    new_train, new_test = train_test_split(X,
                                           test_size=0.3,
                                           random_state=rs+i)
    print(np.all(train == new_train), np.all(test == new_test)) 