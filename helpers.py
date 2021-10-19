# Here are a few small functions that are used in the model

from math import log

# This is to avoid value errors when computing utilities
def my_log(n):
    if n == 0:
        return -9999999
    else:
        return log(n)


# This function takes two dicts and outputs all the possible pairs of values
# of the form [dict1[k], dict2[k']]
def list_paired_vals(dic1, dic2):
    lis = []
    for key in dic1.keys():
        for k in dic2.keys():
            lis.append((dic1[key], dic2[k]))
    return lis #[item for sublist in lis for item in sublist]

def list_paired_keys(dic1, dic2):
    lis = []
    for key in dic1.keys():
        for k in dic2.keys():
            lis.append((key, k))
    return lis #[item for sublist in lis for item in sublist]