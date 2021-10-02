# This is the world class. It is supposed to represent worlds in the model
# , along with their attributes (mostly orders of worth).
# The orders of worth have to be set manually right now, but once we have
# all the properties we're interested in along with the orders of worth, we can
# easily generate a world only using its name.

class World:
    def __init__(self, world_name) -> None:
        self.world_name = world_name
        self.__world_construction()
        self.order_of_worth = [self.properties[0], self.properties[1]]

    def __world_construction(self):

        def __industrial():
            self.properties = ["competent", "incompetent"]
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

        return wc.get(self.world_name, "Not a valid world name.")()

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
