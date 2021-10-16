# These are our player classes. They are divided into two main subclasses, 
# Listener and Speaker. These two are themselves divided into many subclasses
# Reflecting the various configurations of the game that are presented in the 
# dissertation.

# IMPORT PACKAGES
from math import exp
from helpers import *
from lexica import *

# This is our Player class. I assume that from a cognitive standpoint it makes
# sense that all players have access to the literal listener, so this is 
# essentially a literal listener.
# All players are constructed with priors that are Priors objects. 
# Those priors are envisioned as the priors of the literal listener in the model.
class Player:
    def __init__(self, priors) -> None:
        # These are the full priors for the player, the .priors attr
        # of a Priors object
        self.priors = priors.priors

    def l0_interpretation(self, lexs : list, socs : list, world : str, utt : str):
        l0_w_given_m = sum([self.lex_choice(l, socs, utt) * 
        self.lexicalized_content_interpretation(l, world, utt) for l in lexs])
        return l0_w_given_m

    def lexicalized_content_interpretation(self, lex : Lex, world : str, utt : str):
        lex_w_given_m = ((self._sem_interpret(utt, world, lex))
                         / (sum([self._sem_interpret(utt, w, lex) 
                         for w in self.priors['worlds'].keys()])))
        return lex_w_given_m

    def lex_choice(self, lex : Lex, socs : list, utt : str):
        personae = self.priors['personae'].keys()
        lex_given_m = sum([self.general_social_interpretation(p, utt, socs) *
        self.priors['pi_lex'][p][lex.name] for p in personae])
        return lex_given_m

    def general_social_interpretation(self, pers, utt, socs : list):
        pi_given_m = sum([self.lexicalized_social_interpretation(s, pers, utt) *
        self.priors['delta_soc'][s.name] for s in socs])
        return pi_given_m
        

    def lexicalized_social_interpretation(self, soc, pers, utt):
        soc_pi_given_m = ((self._soc_interpret(utt, pers, soc))
                         / (sum([self._soc_interpret(utt, p, soc) 
                         for p in self.priors['personae'].keys()])))
        return soc_pi_given_m

    def _soc_interpret(self, utt, i, inters : Pers): return 1 \
        if i in inters._Pers__social_meaning[utt]\
        else 0

    def _sem_interpret(self, utt, i, inters : Lex): return 1 \
        if i in inters._Lex__semantics[utt]\
        else 0


# This is the Speaker class, it takes a world and a temperature parameter as
# arguments. It inherits the literal interpretations from the player class.
class Speaker(Player):
    def __init__(self, priors, alpha) -> None:
        super().__init__(priors)
        self.alpha = alpha

    def utility(self, world, prop, utt):
        return my_log(self.literal_content_interpretation(world, prop, utt) * self.priors[world][0])

    def choice_rule(self, world, utt, messages, prop):
        return (exp(self.alpha * self.utility(world, prop, utt))
                / sum([exp(self.alpha * self.utility(world, prop, message)) for message in messages]))

    def prediction(self, world, messages):
        props = World(world).properties
        preds = {p:
                 {m: self.choice_rule(world, m, messages, p)
                  for m in messages}
                 for p in props}
        return preds

    def full_predictions(self, messages):
        preds = {}
        for w in self.priors:
            props = World(w).properties
            preds[w] =  [self.priors[w][0],
                        {p:
                        {m: self.choice_rule(w, m, messages, p)
                        for m in messages}
                        for p in props}
                        ]
        return preds

# This is the Li for  {m: self.choice_rule(world, m, messages, p)p in props}stener class. Not much to say here except that this layout makes
# it clear that the l  for m in messages}istener envisions the speaker as belonging to the same
# world as them, whicfor p in props}h is not necessarily true and something we might want
# to play with once we have more of an idea how clashes work.
# In any case, each listener envisions their own player.


class Listener(Player):
    def __init__(self, priors, alpha, beta) -> None:
        super().__init__(priors)
        self._speaker = Speaker(priors, alpha)
        self.alpha = alpha
        self.beta = beta

    def lis(self, world, prop, utt, messages):
        return ((self.priors[world][1][prop] * self._speaker.choice_rule(world, utt, messages, prop)) /
                sum([self.priors[world][1][p] * self._speaker.choice_rule(world, utt, messages, p)
                     for p in World(world).properties]))

    def update_world_priors(self, utt, messages):
        scores = []
        for w in self.priors:
            for p in World(w).properties:
                if World(w).order_of_worth.index(p) == 0:
                    score = self.priors[w][0] + self.priors[w][0] * \
                        self.lis(w, p, utt, messages)
                else:
                    pass
            scores.append(score)
        i = 0
        for w in self.priors:
            self.priors[w][0] = (exp(self.beta * scores[i]) /
                                 sum([exp(self.beta * score) for score in scores]))
            i += 1

    def prediction(self, world, messages):
        props = World(world).properties
        preds = {m:
                 {p: self.lis(world, p, m, messages)
                  for p in props}
                 for m in messages}
        return preds

    def full_predictions(self, messages):
        preds = {}
        for m in messages:
            old_priors = self.priors
            self.update_world_priors(m, messages)
            preds[m] = {}
            for w in self.priors:
                props = World(w).properties
                preds[m][w] = [self.priors[w][0],
                {p:
                {m: self.lis(w, p, m, messages)
                for m in messages}
                for p in props}]
            self.priors = old_priors
        return preds