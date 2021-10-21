# Here are a few small functions that are used in the model
from itertools import product
from math import log

from lexica import Pers

# This is to avoid value errors when computing utilities
def my_log(n):
    if n == 0:
        return -9999999
    else:
        return log(n)


# This function takes two dicts and outputs all the possible pairs of values
# of the form (dict1[k], dict2[k'])
def list_paired_vals(dic1, dic2):
    lis = []
    for key in dic1.keys():
        for k in dic2.keys():
            lis.append((dic1[key], dic2[k]))
    return lis

def list_paired_keys(dic1, dic2):
    lis = []
    for key in dic1.keys():
        for k in dic2.keys():
            lis.append((key, k))
    return lis 

# This function generates the states of  a truth table given a number of 
# arguments and a number of states (as a list).
def truthtable(n, vals = [0, 1]):
  if n < 1:
    return [[]]
  subtable = truthtable(n-1, vals)
  return [row + [v] for row in subtable for v in vals]

# This generates the state preferences for a speaker after first generating all
# state combinations using the previous function.
def preferences_generation(states : list,
                        preferred_states = [], 
                        dispreferred_states = [], 
                        players = 2):
    sstates = truthtable(players, states)

    preferences = {}

    for state in sstates:
        if state in preferred_states:
            preferences[str(state)] = {"state" : state,
                                        "score" : 2}
        elif state in dispreferred_states:
            preferences[str(state)] = {"state" : state,
                                        "score" : 0}
        else:
            preferences[str(state)] = {"state" : state,
                                        "score" : 1}
    return preferences

