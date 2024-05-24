import numpy as np
import random

#  simulation environment parameters
NUM_INTERSECTIONS = 4
GREEN_DURATION = 30  # Duration of green signal in seconds
YELLOW_DURATION = 3  # Duration of yellow signal in seconds
RED_DURATION = 30  # Duration of red signal in seconds
NUM_ACTIONS = 3

# Define traffic simulation environment
class TrafficSimulation:
    def __init__(self, num_intersections, green_duration, yellow_duration, red_duration):
        self.num_intersections = num_intersections
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.reset()

    def step(self, action):
        # Update traffic signal timings based on action
        if action == 7:  # Increase green duration
            self.current_state = np.minimum(self.current_state + self.green_duration, self.green_duration)
        elif action == 1:  # Decrease green duration
            self.current_state = np.maximum(self.current_state - self.green_duration, 0)

        # Simulate traffic flow
        self.traffic_density = np.random.uniform(0.1, 1, self.num_intersections)
        
        # Calculate reward based on traffic conditions
        reward = -np.sum(self.traffic_density)  # Negative reward for higher traffic density

        done = False

        return self.current_state, reward, done

    def reset(self):
        self.current_state = np.zeros(self.num_intersections, dtype=int)
        self.traffic_density = np.random.uniform(0.1, 1, self.num_intersections)
        return self.current_state

# Define reinforcement learning agent
class RLAgent:
    def __init__(self, num_actions, num_intersections, learning_rate=0.1, discount_factor=0.9, exploration_rate=0.1):
        self.num_actions = num_actions
        self.num_intersections = num_intersections
        self.Q_table = np.zeros((num_intersections, num_actions))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

    def select_action(self, state):
        state_index = self.get_state_index(state)
        if np.random.rand() < self.exploration_rate:
            return np.random.randint(self.num_actions)
        else:
            return np.argmax(self.Q_table[state_index])

    def update_Q_table(self, state, action, reward, next_state):
        state_index = self.get_state_index(state)
        next_state_index = self.get_state_index(next_state)
        best_next_action = np.argmax(self.Q_table[next_state_index])
        td_target = reward + self.discount_factor * self.Q_table[next_state_index, best_next_action]
        self.Q_table[state_index, action] += self.learning_rate * (td_target - self.Q_table[state_index, action])

    def get_state_index(self, state):
        return hash(tuple(state)) % self.num_intersections

def train_traffic_optimization(agent, sim_env, num_episodes=200, max_steps_per_episode=100):
    for episode in range(num_episodes):
        state = sim_env.reset()
        total_reward = 0

        for step in range(max_steps_per_episode):
            action = agent.select_action(state)
            next_state, reward, done = sim_env.step(action)
            agent.update_Q_table(state, action, reward, next_state)
            total_reward += reward
            state = next_state
        
        print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

def evaluate_trained_agent(agent, sim_env, num_episodes=10, max_steps_per_episode=100):
    for episode in range(num_episodes):
        state = sim_env.reset()
        total_reward = 0

        for step in range(max_steps_per_episode):
            action = agent.select_action(state)
            next_state, reward, done = sim_env.step(action)
            total_reward += reward
            state = next_state
        
        print(f"Evaluation Episode: {episode + 1}, Total Reward: {total_reward}")

if __name__ == "__main__":
    sim_env = TrafficSimulation(NUM_INTERSECTIONS, GREEN_DURATION, YELLOW_DURATION, RED_DURATION)
    agent = RLAgent(NUM_ACTIONS, NUM_INTERSECTIONS)

    print("Training the agent...")
    train_traffic_optimization(agent, sim_env)
    
    print("Evaluating the trained agent...")
    evaluate_trained_agent(agent, sim_env)
