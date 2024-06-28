# 🚦🚦🚦Traffic Signal Optimization with Reinforcement Learning🚥🚥🚥

This project simulates a traffic signal control system using reinforcement learning to optimize the timing of traffic signals at multiple intersections. The goal is to minimize traffic congestion by adjusting the duration of green, yellow, and red signals based on the current traffic conditions.

## Project Structure🛠

- `TrafficSimulation` class: Defines the traffic simulation environment.
- `RLAgent` class: Defines the reinforcement learning agent.
- Training and evaluation functions: Train and evaluate the RL agent on the traffic simulation environment.

## Simulation Environment Parameters🚦

- **NUM_INTERSECTIONS**: Number of intersections in the simulation (default: 4).
- **GREEN_DURATION**: Duration of the green signal in seconds (default: 30).
- **YELLOW_DURATION**: Duration of the yellow signal in seconds (default: 3).
- **RED_DURATION**: Duration of the red signal in seconds (default: 30).
- **NUM_ACTIONS**: Number of actions the agent can take (default: 3).

## Classes and Methods

### `TrafficSimulation`🚘

- `__init__(self, num_intersections, green_duration, yellow_duration, red_duration)`: Initializes the simulation environment with the specified parameters.
- `step(self, action)`: Updates traffic signal timings based on the action and simulates traffic flow. Returns the new state, reward, and whether the episode is done.
- `reset(self)`: Resets the simulation environment to the initial state. Returns the initial state.

### `RLAgent`🤖

- `__init__(self, num_actions, num_intersections, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1)`: Initializes the RL agent with the specified parameters.
- `select_action(self, state)`: Selects an action based on the current state using an epsilon-greedy policy.
- `update_Q_table(self, state, action, reward, next_state)`: Updates the Q-table based on the received reward and next state.
- `get_state_index(self, state)`: Maps a state to a corresponding index in the Q-table.

### Training and Evaluation Functions

- `train_traffic_optimization(agent, sim_env, num_episodes=200, max_steps_per_episode=100)`: Trains the RL agent on the traffic simulation environment.
- `evaluate_trained_agent(agent, sim_env, num_episodes=10, max_steps_per_episode=100)`: Evaluates the performance of the trained RL agent.

## Usage

1. Initialize the traffic simulation environment and the RL agent.
2. Train the agent using the `train_traffic_optimization` function.
3. Evaluate the trained agent using the `evaluate_trained_agent` function.

```python
if __name__ == "__main__":
    sim_env = TrafficSimulation(NUM_INTERSECTIONS, GREEN_DURATION, YELLOW_DURATION, RED_DURATION)
    agent = RLAgent(NUM_ACTIONS, NUM_INTERSECTIONS)

    print("Training the agent...")
    train_traffic_optimization(agent, sim_env)
    
    print("Evaluating the trained agent...")
    evaluate_trained_agent(agent, sim_env)
```

## Requirements

- `numpy`

## Installation⚓

Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/AdityaJoshi187-ADITORIUM/traffic-signal-optimization.git
cd traffic-signal-optimization
```

**Run the application**:🏳
    ```bash
    python app.py
    ```

**Install the dependencies**:
    ```bash
    pip install numpy
    ```
### License

  This project is licensed under the MIT License.
