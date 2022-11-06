import numpy as np 

class SemiGradientSarsa():
    def __init__(self,env, alpha, eps):
        super(SemiGradientSarsa, self).__init__()
        self.env = env 
        self.alpha = alpha 
        self.epsilon = eps 

        self.QTable = np.zeros([1,4])


    def gradient_descent(self, start, gradient, learn_rate, max_iter, tol=0.01):
        steps = [start] # history tracking
        x = start

        for _ in range(max_iter):
            diff = learn_rate*gradient(x)
            if np.abs(diff)<tol:
                break
            x = x - diff
            steps.append(x) # history tracing

        return steps, x


    def train(self, episodes):
        pass


