import gym
from gym import spaces
import numpy as np
from dynamicTransition import dynTransition


class Maze(gym.Env):
  def __init__(self):
    # 0 is wall; 1 is floor 
    self.level = np.array([  
        [0,0,0,0,0,0,0,0,0,0],
        [0,3,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,4,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,2,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]])

    self.terminalState = ','.join(map(str, np.array([  
        [0,0,0,0,0,0,0,0,0,0],
        [0,2,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,4,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]).ravel())) 

    self.dangerState =','.join(map(str, np.array([  
        [0,0,0,0,0,0,0,0,0,0],
        [0,3,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,2,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]).ravel())) 

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
            print("Step.............",np.argwhere(self.level == 2), ac,self.currentState)
            next_state = self.h.getNextStateDynamically(self.currentState,ac)

            

            print("Cu",self.currentState)
            print("Ne",next_state)
            self.h.isFirstIter = False

            
            
            stringNextState = ','.join(map(str, next_state.ravel()))  

            # if(next_state == self.currentState).all():
            #     return next_state, -10, self.done, {}

            # If agent takes path to the left it falls into the hole i.e #4 and game is over
            if(stringNextState == self.dangerState):
                self.reset()
                return next_state, -5, self.done, {}
            # If agent hits terminal state
            if(stringNextState == self.terminalState):
                self.done = True
                self.reset()
                return next_state, 10, self.done, {}
            # All other steps agent gets -1    
            else:
                # print(next_state, -1, self.done)
                return next_state, -1, self.done, {}

