from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import balanced_accuracy_score
from sklearn.tree import DecisionTreeClassifier

from imblearn.ensemble import BalancedBaggingClassifier

X, y = make_classification(n_samples=10000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=3,
                           n_clusters_per_class=1,
                           weights=[0.01, 0.05, 0.94], class_sep=0.8,
                           random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

bbc = BalancedBaggingClassifier(random_state=42)

bbc.fit(X_train, y_train)
y_pred = bbc.predict(X_test)
print(balanced_accuracy_score(y_test, y_pred))