import pandas as pd

# 데이터 불러오기
df = pd.read_csv('SURFACE_ASOS_108.csv')
df.fillna(df.mean(),inplace=True)

# target 데이터 나누기
X = df.drop(columns=['quantity'])
y = df['quantity'].values

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
print(knn.score(X_test, y_test))
