from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#read dataset
df = pd.read_csv('heart.csv')

#drop target column
x=df.drop(columns=['target'])

#separate target values
y = df['target'].values

cri = ['gini','entropy']
pArray=[]
for c in cri:
    tree1_cv = DecisionTreeClassifier(criterion=c)
    predict = cross_val_predict(tree1_cv, x, y, cv=10)
    pArray.append(predict)

import seaborn as sn
for p in pArray:
    data = {'y_Predicted':p,'y_Actual':y}
    dframe = pd.DataFrame(data,columns=['y_Predicted','y_Actual'])
    confusion = pd.crosstab(dframe['y_Actual'],dframe['y_Predicted'],rownames=['actual'],colnames=['predicted'])

    sn.heatmap(confusion,annot=True)
    plt.show()