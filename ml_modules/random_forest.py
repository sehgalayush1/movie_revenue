#!/usr/bin/env python

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from normalize import getData

file_path = 'data/final_data.csv'
obj = getData(file_path)

features, labels = obj.normalize_data()

features = features.as_matrix()
labels = labels.as_matrix()

features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels)

clf = RandomForestClassifier()
clf.fit(features_train, labels_train)

predection = clf.predict(features_test)

accuracy = accuracy_score(labels_test, predection)

print(accuracy)
