#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

from normalize import getData

class SVMTrainer():
    def __init__(self, file_path):
        self.file_path = file_path
        self.obj = getData(self.file_path)
    
    def train(self):
        self.features, self.labels = self.obj.normalize_data()
        self.features = self.features.as_matrix()
        self.labels = self.labels.as_matrix()

        # self.features_train, self.features_test, self.labels_train, self.labels_test = train_test_split(self.features, self.labels)

        self.clf_svc = svm.SVC()
        self.clf_linear_svc =  svm.LinearSVC()
        self.clf_svc.fit(self.features, self.labels)
        self.clf_linear_svc.fit(self.features, self.labels)

        joblib.dump(self.clf_svc, 'models/svm_svc.pkl')
        joblib.dump(self.clf_linear_svc, 'models/svm_linear_svc.pkl')



class SVMPredictor():
    def __init__(self, file_path):
        self.file_path = file_path
        self.obj = getData(self.file_path)
    
    def predict(self):
        self.features, self.labels = self.obj.normalize_data()
        self.features = self.features.as_matrix()
        self.labels = self.labels.as_matrix()

        self.clf_svc = joblib.load('models/svm_svc.pkl')
        self.clf_linear_svc = joblib.load('models/svm_linear_svc.pkl')
        prediction_svc = self.clf_svc.predict(self.features)
        prediction_linear_svc = self.clf_linear_svc.predict(self.features)

        return prediction_svc, prediction_linear_svc, self.labels




def run(file_path):
    obj = getData(file_path)

    features, labels = obj.normalize_data()

    # Convert DataFrames or Series into Numpy arrays
    features = features.as_matrix()
    labels = labels.as_matrix()

    # Seperate train and test sets
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels)

    # Train and predict
    # clf = svm.SVC()
    clf = svm.LinearSVC()
    clf.fit(features_train, labels_train)

    prediction = clf.predict(features_test)

    accuracy = accuracy_score(labels_test, prediction)

    print(accuracy)


if __name__ == '__main__':
    file_path = 'data/main_data.csv'
    run(file_path)