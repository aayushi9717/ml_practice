

import pandas as pd 
from sklearn.cross_validation  import train_test_split
mydataset=pd.read_csv('data.csv')
print("shape:",mydataset.lost_time)
x=mydataset[mydataset.columns[:-1]]
y=mydataset[mydataset.columns[-1]]
from sklearn.model_selection import  train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=1)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)

from sklearn import metrics
print("knn model accuracy:",metrics.accuracy_score(y_test,y_pred))

