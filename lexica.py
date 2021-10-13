# This is the lexica class. Given a lexicon name it will basically generate
# a table containing the truth-values for a given utterance.

class Lex:
    def __init__(self, utterances) -> None:
        self.utterances = utterances
        self.__lex_construction()

    def __lex_construction(self):

        def __industrial():
            self.semantics = ["competent", "incompetent"]
            self.interpretation_function = {"ing": [self.properties[0]],
                                            "in": [self.properties[1]]}
        def __civic():
            self.properties = ["friendly", "unfriendly"]
            self.interpretation_function = {"ing": [self.properties[1]],
                                            "in": [self.properties[0]]}
        def __inspired():
            self.properties = ["insightful", "uninsightful"]
            self.interpretation_function = {"ing": [self.properties[0], self.properties[1]],
                                            "in": [self.properties[0], self.properties[1]]}
        def __domestic():
            self.properties = ["traditional", "non-traditional"]
            self.interpretation_function = {"ing": [self.properties[0]],
                                            "in": [self.properties[1]]}
        def __fame():
            self.properties = ["cool", "uncool"]
            self.interpretation_function = {"ing": [self.properties[1]],
                                                "in": [self.properties[0]]}

        wc = {
            "industrial": __industrial,
            "civic": __civic,
            "inspired": __inspired,
            "domestic": __domestic,
            "fame": __fame,
        }

        return wc.get(self.lex_name, "Not a valid world name.")()

# This class is the priors, it is a special kind of dictionary to make it
# easy to store the priors for each player in the correct format.


class Priors:
    def __init__(self, world_priors, pers_priors) -> None:
        self.world_priors = world_priors
        self.prop_priors = pers_priors
        self.priors = {}
        for world in world_priors:
            self.priors[world] = [world_priors[world],
                                  {pers: prob for pers, prob in pers_priors.items()
                                   if pers in World(world).properties}]
