# Fantasy Football Monte Carlo Simulation

## Project Overview

This project implements a sophisticated Monte Carlo simulation for fantasy football matchups. It uses advanced statistical techniques to provide accurate win probabilities and score projections.

## Key Features

- **Beta Distribution Modeling**: Utilizes beta distribution for more realistic player score simulations.
- **Dynamic Floor and Ceiling**: Incorporates player-specific and position-based performance limits.
- **Flexible Team Composition**: Supports various team structures and player positions.
- **Large-scale Simulation**: Runs thousands of game simulations for statistically significant results.

## Code Highlights

```python
def simulate_player_score(player, std_dev_factor=0.25):
    std_dev = player['proj'] * std_dev_factor
    beta_sample = np.random.beta(4, 4)
    simulated_score = player['proj'] + (beta_sample - 0.5) * std_dev * 2
    return max(player['floor'], min(player['ceiling'], simulated_score))
```

## Outputs

- Win probabilities for each team
- Average score difference
- Position-based team breakdowns
- Player-specific floor and ceiling values

## 🚧 Future Enhancements

- Incorporate player correlations (e.g., QB-WR stacks)
- Add support for different scoring systems (PPR, Half-PPR, etc.)
- Implement a user-friendly interface for inputting teams and viewing results

## 📝 How to Use

1. Clone the repository
2. Update the player data in the script with your fantasy football matchup information
3. Run the script to get simulation results
