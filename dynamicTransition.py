
import numpy as np

class dynTransition():
    def __init__(self, oldTileUnderPlayerbefore, newTileUnderPlayerAfter, isFirstIter):
        self.oldTileUnderPlayerbefore = oldTileUnderPlayerbefore
        self.newTileUnderPlayerAfter = newTileUnderPlayerAfter
        self.isFirstIter = isFirstIter

    def getNextState(self, map, action):
        pass

    def getReward(self):
        pass

    def getNextStateDynamically(self, currentState: str, action: str):
        position_of_player_sPrime_row = 0
        position_of_player_sPrime_col = 0

        list_of_integers_s = currentState
        print(list_of_integers_s)
        position_of_player_s = np.argwhere(np.array(list_of_integers_s == 2))
        print("Here", position_of_player_s)
        position_of_player_sPrime_row, position_of_player_sPrime_col = self.getPlayerSprime(action, position_of_player_s)

        print("Running collision detection with walls")
        if(list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]) == 0:
#       # Hit a wall so return the same state as agent does not moove
            print('Hit a wall',)
            return currentState
        else:
         print("Freespace detected")
         # In first Iter the player always stands on a floor tile with value 1
         if(self.isFirstIter == True): 
            print("This is 1st iter")
            self.oldTileUnderPlayerbefore = 1
         else:
          pass
        self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]
        print("Tile after player is", self.newTileUnderPlayerAfter)
        # Before moving player check if there is box in the direction player is moving
        self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] # backup of sprime of player
        list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] = 2 # Set new player position
        list_of_integers_s[position_of_player_s[0][0]][position_of_player_s[0][1]] = self.oldTileUnderPlayerbefore # change previous tile to old value
        self.oldTileUnderPlayerbefore = self.newTileUnderPlayerAfter # New tile now becomes old tile for next iter
        print("next state is", list_of_integers_s)
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


# class Helpers(): 
#   def __init__(self, oldTileUnderPlayerbefore, newTileUnderPlayerAfter, isFirstIter ):
#         self.oldTileUnderPlayerbefore = oldTileUnderPlayerbefore
#         self.newTileUnderPlayerAfter = newTileUnderPlayerAfter
#         self.isFirstIter = isFirstIter
#         self.NewBoxPos_oldValue = 1

#   # get next sprime of player using action
#   def getPlayerSprime(self,action, position_of_player_s):
#     position_of_player_sPrime_row = 0
#     position_of_player_sPrime_col = 0
#     if(action == 'down'):
#       position_of_player_sPrime_row = position_of_player_s[0][0] + 1
#       position_of_player_sPrime_col = position_of_player_s[0][1] 
#     if(action == 'up'):
#         position_of_player_sPrime_row = position_of_player_s[0][0] - 1
#         position_of_player_sPrime_col = position_of_player_s[0][1] 
#     if(action == 'right'):
#         position_of_player_sPrime_row = position_of_player_s[0][0] 
#         position_of_player_sPrime_col = position_of_player_s[0][1] + 1
#     if(action == 'left'):
#         position_of_player_sPrime_row = position_of_player_s[0][0] 
#         position_of_player_sPrime_col = position_of_player_s[0][1] - 1
#     return position_of_player_sPrime_row, position_of_player_sPrime_col

#   # get sprime of box
#   def setNewPosOfBox(self, list_of_integers_s ,position_of_player_sPrime_row, position_of_player_sPrime_col, action):
#     if(action == 'down'):
#       list_of_integers_s[position_of_player_sPrime_row + 1][position_of_player_sPrime_col] = 3 # Set new position of box
#       return list_of_integers_s
#     if(action == 'up'):
#       list_of_integers_s[position_of_player_sPrime_row - 1][position_of_player_sPrime_col] = 3 # Set new position of box
#       return list_of_integers_s
#     if(action == 'right'):
#       list_of_integers_s[position_of_player_sPrime_row ][position_of_player_sPrime_col + 1] = 3 # Set new position of box
#       return list_of_integers_s
#     if(action == 'left'):
#       list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col - 1] = 3 # Set new position of box
#       return list_of_integers_s

