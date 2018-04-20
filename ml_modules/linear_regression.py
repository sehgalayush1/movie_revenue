#!/usr/bin/env python

import numpy as np
import pandas as pd
from normalize import getData

class Trainer:
    def __init__(self):
        file_path = 'data/final_data.csv'
        obj = getData(file_path)
        frame_norm, labels = obj.normalize_data()

        class1 = labels[labels < 10000000]
        class2 = labels[(labels > 10000000) & (labels < 1000000000)]

        print("Class1 - ", class1.size)
        print("Class2 - ", class2.size)
        print("Total - ", labels.size)

if __name__ == '__main__':
    train = Trainer()
    print('tested!')
