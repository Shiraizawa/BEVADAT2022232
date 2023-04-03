import pandas as pd
import numpy as np
import seaborn as sns
from typing import Tuple
from scipy.stats import mode
from sklearn.metrics import confusion_matrix


class KNNClassifier:
    def __init__(self, k: int, test_split_ratio: float):
        self.k = k
        self.test_split_ratio = test_split_ratio
        
    @property
    def k_neighbors(self):
        return self.k
        
    @staticmethod
    def load_csv( csv_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        dataset = pd.read_csv(csv_path)
        dataset = dataset.sample(frac=1, random_state=42).reset_index(drop=True)
        x, y = dataset.iloc[:, :-1], dataset.iloc[:, -1]
        return x, y
        
    def train_test_split(self, features: pd.DataFrame, labels: pd.DataFrame):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        self.x_test, self.y_test = features.iloc[train_size:train_size+test_size, :], labels.iloc[train_size:train_size+test_size]
        self.y_train.reset_index(drop=True)
        self.x_train.reset_index(drop=True)
        self.y_test.reset_index(drop=True)
        self.x_test.reset_index(drop=True)
        
    def euclidean(self, element_of_x: pd.DataFrame) -> pd.Series:
        x=self.x_train
        element=element_of_x
        return ((x - element)**2).sum(axis=1).pow(1/2)
    
    def predict(self, x_test: pd.DataFrame) -> pd.DataFrame:
        labels_pred = []
        x_test.reset_index(drop=True)
        self.y_train.reset_index(drop=True)
        self.x_train.reset_index(drop=True)
        for _, x_test_element in x_test.iterrows():
            distances = self.euclidean(x_test_element)
            distances = pd.concat([distances, self.y_train], axis=1)
            distances = distances.sort_values(by=[0])
            label_pred = mode(distances.iloc[:self.k, 1], keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = pd.Series(labels_pred)
        
    def accuracy(self) -> float:
        yPredSeries=self.y_preds[0]
        ytest=pd.Series(self.y_test)
        true_positive = (ytest.reset_index(drop=True) == yPredSeries.reset_index(drop=True)).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self)  -> np.ndarray:
        yPredSeries=self.y_preds[0]
        yPredSeries=yPredSeries.astype(int)
        ytest=pd.Series(self.y_test)
        ytest=ytest.astype(int)
        conf_matrix = confusion_matrix(ytest.reset_index(drop=True),yPredSeries.reset_index(drop=True))
        return conf_matrix
    
    def best_k(self):
        old_k=self.k
        best_accuracy=0
        best_k_value=0
        for i in range(21):
          self.k=i
          self.predict(self.x_test)
          predicted_value=self.accuracy()
          if(best_accuracy<predicted_value):
              best_accuracy=predicted_value
              best_k_value=i
        self.k=old_k
        return (best_k_value,best_accuracy.round(2))