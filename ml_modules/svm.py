#!/usr/bin/env python

import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from normalize import getData

file_path = 'data/final_data.csv'
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
# print(labels.to_string())