#   # check if box is next to a wall
#   def isBoxNextToWall(self,list_of_integers_s, position_of_player_sPrime_row, position_of_player_sPrime_col, action):
#     # print("Agent sPrime pos is", position_of_player_sPrime_row, position_of_player_sPrime_col)
#     if(action == 'down'):
#       # print("Action is down")
#       position_of_box_sPrime_row = position_of_player_sPrime_row + 1
#       position_of_box_sPrime_col = position_of_player_sPrime_col
#       # print("Box location is", position_of_box_sPrime_row, position_of_box_sPrime_col)
#       boxDownWallCheck = list_of_integers_s[position_of_player_sPrime_row + 1][position_of_player_sPrime_col]
#       self.NewBoxPos_oldValue = list_of_integers_s[position_of_player_sPrime_row + 1][position_of_player_sPrime_col]
#       # print("Box wall check is", boxDownWallCheck)
#       if(boxDownWallCheck == 0):
#         return True
#       else:
#         return False
#     if(action == 'up'):
#       # print("Action is up")
#       position_of_box_sPrime_row = position_of_player_sPrime_row - 1
#       position_of_box_sPrime_col = position_of_player_sPrime_col
#       # print("Box location is", position_of_box_sPrime_row, position_of_box_sPrime_col)
#       boxDownWallCheck = list_of_integers_s[position_of_player_sPrime_row - 1][position_of_player_sPrime_col]
#       self.NewBoxPos_oldValue = list_of_integers_s[position_of_player_sPrime_row - 1][position_of_player_sPrime_col]
#       # print("Box wall check is", boxDownWallCheck)
#       if(boxDownWallCheck == 0):
#         return True
#       else:
#         return False
#     if(action == 'right'):
#       print("Action is right")
#       position_of_box_sPrime_row = position_of_player_sPrime_row 
#       position_of_box_sPrime_col = position_of_player_sPrime_col + 1
#       # print("Box location is", position_of_box_sPrime_row, position_of_box_sPrime_col)
#       boxDownWallCheck = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col + 1]
#       self.NewBoxPos_oldValue = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col + 1]
#       # print("Box wall check is", boxDownWallCheck)
#       if(boxDownWallCheck == 0):
#         return True
#       else:
#         return False 
#     if(action == 'left'):
#         position_of_box_sPrime_row = position_of_player_sPrime_row 
#         position_of_box_sPrime_col = position_of_player_sPrime_col - 1
#         # print("Box location is", position_of_box_sPrime_row, position_of_box_sPrime_col)
#         boxDownWallCheck = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col - 1]
#         self.NewBoxPos_oldValue = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col - 1]
#         if(boxDownWallCheck == 0):
#             return True
#         else:
#             return False

#   # get next state dynamically instaed of using a table. 
#   def getNextStateDynamically(self, currentState: str, action: str):
#     # print("Getting")
#     position_of_player_sPrime_row = 0
#     position_of_player_sPrime_col = 0

#     list_of_integers_s = np.array(list(map(int, currentState.split(',')))).reshape(5,5)
#     position_of_player_s = np.argwhere(np.array(list_of_integers_s == 5))
    
#     # print(list_of_integers_s, position_of_player_s)

#     # Get s prime position sof player
#     position_of_player_sPrime_row, position_of_player_sPrime_col = self.getPlayerSprime(action, position_of_player_s)

#     print("Running collision detection with walls")
#     if(list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]) == 0:
#       # Hit a wall so return the same state as agent does not moove
#         # print('Hit a wall',)
#         return np.array(list(map(int, currentState.split(',')))).reshape(5,5)
#      # Else there is freespace ahead to move   
#     else:
#       #  print("Freespace detected")
#        # In first Iter the player always stands on a floor tile with value 1
#        if(self.isFirstIter == True): 
#         #  print("This is 1st iter")
#          self.oldTileUnderPlayerbefore = 1
#        else:
#         pass
#        self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col]
#       #  print("Tile after player is", self.newTileUnderPlayerAfter)
#         # Before moving player check if there is box in the direction player is moving

       
#       #  print("Tile after player is", self.newTileUnderPlayerAfter)
#        # Before moving player check if there is box in the direction player is moving
#        if(self.newTileUnderPlayerAfter == 3):
#         #  print("Collided with a box", position_of_player_sPrime_row, position_of_player_sPrime_col)
#          # Check if sprime of box is a wall
#          isWallNextToBox = self.isBoxNextToWall(list_of_integers_s, position_of_player_sPrime_row, position_of_player_sPrime_col, action)
#         #  print("Box is next to wall", isWallNextToBox)
#          if(isWallNextToBox == True):
#            return list_of_integers_s
#          else: 
#            # Update position of box
#           #  print("Freespace behind box",position_of_player_sPrime_row, position_of_player_sPrime_col)
#            new_list_integers = self.setNewPosOfBox(list_of_integers_s,position_of_player_sPrime_row, position_of_player_sPrime_col, action)
#            # print("New list is", new_list_integers)
#            # Update position of player 
#            self.newTileUnderPlayerAfter = new_list_integers[position_of_player_sPrime_row][position_of_player_sPrime_col] # backup of sprime of player
#            new_list_integers[position_of_player_sPrime_row][position_of_player_sPrime_col] = 5 # Set new player position
#            new_list_integers[position_of_player_s[0][0]][position_of_player_s[0][1]] = self.oldTileUnderPlayerbefore # change previous tile to old value
#            self.oldTileUnderPlayerbefore = self.newTileUnderPlayerAfter # New tile now becomes old tile for next iter 
#            return new_list_integers
#        else:
#         #  print("Did not collide with any box, transitioning normally..")
#          # Update position of player normally
#          self.newTileUnderPlayerAfter = list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] # backup of sprime of player
#          list_of_integers_s[position_of_player_sPrime_row][position_of_player_sPrime_col] = 5 # Set new player position
#          list_of_integers_s[position_of_player_s[0][0]][position_of_player_s[0][1]] = self.oldTileUnderPlayerbefore # change previous tile to old value
#          self.oldTileUnderPlayerbefore = self.newTileUnderPlayerAfter # New tile now becomes old tile for next iter
#          return list_of_integers_s
