
import numpy as np

class dynTransition():
    def __init__(self, oldTileUnderPlayerbefore, newTileUnderPlayerAfter, isFirstIter):
        # init variables to keep track of tile value which player is on i.e floor and after since we also have a danger state where the agent can fall into
        self.oldTileUnderPlayerbefore = oldTileUnderPlayerbefore
        self.newTileUnderPlayerAfter = newTileUnderPlayerAfter
        self.isFirstIter = isFirstIter



    def getNextStateDynamically(self, currentState: str, action: str):
        # init and zero positions of player before calcuations 
        position_of_player_sPrime_row = 0
        position_of_player_sPrime_col = 0

        # Get pos of player from current state
        position_of_player_s = np.argwhere(currentState == 2)
        # print("Here", position_of_player_s)
        position_of_player_sPrime_row, position_of_player_sPrime_col = self.getPlayerSprime(action, position_of_player_s)
        
        # Chek collision with walls
        # print("Running collision detection with walls")
        if(currentState[position_of_player_sPrime_row][position_of_player_sPrime_col]) == 0:
#       # Hit a wall so return the same state as agent does not moove
            # print('Hit a wall',)
            return currentState
        else:
        #  print("Freespace detected")
         # In first Iter the player always stands on a floor tile with value 1
            if(self.isFirstIter == True): 
                # print("This is 1st iter")
                self.oldTileUnderPlayerbefore = 1
            else:
             pass
            self.newTileUnderPlayerAfter = currentState[position_of_player_sPrime_row][position_of_player_sPrime_col]
            # print("Tile after player is", self.newTileUnderPlayerAfter)
            # Before moving player check if there is box in the direction player is moving
            self.newTileUnderPlayerAfter = currentState[position_of_player_sPrime_row][position_of_player_sPrime_col] # backup of sprime of player
            currentState[position_of_player_sPrime_row][position_of_player_sPrime_col] = 2 # Set new player position
            currentState[position_of_player_s[0][0]][position_of_player_s[0][1]] = self.oldTileUnderPlayerbefore # change previous tile to old value
            self.oldTileUnderPlayerbefore = self.newTileUnderPlayerAfter # New tile now becomes old tile for next iter
            # print("next state is", currentState)
            return currentState

    def getPlayerSprime(self,action, position_of_player_s):
        position_of_player_sPrime_row = 0
        position_of_player_sPrime_col = 0
        if(action == 'down'):
            position_of_player_sPrime_row = position_of_player_s[0][0] + 1
            position_of_player_sPrime_col = position_of_player_s[0][1] 
        if(action == 'up'):
            position_of_player_sPrime_row = position_of_player_s[0][0] - 1
            position_of_player_sPrime_col = position_of_player_s[0][1] 
        if(action == 'right'):
            position_of_player_sPrime_row = position_of_player_s[0][0] 
            position_of_player_sPrime_col = position_of_player_s[0][1] + 1
        if(action == 'left'):
            position_of_player_sPrime_row = position_of_player_s[0][0] 
            position_of_player_sPrime_col = position_of_player_s[0][1] - 1
        return position_of_player_sPrime_row, position_of_player_sPrime_col
