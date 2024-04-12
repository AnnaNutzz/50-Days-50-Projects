"""
Build a multiplayer gambling game like blackjack but with dice numbers and 
when a player rolls '1', their total should be 0
"""


import random

def roll():
    roll = random.randint(1,6)

    return roll

while True:
    players = input("Number of players?? (2-4): ")
    
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("2-4 players only")
    else:
        print("invalid")


max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    
    for play_index in range(players):
        print(f"\n Player {play_index+1} has started \n")
        print(f"Total score is : {player_score[play_index]} \n")

        current_score = 0

        while True:
            should_roll = input("Rolling??: ")
            if should_roll.lower() != 'y':
                break

            value = roll()

            if value == 1:
                print("You rolled 1!")
                current_score = 0
                break
            else: 
                current_score += value
                print(f"You rolled a {value}")

        player_score[play_index] += current_score
        print("total score is: ", player_score[play_index])

max_score = max(player_score)
winner = player_score.index(max_score)

print(f"Player {winner} has won with the score of {max_score}")