# This is the Lexicon class. It serves as a basis for semantic and social
# lexica.
# All lexica are kinds of dictionaries under the hood
class Lexicon:
    def __init__(self, utt_dic) -> None:
        self._utt_dic = utt_dic
        self.lexical_units = [k for k in utt_dic.keys()]

# This is the semantics lexicon
class Lex(Lexicon):
    def __init__(self, utt_dic, name="lex") -> None:
        super().__init__(utt_dic)
        self.name = name
        self.__build_semantics()

    def __build_semantics(self):
        self.__semantics = {}
        for k in self._utt_dic.keys():
            self.__semantics[k] = self._utt_dic[k]["worlds"]
        return self.__semantics

    def semantics(self, lexical_unit):
        if lexical_unit in self.lexical_units:
            return self.__semantics[lexical_unit]
        else:
            print("This lexical unit is not defined in the lexicon")

# This is the social meaning lexicon
class Pers(Lexicon):
    def __init__(self, utt_dic, name="soc") -> None:
        super().__init__(utt_dic)
        self.name = name
        self.__build_social_meaning()

    def __build_social_meaning(self):
        self.__social_meaning = {}
        for k in self._utt_dic.keys():
            self.__social_meaning[k] = self._utt_dic[k]["personae"]
        return self.__social_meaning

    def social_meaning(self, lexical_unit):
        if lexical_unit in self.lexical_units:
            return self.__social_meaning[lexical_unit]
        else:
            print("This lexical unit is not defined in the social meaning lexicon")

# This class is the priors, it is a special kind of dictionary to make it
# easy to store the priors for each player in the correct format.

class Priors:
    def __init__(self, world_priors, pers_priors, delta_soc, pi_lex) -> None:
        self.world_priors = world_priors
        self.pers_priors = pers_priors
        self.delta_soc = delta_soc
        self.pi_lex = pi_lex
        self.priors = {
            'worlds': {}, 
            'personae': {},
            'delta_soc': {},
            'pi_lex': {}
        }
        for w in world_priors:
            self.priors['worlds'][w] = world_priors[w]
        for p in pers_priors.keys():
            self.priors['personae'][p] = pers_priors[p]
        for s in delta_soc:
            self.priors['delta_soc'][s] = delta_soc[s]
        for l in pi_lex:
            self.priors['pi_lex'][l] = pi_lex[l]