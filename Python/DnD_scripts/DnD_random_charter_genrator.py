# INFO: This is a Random name and charter genrator for DnD DM. it will crate 5 random charters with name stats race class and level information. 
#
# Arther: GhostWolf
# Cration: 5/10/2023
# Last mdifyed: 5/10/2023

import random

def generate_stats():
    stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    character_stats = {}
    
    for stat in stats:
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        total = sum(rolls)
        character_stats[stat] = total
    
    return character_stats

def generate_random_character():
    race = random.choice(['Human', 'Elf', 'Dwarf', 'Halfling', 'Orc'])
    character_class = random.choice(['Fighter', 'Wizard', 'Rogue', 'Cleric', 'Bard'])
    level = random.randint(1, 20)
    Charctername = generate_random_name()

    print(f"Charcter name: {Charctername}")
    print(f"Race: {race}")
    print(f"Class: {character_class}")
    print(f"Level: {level}")
    print("\nCharacter stats:")
    

    stats = generate_stats()
    for stat, value in stats.items():
        print(f"{stat}: {value}")
    
    print("---------------\n")

# List of name components for generating random names
def generate_random_name():
    name_prefixes = ['Aer', 'Bran', 'Cael', 'Dag', 'Eld', 'Fael', 'Gwyn', 'Hael', 'Ith', 'Jor']
    name_suffixes = ['a', 'en', 'is', 'orin', 'us', 'wyn', 'thor', 'lind', 'ara', 'don']
    prefix = random.choice(name_prefixes)
    suffix = random.choice(name_suffixes)
    name = prefix + suffix
    
    return name

# Generate 5 random characters
for _ in range(5):
    generate_random_character()
    