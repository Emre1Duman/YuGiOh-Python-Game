import random

# Create a dictionary of monsters with their name & attack
#Yugioh monsters
monsters = [
    {
    "name": "Blue eyes",
    "attack": 3000,
},
{
    "name": "Dark magician",
    "attack": 2400,
},
{
    "name": "Stardust Dragon",
    "attack": 2600,
},
{
    "name": "Red Dragon Archfiend",
    "attack": 3000,
},
{
    "name": "Cyber dragon",
    "attack": 2200,
},
{
    "name": "Black rose dragon",
    "attack": 2500,
},
{
    "name": "Crystal wing synchro dragon",
    "attack": 2700,
},
{
    "name": "Dark magician girl",
    "attack": 2300,
},
{
    "name": "exodia",
    "attack": 2800,
},
{
    "name": "Junk warrior",
    "attack": 2300,
}
]



# Randomly pick 2 monsters add to user hand and computer
user_hand = []
computer_hand = []

user_lp = 4000
computer_lp = 4000


def setup_game():
    for _ in range(2):
        user_hand.append(random.choice(monsters))
        computer_hand.append(random.choice(monsters))

setup_game()
# computer chooses random card to spawn
computer_spawn = random.choice(computer_hand)
comp_monster_name = computer_spawn['name']
comp_monster_attack = computer_spawn['attack']


print(f"Computer spawns {comp_monster_name}, attack = {comp_monster_attack}")

# user chooses one of 2 cards in their hands
print(f" You have {user_hand[0]['name']}, attack = {user_hand[0]['attack']} and, {user_hand[1]['name']}, attack = {user_hand[1]['attack']}")
choose_monster = input("Choose a card to spawn, type 'A' for the first card in your hand, or 'B' for second: ").lower()

if choose_monster == 'a':
    user_monster_name = user_hand[0]['name']
    user_monster_attack = user_hand[0]['attack']
elif choose_monster == 'b':
    user_monster_name = user_hand[1]['name']
    user_monster_attack = user_hand[1]['attack']

# 2 monsters attack, the higher attack monster wins, the loser loses LP based on the difference of attack points, if monsters have the same attack they both die, no one loses LP
if choose_monster == 'a':
    if user_monster_attack > comp_monster_attack:
        damage = user_monster_attack - comp_monster_attack
        computer_lp -= damage
        print(f"Your {user_monster_name} destroyed {comp_monster_name}")
        print(f"Your oppenent took {damage} damage, thier LP is now {computer_lp}")
elif choose_monster == 'b':
    if user_monster_attack > comp_monster_attack:
        damage = user_monster_attack - comp_monster_attack
        computer_lp -= damage
        print(f"Your {user_monster_name} destroyed {comp_monster_name}")
        print(f"Your oppenent took {damage} damage, thier LP is now {computer_lp}")




#https://docs.python.org/3/tutorial/datastructures.html
#Using pop feature for removing yugioh card from a list and displaying it