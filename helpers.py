# Here are a few small functions that are used in the model

from math import log

# This is to avoid value errors when computing utilities
def my_log(n):
    if n == 0:
        return -9999999
    else:
        return log(n)