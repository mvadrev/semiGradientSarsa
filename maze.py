import gym
from gym import spaces
import numpy as np
from dynamicTransition import dynTransition


class Maze(gym.Env):
  def __init__(self):
    # 0 is wall; 1 is floor  #3 is goal state #4 is danger state #2 player
    self.level = np.array([  
        [0,0,0,0,0,0,0,0,0,0],
        [0,3,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,1,1,1,0],
        [0,4,1,1,1,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,2,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]])

    self.terminalState = np.array([  
        [0,0,0,0,0,0,0,0,0,0],
        [0,2,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,1,1,1,0],
        [0,4,1,1,1,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]])

    self.dangerState = np.array([  
        [0,0,0,0,0,0,0,0,0,0],
        [0,3,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,0,0,0,1,1,1,0],
        [0,2,1,1,1,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
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

        while(self.done == False):
            ac = self.actionMap[action]

            # Get bext state
            next_state = self.h.getNextStateDynamically(self.currentState,ac)

            # DO if done is false
            self.h.isFirstIter = False
            # If agent takes path to the left it falls into the hole i.e #4 and game is over
            if(next_state == self.dangerState).all():
                self.reset()
                return next_state, -50, self.done, {}
            # If agent hits terminal state
            if(next_state == self.terminalState).all():
                self.done = True
                self.reset()
                return next_state, 10, self.done, {}
            # All other steps agent gets -1    
            else:
                # print(next_state, -1, self.done)
                return next_state, -1, self.done, {}

