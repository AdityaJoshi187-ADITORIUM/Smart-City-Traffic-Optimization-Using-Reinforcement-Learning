# Smart-City-Traffic-Optimization-Using-Reinforcement-Learnig

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


# SAMPLE OUTPUT

Training the agent...
Episode: 1, Total Reward: -224.66139592045948
Episode: 2, Total Reward: -218.34609708979673
Episode: 3, Total Reward: -219.56562272258506
Episode: 4, Total Reward: -223.65576866906449
Episode: 5, Total Reward: -217.41373661713808
Episode: 6, Total Reward: -224.02455140149024
Episode: 7, Total Reward: -216.7984742867231
Episode: 8, Total Reward: -221.91930542180285
Episode: 9, Total Reward: -226.80272792188845
Episode: 10, Total Reward: -221.70439694817244
Episode: 11, Total Reward: -217.96698366452028
Episode: 12, Total Reward: -214.26715344184927
Episode: 13, Total Reward: -223.07921711804198
Episode: 14, Total Reward: -222.60668935504813
Episode: 15, Total Reward: -231.4275581642
Episode: 16, Total Reward: -220.6286790235501
Episode: 17, Total Reward: -217.64178927982866
Episode: 18, Total Reward: -224.05474597263216
Episode: 19, Total Reward: -218.88132512517888
Episode: 20, Total Reward: -216.8790588429281
Episode: 21, Total Reward: -215.64239946856938
Episode: 22, Total Reward: -226.50689493171984
Episode: 23, Total Reward: -223.19963711295506
Episode: 24, Total Reward: -220.1697757420411
Episode: 25, Total Reward: -221.84267684652582
Episode: 26, Total Reward: -208.38156033648406
Episode: 27, Total Reward: -219.44808265071092
Episode: 28, Total Reward: -223.2154570828991
Episode: 29, Total Reward: -219.14167326769007
Episode: 30, Total Reward: -221.55959938055
Episode: 31, Total Reward: -220.66931220204782
Episode: 32, Total Reward: -222.1038985201279
Episode: 33, Total Reward: -222.6288266863597
Episode: 34, Total Reward: -226.93311840238633
Episode: 35, Total Reward: -230.39146494167247
Episode: 36, Total Reward: -220.67831048951473
Episode: 37, Total Reward: -220.27899657562727
Episode: 38, Total Reward: -220.8856011431364
Episode: 39, Total Reward: -224.7001922222747
Episode: 40, Total Reward: -229.89447387620726
Episode: 41, Total Reward: -215.24632531229395
Episode: 42, Total Reward: -221.8695210421747
Episode: 43, Total Reward: -218.24240720347387
Episode: 44, Total Reward: -220.26561367869763
Episode: 45, Total Reward: -230.13737172312233
Episode: 46, Total Reward: -219.47176315012462
Episode: 47, Total Reward: -238.66718552670923
Episode: 48, Total Reward: -214.59315895146827
Episode: 49, Total Reward: -221.91548866656652
Episode: 50, Total Reward: -217.0960253681897
Episode: 51, Total Reward: -218.02341636730716
Episode: 52, Total Reward: -217.62682489880345
Episode: 53, Total Reward: -213.01939471878126
Episode: 54, Total Reward: -230.15196223499976
Episode: 55, Total Reward: -221.03382736191222
Episode: 56, Total Reward: -222.68233186302837
Episode: 57, Total Reward: -215.76690583212604
Episode: 58, Total Reward: -218.2225810370746
Episode: 59, Total Reward: -214.65633855383152
Episode: 60, Total Reward: -223.29861435867755
Episode: 61, Total Reward: -218.80503503488566
Episode: 62, Total Reward: -220.9938762598988
Episode: 63, Total Reward: -215.86931852250223
Episode: 64, Total Reward: -207.01461252589272
Episode: 65, Total Reward: -229.118295570961
Episode: 66, Total Reward: -212.86605765596082
Episode: 67, Total Reward: -220.99791113293597
Episode: 68, Total Reward: -223.51757634116274
Episode: 69, Total Reward: -222.2542459215178
Episode: 70, Total Reward: -209.02831980644802
Episode: 71, Total Reward: -222.3156710486609
Episode: 72, Total Reward: -212.8794315728084
Episode: 73, Total Reward: -226.302076535594
Episode: 74, Total Reward: -221.75920963667454
Episode: 75, Total Reward: -218.6212366937139
Episode: 76, Total Reward: -227.15668787457656
Episode: 77, Total Reward: -221.22274701477698
Episode: 78, Total Reward: -227.16657338329253
Episode: 79, Total Reward: -224.76797164876822
Episode: 80, Total Reward: -218.37100216187542
Episode: 81, Total Reward: -215.52731033869946
Episode: 82, Total Reward: -220.81072968430163
Episode: 83, Total Reward: -214.65272957473087
Episode: 84, Total Reward: -216.42405295757536
Episode: 85, Total Reward: -213.03072761006115
Episode: 86, Total Reward: -219.19076563351177
Episode: 87, Total Reward: -219.0350652982437
Episode: 88, Total Reward: -218.74978133429877
Episode: 89, Total Reward: -223.457159994906
Episode: 90, Total Reward: -218.32471567641446
Episode: 91, Total Reward: -217.37497989370559
Episode: 92, Total Reward: -223.41417751304314
Episode: 93, Total Reward: -215.38484682190727
Episode: 94, Total Reward: -225.03508539094534
Episode: 95, Total Reward: -220.175626139912
Episode: 96, Total Reward: -216.31538599973436
Episode: 97, Total Reward: -221.0744698903063
Episode: 98, Total Reward: -220.43850627917348
Episode: 99, Total Reward: -221.3396678007509
Episode: 100, Total Reward: -225.65486911910696
Episode: 101, Total Reward: -217.9245342159985
Episode: 102, Total Reward: -222.35972763844293
Episode: 103, Total Reward: -219.11911767346186
Episode: 104, Total Reward: -220.33339612573073
Episode: 105, Total Reward: -221.97857586032347
Episode: 106, Total Reward: -223.30423139230146
Episode: 107, Total Reward: -223.41839932826755
Episode: 108, Total Reward: -219.86306845271008
Episode: 109, Total Reward: -220.57570215088694
Episode: 110, Total Reward: -221.10679097830592
Episode: 111, Total Reward: -222.4462276085747
Episode: 112, Total Reward: -214.3998089611062
Episode: 113, Total Reward: -221.06273445239404
Episode: 114, Total Reward: -208.79823343309133
Episode: 115, Total Reward: -218.28686123407263
Episode: 116, Total Reward: -219.5114976148025
Episode: 117, Total Reward: -219.70760354642817
Episode: 118, Total Reward: -222.26904551950457
Episode: 119, Total Reward: -214.07202067658744
Episode: 120, Total Reward: -215.19715523139644
Episode: 121, Total Reward: -219.74490800511177
Episode: 122, Total Reward: -227.99071111146603
Episode: 123, Total Reward: -213.41150265981688
Episode: 124, Total Reward: -218.3320312601116
Episode: 125, Total Reward: -224.64200328473368
Episode: 126, Total Reward: -216.54230561685497
Episode: 127, Total Reward: -220.51584953191167
Episode: 128, Total Reward: -215.7253720747039
Episode: 129, Total Reward: -213.0853581024589
Episode: 130, Total Reward: -214.48809007432675
Episode: 131, Total Reward: -228.06699879751415
Episode: 132, Total Reward: -210.80706056712097
Episode: 133, Total Reward: -217.2161433971787
Episode: 134, Total Reward: -225.7393470963271
Episode: 135, Total Reward: -218.6319287604005
Episode: 136, Total Reward: -220.14948146078115
Episode: 137, Total Reward: -222.6304810555779
Episode: 138, Total Reward: -226.35584539101828
Episode: 139, Total Reward: -215.81221923575592
Episode: 140, Total Reward: -219.9881365496993
Episode: 141, Total Reward: -218.76096225541812
Episode: 142, Total Reward: -224.65908055374877
Episode: 143, Total Reward: -226.96822638333586
Episode: 144, Total Reward: -218.26646144197542
Episode: 145, Total Reward: -228.3308397723567
Episode: 146, Total Reward: -222.20875420336753
Episode: 147, Total Reward: -221.9135180972402
Episode: 148, Total Reward: -224.10425769243557
Episode: 149, Total Reward: -218.56258100892532
Episode: 150, Total Reward: -222.0638515800021
Episode: 151, Total Reward: -226.28476607465808
Episode: 152, Total Reward: -217.49376790335876
Episode: 153, Total Reward: -221.16010343643697
Episode: 154, Total Reward: -217.78077720458793
Episode: 155, Total Reward: -224.9259185196553
Episode: 156, Total Reward: -217.73610092580216
Episode: 157, Total Reward: -218.52888943141022
Episode: 158, Total Reward: -215.24429402289203
Episode: 159, Total Reward: -218.4682898932997
Episode: 160, Total Reward: -213.68146290598395
Episode: 161, Total Reward: -224.71489010278947
Episode: 162, Total Reward: -221.55038008530087
Episode: 163, Total Reward: -215.70139796580654
Episode: 164, Total Reward: -207.9926353696919
Episode: 165, Total Reward: -231.47109056618484
Episode: 166, Total Reward: -211.6969945977434
Episode: 167, Total Reward: -227.34738843484774
Episode: 168, Total Reward: -219.30574932947286
Episode: 169, Total Reward: -215.76235024106794
Episode: 170, Total Reward: -224.948545942736
Episode: 171, Total Reward: -221.99257221577668
Episode: 172, Total Reward: -221.47381557795202
Episode: 173, Total Reward: -216.00330659253476
Episode: 174, Total Reward: -216.10976571221644
Episode: 175, Total Reward: -225.4877580212062
Episode: 176, Total Reward: -217.10041153635368
Episode: 177, Total Reward: -220.91379419097865
Episode: 178, Total Reward: -222.8683852666162
Episode: 179, Total Reward: -221.39413742077653
Episode: 180, Total Reward: -230.17574518099423
Episode: 181, Total Reward: -223.405514075192
Episode: 182, Total Reward: -213.505347844925
Episode: 183, Total Reward: -224.50289864738457
Episode: 184, Total Reward: -225.7534412425655
Episode: 185, Total Reward: -214.8580368799619
Episode: 186, Total Reward: -226.79299353490052
Episode: 187, Total Reward: -222.0615398455291
Episode: 188, Total Reward: -225.87945362795077
Episode: 189, Total Reward: -225.0621134485838
Episode: 190, Total Reward: -221.82056778035422
Episode: 191, Total Reward: -221.98408386280664
Episode: 192, Total Reward: -226.13541746998936
Episode: 193, Total Reward: -226.79817070723956
Episode: 194, Total Reward: -227.78175910740052
Episode: 195, Total Reward: -223.37687868148583
Episode: 196, Total Reward: -225.20328318643166
Episode: 197, Total Reward: -211.9032807379367
Episode: 198, Total Reward: -221.3233229646783
Episode: 199, Total Reward: -220.671242026116
Episode: 200, Total Reward: -221.4473702268628
Evaluating the trained agent...
Evaluation Episode: 1, Total Reward: -221.95159079949087
Evaluation Episode: 2, Total Reward: -223.51990401716498
Evaluation Episode: 3, Total Reward: -224.2885003211126
Evaluation Episode: 4, Total Reward: -211.61122497028992
Evaluation Episode: 5, Total Reward: -210.30991378645325
Evaluation Episode: 6, Total Reward: -225.75465863049124
Evaluation Episode: 7, Total Reward: -222.9357456356156
Evaluation Episode: 8, Total Reward: -223.47665683326625
Evaluation Episode: 9, Total Reward: -217.96638133114877
Evaluation Episode: 10, Total Reward: -217.22489677173687
