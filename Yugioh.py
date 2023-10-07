import random, os
from Monsters import monsters
from art import win, lose
clear = lambda: os.system('clear')


# Randomly pick 2 monsters add to user hand and computer
user_hand = []
computer_hand = []

user_lp = 1000
computer_lp = 1000


def setup_game():
    for _ in range(2):
        user_hand.append(random.choice(monsters))
        computer_hand.append(random.choice(monsters))

def damage(attack1, attack2):
    damage = attack1 - attack2
    return damage

def destroy_card(hand, card):
    hand.remove(card)

def add_new_card(hand):
    return hand.append(random.choice(monsters))


setup_game()

continue_game = True
while continue_game:

    while user_hand[0] == user_hand[1]:
        user_hand[1] = random.choice(monsters)


    # computer chooses random card to spawn
    computer_spawn = random.choice(computer_hand)
    comp_monster_name = computer_spawn['name']
    comp_monster_attack = computer_spawn['attack']
    print(f" Computer spawns {comp_monster_name}, attack = {comp_monster_attack}")

    # user chooses one of 2 cards in their hands
    print(f"    You have {user_hand[0]['name']}, attack = {user_hand[0]['attack']} and, {user_hand[1]['name']}, attack = {user_hand[1]['attack']}")
    choose_monster = input("    Choose a card to spawn, type 'A' for the first card in your hand, or 'B' for second: ").lower()

    if choose_monster == 'a':
        user_spawn = user_hand[0]
        user_monster_name = user_spawn['name']
        user_monster_attack = user_spawn['attack']
    elif choose_monster == 'b':
        user_spawn = user_hand[1]
        user_monster_name = user_spawn['name']
        user_monster_attack = user_spawn['attack']

    #monsters attack, the higher attack monster wins, the loser loses LP based on the difference of attack points, if monsters have the same attack they both die, no one loses LP
    if choose_monster == 'a' or 'b':
        if user_monster_attack > comp_monster_attack: 
            damage_taken = damage(user_monster_attack,comp_monster_attack)
            computer_lp -= damage_taken
            clear()
            print(f"Your {user_monster_name} destroyed {comp_monster_name}")
            print(f"Your oppenent took {damage_taken} damage, their LP is now {computer_lp}. Your LP is {user_lp}")
            print("\n")
            destroy_card(computer_hand, computer_spawn)
            print("Opponent draws a new card...")
            add_new_card(computer_hand)
            if computer_lp <= 0:
                print(win)
                print("You win this duel! You are the King of the games!")
                continue_game = False
                
        elif comp_monster_attack > user_monster_attack:
            damage_taken = damage(comp_monster_attack, user_monster_attack)
            user_lp -= damage_taken
            clear()
            print(f"Your {user_monster_name} got destroyed by {comp_monster_name}")
            print(f"You took {damage_taken} damage, Your LP is now {user_lp}. Your oppenents is {computer_lp}")
            print("\n")
            destroy_card(user_hand, user_spawn)
            print("You draw a new card...")
            add_new_card(user_hand)
            if user_lp <= 0:
                print(lose)
                print("You lose this duel! Definitely not the King of the games! boohoo")
                continue_game = False
        else:
            clear()
            print("Both monsters get destroyed, no one takes damage")
            print("/n")
            destroy_card(computer_hand, computer_spawn)
            destroy_card(user_hand, user_spawn)
            add_new_card(computer_hand)
            add_new_card(user_hand)
