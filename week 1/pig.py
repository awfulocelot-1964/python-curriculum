# import random
import random


# define a function for a dice roll between 1 and 5
def roll():
    min_value = 1
    max_value = 5

    roll_value = random.randint(min_value, max_value)

    return roll_value


# create a while loop to get a number of characters
while True:
    player_count = input("enter the number of players: ")
    player_count = int(player_count)
    if 1 < player_count < 5:
        break
    else:
        print("must be between 2 and 4 players.")

print(player_count)

# define a variable for player scores:
# which one?

max_scores = 50

# list comprehension

player_scores = [0 for _ in range(player_count)]
print(player_scores)

# game loop
while max(player_scores) < max_scores:
    current_scores = 0

    for player_index in range(player_count):
        print(f"it is player {player_index + 1}'s turn!")

        while True:
            # asking if the player wants to roll:
            player_roll = input("would you like to roll (y/n)? ")

            if player_roll != "y":
                print("skipping your roll.")
                break

            elif player_roll.lower() == "y":
                roll_value = roll()
                if roll_value == 1:
                    print("you rolled a 1! turn over.")
                    current_scores = 0
                    break

                else:
                    current_scores += roll_value
                    print(f"you rolled a {roll_value}!")

                print(f"your score is {current_scores}.")

        player_scores[player_index] += current_scores

    print(f"total score: {player_scores[player_index]}")
