from classes.Person import Person
from classes.game import bcolors, load_magic, load_inventory, do_attack, do_magic, do_use_items, user_choice, who_wins

import random


def do_move(striker, defending, index, user = True, strikers=None):

    if striker.get_actions()[index] == "Attack":
        return do_attack(striker, defending)

    elif striker.get_actions()[index] == "Magic":
        return do_magic(striker, defending, user)

    elif striker.get_actions()[index] == "Items":
        return do_use_items(striker, defending, strikers)

    else:
        return True


def main():
    magic = load_magic()
    inventory = load_inventory()
    player1 = Person('Charmine', 60, 15, 90, 123, [magic[0], magic[2], magic[6]], [inventory[0], inventory[5]])
    player2 = Person('Ficusaur', 80, 95, 600, 2, [magic[1], magic[2], magic[4]], [inventory[2], inventory[3], inventory[4]])
    player3 = Person('AcerDesh', 60, 25, 80, 712, [magic[3], magic[5], magic[6]], [inventory[0], inventory[1]])
    enemy = Person('Devil', 11900, 60, 60, 25, [magic[1], magic[3], magic[5]], inventory)
    
    players = [player1, player2, player3]

    running = True

    print(bcolors.BACKGROUND_WHITE + bcolors.LIGHT_RED + bcolors.BOLD + "A WILD ENEMY APPEARED!" + bcolors.ENDC)
    enemy.__str__()

    while running:
        player_counter = 0
        print("======================")
        print("\n")
        print("NAME                 HP                                         MP")
        for player in players:
            player.show_stats()
        
        print("\n")
        enemy.show_enemy_stats()
        
        for player in players:
            if not player.is_dead():
                print(player.is_dead())
                index = user_choice(player, 'Actions')
        
                if abs(index) > len(player.get_actions()):
                    continue
                print("You chose", player.get_actions()[index], "!")
                re_choose = do_move(player, enemy, index, True, players)
                if re_choose:
                    player_counter += 1
            else:
                players.remove(player)
                
        if player_counter >= len(players):
            continue

        enemy_action = random.randrange(1, 2)
        
        if len(players) > 1:
            do_move(enemy, players[random.randrange(1, len(players))], enemy_action, False)
            for player in players:
                if player.has_died():
                    player.set_dead()
                    players.remove(player)
            running = True
        else:
            do_move(enemy, players[0], enemy_action, False)
            running = who_wins(players[0], enemy)

        

if __name__ == "__main__":
    main()