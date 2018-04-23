#!/usr/bin/env python

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

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
            ['screens', 'footfall', 'budget', 'first_day', 'first_weekend', 'first_week',
                'actors_movieCount', 'actors_ratingSum', 'actors_normalizedMovieRank',
                'actors_googleHits', 'actors_normalizedGoogleRank', 'actors_normalizedRating',
                'directors_ratingSum', 'directors_normalizedMovieRank', 'directors_googleHits',
                'directors_normalizedGoogleRank', 'directors_normalizedRating', 'india_gross'])

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
    

    def plot_graphs(self):
        self.frame = self.frame.filter(['screens', 'budget', 'footfall', 'first_day',
            'first_weekend', 'first_week', 'worldwide_first_weekend', 'worldwide_first_week',
            'worldwide_gross', 'india_gross'])
        self.optimize_data()
        # screens = self.frame['screens'].tolist()
        # budget = self.frame['budget'].tolist()
        # footfall = self.frame['footfall'].tolist()
        # first_day = self.frame['first_day'].tolist()
        # india_gross = self.frame['india_gross'].tolist()

        # Plot graphs
        self.frame = self.frame.cumsum()
        self.frame.plot(x='budget', y=['first_day',
            'first_weekend', 'first_week', 'worldwide_first_weekend', 'worldwide_first_week',
            'worldwide_gross', 'india_gross'], kind='pie', title='Budgets vs Earnings')
        plt.show()