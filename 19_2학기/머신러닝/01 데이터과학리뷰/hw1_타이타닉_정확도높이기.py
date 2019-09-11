import pandas as pd
import numpy as np
from scipy.stats import stats

train = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv")
test = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv")

#missing value 평군으로 채우기
train.fillna(train.mean(), inplace=True)
test.fillna(train.mean(), inplace=True)

#필요없는 feature drop
train = train.drop(['Name','Ticket','Cabin','Embarked','PassengerId'], axis=1)
test = test.drop(['Name','Ticket','Cabin','Embarked','PassengerId'], axis=1)


#글자인 성별을 숫자로 변환
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

labelEncoder = LabelEncoder()
labelEncoder.fit(train['Sex'])
labelEncoder.fit(test['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
test['Sex'] = labelEncoder.transform(test['Sex'])


#아웃라이어 제거
train = train[(np.abs(stats.zscore(train)) < float(3)).all(axis=1)]

#타겟 분리 + float형으로 변환
X = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])

#모델 생성
from sklearn.cluster import KMeans
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
#kmeans = KMeans(n_clusters=2, max_iter=1000, algorithm='auto')
kmeans = KMeans(algorithm='auto', copy_x=True, init='k-means++',max_iter=1000,
       n_clusters=2, n_init=10, n_jobs=1, precompute_distances='auto',
       random_state=None,tol=0.0001, verbose=0)
kmeans.fit(X_scaled)


#정답률 확인
correct = 0

for i in range(len(X)):
    predict_me = np.array(X[i].astype(float))
    predict_me = predict_me.reshape(-1,len(predict_me))
    prediction = kmeans.predict(predict_me)
    if prediction[0] == y[i]:
        correct += 1

print(correct/len(X))
#0.7280487804878049