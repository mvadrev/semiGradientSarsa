import gym 
import numpy as np 
from semigradsarsa import SemiGradientSarsa
from maze import Maze


if __name__ == "__main__":

    env = Maze()
    alg = SemiGradientSarsa(env, 0.01, 0.1)
    env.reset()
    env.step(1)

