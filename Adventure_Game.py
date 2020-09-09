import time
import random
import fantasy_list

# Below is a function that helps print statements with a chosen time delay


def print_pause(statement):
    print(statement)
    time.sleep(2)

# This function works as an introduction


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house")
    print_pause("To your right is a dark cave")
    print_pause("In your hand you hold a trusty "
                "(but not very effective) dagger.")


# This function gives the player a choice of different paths they can choose
# and then runs the relevant function for that


def path(backpack):
    print_pause("Enter 1 to knock on the door of the house")
    print_pause("Enter 2 to peer into the cave.")
    response = input("What would you like to do?\n"
                     "(Please enter 1 or 2)\n")
    if "1" in response:
        house(backpack)
    elif "2" in response:
        cave(backpack)
    else:
        path(backpack)


# This function handles what happens if the player chooses to go to the house


def house(backpack):
    # This variable randomly assigns an opponent
    monster = random.choice(fantasy_list.monsters)
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and "
                "out steps a " + str(monster) + ".")
    print_pause("Eep! This is " + str(monster) + "'s house.")
    print_pause("The " + str(monster) + " attacks you!")
    # This path assumes the player has visited the cave already
    if "sword" in backpack:
        answer = input("Would you like to (1) fight or (2) run away?\n")
        # This will lead to victory
        if "1" in answer:
            print_pause("As the "+ str(monster) + " moves to attack you, "
                        "you unsheath your new sword.")
            print_pause("Your new sword shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause("But the " + str(monster) + " takes one look at "
                        "your shiny new toy and runs away!")
            print_pause("You have rid the town of the " + str(monster) + ".")
            play_again()
        # This will lead the player back to the original choice
        # but has no effect on the outcome of the game
        if "2" in answer:
            print_pause("You run back into the field. "
                        "Luckily, you don't seem to have been followed.\n")
            path(backpack)
    else:
        # This path will give the player a choice to fight using their rusty
        # weapon or run away and find the sword
        print_pause("You feel a little unprepared for this, "
                    "what with only having a tiny dagger.")
        answer = input("Would you like to (1) fight or (2) run away?\n")
        # This path leads to defeat
        if "1" in answer:
            print_pause("You do your best...")
            print_pause("But your dagger is no match for the " + str(monster) +
                        ".")
            print_pause("You have been defeated.")
            play_again()
        # This path saves the player and allows them to make a better choice
        if "2" in answer:
            print_pause("You run back into the open field. "
                        "Luckily, you don't seem to have been followed.\n")
            path(backpack)

# Below functions handles what happens when the player chooses to go to the cave


def cave(backpack):
    # This variable randomly assigns the weapon
    weapon = random.choice(fantasy_list.weapons)
    # This path handles cases where the player has resturned to the cave
    # for some reason
    if "sword" in backpack:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before and gotten all the good stuff "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        path()
    # By following this path, the player will discover their new weapon
    # and the programme will add it to the backpack list
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock")
        print_pause("You have found the magical " + str(weapon) + "!")
        backpack.append("sword")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You run back out into the field.\n")
        path(backpack)

# This function allows the player to decided if they want to play again


def play_again():
    answer = input("Would you like to play again? (y/n)\n")
    # This will end the game
    if "n" in answer:
        print_pause("Thanks for playing! See you next time.")
    # This will restart the game from scratch
    if "y" in answer:
        print_pause("Excellent! Restarting the game.\n")
        play_game()

# This function wraps everything into a simple play_game command


def play_game():
    backpack = []
    intro()
    path(backpack)

play_game()
