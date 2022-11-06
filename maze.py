import gym
from gym import spaces
import numpy as np
from dynamicTransition import dynTransition


class Maze(gym.Env):
  def __init__(self):
    # 0 is wall; 1 is floor 
    self.level = np.array([  
        [0,0,3,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,2,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]])
    self.currentState = self.level
    self.action_space = spaces.Discrete(4)
    self.observation_space = spaces.Box(0, 5, shape=(1,25), dtype='int')
    self.actionMap = {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
    self.observation_space = spaces.Box(0, 4, shape=(10,10), dtype='int')
    self.done = False
    self.h = dynTransition(1,0, True)
  

    # Initialize random policy
    self.initialPolicy = np.zeros([10, 10])

  def reset(self):
        self.currentState = self.level
        self.done = False
        return self.currentState

  def step(self, action): 
        ac = self.actionMap[action]
        print("Step.............",np.argwhere(self.level == 3), ac,)
        next_state = self.h.getNextStateDynamically(self.currentState, ac)

  def epsilonGreedy(self, currentState):
        randomProb = np.random.random()
        stateIndex = self.stateTable.index(currentState)
        if (randomProb > self.epsilon):
            print("exploring...")
            actions = [0,1,2,3]
            randomChoiceAction = np.random.choice(actions)
            return randomChoiceAction
        else:
            print("exploiting.. Choosing best action from Qtable", np.argmax(self.stateTable[stateIndex]))
            return np.argmax(self.stateTable[stateIndex]) # check this later