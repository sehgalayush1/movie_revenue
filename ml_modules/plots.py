#!/usr/bin/env python

from normalize import getData

training_file = 'data/main_data.csv'

obj = getData(training_file)
obj.plot_graphs()