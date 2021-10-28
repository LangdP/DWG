# This script tests the model on the standard SMG (no persona selection).
# The DWG model successfully makes the same predictions.

from players import *
from helpers import *
from lexica import *
from viz import *


# Available messages
messages = ["in", "ing"]

meanings = {
    "in": {"worlds": ["w"], "personae": ["doofus", "cool guy", "asshole"]},
    "ing": {"worlds": ["w"], "personae": ["stern leader", "cool guy", "asshole"]},
}

# Setting the priors.
# Define priors over possible worlds here, worlds don't count in SMG so we have 
# only one, necessary world.
world_priors = {"w": 1}

# Define priors over personae here. They have to add up to 1.
pers_priors = {
    "stern leader": 0.3,
    "doofus": 0.2,
    "cool guy": 0.2,
    "asshole": 0.3,
    }

delta_soc = {"soc": 1}

pi_lex = {
    "stern leader": {"lex": 1},
    "doofus": {"lex": 1},
    "cool guy":{"lex": 1},
    "asshole":{"lex": 1},
    }

# Build priors as an instance of the Priors class.
priors = Priors(world_priors, pers_priors, delta_soc, pi_lex)

# Constructing lexica and storing in lists
socs = [Pers(meanings, "soc")]
lexs = [Lex(meanings, "lex")]

# Literal listener
lis0 = Player(priors)

# Predictions for pers
for m in messages:
    print(
        "When hearing message \'" +
    m + "\', the probability that a literal listener interprets the world\
        described by the speaker as being \'w\' is equal to: " +
        str(lis0.l0_interpretation("w", m, socs, lexs))
        )

# Predictions for worlds
lis0.full_predictions(socs, lexs)

# Constructing the speaker
speak = HonestNdivSpeaker(priors, world_sensitivity = 0)

# Predictions for (worlds, personae) pairs
speak.full_predictions(socs, lexs)

# Constructing the speaker
lis1 = Listener(priors, world_sensitivity = 0)

# Predictions for (worlds, personae) pairs
lis1.full_predictions(socs, lexs)