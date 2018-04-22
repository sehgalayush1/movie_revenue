#!/usr/bin/env python

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

from normalize import getData

class RandomForestTrainer():
    def __init__(self, file_path):
        self.file_path = file_path
        self.obj = getData(self.file_path)
    
    def train(self):
        self.features, self.labels = self.obj.normalize_data()
        self.features = self.features.as_matrix()
        self.labels = self.labels.as_matrix()

        # self.features_train, self.features_test, self.labels_train, self.labels_test = train_test_split(self.features, self.labels)

        self.clf = RandomForestClassifier()
        self.clf.fit(self.features, self.labels)

        joblib.dump(self.clf, 'models/random_forest.pkl')



class RandomForestPredictor():
    def __init__(self, file_path):
        self.file_path = file_path
        self.obj = getData(self.file_path)
    
    def predict(self):
        self.features, self.labels = self.obj.normalize_data()
        self.features = self.features.as_matrix()
        self.labels = self.labels.as_matrix()

        self.clf = joblib.load('models/random_forest.pkl')
        prediction = self.clf.predict(self.features)

        return prediction, self.labels






def run(file_path):
    obj = getData(file_path)

    features, labels = obj.normalize_data()

    features = features.as_matrix()
    labels = labels.as_matrix()

    features_train, features_test, labels_train, labels_test = train_test_split(features, labels)

    clf = RandomForestClassifier()
    clf.fit(features_train, labels_train)

    predection = clf.predict(features_test)

    accuracy = accuracy_score(labels_test, predection)

    print(accuracy)


if __name__ == '__main__':
    file_path = 'data/main_data.csv'
    run(file_path)