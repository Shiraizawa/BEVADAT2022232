import pandas as pd
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
    def load_csv(csv_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        pd.random.seed(42)
        dataset = pd.read_csv(csv_path, header=None)
        dataset = dataset.sample(frac=1, random_state=42)
        x, y = dataset.iloc[:, :-1], dataset.iloc[:, -1]
        return x, y
        
    def train_test_split(self, features: pd.DataFrame, labels: pd.DataFrame):
        test_size = int(len(features) * self.test_split_ratio)
        train_size = len(features) - test_size
        assert len(features) == test_size + train_size, "Size mismatch!"

        self.x_train, self.y_train = features.iloc[:train_size, :], labels.iloc[:train_size]
        self.x_test, self.y_test = features.iloc[train_size:train_size+test_size, :], labels.iloc[train_size:train_size+test_size]
        
    def euclidean(self, element_of_x: pd.DataFrame) -> pd.Series:
        return ((self.points - element_of_x)**2).sum(axis=1).pow(1/2)
    
    def predict(self, x_test: pd.DataFrame) -> pd.DataFrame:
        labels_pred = []
        for _, x_test_element in x_test.iterrows():
            distances = self.euclidean(self.x_train, x_test_element)
            distances = pd.concat([distances, self.y_train], axis=1)
            distances = distances.sort_values(by=[0, 1])
            label_pred = mode(distances.iloc[:self.k, 1], keepdims=False).mode
            labels_pred.append(label_pred)
        self.y_preds = pd.DataFrame(labels_pred, dtype=pd.Int32Dtype)
        
    def accuracy(self) -> float:
        true_positive = (self.y_test == self.y_preds[0]).sum()
        return true_positive / len(self.y_test) * 100
    
    def confusion_matrix(self) -> pd.DataFrame:
        conf_matrix = confusion_matrix(self.y_test, self.y_preds[0])
        return pd.DataFrame(conf_matrix)
