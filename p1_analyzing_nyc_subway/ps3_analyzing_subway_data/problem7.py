import numpy as np
import scipy
import matplotlib.pyplot as plt
import sys

def compute_r_squared(data, predictions):
    r_squared = 1 - (np.square(data - predictions).sum()/(np.square(data - np.average(data)).sum()))
    
    return r_squared