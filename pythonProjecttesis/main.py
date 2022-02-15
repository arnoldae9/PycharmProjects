import numpy as np
import random
from IPython.display import clear_output
import gym

enviroment = gym.make("Taxi-v2").env
enviroment.render()

print('Number of states: {}'.format(enviroment.observation_space.n))
print('Number of actions: {}'.format(enviroment.action_space.n))
