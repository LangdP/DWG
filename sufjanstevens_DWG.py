# This is the testing of the model on the Sufjan Stevens examples that
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
world_priors_q = {"w_m": 0.5, "w_jc": 0.5}

# Define priors over personae here. They have to add up to 1.
pers_priors_q = {"piQS": 0.5, "piCS": 0.5}

delta_soc_q = {"soc_Q": 1, "soc_CH": 0}

pi_lex_q = {"piQS": {"lex_QS": 1, "lex_CS": 0}, "piCS": {"lex_QS": 0, "lex_CS": 1}}

# Build priors as an instance of the Priors class.
priors_q = Priors(world_priors_q, pers_priors_q, delta_soc_q, pi_lex_q)

# For straight default reader
# Define priors over possible worlds here, they have to add up to 1.
world_priors_ch = {"w_m": 0.5, "w_jc": 0.5}

# Define priors over personae here. They have to add up to 1.
pers_priors_ch = {"piQS": 0.5, "piCS": 0.5}

delta_soc_ch = {"soc_Q": 0, "soc_CH": 1}

pi_lex_ch = {"piQS": {"lex_QS": 1, "lex_CS": 0}, "piCS": {"lex_QS": 0, "lex_CS": 1}}

# Build priors as an instance of the Priors class.
priors_ch = Priors(world_priors_ch, pers_priors_ch, delta_soc_ch, pi_lex_ch)

# Build utterances, one per preferred indexation/interpretation function
# for each player

utterances_qs = {
    "you": {"worlds": ["w_m"], "personae": ["piQS", "piCS"]},
    "lover": {"worlds": ["w_m"], "personae": ["piQS"]},
    "jesus": {"worlds": ["w_jc"], "personae": ["piCS"]},
}

utterances_cs = {
    "you": {"worlds": ["w_m"], "personae": ["piQS", "piCS"]},
    "lover": {"worlds": ["w_m"], "personae": ["piQS"]},
    "jesus": {"worlds": ["w_jc"], "personae": ["piCS"]},
}
# Constructing lexica and storing in lists

socs = [Pers(utterances_cs, "soc_CH"), Pers(utterances_qs, "soc_Q")]
lexs = [Lex(utterances_cs, "lex_CS"), Lex(utterances_qs, "lex_QS")]

no_world_preferences = preferences_generation(list(world_priors_q.keys()))
no_personae_preferences = preferences_generation(list(pers_priors_q.keys()))


# Testing

# Literal listeners
L_0_gf = Player(priors_q)
L_0_sd = Player(priors_ch)

# Vizualize
lis_viz(L_0_gf, socs, lexs)
lis_viz(L_0_gf, socs, lexs, interpretation="personae_interpretation")

lis_viz(L_0_sd, socs, lexs)
lis_viz(L_0_sd, socs, lexs, interpretation="personae_interpretation")

# Reg Speaker
S_Reg_gf = HonestNdivSpeaker(priors_q)
speak_viz(S_Reg_gf, socs, lexs)

# Reg Speaker
S_Reg_sd = HonestNdivSpeaker(priors_ch)
speak_viz(S_Reg_sd, socs, lexs)

# Div Speaker
S_Div = HonestDivSpeaker([priors_q, priors_ch])
speak_viz(S_Div, socs, lexs)

# Pragmatic Listeners
Lis_1_gf = Listener(priors_q)

lis_viz(Lis_1_gf, socs, lexs)
lis_viz(Lis_1_gf, socs, lexs, interpretation="personae_interpretation")


Lis_1_sd = Listener(priors_ch)

lis_viz(Lis_1_sd, socs, lexs)
lis_viz(Lis_1_sd, socs, lexs, interpretation="personae_interpretation")

# L_2
Lis_2_gf = ListenerPlus(priors_q)

lis_viz(Lis_2_gf, socs, lexs)
lis_viz(Lis_2_gf, socs, lexs, interpretation="personae_interpretation")


Lis_2_sd = ListenerPlus(priors_ch)

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
    [priors_q, priors_ch], no_world_preferences, no_personae_preferences
)

# L_Cag_u = UncovCageyListener([priors_gf, priors_sd],
#                            worlds_prefs_priors, pers_prefs_priors)
