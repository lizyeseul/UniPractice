import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_csv('diabetes.csv')

# target 데이터 나누기
X = df.drop(columns=['Outcome'])
y = df['Outcome'].values

from sklearn.model_selection import GridSearchCV

#모델 만들기
from sklearn.neighbors import KNeighborsClassifier
knn2 = KNeighborsClassifier()

#찾을 k의 범위
param_grid={'n_neighbors': np.arange(1,25)}

#grid search
knn_gscv = GridSearchCV(knn2,param_grid,cv=5)

knn_gscv.fit(X,y)

print(knn_gscv.best_params_)
print(knn_gscv.best_score_)