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
}

# Define priors over personae here. They have to add up to 1.
pers_priors_i = {
}

# Build priors as an instance of the Priors class.
priors_i = Priors(world_priors_i, pers_priors_i)

# For listener j
# Define priors over possible worlds here, they have to add up to 1.
world_priors_j = {
}

# Define priors over personae here. They have to add up to 1.
pers_priors_j = {
}

# Build priors as an instance of the Priors class.
priors_j = Priors(world_priors_j, pers_priors_j)

# We then need a set of messages along with their interpretation from a
# lexical standpoint (Lex object) and the social meaning standpoint
# (Soc object).

# We construct our Speaker and Listener objects using our priors.
