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

no_world_preferences = preferences_generation(list(world_priors_q.keys()))
no_personae_preferences = preferences_generation(list(pers_priors_q.keys()))


# Testing

# Literal listeners
L_0_q = Player(priors_q)
L_0_c = Player(priors_ch)

# Vizualize
lis_viz(L_0_q, socs, lexs)
lis_viz(L_0_q, socs, lexs, interpretation="personae_interpretation")

lis_viz(L_0_c, socs, lexs)
lis_viz(L_0_c, socs, lexs, interpretation="personae_interpretation")

# Reg Speaker
S_Reg_qs = HonestNdivSpeaker(priors_q)
speak_viz(S_Reg_qs, socs, lexs)

# Reg Speaker
S_Reg_cs = HonestNdivSpeaker(priors_ch)
speak_viz(S_Reg_cs, socs, lexs)

# Div Speaker
S_Div = HonestDivSpeaker([priors_q, priors_ch])
speak_viz(S_Div, socs, lexs)

# Pragmatic Listeners
Lis_1_q = Listener(priors_q)

lis_viz(Lis_1_q, socs, lexs)
lis_viz(Lis_1_q, socs, lexs, interpretation="personae_interpretation")


Lis_1_c = Listener(priors_ch)

lis_viz(Lis_1_c, socs, lexs)
lis_viz(Lis_1_c, socs, lexs, interpretation="personae_interpretation")

# L_2
Lis_2_gf = ListenerPlus(priors_q)

lis_viz(Lis_2_gf, socs, lexs)
lis_viz(Lis_2_gf, socs, lexs, interpretation="personae_interpretation")


Lis_2_sd = ListenerPlus(priors_ch)

lis_viz(Lis_2_sd, socs, lexs)
lis_viz(Lis_2_sd, socs, lexs, interpretation="personae_interpretation")

# S_Dup, Sufjan himself
Suf = DupSpeaker([priors_q, priors_ch], 
                    no_world_preferences, 
                    no_personae_preferences)

# Printing results one by one to identify anomalies

w = ["w_m", "w_jc"]
p = ["piQS", "piCS"]
situations = list(
    product(
        truthtable(2, w), 
        truthtable(2, p)
        )
    )

for u in ["you", "lover", "jesus"]:
    print("Results for " + u + ":\n")
    for s in situations:
        print("Here is what we have for situation " + str(s) + ":\n")
        pprint(Suf.dup_choice_rule(s[0], s[1], u, socs, lexs))
        

# Scholarly reader
L_Cag = CageyListener(
    [priors_q, priors_ch], no_world_preferences, no_personae_preferences
)
