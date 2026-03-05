import numpy as np

def linear(x, a, b):
    return a * x + b

def quadratic(x, a, b, c):
    return a * x ** 2 + b * x + c

def sinus(x):
    return np.sin(x)

def exponential(x):
    return np.exp(x)

def custom(x):
    return np.log(np.abs(x) + 1)
