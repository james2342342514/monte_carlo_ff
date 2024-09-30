import random
import numpy as np
from collections import defaultdict

def simulate_player_score(player, std_dev_factor=0.25):
    # Adjust standard deviation based on position and projected score
    std_dev = player['proj'] * std_dev_factor
    
    # Use a beta distribution for more realistic score distribution
    a, b = 4, 4  # shape parameters for beta distribution
    beta_sample = np.random.beta(a, b)
    
    # Scale and shift the beta sample to match the projected mean and calculated std dev
    simulated_score = player['proj'] + (beta_sample - 0.5) * std_dev * 2
    
    # Apply floor and ceiling
    simulated_score = max(player['floor'], min(player['ceiling'], simulated_score))
    
    return simulated_score

def simulate_game(team1, team2, current_score_team1, current_score_team2, num_simulations=10000):
    team1_wins = 0
    score_diff_sum = 0
    
    for _ in range(num_simulations):
        team1_score = current_score_team1 + sum(simulate_player_score(player) for player in team1)
        team2_score = current_score_team2 + sum(simulate_player_score(player) for player in team2)
        
        score_diff = team1_score - team2_score
        score_diff_sum += score_diff
        
        if score_diff > 0:
            team1_wins += 1
    
    win_probability = team1_wins / num_simulations
    avg_score_diff = score_diff_sum / num_simulations
    
    return win_probability, avg_score_diff

def get_position_breakdown(team):
    breakdown = defaultdict(float)
    for player in team:
        breakdown[player['position']] += player['proj']
    return dict(breakdown)

def generate_floor_ceiling(proj, position):
    if position == 'DEF':
        return max(0, proj - 10), proj + 15
    elif position == 'RB':
        return max(0, proj - 12), proj + 20
    elif position == 'WR':
        return max(0, proj - 10), proj + 25
    else:  # Default for other positions
        return max(0, proj - 10), proj + 20

# Define teams with more detailed player information including floors and ceilings
james = [
    {'name': 'T. Hill', 'proj': 20, 'position': 'WR', 'floor': 5, 'ceiling': 30},
    {'name': 'T. Lockett', 'proj': 15, 'position': 'WR', 'floor': 3, 'ceiling': 20},
    {'name': 'T. Pollard', 'proj': 15, 'position': 'RB', 'floor': 5, 'ceiling': 20},
]

zach = [
    {'name': 'D. Achane', 'proj': 20, 'position': 'RB', 'floor': 5, 'ceiling': 35},
    {'name': 'Miami DEF', 'proj': 5, 'position': 'DEF', 'floor': 0, 'ceiling': 20}
]

# Automatically generate floors and ceilings if not provided
for team in [james, zach]:
    for player in team:
        if 'floor' not in player or 'ceiling' not in player:
            player['floor'], player['ceiling'] = generate_floor_ceiling(player['proj'], player['position'])

# Current scores
current_score_team1 = 73.14
current_score_team2 = 96.64

# Run simulation
win_prob, avg_score_diff = simulate_game(james, zach, current_score_team1, current_score_team2)

print(f"James win probability: {win_prob:.2%}")
print(f"Zach win probability: {1-win_prob:.2%}")
print(f"Average score difference (James - Zach): {avg_score_diff:.2f}")

# Position breakdown
print("\nJames Position Breakdown:")
for pos, score in get_position_breakdown(james).items():
    print(f"{pos}: {score:.2f}")

print("\nZach Position Breakdown:")
for pos, score in get_position_breakdown(zach).items():
    print(f"{pos}: {score:.2f}")

# Print floors and ceilings
print("\nPlayer Floors and Ceilings:")
for team, name in [(james, "James"), (zach, "Zach")]:
    print(f"\n{name}'s Team:")
    for player in team:
        print(f"{player['name']} ({player['position']}): Floor = {player['floor']}, Ceiling = {player['ceiling']}")