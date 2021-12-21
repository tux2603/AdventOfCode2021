from functools import lru_cache

possible_rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

@lru_cache(maxsize=None)
def get_winning_positions(player_positions: tuple, player_scores: tuple, turn: int):
    player_wins = [0, 0]

    for key, value in possible_rolls.items():
        new_position = (player_positions[turn] + key) % 10
        new_score = player_scores[turn] + new_position + 1

        if new_score >= 21:
            player_wins[turn] += value
        
        else:
            new_player_positions = list(player_positions)
            new_player_positions[turn] = new_position
            new_player_scores = list(player_scores)
            new_player_scores[turn] = new_score

            new_wins = get_winning_positions(tuple(new_player_positions), tuple(new_player_scores), (turn + 1) % 2)
            player_wins[0] += new_wins[0] * value
            player_wins[1] += new_wins[1] * value

    return player_wins


if __name__ == '__main__':
    with open('input') as f:
        player_one_location = int(f.readline().strip().split()[-1]) - 1
        player_two_location = int(f.readline().strip().split()[-1]) - 1

    winning_positions = get_winning_positions((player_one_location, player_two_location), (0, 0), 0)
    print(winning_positions)
    print(max(winning_positions))
