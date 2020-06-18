import random
from classes.game import bcolors
# todo make private members


class Person:

    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.__name = name
        self.__max_hp = hp
        self.__hp = hp
        self.__max_mp = mp
        self.__mp = mp
        self.__atk_high = atk + 15
        self.__atk_low = atk - 15
        self.__df = df
        self.__magic = magic
        self.__actions = ["Attack", "Magic", "Items"]
        self.__items = items
        self.__dead = False

    def __str__(self):
        summary = self._Person__name + " Summary: " + \
                  "\n Hit Points: " + str(self._Person__hp) + \
                  "\n Defense: " + str(self._Person__df) + \
                  "\n Attack Points: " + str(self._Person__atk_high) + \
                  "\n Actions: " + str(self._Person__actions)
        print(bcolors.LIGHT_YELLOW + summary + bcolors.ENDC)

    def get_name(self):
        return str(self._Person__name)
    
    def is_dead(self):
        return self._Person__dead
    
    def set_dead(self):
        self.__dead = True

    def get_hp(self):
        return self._Person__hp

    def get_max_hp(self):
        return self._Person__max_hp

    def get_mp(self):
        return self._Person__mp

    def get_max_mp(self):
        return self._Person__max_mp

    def get_df(self):
        return self._Person__df

    def get_actions(self):
        return self._Person__actions

    def get_magic(self):
        return self._Person__magic

    def get_items(self):
        return self._Person__items

    def generate_damage(self):
        return random.randrange(self._Person__atk_low, self._Person__atk_high)

    def take_damage(self, dmg):
        self.__hp -= dmg
        if self.__hp < 0:
            self.__hp = 0
        return self._Person__hp

    def heal(self, dmg):
        self.__hp += dmg
        if self.__hp > self._Person__max_hp:
            self.__hp = self._Person__max_hp

    def take_elixir(self):
        self.__hp = self._Person__max_hp
        self.__mp = self._Person__max_mp

    def reduce_mp(self, cost):
        self.__mp -= cost

    def choose_actions(self):
        index = 1
        print(bcolors.BLUE + bcolors.BOLD + "    " + self._Person__name + "'s ACTIONS!" + bcolors.ENDC)
        for action in self._Person__actions:
            print("    " + str(index) + ":", action)
            index += 1

    def choose_magic(self):
        index = 1
        print("\n" + bcolors.BLUE + bcolors.BOLD + "    " + self._Person__name + "'s MAGIC" + bcolors.ENDC)
        for spell in self._Person__magic:
            print("     " + "    " + str(index) + ":", str(spell.get_name()), "(Cost:", str(spell.get_cost()), ")")
            index += 1

    def choose_item(self):
        index = 1
        print("\n" + bcolors.LIGHT_MAGENTA + bcolors.BOLD + "    " + self._Person__name + "'s ITEM" + bcolors.ENDC)
        for item in self._Person__items:
            print("     " + "    " + str(index) + ":", str(item.get_name()), "(Description:", str(item.get_description()), ") ",
                  "x", item.get_quantity())
            index += 1
            
    def show_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self._Person__hp / self._Person__max_hp) * 100 / 4
        mp_bar = ""
        mp_bar_ticks = (self._Person__mp / self._Person__max_mp) * 100 / 10
        
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1
            
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "
            
        hp_string = str(self._Person__hp) + "/" + str(self._Person__max_hp)
        mp_string = str(self._Person__mp) + "/" + str(self._Person__max_mp)
        
        current_hp = ""
        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)
            
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            
            current_hp += hp_string
        else:
            current_hp = hp_string

        current_mp = ""
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
    
            while decreased > 0:
                current_mp += " "
                decreased -= 1
    
            current_mp += mp_string
        else:
            current_mp = hp_string
        
        print("                     _________________________                    __________")
        print(bcolors.BOLD + self._Person__name, current_hp +
              "    |" + bcolors.GREEN + hp_bar + bcolors.ENDC + "|         " + bcolors.BOLD,
              current_mp + " |" + bcolors.BLUE + mp_bar + bcolors.ENDC + "|")
        
    def show_enemy_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self._Person__hp / self._Person__max_hp) * 100 / 2
        
        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self._Person__hp) + "/" + str(self._Person__max_hp)
        
        current_hp = ""
        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
    
            while decreased > 0:
                current_hp += " "
                decreased -= 1
    
            current_hp += hp_string
        else:
            current_hp = hp_string
            
        print("                      __________________________________________________")
        print(bcolors.BOLD + self._Person__name, current_hp +
              "    |" + bcolors.RED + hp_bar + bcolors.ENDC + "|         " + bcolors.BOLD)
        print("\n")

    def has_died(self):
        if self.__hp == 0:
            return True
        else:
            return False
        