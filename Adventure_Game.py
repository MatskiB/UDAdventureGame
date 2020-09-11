import time
import random
import fantasy_list

# Below is a function that helps print statements with a chosen time delay


def print_pause(statement, t):
    print(statement)
    time.sleep(t)

# This function works as an introduction


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.", 2)
    print_pause("Rumor has it that a wicked fairie is somewhere "
                "around here, and has been terrifying the nearby village.", 2)
    print_pause("In front of you is a house", 2)
    print_pause("To your right is a dark cave", 2)
    print_pause("In your hand you hold a trusty "
                "(but not very effective) dagger.", 2)


# This function gives the player a choice of different paths they can choose
# and then runs the relevant function for that


def path(backpack, monster):
    print_pause("Enter 1 to knock on the door of the house", 2)
    print_pause("Enter 2 to peer into the cave.", 2)
    response = input("What would you like to do?\n"
                     "(Please enter 1 or 2)\n")
    if response == "1":
        house(backpack, monster)
    elif response == "2":
        cave(backpack, monster)
    else:
        print_pause("Computer says no. Please try again", 2)
        path(backpack, monster)

# This is the fight scene with different scenarios


def fight(backpack, monster):
    if "sword" in backpack:
        answer = input("Would you like to (1) fight or (2) run away?\n")
        # This will lead to victory
        if answer == "1":
            print_pause("As the " + str(monster) + " moves to attack you, "
                        "you unsheath your new sword.", 2)
            print_pause("Your new sword shines brightly in your hand "
                        "as you brace yourself for the attack.", 2)
            print_pause("But the " + str(monster) + " takes one look at "
                        "your shiny new toy and runs away!", 2)
            print_pause("You have rid the town of the " + str(monster) +
                        ".", 2)
            play_again()
        # This will lead the player back to the original choice
        # but has no effect on the outcome of the game
        elif answer == "2":
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been followed.\n", 2)
            path(backpack, monster)
        else:
            print_pause("Please try this again", 2)
            fight(backpack, monster)
    else:
        # This path will give the player a choice to fight using their rusty
        # weapon or run away and find the sword
        print_pause("You feel a little unprepared for this, "
                    "what with only having a tiny dagger.", 2)
        answer = input("Would you like to (1) fight or (2) run away?\n")
        # This path leads to defeat
        if answer == "1":
            print_pause("You do your best...", 2)
            print_pause("But your dagger is no match for the " + str(monster) +
                        ".", 2)
            print_pause("You have been defeated.", 2)
            play_again()
        # This path saves the player and allows them to make a better choice
        elif answer == "2":
            print_pause("You run back into the open field. "
                        "Luckily, you don't seem to have been followed.\n", 2)
            path(backpack, monster)
        else:
            print_pause("Please try this again", 2)
            house(backpack, monster)


def house(backpack, monster):
    print_pause("You approach the door of the house.", 2)
    print_pause("You are about to knock when the door opens and "
                "out steps a " + str(monster) + ".", 2)
    print_pause("Eep! This is " + str(monster) + "'s house.", 2)
    print_pause("The " + str(monster) + " attacks you!", 2)
    fight(backpack, monster)


# Below functions handles what happens when
# the player chooses to go to the cave


def cave(backpack, monster):
    # This variable randomly assigns the weapon
    weapon = random.choice(fantasy_list.weapons)
    # This path handles cases where the player has returned to the cave
    # for some reason
    if "sword" in backpack:
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("You've been here before and gotten all the good stuff "
                    "It's just an empty cave now.", 2)
        print_pause("You walk back out to the field.\n", 2)
        path(backpack, monster)
    # By following this path, the player will discover their new weapon
    # and the programme will add it to the backpack list
    else:
        print_pause("You peer cautiously into the cave.", 2)
        print_pause("It turns out to be a very small cave.", 2)
        print_pause("Your eye catches a glint of metal behind a rock", 2)
        print_pause("You have found the magical " + str(weapon) + "!", 2)
        backpack.append("sword")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.", 2)
        print_pause("You run back out into the field.\n", 2)
        path(backpack, monster)

# This function allows the player to decided if they want to play again


def play_again():
    answer = input("Would you like to play again? (y/n)\n").lower()
    # This will end the game
    if answer == "n":
        print_pause("Thanks for playing! See you next time.", 2)
    # This will restart the game from scratch
    elif answer == "y":
        print_pause("Excellent! Restarting the game.\n", 2)
        play_game()
    else:
        print_pause("This was a simple question "
                    "Please try again.", 2)
        play_again()

# This function wraps everything into a simple play_game command


def play_game():
    backpack = []
    monster = random.choice(fantasy_list.monsters)
    intro()
    path(backpack, monster)

play_game()
