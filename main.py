import random
import time
from resources import (
    wheel,
    around_the_house,
    fictional_characters,
    food_and_drink,
    phrases,
    puzzles,
    consonants,
    vowels,
    player,
    spin_the_wheel,
    find_all_occurrences,
    flip_letters
)

print("WHEEL...")
time.sleep(1)
print("OF...")
time.sleep(1)
print("FORTUNE!")
time.sleep(1)
print(
      "\n"
      "Welcome to Wheel of Fortune! Lined up for you are 3 rounds, each with a unique puzzle, plus a bonus round. \n"
      "This game requires 3 players to play. \n"
)
time.sleep(1)

player_one = input("Player 1, please enter your name: ")
player_one = player.append([player_one, 0])

player_two = input("Player 2, please enter your name: ")
player_two = player.append([player_two, 0])

player_three = input("Player 3, please enter your name: ")
player_three = player.append([player_three, 0])
    
print("\n"
      "Are you ready?")
time.sleep(1)
print("\n"
      "Let's begin the first round.")
time.sleep(1)

random_category = random.choice(puzzles)
rand_int = random.randint(0, 4)
random_puzzle = random_category[rand_int]
random_puzzle = list(random_puzzle)

if random_category == around_the_house:
    random_category = "Around the House"
elif random_category == fictional_characters:
    random_category = "Fictional Characters"
elif random_category == food_and_drink:
    random_category = "Food and Drink"
elif random_category == phrases:
    random_category = "Phrases"

print("\n")
print(f"The category is: {random_category}")
print("And here is the puzzle: \n")

print(random_puzzle[1])
print(random_puzzle[0])

i = 0

while True:
    while i < len(player):
        current_player = player[i]
        if i > len(player):
            i = 0
    
        print(f"{current_player[0]}, it's your turn!")
        print(random_puzzle[1])
        action = input("Would you like to [spin] the wheel, [buy] a vowel, or [solve] the puzzle? ")
        
        if action == "spin":
            result = spin_the_wheel()
            print(f"{result}!")
            letter = input("Now, pick a letter: ")
            # ADD A FUNCTION TO REMOVE THAT LETTER FROM THE APPROPRIATE LIST SO IT DOESNT GET PICKED AGAIN
            # ALSO MAKE SURE THE LETTER PICKED IS A CONSONANT AND NOT A VOWEL (CAUSE YOU GOTTA PAY FOR THAT)

            if letter in random_puzzle[0]:
                indices = find_all_occurrences(random_puzzle, letter)
                occurrences = random_puzzle[0].count(letter)
                print(f"We have {occurrences} of that letter.")
                random_puzzle = flip_letters(random_puzzle, letter, indices)
            else:
                print("Sorry! There are none of those in the puzzle.")
                i += 1