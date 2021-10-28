# This script tests the model on the standard RSA scalar implicatures.
# The DWG model successfully makes the same predictions.

from players import *
from helpers import *
from lexica import *
from viz import rsa_ll_viz


# Available messages
messages = ["none", "some", "all"]

meanings = {
    "none": {"worlds": ["w0"], "personae": ["pi"]},
    "some": {"worlds": ["w1", "w2", "w3"], "personae": ["pi"]},
    "all": {"worlds": ["w3"], "personae": ["pi"]},
}

# Setting the priors.
# Define priors over possible worlds here, they have to add up to 1.
world_priors = {
    "w0": 1 / 4,
    "w1": 1 / 4,
    "w2": 1 / 4,
    "w3": 1 / 4,
}

# Define priors over personae here. They have to add up to 1.
pers_priors = {"pi": 1}

delta_soc = {"soc": 1}

pi_lex = {"pi": {"lex": 1}}

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
    m + "\', the probability that a literal listener interprets the persona\
        displayed by the speaker as being \'\pi\' is equal to: " +
        str(lis0.general_social_interpretation("pi", m, socs))
        )

# Predictions for worlds
rsa_ll_viz(lis0, socs, lexs)

# Constructing the speaker
speak = HonestNdivSpeaker(priors)

# Predictions for (worlds, personae) pairs
speak.full_predictions(socs, lexs)

# Constructing the speaker
lis1 = Listener(priors)

# Predictions for (worlds, personae) pairs
lis1.full_predictions(socs, lexs)