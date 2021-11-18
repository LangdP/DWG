# This is the testing of the model on the Walt Whitman examples that
# are discussed in chapter 6 of my dissertation

# Import packages
from players import *
from lexica import *
from helpers import *
from viz import *

# We first have to define the priors for each listener, in the form of two
# dictionaries. The dictionaries are then merged into a Priors object.

# For gay friendly reader
# Define priors over possible worlds here, they have to add up to 1.
world_priors_gf = {"wM": 0.5, "wF": 0.5}

# Define priors over personae here. They have to add up to 1.
pers_priors_gf = {"piGP": 0.5, "piSP": 0.5}

delta_soc_gf = {"soc_GF": 1, "soc_SD": 0}

pi_lex_gf = {"piGP": {"lex_GP": 1, "lex_SP": 0}, "piSP": {"lex_GP": 0, "lex_SP": 1}}

# Build priors as an instance of the Priors class.
priors_gf = Priors(world_priors_gf, pers_priors_gf, delta_soc_gf, pi_lex_gf)

# For straight default reader
# Define priors over possible worlds here, they have to add up to 1.
world_priors_sd = {"wM": 0.5, "wF": 0.5}

# Define priors over personae here. They have to add up to 1.
pers_priors_sd = {"piGP": 0.5, "piSP": 0.5}

delta_soc_sd = {"soc_GF": 0, "soc_SD": 1}

pi_lex_sd = {"piGP": {"lex_GP": 1, "lex_SP": 0}, "piSP": {"lex_GP": 0, "lex_SP": 1}}

# Build priors as an instance of the Priors class.
priors_sd = Priors(world_priors_sd, pers_priors_sd, delta_soc_sd, pi_lex_sd)

# Build utterances, one per preferred indexation/interpretation function
# for each player

utterances_gf = {
    "lover": {"worlds": ["wM"], "personae": ["piGP", "piSP"]},
    "donna": {"worlds": ["wF"], "personae": ["piSP"]},
    "gallant": {"worlds": ["wM"], "personae": ["piGP"]},
}

utterances_sd = {
    "lover": {"worlds": ["wF"], "personae": ["piSP"]},
    "donna": {"worlds": ["wF"], "personae": ["piSP"]},
    "gallant": {"worlds": ["wM"], "personae": ["piGP"]},
}
# Constructing lexica and storing in lists

socs = [Pers(utterances_sd, "soc_SD"), Pers(utterances_gf, "soc_GF")]
lexs = [Lex(utterances_sd, "lex_SP"), Lex(utterances_gf, "lex_GP")]

## Constructing speaker preferences
# dw_world_preferences = preferences_generation(
#    list(world_priors_gf.keys()),
#    preferred_states=[["wR", "wNR"]],
#    dispreferred_states=[["wNR", "wR"], ["wR", "wR"]],
# )
# dw_personae_preferences = preferences_generation(
#    list(pers_priors_gf.keys()),
#    preferred_states=[["piRC", "piNRC"]],
#    dispreferred_states=[["piNRC", "piRC"], ["piRC", "piRC"]],
# )

no_world_preferences = preferences_generation(list(world_priors_gf.keys()))
no_personae_preferences = preferences_generation(list(pers_priors_gf.keys()))


# Testing

# Literal listeners
L_0_gf = Player(priors_gf)
L_0_sd = Player(priors_sd)

# Vizualize
lis_viz(L_0_gf, socs, lexs)
lis_viz(L_0_gf, socs, lexs, interpretation="personae_interpretation")

lis_viz(L_0_sd, socs, lexs)
lis_viz(L_0_sd, socs, lexs, interpretation="personae_interpretation")

# Reg Speaker
S_Reg_gf = HonestNdivSpeaker(priors_gf)
speak_viz(S_Reg_gf, socs, lexs)

# Reg Speaker
S_Reg_sd = HonestNdivSpeaker(priors_sd)
speak_viz(S_Reg_sd, socs, lexs)

# Div Speaker
S_Div = HonestDivSpeaker([priors_gf, priors_sd])
speak_viz(S_Div, socs, lexs)

# Pragmatic Listeners
Lis_1_gf = Listener(priors_gf)

lis_viz(Lis_1_gf, socs, lexs)
lis_viz(Lis_1_gf, socs, lexs, interpretation="personae_interpretation")


Lis_1_sd = Listener(priors_sd)

lis_viz(Lis_1_sd, socs, lexs)
lis_viz(Lis_1_sd, socs, lexs, interpretation="personae_interpretation")

# L_2
Lis_2_gf = ListenerPlus(priors_gf)

lis_viz(Lis_2_gf, socs, lexs)
lis_viz(Lis_2_gf, socs, lexs, interpretation="personae_interpretation")


Lis_2_sd = ListenerPlus(priors_sd)

lis_viz(Lis_2_sd, socs, lexs)
lis_viz(Lis_2_sd, socs, lexs, interpretation="personae_interpretation")

# For super gay friendly reader
# Define priors over possible worlds here, they have to add up to 1.
world_priors_sgf = {"wM": 0.5, "wF": 0.5}

# Define priors over personae here. They have to add up to 1.
pers_priors_sgf = {"piGP": 0.8, "piSP": 0.2}

delta_soc_sgf = {"soc_GF": 1, "soc_SD": 0}

pi_lex_sgf = {"piGP": {"lex_GP": 1, "lex_SP": 0}, "piSP": {"lex_GP": 0, "lex_SP": 1}}

# Build priors as an instance of the Priors class.
priors_sgf = Priors(world_priors_sgf, pers_priors_sgf, delta_soc_sgf, pi_lex_sgf)

# Literal listeners
L_0_sgf = Player(priors_sgf)
lis_viz(L_0_sgf, socs, lexs)
lis_viz(L_0_sgf, socs, lexs, interpretation="personae_interpretation")

S_Reg_sgf = HonestNdivSpeaker(priors_sgf)
speak_viz(S_Reg_sgf, socs, lexs)

Lis_1_sgf = Listener(priors_sgf)
lis_viz(Lis_1_sgf, socs, lexs)
lis_viz(Lis_1_sgf, socs, lexs, interpretation="personae_interpretation")


# Scholarly reader
# Constructing the probabilty distribution on priors for the uncovering cagey
# listener

# worlds_prefs_priors = {
#    "dw_prefs": {"prefs": dw_world_preferences, "prior": 0.5},
#    "npref": {"prefs": no_world_preferences, "prior": 0.5},
# }
#
# pers_prefs_priors = {
#    "dw_prefs": {"prefs": dw_personae_preferences, "prior": 0.5},
#    "npref": {"prefs": no_personae_preferences, "prior": 0.5},
# }
#
L_Cag = CageyListener(
    [priors_gf, priors_sd], no_world_preferences, no_personae_preferences
)

# L_Cag_u = UncovCageyListener([priors_gf, priors_sd],
#                            worlds_prefs_priors, pers_prefs_priors)
