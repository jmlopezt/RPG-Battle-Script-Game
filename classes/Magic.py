import random


class Spell:
    def __init__(self, name, cost, damage, type):
        self.__private_name = name
        self.__private_cost = cost
        self.__private_damage = damage
        self.__private_type = type

    def generate_damage(self):
        low = self.__private_damage - 8
        high = self.__private_damage + 5

        return random.randrange(low, high)

    def get_name(self):
        return self._Spell__private_name

    def get_cost(self):
        return self._Spell__private_cost

    def get_type(self):
        return self._Spell__private_type

    def set_name(self, name):
        self.__private_name = name

    def set_cost(self, cost):
        self.__private_cost = cost

    def set_type(self, typ):
        self.__private_type = typ

    def set_damage(self, dmg):
        self.__private_damage = dmg


