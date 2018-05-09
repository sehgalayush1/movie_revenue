#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from normalize import getData

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model

file_path = 'data/main_data.csv'

obj = getData(file_path)

features, labels = obj.normalize_data()

features = features.as_matrix()
labels = labels.as_matrix()

features_train, features_test, labels_train, labels_test = train_test_split(features, labels)

# Classifiers
naive_bayes_clf = GaussianNB()
decision_tree_clf = tree.DecisionTreeClassifier(class_weight='balanced')
svm_svc_clf = svm.SVC(class_weight='balanced')
svm_linear_svc_clf = svm.LinearSVC(class_weight='balanced')
random_forest_clf = RandomForestClassifier(class_weight='balanced')
logistic_clf = linear_model.LogisticRegression()

# Fit data in classifier
naive_bayes_clf.fit(features_train, labels_train)
decision_tree_clf.fit(features_train, labels_train)
svm_svc_clf.fit(features_train, labels_train)
svm_linear_svc_clf.fit(features_train, labels_train)
random_forest_clf.fit(features_train, labels_train)
logistic_clf.fit(features_train, labels_train)

# Prediction
naive_bayes_pred = naive_bayes_clf.predict(features_test)
decision_tree_pred = decision_tree_clf.predict(features_test)
svm_svc_pred = svm_svc_clf.predict(features_test)
svm_linear_svc_pred = svm_linear_svc_clf.predict(features_test)
random_forest_pred = random_forest_clf.predict(features_test)
logistic_pred = logistic_clf.predict(features_test)

# Score
naive_bayes_score = len([i for i, j in zip(naive_bayes_pred, labels_test) if i == j])
print("Naive Bayes => ", naive_bayes_score, "/", len(labels_test))

decision_tree_score = len([i for i, j in zip(decision_tree_pred, labels_test) if i == j])
print("Decision Tree => ", decision_tree_score, "/", len(labels_test))

svm_svc_score = len([i for i, j in zip(svm_svc_pred, labels_test) if i == j])
print("Decision Tree => ", svm_svc_score, "/", len(labels_test))

svm_linear_svc_score = len([i for i, j in zip(svm_linear_svc_pred, labels_test) if i == j])
print("Decision Tree => ", svm_linear_svc_score, "/", len(labels_test))

random_forest_score = len([i for i, j in zip(random_forest_pred, labels_test) if i == j])
print("Decision Tree => ", random_forest_score, "/", len(labels_test))

logistic_score = len([i for i, j in zip(logistic_pred, labels_test) if i == j])
print("Decision Tree => ", logistic_score, "/", len(labels_test))


# Plot Graphs
models = ['Decision Tree', 'Random Forest', 'SVM SVC', 'SVM Linear SVC', 'Naive Bayes', 'Logistic Regression']
values = [decision_tree_score, random_forest_score, svm_svc_score, svm_linear_svc_score, naive_bayes_score, logistic_score]

# plt.bar(models, values)
# plt.title('Model Scores')
# plt.ylabel('Testing on 228 movies')
# plt.show()

fig, ax = plt.subplots()
width = 0.75
ind = np.arange(len(values))
ax.bar(ind, values, width)
ax.set_xticks(ind)
ax.set_xticklabels(models, minor=False)
ax.set_ylabel('Test Movies (%d)' % len(labels_test))
ax.set_xlabel('Models')
ax.set_title('Scores of all the models')

for i, v in enumerate(values):
    ax.text(i-0.25, v+3, str(v) + '(' + str(round((v/len(labels_test))*100, 2)) + '%)', color='black', fontweight='bold')

plt.show()