import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np

#read dataset
df = pd.read_csv('heart.csv')

#drop target column
x=df.drop(columns=['target'])

#separate target values
y = df['target'].values

import matplotlib.pyplot as plt
import seaborn as sn
from mpl_toolkits.mplot3d import axes3d

#decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict

cri = ['gini','entropy']
bar = []
for c in cri:
    tree1_cv = DecisionTreeClassifier(criterion=c)
    score = cross_val_score(tree1_cv, x, y, cv=10)
    print(np.mean(score))
    #score

    bar.append(np.mean(score))
    data = {'y_Predicted':cross_val_predict(tree1_cv, x, y, cv=10),'y_Actual':y}
    dframe = pd.DataFrame(data,columns=['y_Predicted','y_Actual'])
    confusion = pd.crosstab(dframe['y_Actual'],dframe['y_Predicted'],rownames=['actual'],colnames=['predicted'], margins=True)
    print(confusion)
    #confusion matrix

    # sn.heatmap(confusion,annot=True)
    # plt.xlabel(c)
    # plt.show()
    # print()
    #heatmap

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar3d([0,2], [0,0], [0,0], [1,1], [1,1], bar)
#chart = plt.bar(cri, bar)
# for rect in chart:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, '%f' % height, ha='center', va='bottom')
plt.show()

#logistic regression
print('logistic')
from sklearn.linear_model import LogisticRegression
bar = []
index = []
SOLVER=['liblinear','lbfgs','sag']
ITER=[50,100,200]

for s in SOLVER:
    for i in ITER:
        index.append(s+str(i))
        logistic =LogisticRegression(solver= s,max_iter = i)
        score = cross_val_score(logistic, x, y, cv=10)
        print(np.mean(score))
        # score

        bar.append(np.mean(score))
        data = {'y_Predicted': cross_val_predict(logistic, x, y, cv=10), 'y_Actual': y}
        dframe = pd.DataFrame(data, columns=['y_Predicted', 'y_Actual'])
        confusion = pd.crosstab(dframe['y_Actual'], dframe['y_Predicted'], rownames=['actual'], colnames=['predicted'], margins=True)
        print(confusion)
        # confusion matrix

        # sn.heatmap(confusion, annot=True)
        # plt.xlabel(s+' '+str(i))
        # plt.show()
        # print()
        # # heatmap

# chart = plt.bar(index, bar)
# for rect in chart:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width()/2.0, height, height, ha='center', va='bottom')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar3d([0,0,0,2,2,2,4,4,4], [0,2,4,0,2,4,0,2,4], np.zeros(9), np.ones(9), np.ones(9), bar)
plt.show()

#svm
bar = []
index = []
from sklearn.svm import SVC
c=[0.1,1.0,10.0]
KERNEL=['linear','rbf','sigmoid']
GAMMA = [10,100]

from sklearn.model_selection import cross_val_predict

for i in c:
    for k in KERNEL:
        for g in GAMMA:
            index.append(str(i)+k+str(g))
            clf = SVC(kernel = k,C=i, gamma=g)
            predict = cross_val_predict(clf, x, y, cv=10)
            score = cross_val_score(clf, x, y, cv=10)
            print(np.mean(score)),
            # score

            bar.append(np.mean(score))
            data = {'y_Predicted': cross_val_predict(clf, x, y, cv=10), 'y_Actual': y}
            dframe = pd.DataFrame(data, columns=['y_Predicted', 'y_Actual'])
            confusion = pd.crosstab(dframe['y_Actual'], dframe['y_Predicted'], rownames=['actual'],  colnames=['predicted'],margins=True)
            print(confusion)
            # confusion matrix

            sn.heatmap(confusion, annot=True)
            plt.xlabel(str(i)+' '+k+' '+str(g))
            plt.show()
            print()
            # heatmap

chart = plt.bar(index, bar)
for rect in chart:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%f' % height, ha='center', va='bottom')
plt.show()