from classes.Magic import Spell
from classes.inventory import Item
import random
    
    
def who_wins(player, enemy):
    running = True
    
    if enemy.get_hp() == 0:
        print(bcolors.GREEN + "You win!" + bcolors.ENDC)
        running = False

    elif player.has_died():
        player.set_dead()
        print(bcolors.BACKGROUND_BLACK + bcolors.RED + "YOU DIED!" + bcolors.ENDC)
        running = False

    return running


def load_magic():
    magic = [Spell("Ashes", 40, 20, "Dakhor"), Spell("Embers", 40, 30, "Dakhor"), Spell("Bubbles", 45, 139, "Dakhor"),
             Spell("Mud", 5, 10, "Dakhor"), Spell("Thunder Reign", 100, 300, "Dakhor"),
             Spell("Lava", 100, 100, "Dakhor"), Spell("Cure", 12, 120, "healing")]

    return magic


def load_inventory():
    inventory = [Item("Potion", "potion", "Heals 50 HP", 50, 5),
                 Item("Hi-Potion", "potion", "Heals 100 HP", 100, 3),
                 Item("Super-Potion", "potion", "Heals 200 HP", 200, 2),
                 Item("Elixir", "elixir", "Full recovery of one user", 9999, 1),
                 Item("Mega-Elixir", "Mega-elixir", "Full recovery", 9999, 1),
                 Item("Grenade", "attack", "It Explodes. Hit for 500 HP", 500, 1)]

    return inventory


def user_cast_spell(player, enemy, spell):

    magic_damage = spell.generate_damage()
    if spell.get_type() == "healing":
        player.heal(magic_damage)

        print(bcolors.GREEN + "\n" + str(spell.get_name()) + " heals you for", str(magic_damage),
              "HP" + bcolors.ENDC)
    else:
        enemy.take_damage(magic_damage)

        print(bcolors.BLUE + "\n" + str(spell.get_name()) + " hits for", str(magic_damage),
              "points of damage" + bcolors.ENDC)


def enemy_cast_spell(enemy, player):

    magic_index = random.randrange(0, len(enemy.get_magic()))
    spell = enemy.get_magic()[magic_index]

    print(enemy.get_name(), "hits " + player.get_name() + " with", str(spell.get_name()), "!")

    magic_damage = spell.generate_damage()
    player.take_damage(magic_damage)

    print(enemy.get_name(), "hits " + player.get_name() + " with ", magic_damage, "point of damage.")


def user_choice(striker, choice=None):

    if choice == 'Actions':
        message = '    Choose your moves!:'
        striker.choose_actions()

    elif choice == 'Magic':
        message = '    Choose your spell!:'
        striker.choose_magic()

    elif choice == 'Item':
        message = '    Choose your Item!:'
        striker.choose_item()

    else:
        message = '    Choose anything'
        index = -1

    index = int(input(message)) - 1

    return index


def consume_item(player, enemy, item, players=None):

    prop = item.get_prop()
    item_quantity = item.get_quantity()
    item_type = item.get_type()

    if item_quantity > 0:
        item.reduce_quantity()
        if item_type == 'potion':
            player.heal(prop)
            print(bcolors.GREEN + "\n" + str(item.get_name()) + " heals you for", str(prop), "HP" + bcolors.ENDC)
        elif item_type == "attack":
            enemy.take_damage(prop)
            print(bcolors.RED + "\n" + str(item.get_name()) + " hits for", str(prop),
                  "points of damage" + bcolors.ENDC)
        elif item_type == "elixir":
            player.take_elixir()
            print(bcolors.GREEN + "\n" + str(item.get_name()) + " fully heals you " + bcolors.ENDC)
        elif item_type == "Mega-elixir":
            for player in players:
                player.take_elixir()
            print(bcolors.GREEN + "\n" + str(item.get_name()) + " fully heals the team" + bcolors.ENDC)
    else:
        print(bcolors.RED + "\n" + "YOU DON'T HAVE ANY " + str(item.get_name()).upper() + bcolors.ENDC)
        return True
    return False


def do_attack(striker, defending):
    damage = striker.generate_damage()
    defending.take_damage(damage)
    print(striker.get_name(), "Hits" + defending.get_name() + " for", damage, "point of damage.")

    return False


def do_magic(striker, defending, user):

    if user:
        magic_index = user_choice(striker, 'Magic')

        if abs(magic_index) > len(striker.get_magic()):
            return True

        spell = striker.get_magic()[magic_index]
        print("You chose", str(spell.get_name()), "!")

        cost = spell.get_cost()
        current_mp = striker.get_mp()

        if cost > current_mp:
            print(bcolors.RED + "\nNot enough MP\n" + bcolors.ENDC)
            return True

        striker.reduce_mp(cost)

        user_cast_spell(striker, defending, spell)
        return False

    else:
        enemy_cast_spell(striker, defending)
        return False


def do_use_items(striker, defending, strikers=None):

    item_index = user_choice(striker, 'Item')
    if abs(item_index) > len(striker.get_items()):
        return True

    item = striker.get_items()[item_index]
    print("You chose", str(item.get_name()), "!")

    return consume_item(striker, defending, item, strikers)


class bcolors:
    LIGHT_MAGENTA = '\033[95m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[32m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_RED = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINED = '\033[4m'

    # Dim        = "\033[2m"
    # Blink      = "\033[5m"
    # Reverse    = "\033[7m"
    # Hidden     = "\033[8m"
    #
    # ResetBold       = "\033[21m"
    # ResetDim        = "\033[22m"
    # ResetUnderlined = "\033[24m"
    # ResetBlink      = "\033[25m"
    # ResetReverse    = "\033[27m"
    # ResetHidden     = "\033[28m"

    BACKGROUND_DEFAULT = "\033[49m"
    BACKGROUND_WHITE = "\033[40m"
    BACKGROUND_RED = "\033[41m"
    BACKGROUND_GREEN = "\033[42m"
    BACKGROUND_YELLOW = "\033[43m"
    BACKGROUND_BLUE = "\033[44m"
    BACKGROUND_MAGENTA = "\033[45m"
    BACKGROUND_CYAN = "\033[46m"
    BACKGROUND_LIGHT_GRAY = "\033[47m"
    BACKGROUND_DARK_GRAY = "\033[100m"
    BACKGROUND_LIGHT_RED = "\033[101m"
    BACKGROUND_LIGHT_GREEN = "\033[102m"
    BACKGROUND_LIGHT_YELLOW = "\033[103m"
    BACKGROUND_LIGHT_BLUE = "\033[104m"
    BACKGROUND_LIGHT_MAGENTA = "\033[105m"
    BACKGROUND_LIGHT_CYAN = "\033[106m"
    BACKGROUND_BLACK = "\033[107m"
