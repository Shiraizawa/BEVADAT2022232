from LinearRegressionSkeleton import LinearRegression
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
X = df['petal width (cm)'].values
y = df['sepal length (cm)'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   
model=LinearRegression(epochs=5000)
model.fit(X_train,y_train)

model.predict(X_test,y_test)