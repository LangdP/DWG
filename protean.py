# This is the testing of the model on the Sufjan Stevens examples that
# are discussed in chapter 6 of my dissertation

# Import packages
from players import *
from lexica import *
from helpers import *
from viz import *
from pprint import pprint

# We first have to define the priors for each listener, in the form of two
# dictionaries. The dictionaries are then merged into a Priors object.

# For gay friendly reader
# Define priors over possible worlds here, they have to add up to 1.
world_priors_r = {"w_e": 1/5, 
"w_ee": 1/5,
"w_s": 1/5,
"w_m": 1/5,
"w_d": 1/5,
}

# Define priors over personae here. They have to add up to 1.
pers_priors_r = {"piRC": 0.5, "piNRC": 0.5}

delta_soc_r = {"soc_R": 1, "soc_L": 0}

pi_lex_r = {"piRC": {"lex_RC": 1, "lex_NRC": 0}, "piNRC": {"lex_RC": 0, "lex_NRC": 1}}

# Build priors as an instance of the Priors class.
priors_r = Priors(world_priors_r, pers_priors_r, delta_soc_r, pi_lex_r)

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
    "you": {"worlds": ["w_m"], "personae": ["piQS"]},
    "lover": {"worlds": ["w_m"], "personae": ["piQS"]},
    "jesus": {"worlds": ["w_jc"], "personae": ["piCS"]},
}

utterances_cs = {
    "you": {"worlds": ["w_jc"], "personae": ["piQS", "piCS"]},
    "lover": {"worlds": ["w_m"], "personae": ["piQS"]},
    "jesus": {"worlds": ["w_jc"], "personae": ["piCS"]},
}
# Constructing lexica and storing in lists

socs = [Pers(utterances_cs, "soc_CH"), Pers(utterances_qs, "soc_Q")]
lexs = [Lex(utterances_cs, "lex_CS"), Lex(utterances_qs, "lex_QS")]

# Constructing speaker preferences
dw_world_preferences = preferences_generation(
    list(world_priors_r.keys()),
    preferred_states=[["w_m", "w_jc"], ["w_jc", "w_m"]],
    dispreferred_states=[],
)
dw_personae_preferences = preferences_generation(
    list(pers_priors_ch.keys()),
    preferred_states=[["piQS", "piCS"], ["piCS", "piQS"]],
    dispreferred_states=[],
)


no_world_preferences = preferences_generation(list(world_priors_r.keys()))
no_personae_preferences = preferences_generation(list(pers_priors_r.keys()))


# Testing

# Literal listeners
L_0_q = Player(priors_r)
L_0_c = Player(priors_ch)

# Vizualize
lis_viz(L_0_q, socs, lexs)
lis_viz(L_0_q, socs, lexs, interpretation="personae_interpretation")

lis_viz(L_0_c, socs, lexs)
lis_viz(L_0_c, socs, lexs, interpretation="personae_interpretation")

# Reg Speaker
S_Reg_qs = HonestNdivSpeaker(priors_r)
speak_viz(S_Reg_qs, socs, lexs)

# Reg Speaker
S_Reg_cs = HonestNdivSpeaker(priors_ch)
speak_viz(S_Reg_cs, socs, lexs)

# Div Speaker
S_Div = HonestDivSpeaker([priors_r, priors_ch])
speak_viz(S_Div, socs, lexs)

# Pragmatic Listeners
Lis_1_q = Listener(priors_r)

lis_viz(Lis_1_q, socs, lexs)
lis_viz(Lis_1_q, socs, lexs, interpretation="personae_interpretation")


Lis_1_c = Listener(priors_ch)

lis_viz(Lis_1_c, socs, lexs)
lis_viz(Lis_1_c, socs, lexs, interpretation="personae_interpretation")

# L_2
Lis_2_gf = ListenerPlus(priors_r)

lis_viz(Lis_2_gf, socs, lexs)
lis_viz(Lis_2_gf, socs, lexs, interpretation="personae_interpretation")


Lis_2_sd = ListenerPlus(priors_ch)

lis_viz(Lis_2_sd, socs, lexs)
lis_viz(Lis_2_sd, socs, lexs, interpretation="personae_interpretation")

# S_Dup, Sufjan himself
Suf = DupSpeaker([priors_r, priors_ch], 
                    no_world_preferences, 
                    no_personae_preferences)

Suf_prefs = DupSpeaker([priors_r, priors_ch], 
                    dw_world_preferences, 
                    dw_personae_preferences)

# Scholarly reader
L_Cag = CageyListener(
    [priors_r, priors_ch], no_world_preferences, no_personae_preferences
)
