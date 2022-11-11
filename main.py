import gym 
import numpy as np 
from semigradsarsa import SemiGradientSarsa
from maze import Maze


if __name__ == "__main__":
    env = Maze()
    model = SemiGradientSarsa(env, 1e-5, 0.9)
    env.reset()
    model.train(1)
    # policyRunner = policyEvolution(model.weights)



