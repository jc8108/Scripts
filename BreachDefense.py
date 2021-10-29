# Created by Joshua Curry
# This is just a simple "game" of hacker vs defender
# It takes no input, just runs and sometimes you win and sometimes you don't

import random
import sys

# ---------------------------------------
# TODO
# add special attacks
# build in different responses/accept user input
# add extra functionality to hackers depending on attribute
# --------------------------------------------

# these are used to alternate turns during the breach

hackers_turn = False
defenders_turn = False


# increases every encounter, if elite it will increase both

hacked_count = 0
elite_count = 0


# attributes are just for fun, a bit of randomness
# hacker_types is used to randomly pick/initialize a hacker to battle

attribute = ['malicious', 'sophisticated', '150 IQ', 'political', 'motivated']
hacker_types = ['Ransomware Hacker', 'Insider', 'Hacktivist', 'Script Kiddy']

#  each hacker drops its own unique item which gets added to inv after they're defeated

inventory = []
loot = {'Ransomware Hacker': 'Battle-proven Backups',
        'Insider': 'Vulnerability Report',
        'Hacktivist': 'Multi-Factor Authentication',
        'Script Kiddy': 'Phishing Protection'}


# player is from the POV of a defender

class Player:
    def __init__(self, name, network_health, skill, alive):
        self.name = name
        self.health = network_health
        self.skill = skill
        self.alive = alive

# if the network health reaches 0 dies is called and
# the battle loop gets broken and game over screen is displayed

    def dies(self):
        defender.alive = False
        print(f"All the companies data and money is gone... you've been told to pack up your things and get out. \n"
              f"Game over.\n"
              f"You faced {hacked_count} hackers and {elite_count} were elites.")
        sys.exit()

# on players turn they use their skill to damage the hacker
# turn reset cleans the slate because on first encounter a coin flip decides who goes first
# similar to player.dies hacker.dies is used to reset the loop

    def defend(self):
        print(f'The {self.name} defends the network with {self.skill} skill! ')
        hacker.health = hacker.health - self.skill
        if hacker.health < 0:
            hacker.dies()
            turn_reset()
            hacker.health = 0
        print(f'{hacker.name} health: {hacker.health}.\n')


def turn_reset():
    global hackers_turn, defenders_turn
    hackers_turn = False
    defenders_turn = False


# threat actor is the hacker parent class


class ThreatActor:
    def __init__(self, health, damage, attr, name, active):
        self.health = health
        self.damage = damage
        self.attribute = attr
        self.name = name
        self.active = active

# intro tells you who you are fighting increases the count and
# has random chance to make the hacker have double health and damage AKA an elite

    def intro(self):
        global hacked_count, elite_count
        hacked_count += 1
        if random.randint(1, 100) > 75:
            elite_count += 1
            self.health = self.health * 2
            self.damage = self.damage * 2
            print('The overall bandwidth seems to have slowed greatly...')
        print(f'The logs show a {self.attribute} {self.name} lurking in the network! They have {self.health} health.')

# dies resets the loop and gives the player some bonus damage for the win
# it also drops the loot, if the player all ready has the dropped item all you get
# is the bonus damage

    def dies(self):
        defender.skill = defender.skill + 5
        hacker.active = False  # required to end the battle loop
        print(f'You have defeated the {self.attribute} {self.name}!\n')
        for k in loot:
            if k == self.name and loot[k] not in inventory:
                inventory.append(loot[k])
                print(f'The {self.name} dropped {loot[k]}! You added it to your inventory.')
                print(f'Inventory: {list_to_string(inventory)}\n\n')


# these are child classes who just have unique print functions for their attacks
# the health resets to 0 if it goes under 0 because having -negative health didn't make sense

class RansomHacker(ThreatActor):  # index 0
    def attacks(self):
        print(f'The {self.name} is encrypting your files! The network takes {self.damage} damage!')
        defender.health = defender.health - hacker.damage
        if defender.health < 0:
            defender.health = 0
        print(f'{defender.name} health: {defender.health}.\n')


