# This is the implementation of the DWG model that I describe in my 
# dissertation

# Import packages
from players import *
from lexica import *
from helpers import *
from viz import *

# We first have to define the priors for each listener, in the form of two
# dictionaries. The dictionaries are then merged into a Priors object.

# For listener i
# Define priors over possible worlds here, they have to add up to 1.
world_priors_i = {
    "r" : 0.5,
    "nr" : 0.5
}

# Define priors over personae here. They have to add up to 1.
pers_priors_i = {
    "rc" : 0.5,
    "nrc" : 0.5
}

# Build priors as an instance of the Priors class.
priors_i = Priors(world_priors_i, pers_priors_i)

# For listener j
# Define priors over possible worlds here, they have to add up to 1.
world_priors_j = {
    "r" : 0.5,
    "nr" : 0.5
}

# Define priors over personae here. They have to add up to 1.
pers_priors_j = {
    "rc" : 0.5,
    "nrc" : 0.5
}

# Build priors as an instance of the Priors class.
priors_j = Priors(world_priors_j, pers_priors_j)

# We then need a set of messages along with their interpretation from a
# lexical standpoint (Lex object) and the social meaning standpoint
# (Soc object).

utterances_nrc = {
    "mR" : {
        "worlds" : ["r"],
        "personae" : ["rc"]
    }, 
    "mNR" : {
        "worlds" : ["nr"],
        "personae" : ["nrc", "rc"]
    }, 
    "mDW" : {
        "worlds" : ["nr"],
        "personae" : ["nrc", "rc"]
    } 
    }

utterances_rc = {
    "mR" : {
        "worlds" : ["r"],
        "personae" : ["rc"]
    }, 
    "mNR" : {
        "worlds" : ["nr"],
        "personae" : ["nrc", "rc"]
    }, 
    "mDW" : {
        "worlds" : ["r", "nr"],
        "personae" : ["rc"]
    } 
    }
# We construct our Speaker and Listener objects using our priors.
