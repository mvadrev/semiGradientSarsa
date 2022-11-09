
import numpy as np

class dynTransition():
    def __init__(self, oldTileUnderPlayerbefore, newTileUnderPlayerAfter, isFirstIter):
        self.oldTileUnderPlayerbefore = oldTileUnderPlayerbefore
        self.newTileUnderPlayerAfter = newTileUnderPlayerAfter
        self.isFirstIter = isFirstIter



    def getNextStateDynamically(self, currentState: str, action: str):
        position_of_player_sPrime_row = 0
        position_of_player_sPrime_col = 0

        list_of_integers_s = np.copy(currentState)
        # print(list_of_integers_s)
        position_of_player_s = np.argwhere(list_of_integers_s == 2)
        # print("Here", position_of_player_s)
        position_of_player_sPrime_row, position_of_player_sPrime_col = self.getPlayerSprime(action, position_of_player_s)

        # print("Running collision detection with walls")
        if(list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]) == 0:
#       # Hit a wall so return the same state as agent does not moove
            print('Hit a wall',)
            return list_of_integers_s
        else:
         print("Freespace detected")
         # In first Iter the player always stands on a floor tile with value 1
         if(self.isFirstIter == True): 
            print("This is 1st iter")
            self.oldTileUnderPlayerbefore = 1
         else:
        #   pass
          self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]
        # print("Tile after player is", self.newTileUnderPlayerAfter)
        # Before moving player check if there is box in the direction player is moving
        self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] # backup of sprime of player
        list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] = 2 # Set new player position
        list_of_integers_s[position_of_player_s[0][0]][position_of_player_s[0][1]] = self.oldTileUnderPlayerbefore # change previous tile to old value
        self.oldTileUnderPlayerbefore = self.newTileUnderPlayerAfter # New tile now becomes old tile for next iter
        # print("next state is", list_of_integers_s)
        return list_of_integers_s

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
