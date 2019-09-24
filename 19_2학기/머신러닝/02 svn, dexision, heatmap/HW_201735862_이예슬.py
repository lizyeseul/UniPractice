import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import matplotlib.pyplot as plt

from scipy.io import loadmat
mnist = loadmat("mnist-original.mat")
mnist_data = mnist["data"].T
mnist_label = mnist["label"][0]

#read dataset
#df = pd.read_csv('heart.csv')

#drop target column
#x=mnist_data.drop(columns=['target'])
x=pd.DataFrame(mnist_data)

#separate target values
#y = mnist_data['target'].values
y=pd.DataFrame(mnist_label)


from sklearn.model_selection import train_test_split
xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.01, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(xte,yte, test_size=0.2, random_state=1)
#d1_train, d2_test = train_test_split(df, test_size=0.1, random_state=1)


from sklearn.linear_model import LogisticRegression
logic = LogisticRegression(solver='lbfgs',random_state=1, max_iter=100)

from sklearn.svm import SVC
svm1 = SVC(kernel = 'linear',C=1.0, gamma=100)
svm2 = SVC(kernel = 'rbf',C=1.0, gamma=100)

#앙상블
from sklearn.ensemble import VotingClassifier
import seaborn as sn
voting = VotingClassifier(estimators=[('lr',logic),('svc1',svm1),('svc2',svm2)], voting='hard')
voting.fit(X_train, y_train)
y_pred = voting.predict(X_test)
dframe = pd.DataFrame({'y_Predicted': y_pred, 'y_Actual': y_test[0]})
confusion = pd.crosstab(dframe['y_Actual'], dframe['y_Predicted'], rownames=['actual'], colnames=['predicted'],margins=True)
sn.heatmap(confusion, annot=True)
plt.show()



from sklearn.metrics import accuracy_score
for clf in (logic, svm1, svm2):
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    dframe = pd.DataFrame({'y_Predicted':y_pred,'y_Actual':y_test[0]})
    confusion = pd.crosstab(dframe['y_Actual'],dframe['y_Predicted'], rownames=['actual'], colnames=['predicted'], margins=True)
    #print(confusion)
    sn.heatmap(confusion, annot=True)
    plt.show()