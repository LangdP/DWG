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
    "wR" : 0.5,
    "wNR" : 0.5
}

# Define priors over personae here. They have to add up to 1.
pers_priors_i = {
    "piRC" : 0.5,
    "piNRC" : 0.5
}

delta_soc_i = {
    "soc_RC": 1,
    "soc_NRC": 0
}

pi_lex_i = {
    "piRC": {
        "lex_RC": 1,
        "lex_NRC": 0
    },
    "piNRC": {
        "lex_RC": 0,
        "lex_NRC": 1
    }
}

# Build priors as an instance of the Priors class.
priors_i = Priors(world_priors_i, pers_priors_i, delta_soc_i, pi_lex_i)

# For listener j
# Define priors over possible worlds here, they have to add up to 1.
world_priors_j = {
    "wR" : 0.5,
    "wNR" : 0.5
}

# Define priors over personae here. They have to add up to 1.
pers_priors_j = {
    "piRC" : 0.5,
    "piNRC" : 0.5
}

delta_soc_j = {
    "soc_RC": 0,
    "soc_NRC": 1
}

pi_lex_j = {
    "piRC": {
        "lex_RC": 0,
        "lex_NRC": 1 
    },
    "piNRC": {
        "lex_RC": 0,
        "lex_NRC": 1
    }
}
# Build priors as an instance of the Priors class.
priors_j = Priors(world_priors_j, pers_priors_j, delta_soc_j, pi_lex_j)

# We then need a set of messages along with their interpretation from a
# lexical standpoint (Lex object) and the social meaning standpoint
# (Soc object).

utterances_nrc = {
    "mR" : {
        "worlds" : ["wR"],
        "personae" : ["piRC"]
    }, 
    "mNR" : {
        "worlds" : ["wNR"],
        "personae" : ["piNRC", "piRC"]
    }, 
    "mDW" : {
        "worlds" : ["wNR"],
        "personae" : ["piNRC", "piRC"]
    } 
    }

utterances_rc = {
    "mR" : {
        "worlds" : ["wR"],
        "personae" : ["piRC"]
    }, 
    "mNR" : {
        "worlds" : ["wNR"],
        "personae" : ["piNRC", "piRC"]
    }, 
    "mDW" : {
        "worlds" : ["wR", "wNR"],
        "personae" : ["piRC"]
    } 
    }

# Constructing lexica and storing in lists

socs = [Pers(utterances_rc, "soc_RC"), Pers(utterances_nrc, "soc_NRC")]
lexs = [Lex(utterances_rc, "lex_RC"), Lex(utterances_nrc, "lex_NRC")]

# Constructing speaker preferences
world_preferences = preferences_generation(list(world_priors_i.keys()),
                                            preferred_states=[["wR", "wNR"]],
                                            dispreferred_states=[["wNR", "wR"],
                                                                 ["wR", "wR"]]
                                             )
personae_preferences = preferences_generation(list(pers_priors_i.keys()),
                                            preferred_states=[["piRC", "piNRC"]],
                                            dispreferred_states=[["piNRC", "piRC"],
                                                                 ["piRC", "piRC"]]
                                                                 )