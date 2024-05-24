# Smart-City-Traffic-Optimization-Using-Reinforcement-Learning

## Environment Setup
# Parameters and Constants:
NUM_INTERSECTIONS: Number of intersections in the simulation.

GREEN_DURATION: Duration of the green light in seconds.

YELLOW_DURATION: Duration of the yellow light in seconds.

RED_DURATION: Duration of the red light in seconds.

NUM_ACTIONS: Number of possible actions the agent can take (3 in this case).

## Traffic Simulation Environment
# TrafficSimulation Class:

Initialization (__init__ method): Sets up the environment with the given parameters and resets the state.

Step Function (step method):

Takes an action to either increase or decrease the green light duration or maintain it.

Simulates the traffic flow by updating traffic density with random values between 0.1 and 1.

Computes a reward based on the traffic density (negative reward for higher density).

Returns the new state, reward, and a boolean indicating if the simulation is done (always False in 
this case).

Reset Function (reset method): Resets the traffic signal durations and traffic density to initial values.

## Reinforcement Learning Agent

# RLAgent Class:
Initialization (__init__ method): Sets up the Q-table and learning parameters (learning rate, discount factor, exploration rate).

Select Action (select_action method): Chooses an action based on the exploration-exploitation trade-off:

With probability equal to exploration_rate, selects a random action.

Otherwise, selects the action with the highest Q-value for the current state.

Update Q-Table (update_Q_table method): Updates the Q-value for a given state-action pair based on the reward received and the estimated future rewards.

State Index (get_state_index method): Computes an index for the state to use in the Q-table (hashing the state tuple).

# Training and Evaluation Functions
## Training Function (train_traffic_optimization):
Runs the training process for a specified number of episodes.

For each episode, the environment is reset, and the agent interacts with the environment for a maximum number of steps.

At each step, the agent selects an action, the environment returns the new state and reward, and the agent updates the Q-table.

The total reward for each episode is printed.
# Evaluation Function (evaluate_trained_agent):

Evaluates the trained agent by running the simulation for a specified number of episodes without updating the Q-table.

Prints the total reward for each evaluation episode.
#Main Execution

Main Execution Block:
Initializes the simulation environment and the RL agent.

Trains the agent using the train_traffic_optimization function.

Evaluates the trained agent using the evaluate_trained_agent function.
#Summary:
Simulation Environment: Models traffic signal control at multiple intersections.

Reinforcement Learning Agent: Learns to control the traffic signals to minimize traffic density using Q-learning.

Training: The agent learns through interaction with the environment over multiple episodes.

Evaluation: The performance of the trained agent is assessed.

This code sets up a framework for using reinforcement learning to optimize traffic signal timings, potentially leading to reduced traffic congestion.
