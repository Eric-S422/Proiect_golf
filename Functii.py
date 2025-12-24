# utils.py
import numpy as np

def mean_distance(values):
    return np.mean(values)

def normalize_data(x):
    return (x - np.mean(x)) / np.std(x)
