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
world_priors_l = {"w_e": 1/5, 
"w_ee": 1/5,
"w_s": 1/5,
"w_m": 1/5,
"w_d": 1/5,
}

# Define priors over personae here. They have to add up to 1.
pers_priors_l = {"piRC": 0.5, "piNRC": 0.5}

delta_soc_l = {"soc_R": 0, "soc_L": 1}

pi_lex_l = {"piRC": {"lex_RC": 0, "lex_NRC": 1}, "piNRC": {"lex_RC": 0, "lex_NRC": 1}}

# Build priors as an instance of the Priors class.
priors_l = Priors(world_priors_l, pers_priors_l, delta_soc_l, pi_lex_l)


# Build utterances, one per preferred indexation/interpretation function
# for each player

utterances_rc = {
    "immigration": {"worlds": ["w_e", "w_ee", "w_s", "w_m", "w_d"], "personae": ["piRC"]},
    "eur": {"worlds": ["w_e", "w_ee"], "personae": ["piNRC"]},
    "e-eur": {"worlds": ["w_ee"], "personae": ["piNRC"]},
    "syr": {"worlds": ["w_s"], "personae": ["piRC"]},
    "mus": {"worlds": ["w_m"], "personae": ["piRC"]},
    "drk": {"worlds": ["w_d"], "personae": ["piRC"]},
}

utterances_nrc = {
    "immigration": {"worlds": ["w_e", "w_ee", "w_s"], "personae": ["piNRC"]},
    "eur": {"worlds": ["w_e", "w_ee"], "personae": ["piNRC"]},
    "e-eur": {"worlds": ["w_ee"], "personae": ["piRC"]},
    "syr": {"worlds": ["w_s"], "personae": ["piRC"]},
    "mus": {"worlds": ["w_m"], "personae": ["piRC"]},
    "drk": {"worlds": ["w_d"], "personae": ["piRC"]},
}
# Constructing lexica and storing in lists

socs = [Pers(utterances_nrc, "soc_L"), Pers(utterances_rc, "soc_R")]
lexs = [Lex(utterances_nrc, "lex_NRC"), Lex(utterances_rc, "lex_RC")]

# Constructing speaker preferences
#dw_world_preferences = preferences_generation(
#    list(world_priors_r.keys()),
#    preferred_states=[["w_m", "w_jc"], ["w_jc", "w_m"]],
#    dispreferred_states=[],
#)
#dw_personae_preferences = preferences_generation(
#    list(pers_priors_l.keys()),
#    preferred_states=[["piQS", "piCS"], ["piCS", "piQS"]],
#    dispreferred_states=[],
#)


no_world_preferences = preferences_generation(list(world_priors_r.keys()))
no_personae_preferences = preferences_generation(list(pers_priors_r.keys()))


# Testing
# Literal listeners
L_0_r = Player(priors_r)
L_0_l = Player(priors_l)

# Vizualize
lis_viz(L_0_r, socs, lexs)
lis_viz(L_0_r, socs, lexs, interpretation="personae_interpretation")

lis_viz(L_0_l, socs, lexs)
lis_viz(L_0_l, socs, lexs, interpretation="personae_interpretation")

# Reg Speaker
S_Reg_rc = HonestNdivSpeaker(priors_r)
speak_viz(S_Reg_rc, socs, lexs)

# Reg Speaker
S_Reg_nrc = HonestNdivSpeaker(priors_l)
speak_viz(S_Reg_nrc, socs, lexs)

# Div Speaker
S_Div = HonestDivSpeaker([priors_r, priors_l])
speak_viz(S_Div, socs, lexs)

# Pragmatic Listeners
Lis_1_r = Listener(priors_r)

lis_viz(Lis_1_r, socs, lexs)
lis_viz(Lis_1_r, socs, lexs, interpretation="personae_interpretation")

lis_viz_save(Lis_1_r, socs, lexs, "protean-semlis-r.tex")
lis_viz_save(Lis_1_r, socs, lexs, "protean-soclis-r.tex", 
            interpretation="personae_interpretation")


Lis_1_l = Listener(priors_l)

lis_viz(Lis_1_l, socs, lexs)
lis_viz(Lis_1_l, socs, lexs, interpretation="personae_interpretation")

lis_viz_save(Lis_1_l, socs, lexs, "protean-semlis-l.tex")
lis_viz_save(Lis_1_l, socs, lexs, "protean-soclis-l.tex", 
            interpretation="personae_interpretation")

# L_2
Lis_2_r = ListenerPlus(priors_r)

lis_viz(Lis_2_r, socs, lexs)
lis_viz(Lis_2_r, socs, lexs, interpretation="personae_interpretation")


Lis_2_l = ListenerPlus(priors_l)

lis_viz(Lis_2_l, socs, lexs)
lis_viz(Lis_2_l, socs, lexs, interpretation="personae_interpretation")

# S_Dup, Sufjan himself
S_Dup = DupSpeaker([priors_r, priors_l], 
                    no_world_preferences, 
                    no_personae_preferences)
speak_viz(S_Dup, socs, lexs)

def most_likely(s, socs, lexs):
    preds = s.full_predictions(socs, lexs)[0]
    newdict = {}
    for c in preds:
        maximum = max(preds[c],
            key = preds[c].get)
        newdict[c] = {maximum : preds[c][maximum]}
    return newdict

#Suf_prefs = DupSpeaker([priors_r, priors_l], 
#                    dw_world_preferences, 
#                    dw_personae_preferences)
#
# Scholarly reader
L_Cag = CageyListener(
    [priors_r, priors_l], no_world_preferences, no_personae_preferences
)
