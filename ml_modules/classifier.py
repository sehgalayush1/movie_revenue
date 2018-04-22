#!/usr/bin/env python

import numpy as np
import pandas as pd

from decison_tree import DecisionTreeTrainer, DecisionTreePredictor
from random_forest import RandomForestTrainer, RandomForestPredictor
from svm import SVMTrainer, SVMPredictor
from naive_bayes import NaiveBayesTrainer, NaiveBayesPredictor

training_file = 'data/main_data.csv'
testing_file = 'data/test_data.csv'

# Decision Tree
DecisionTreeTrainer(training_file).train()
decision_tree_output, decision_tree_labels = DecisionTreePredictor(testing_file).predict()

# Random Forest
RandomForestTrainer(training_file).train()
random_forest_output, random_forest_labels = RandomForestPredictor(testing_file).predict()

# SVM
SVMTrainer(training_file).train()
svm_svc_output, svm_linear_svc_output, svm_labels = SVMPredictor(testing_file).predict()

# Naive Bayes
NaiveBayesTrainer(training_file).train()
naive_bayes_output, naive_bayes_labels = NaiveBayesPredictor(testing_file).predict()

# Print Score
decision_tree_score = len([i for i, j in zip(decision_tree_output, decision_tree_labels) if i == j])
print("Decision Tree => ", decision_tree_score, "/", len(decision_tree_labels))

random_forest_score = len([i for i, j in zip(random_forest_output, random_forest_labels) if i == j])
print("Random Forest => ", random_forest_score, "/", len(decision_tree_labels))

svm_svc_score = len([i for i, j in zip(svm_svc_output, svm_labels) if i == j])
svm_linear_svc_score = len([i for i, j in zip(svm_linear_svc_output, svm_labels) if i == j])
print("SVM SVC => ", svm_svc_score, "/", len(decision_tree_labels))
print("SVM Linear SVC => ", svm_linear_svc_score, "/", len(decision_tree_labels))

naive_bayes_score = len([i for i, j in zip(naive_bayes_output, naive_bayes_labels) if i == j])
print("Naive Bayes => ", naive_bayes_score, "/", len(naive_bayes_labels))