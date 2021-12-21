#!/usr/bin/env python

with open('input') as f:
    player_one_location = int(f.readline().strip().split()[-1]) - 1
    player_two_location = int(f.readline().strip().split()[-1]) - 1

die_value = 0
die_rolled = 0

player_one_score = 0
player_two_score = 0

while True:
    # Get the next three rolls of the die
    roll_one = die_value + 1
    die_value = (die_value + 1) % 100
    roll_two = die_value + 1
    die_value = (die_value + 1) % 100
    roll_three = die_value + 1
    die_value = (die_value + 1) % 100

    die_rolled += 3

    # Get the new location of the player
    player_one_location = (player_one_location + roll_one + roll_two + roll_three) % 10
    player_one_score += player_one_location + 1

    # print(f'Player one is one square {player_one_location + 1}, score is {player_one_score}')

    if player_one_score >= 1000:
        break

    # Get the next three rolls of the die
    roll_one = die_value + 1
    die_value = (die_value + 1) % 100
    roll_two = die_value + 1
    die_value = (die_value + 1) % 100
    roll_three = die_value + 1
    die_value = (die_value + 1) % 100

    die_rolled += 3

    # Get the new location of the player
    player_two_location = (player_two_location + roll_one + roll_two + roll_three) % 10
    player_two_score += player_two_location + 1

    # print(f'Player two is one square {player_two_location + 1}, score is {player_two_score}')

    if player_two_score >= 1000:
        break

print(f'Player one score: {player_one_score}, player two score: {player_two_score}')
print(f'Number of rolls: {die_rolled}')
print(min(player_one_score, player_two_score) * die_rolled)