class Insider(ThreatActor):  # 1
    def attacks(self):
        print(f'The {self.name} plugged in a flash drive! The network takes {self.damage} damage!')
        defender.health = defender.health - hacker.damage
        if defender.health < 0:
            defender.health = 0
        print(f'{defender.name} health: {defender.health}.\n')


class Hacktivist(ThreatActor):  # 2
    def attacks(self):
        print(f'The {self.name} vandalized the company website! The network takes {self.damage} damage!')
        defender.health = defender.health - hacker.damage
        if defender.health < 0:
            defender.health = 0
        print(f'{defender.name} health: {defender.health}.\n')


class ScriptKiddy(ThreatActor):  # 3
    def attacks(self):
        print(f'The {self.name} exploited a random vulnerability! The network takes {self.damage} damage!')
        defender.health = defender.health - hacker.damage
        if defender.health < 0:
            defender.health = 0
        print(f'{defender.name} health: {defender.health}.\n')

# just creating a player object


defender = Player('Analyst', 100, random.randint(50, 100), True)


# list to string does exactly what it sounds like it does
# in order to print out the inventory in an aesthetic way

def list_to_string(inv_list):
    pretty_list = ''
    if len(inv_list) == 1:
        return inv_list[0]
    elif len(inv_list) == 2:
        pretty_list = inv_list[0] + ' and ' + inv_list[1]
        return pretty_list
    else:
        for x in inv_list[:-1]:
            pretty_list = pretty_list + x + ', '
        pretty_list = pretty_list + 'and ' + inv_list[-1]
        return pretty_list

# battle is the 2nd function called in the main loop
# it coin flips to see who goes first
# then it stays in a while loop going back and forth between defender and hacker
# when someones health reaches 0- the battle loop breaks
# but gets called again in the main loop until the defender has all the loot

def battle():
    global hackers_turn, defenders_turn
    if random.randint(0, 1) == 1:
        print('1s and 0s flash across the screen as they attempt data exfiltration!\n')
        hackers_turn = True
    else:
        print('You ready your clicking finger and start the remediation!\n')
    while defender.alive and hacker.active:
        if hackers_turn:
            hacker.attacks()
            hackers_turn = False
            defenders_turn = True
            if 20 > defender.health > 1:
                print("You feel the CEO staring over your shoulder...\n")
            if defender.health == 0:
                defender.dies()
        else:
            defender.defend()
            hackers_turn = True
            defenders_turn = False
            if 10 > hacker.health > 1:
                print(f'The {hacker.name} spills Mountain Dew on their keyboard!')

# first just a parent threat actor class is defined
# then depending on the value assigned to name from the hacker_types list
# a child class is created giving it its own unique attack

def hacker_spawns(health, damage, attr, name, active):
    global hacker
    hacker = ThreatActor(health, damage, attr, name, active)
    if hacker.name == hacker_types[0]:
        hacker = RansomHacker(health, damage, attr, name, active)
    elif hacker.name == hacker_types[1]:
        hacker = Insider(health, damage, attr, name, active)
    elif hacker.name == hacker_types[2]:
        hacker = Hacktivist(health, damage, attr, name, active)
    elif hacker.name == hacker_types[3]:
        hacker = ScriptKiddy(health, damage, attr, name, active)
    hacker.intro()


# random.choice(hacker_types) and the following True are required
# in order to give the main loop and ending and to start it
# the other values can be changed to modify the "difficulty"

# this is the main loop, while the defender has health, battle until the hacker doesn't
# and then when one is defeated spawn a new hacker to fight
# if you defeat all the hackers and get all the loot then you win the game

while defender.alive:
    hacker_spawns(random.randint(10, 50),                # health
                  random.randint(5, 15),                 # damage
                  random.choice(attribute),              # attribute- no effect on gameplay
                  random.choice(hacker_types), True)     # don't touch
    battle()
    if len(inventory) == len(loot):
        print(f'Your network is secure for the moment. Congratulations on defeating the hackers!\n'
              f'You faced {hacked_count} hackers and {elite_count} were elites.')
        break
