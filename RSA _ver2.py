# This script tests the model on the standard RSA scalar implicatures.
# The DWG model successfully makes the same predictions.

from players import *
from helpers import *
from lexica import *
from viz import *

# Available messages
messages = ["some", "all"]

meanings = {
    "some": {"worlds": ["w1", "w2", "w3"], "personae": ["pi"]},
    "all": {"worlds": ["w3"], "personae": ["pi"]},
}

# Setting the priors.
# Define priors over possible worlds here, they have to add up to 1.
world_priors = {
    "w1": 1 / 3,
    "w2": 1 / 3,
    "w3": 1 / 3,
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
        "When hearing message '"
        + m
        + "', the probability that a literal listener interprets the persona\
        displayed by the speaker as being '\pi' is equal to: "
        + str(lis0.general_social_interpretation("pi", m, socs))
    )

# Predictions for worlds + fails
lis_viz(lis0, socs, lexs)

speak_fail = HonestNdivSpeaker(priors)
speak_viz(speak_fail, socs, lexs)

lis_fail = Listener(priors)
lis_viz(lis_fail, socs, lexs)

speak_fail_plus = HonestNdivSpeakerPlus(priors)
speak_viz(speak_fail_plus, socs, lexs)

lis_fail_plus = ListenerPlus(priors)
lis_viz(lis_fail_plus, socs, lexs)

# Constructing the speaker
speak = HonestNdivSpeaker(priors, pers_sensitivity=0)

# Predictions for (worlds, personae) pairs
speak.full_predictions(socs, lexs)
speak_viz(speak, socs, lexs)
speak_viz_save(speak, socs, lexs, "rsa-solved-speak.tex")

# Constructing the speaker
lis1 = Listener(priors, pers_sensitivity=0)

# Predictions for (worlds, personae) pairs
lis1.full_predictions(socs, lexs)
lis_viz(lis1, socs, lexs)
lis_viz_save(lis1, socs, lexs, "rsa-solved-lis.tex")

speak_plus = HonestNdivSpeakerPlus(priors, pers_sensitivity=0)
speak_viz(speak_plus, socs, lexs)
speak_viz_save(speak_plus, socs, lexs, "rsa-solved-speak2.tex")

lis_plus = ListenerPlus(priors, pers_sensitivity=0)
lis_viz(lis_plus, socs, lexs)
lis_viz_save(lis_plus, socs, lexs, "rsa-solved-lis2.tex")
