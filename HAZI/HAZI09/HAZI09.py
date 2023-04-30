# imports
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits

class KMeansOnDigits():

    def __init__(self, n_clusters, random_state) -> None:
        self.n_clusters=n_clusters
        self.random_state=random_state

    def load_dataset(self):
        self.digits= load_digits()
        
    def predict(self):
        model=KMeans(n_clusters=self.n_clusters,random_state=self.random_state)
        clusters=model.fit_predict(self.digits.data)
        self.clusters=clusters
        
    def get_labels(self):
        labels = np.full_like(self.clusters,-1)
        for label in np.unique(self.clusters):
            mask=(self.clusters==label)
            target_values = self.digits.target[mask]
            mode = np.bincount(target_values).argmax()
            labels[mask] = mode
        self.labels=labels
        
    def calc_accuracy(self):
        self.acc=accuracy_score(self.digits.target,self.labels).round(2)
        
    def confusion_matrix(self):
        self.mat=confusion_matrix(self.digits.target,self.labels)