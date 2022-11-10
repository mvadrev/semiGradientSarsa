import numpy as np 

class SemiGradientSarsa():
    def __init__(self,env, alpha, eps):
        super(SemiGradientSarsa, self).__init__()
        self.env = env 
        self.alpha = alpha 
        self.epsilon = eps 
        self.weights = np.zeros([7,])
        self.done = False
        self.terminalState = ','.join(map(str, np.array([  
        [0,0,0,0,0,0,0,0,0,0],
        [0,2,1,1,1,1,1,1,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,4,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0]]).ravel())) 

    def generateStateVector(self, state, action):
        player_pos = np.argwhere(state)

        initial_array = [1,]
        initial_array.append(state[0][0])
        initial_array.append(state[0][1])
        initial_array.append(state[0][0] ** 2)
        initial_array.append(state[0][1] ** 2)
        initial_array.append(state[0][0] + action)
        initial_array.append(state[0][1] + action)
        return np.array(initial_array)



    def updateWeightSemiGradientSarsa(self, weights, vHat, vHatPrime, reward, alpha, gamma, isTerminal, feat_vector_s):

        if (isTerminal):
            w = weights + (alpha * (reward- vHat) * feat_vector_s)
            weights + (0.1 * (-1 + 0.9*(vHatPrime) - vHat)) * feat_vector_s
            return w
        else:
            w = weights + (alpha * (reward + gamma*(vHatPrime) - vHat)) * feat_vector_s
            print("New weight is", w)
            return w 

    def isTerminalState(self, currentState):
        new = np.ravel(currentState)
        stringCurrentState = ','.join(map(str, new))  
        if(stringCurrentState == self.terminalState):
            return True
        else:
            return False

    def epsilonGreedy(self, state, action, weight ):
        actions = [0,1,2,3]
        if(np.random.random() < self.epsilon):
            randomChoiceAction = np.random.choice(actions)
            return randomChoiceAction
        else: 
            print("Hello exploiting", [np.dot(weight, self.generateStateVector(state, actions[i])) for i in range(actions)])
            index = np.argmax(np.array([np.dot(weight, self.generateStateVector(state, actions[i])) for i in range(actions)]))
            return index
            


    def train(self,timesteps):
        initialState = self.env.reset()
        # print("States before1", initialState)

        for timestep in range(timesteps):
             while (self.done == False):
                action = self.epsilonGreedy(initialState, 0, self.weights)
                print("Action is ", action)
                # print("States before", initialState)
                next_state, reward, done, meta = self.env.step(action)
                print("Reward is..", reward)
                # print("States next", next_state)
                position_player_s = np.argwhere(initialState == 2)
                print("S player", position_player_s)

                position_player_sPrime = np.argwhere(next_state == 2)
                print("Sprime player", position_player_sPrime)

                feat_vector_s =  self.generateStateVector(position_player_s, action)
                feat_vector_sPrime =  self.generateStateVector(position_player_sPrime, action)

                print("Feature vactors", feat_vector_s, feat_vector_sPrime)
                print("Weights", self.weights)

                vHat = np.dot(self.weights , feat_vector_s)
                vHatPrime = np.dot(self.weights , feat_vector_sPrime)
                print("vhat is", vHat)

                updatedWeight = self.updateWeightSemiGradientSarsa(self.weights,vHat, vHatPrime, reward, self.alpha, self.epsilon, self.isTerminalState(next), feat_vector_s)
                self.weights = updatedWeight
                
                initialState = next_state
                self.env.currentState =  next_state
                if(self.isTerminalState(next_state)):
                    self.done = True
                    print(self.done)
                    print("====================== Terminal State ========================")
                    # break



