import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_csv('SURFACE_ASOS_108.csv')
df.fillna(df.mean(),inplace=True)

# target 데이터 나누기
X = df.drop(columns=['quantity'])
y = df['quantity'].values

from sklearn.model_selection import cross_val_score

# knn모델 생성
from sklearn.neighbors import KNeighborsClassifier
knn_cv = KNeighborsClassifier(n_neighbors=3)

# 모델 학습(5분할)
cv_scores = cross_val_score(knn_cv, X, y, cv=5)

print(cv_scores)
print('mean : {}'.format(np.mean(cv_scores)))
