from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import pandas as pd

d1 = pd.read_csv('/home/ozzycodes/OzzyCodes_ProgrammingTutorials/Udemy_Python_Data/Iris.csv')
print(d1)


iris = load_iris()

print(iris.feature_names)
print(iris.target_names)
print(iris.target)
print(iris.data)


X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors = 1)
print(knn)

knn.fit(X, y)

my_predict = knn.predict([[2, 4, 3, 1]])
print(my_predict)

my_predict = knn.predict([[2, 4, 3 ,1], [4, 6, 5, 3]])
print(my_predict)

knn5 = KNeighborsClassifier(n_neighbors = 5)
knn5.fit(X, y)
my_predict5 = knn5.predict([[2, 4, 3 ,1], [4, 6, 5, 3]])
print(my_predict5)

for x in range(1, 30):
    knnLoop = KNeighborsClassifier(n_neighbors = x)
    knnLoop.fit(X, y)
    my_predictLoop = knnLoop.predict([[2, 4, 3 ,1], [4, 6, 5, 3]])
    print(my_predictLoop)


## Logistic Regression

from sklearn.linear_model import LogisticRegression as lr
logisticreg = lr()
logisticreg.fit(X, y)

predict_lr = logisticreg.predict([[2, 4, 3 ,1], [4, 6, 5, 3]])
print(predict_lr)


print(iris.target_names)
