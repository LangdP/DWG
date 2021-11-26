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
world_priors_i = {"w_e": 1/5, 
"w_ee": 1/5,
"w_s": 1/5,
"w_m": 1/5,
"w_d": 1/5,
}

# Define priors over personae here. They have to add up to 1.
pers_priors_i = {"piRC": 0.5, "piNRC": 0.5}

delta_soc_i = {"soc_I": 0, "soc_W": 1, "soc_L": 0}

pi_lex_i = {"piRC": {"lex_RCI": 1, "lex_RCW" : 0, "lex_NRC": 0}, "piNRC": {"lex_RCI": 0, "lex_RCW" : 0, "lex_NRC": 1}}

# Build priors as an instance of the Priors class.
priors_i = Priors(world_priors_i, pers_priors_i, delta_soc_i, pi_lex_i)

# For gay friendly reader
# Define priors over possible worlds here, they have to add up to 1.
world_priors_w = {"w_e": 1/5, 
"w_ee": 1/5,
"w_s": 1/5,
"w_m": 1/5,
"w_d": 1/5,
}

# Define priors over personae here. They have to add up to 1.
pers_priors_w = {"piRC": 0.5, "piNRC": 0.5}

delta_soc_w = {"soc_I": 0, "soc_W": 1, "soc_L": 0}

pi_lex_w = {"piRC": {"lex_RCI": 0, "lex_RCW" : 1, "lex_NRC": 0}, "piNRC": {"lex_RCI": 0, "lex_RCW" : 0, "lex_NRC": 1}}

# Build priors as an instance of the Priors class.
priors_w = Priors(world_priors_w, pers_priors_w, delta_soc_w, pi_lex_w)

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

delta_soc_l = {"soc_I": 0, "soc_W": 1, "soc_L": 0}

pi_lex_l = {"piRC": {"lex_RCI": 0, "lex_RCW" : 0, "lex_NRC": 1}, "piNRC": {"lex_RCI": 0, "lex_RCW" : 0, "lex_NRC": 1}}

# Build priors as an instance of the Priors class.
priors_l = Priors(world_priors_l, pers_priors_l, delta_soc_l, pi_lex_l)


# Build utterances, one per preferred indexation/interpretation function
# for each player
utterances_rci = {
    "immigration": {"worlds": ["w_m"], "personae": ["piRC"]},
    "eur": {"worlds": ["w_e", "w_ee"], "personae": ["piNRC"]},
    "e-eur": {"worlds": ["w_ee"], "personae": ["piNRC"]},
    "syr": {"worlds": ["w_s"], "personae": ["piRC"]},
    "mus": {"worlds": ["w_m"], "personae": ["piRC"]},
    "drk": {"worlds": ["w_d"], "personae": ["piRC"]},
}

utterances_rcw = {
    "immigration": {"worlds": ["w_d"], "personae": ["piRC"]},
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

socs = [Pers(utterances_nrc, "soc_L"), Pers(utterances_rcw, "soc_W"), Pers(utterances_rci, "soc_I")]
lexs = [Lex(utterances_nrc, "lex_NRC"), Lex(utterances_rcw, "lex_RCW"), Lex(utterances_rci, "lex_RCI")]


no_world_preferences = preferences_generation(list(world_priors_w.keys()), 
                                                players=3)
no_personae_preferences = preferences_generation(list(pers_priors_w.keys()),
                                                players=3)


# Testing
# Literal listeners
L_0_i = Player(priors_i)
L_0_w = Player(priors_w)
L_0_l = Player(priors_l)

# Vizualize
lis_viz(L_0_i, socs, lexs)
lis_viz(L_0_i, socs, lexs, interpretation="personae_interpretation")

lis_viz(L_0_w, socs, lexs)
lis_viz(L_0_w, socs, lexs, interpretation="personae_interpretation")

lis_viz(L_0_l, socs, lexs)
lis_viz(L_0_l, socs, lexs, interpretation="personae_interpretation")

# Reg Speaker
S_Reg_rc = HonestNdivSpeaker(priors_w)
speak_viz(S_Reg_rc, socs, lexs)

# Reg Speaker
S_Reg_nrc = HonestNdivSpeaker(priors_l)
speak_viz(S_Reg_nrc, socs, lexs)

# Div Speaker
S_Div = HonestDivSpeaker([priors_w, priors_l])
speak_viz(S_Div, socs, lexs)

# Pragmatic Listeners

Lis_1_i = Listener(priors_i)

lis_viz(Lis_1_i, socs, lexs)
lis_viz(Lis_1_i, socs, lexs, interpretation="personae_interpretation")

lis_viz_save(Lis_1_i, socs, lexs, "manifold-semlis-i.tex")
lis_viz_save(Lis_1_i, socs, lexs, "manifold-soclis-i.tex", 
            interpretation="personae_interpretation")

Lis_1_w = Listener(priors_w)

lis_viz(Lis_1_w, socs, lexs)
lis_viz(Lis_1_w, socs, lexs, interpretation="personae_interpretation")

lis_viz_save(Lis_1_w, socs, lexs, "manifold-semlis-w.tex")
lis_viz_save(Lis_1_w, socs, lexs, "manifold-soclis-w.tex", 
            interpretation="personae_interpretation")


Lis_1_l = Listener(priors_l)

lis_viz(Lis_1_l, socs, lexs)
lis_viz(Lis_1_l, socs, lexs, interpretation="personae_interpretation")

lis_viz_save(Lis_1_l, socs, lexs, "manifold-semlis-l.tex")
lis_viz_save(Lis_1_l, socs, lexs, "manifold-soclis-l.tex", 
            interpretation="personae_interpretation")

# S_Dup
S_Dup = DupSpeaker([priors_i, priors_w, priors_l], 
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

