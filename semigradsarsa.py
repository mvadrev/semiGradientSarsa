import numpy as np 
import seaborn as sns


class SemiGradientSarsa():
    def __init__(self,env, alpha, eps):
        super(SemiGradientSarsa, self).__init__()
        self.env = env 
        self.alpha = alpha 
        self.epsilon = eps 
        self.weights = np.zeros([11,])
        self.done = False
        self.policy = np.zeros([10,10])
        self.values = np.zeros([10,10])
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

    def generateStateVector(self, state, action):
        player_pos = np.argwhere(state)

        initial_array = [1,]

        initial_array.append(state[0][0])
        # append col
        initial_array.append(state[0][1])
        # append row **2
        initial_array.append(state[0][0] ** 2)
        # append col **2
        initial_array.append(state[0][1] ** 2)
        # Row + a
        initial_array.append(state[0][0] + action)
        # Col + a
        initial_array.append(state[0][1] + action)
        # One hot encoding actions 
        if(action == 0):
            initial_array.append(1)
            initial_array.append(0)
            initial_array.append(0)
            initial_array.append(0)
        if(action == 1):
            initial_array.append(0)
            initial_array.append(1)
            initial_array.append(0)
            initial_array.append(0)
        if(action == 2):
            initial_array.append(0)
            initial_array.append(0)
            initial_array.append(1)
            initial_array.append(0)
        if(action == 3):
            initial_array.append(0)
            initial_array.append(0)
            initial_array.append(0)
            initial_array.append(1)
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

    def epsilonGreedy(self, state, weight ):
        actions = [0,1,2,3]
        if(np.random.random() < self.epsilon):
            randomChoiceAction = np.random.choice(actions)
            return randomChoiceAction
        else: 
            # index = [np.dot(weight, self.generateStateVector(state, actions[i])) for i in range(len(actions))]4
            vals = []
            for action in range(len(actions)):
                x = self.generateStateVector(state, actions[action])
                qhat = np.dot(x, weight)
                vals.append(qhat)
            vals = np.array(vals)
            return np.argmax(vals)

    # this function calculates max action using qhat in s using a and w to get best acition for the given state
    def getBestPolicyAndValue(self, isTerminal):
        if(isTerminal):
            for i in range(self.env.level.shape[0]):
                            for j in range(self.env.level.shape[1]):
                                acs = [0,1,2,3]
                                acs_vals = []
                                if(self.env.level[i][j] == 0):
                                    self.values[i][j] = -20
                                else:
                                    for action in range(len(acs)):
                                        x = self.generateStateVector([[i,j]], action)
                                        qhat = np.dot(x, self.weights)
                                        acs_vals.append(qhat)
                                        index = np.argmax(acs_vals)
                                        self.values[i][j] = round(acs_vals[index],2)
                            
            for i in range(self.policy.shape[0]):
                            for j in range(self.policy.shape[1]):
                                if(i + 1 < 10 & j+ 1  < 10):
                                    offsets =  np.array([self.values[i][j - 1], self.values[i][j +1], self.values[i -1][j], self.values[i +1][j]])
                                    max_offset = np.argmax(offsets)
                                    self.policy[i][j] = max_offset
        print(self.values)
        print(self.policy)
                               
            


    def train(self,timesteps):
        initialState = self.env.reset()
        # print("States before1", initialState)

        for timestep in range(timesteps):
             step = 0 
             while (self.done == False):
                step = step + 1 
                action = self.epsilonGreedy(initialState, self.weights)
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
                

                # Before changing state update policy and value matrix 

                if(step % 10 == 0):
                    print("*********************** showing policy and value  ************************")


                # Change next state to become current state 
                self.env.currentState =  next_state
                initialState = next_state


                if(self.isTerminalState(next_state)):
                    self.done = True
                    print(self.done)
                    print("====================== Terminal State ========================")
                    print("Running policy evolution visulaization for terminal state...")

                    self.getBestPolicyAndValue(True)





