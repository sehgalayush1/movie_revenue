#!/usr/bin/env python

import numpy as np
import pandas as pd

class getData:
    def __init__(self, file):
        self.frame = pd.read_csv(file)

    def optimize_data(self):
        def remove_comma(val):
            if type(val) is str:
                return val.replace(',', '')
            else:
                return val
        # Remove Commas from amounts
        self.frame = self.frame.applymap(remove_comma)

        # Remove rows with none values and convert to float
        self.frame = self.frame.apply(pd.to_numeric, args=('coerce',))

        # Remove rows with missing data
        self.frame = self.frame.dropna()

    def normalize_data(self):
        # Fetch features
        self.frame = self.frame.filter(
            ['screens', 'footfall', 'budget', 'first_day', 'first_weekend', 'first_week', 'india_gross'])

        # Fetch 8 features
        # self.frame = self.frame.filter(
        #     ['screens', 'footfall', 'budget', 'first_day', 'first_weekend', 'first_week', 'worldwide_first_weekend',
        #         'worldwide_first_week', 'worldwide_gross']
        # )

        # Optimize data
        self.optimize_data()

        # Seprate labels from features
        self.labels = self.frame['india_gross']
        self.frame = self.frame.drop(['india_gross'], axis=1)

        # Normalize frame
        self.frame_norm = (self.frame - self.frame.mean()) / (self.frame.max() - self.frame.min())

        # Assign labes based on values
        def classify_labels(val):
            if val <= 1000000000:
                return 0
            elif val <= 1000000000:
                return 1
            elif val <= 2000000000:
                return 2
            else:
                return 3

        self.labels = self.labels.apply(classify_labels)

        return self.frame_norm, self.labels
