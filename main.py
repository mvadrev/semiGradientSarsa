import gym 
import numpy as np 
from semigradsarsa import SemiGradientSarsa
from maze import Maze


if __name__ == "__main__":
    # model = SemiGradientSarsa(1,1)
    env = Maze()
    model = SemiGradientSarsa(env, 1, 1)
    env.reset()
    # print(env.currentState)
    # next, rew, done, meta = env.step(1)
    # print(next)
    model.train(10)


