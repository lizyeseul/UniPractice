import pandas as pd
import numpy as np


# 데이터 불러오기
df = pd.read_csv('SURFACE_ASOS_108.csv')
df.fillna(df.mean(),inplace=True)

# target 데이터 나누기
X = df.drop(columns=['quantity'])
y = df['quantity'].values

#holdout
# train이랑 test로 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

# 모델 생성
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# 예측
knn.predict(X_test)

# 정답률 출력
print('holdout')
print(knn.score(X_test, y_test))

#kfold
from sklearn.model_selection import cross_val_score

# knn모델 생성
from sklearn.neighbors import KNeighborsClassifier
knn_cv = KNeighborsClassifier(n_neighbors=3)

# 모델 학습(5분할)
cv_scores = cross_val_score(knn_cv, X, y, cv=5)

print('\nkfold')
print(cv_scores)
print('mean : {}'.format(np.mean(cv_scores)))
