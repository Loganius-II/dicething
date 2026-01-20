from random import choice, randint

def main():
    # accepts no arguments
    # calls all functions to play the number of games specified
    pass

def output_dice(dice):
    # accepts dice
    # outputs each die in the list
    pass

def roll_die():
    # accepts nothing
    # returns a random iteger between 1 and 6
    return randint(1,7)

def first_roll():
    # accepts nothing
    # returns the random integers between 1 and 12
    list = [roll_die() for num in range(13)]
    print(list)

def count_frequencey(dice, number):
    # accepts a list of 12 random integers and a target die
    # returns how often that target die occurs in the list
    occurances = 0
    for di in dice:
        if di == number:
            occurances += 1

    return occurances    

def find_mode(dice: list):
    # accepts a list of dice
    # uses count_frequencey(dice, die) to determine how often each die occurs
    # returns the mode
    modes = []
    for i in range(1,7):
        modes.append(count_frequencey(dice, i))
    
    return modes.index(max(modes)) + 1

        

def list_unmatched_dice(dice):
    # accepts a list of dice
    # determines which dice need rerolled
    # returns a list of indexes to reroll
    pass

def reroll_one(dice, index):
    # accepts a list of dice and an index
    # uses roll_die to reroll that index
    # returns a new list with that index rerolled
    pass

def reroll_many(dice):
    # accepts a list of dice
    # calls list_unmatched_dice() and reroll_one() to reroll each die != the mode
    # returns a list of rerolled dice
    pass
