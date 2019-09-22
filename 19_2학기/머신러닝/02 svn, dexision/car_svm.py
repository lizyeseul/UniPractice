#lab1
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np

#read dataset
df = pd.read_csv('heart.csv')

#drop target column
x=df.drop(columns=['target'])

#separate target values
y = df['target'].values

#k-fold cross validation
#SVM 모델 생성
from sklearn.svm import SVC

c=[0.1,1.0,10.0]
KERNEL=['linear','rbf','sigmoid']
GAMMA = [10,100]

from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix

for i in c:
    for k in KERNEL:
        for g in GAMMA:
            clf = SVC(kernel = k,C=i, gamma=g)
            predict = cross_val_predict(clf, x, y, cv=10)
            score = cross_val_score(clf, x, y, cv=10)
            matrix = confusion_matrix(y, predict)
            print(matrix)
            print(score)
            print()
print('end')

