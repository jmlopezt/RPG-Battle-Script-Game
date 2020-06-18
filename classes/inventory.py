class Item:

    def __init__(self, name, type, description, prop, quantity):
        self.__private_name = name
        self.__private_type = type
        self.__private_description = description
        self.__private_prop = prop
        self.__private_quantity = quantity

    def get_name(self):
        return self._Item__private_name

    def get_description(self):
        return self._Item__private_description

    def get_type(self):
        return self._Item__private_type

    def get_prop(self):
        return self._Item__private_prop

    def get_quantity(self):
        return self._Item__private_quantity

    def set_name(self, name):
        self.__private_name = name

    def set_type(self, typ):
        self.__private_type = typ

    def set_description(self, description):
        self.__private_description = description

    def set_quantity(self, quantity):
        self.__private_quantity = quantity

    def reduce_quantity(self):
        self.__private_quantity -= 1
