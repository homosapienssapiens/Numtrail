# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 23:28:50 2020

@author: Miguel
"""

import numpy as np

### Class queue and its functions ###
class cola:
    # Constructor
    def __init__(self, cap=100):
        self.data=[]
        self.capacity=cap

    # --Methods--
    
    #Enqueue: Insert an element in the queue
    def enqueue(self, x):
        if len(self.data) <= self.capacity:
            return self.data.append(x)
    
    # Dequeue: Erases the element in the queue
    def dequeue(self):
        return self.data.pop(0)
    
    # Peek: Returns the first element of the queue
    def peek(self):
        return self.data[0]
    
    # Empty: Returns true if queue is empty
    def empty(self):
        return self.data == []
    
    # Print: Imprime la pila en orden.
    def print(self):
            print(self.data)

### Class node and its functions ###
class node:
    
    # Constructor
    def __init__(self, n=0):
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        self.data = n
        
    # ---Méthods---            
    
    # Method: Alpha-beta. It finds the best path in the given four-node tree.
    # Variables:
    # self (current node)
    # kind (max or min)
    # lvl (level in the tree)
    # alpha (alpha value)
    # beta (beta value)
               
    def alphabeta(self, kind, lvl, scr, side, alpha = -1000, beta = 1000):
        aux =  'x'
        if kind:
            scr -= self.data
        else:
            scr += self.data
        if lvl == 0 or (self.up == None and self.right == None and self.down == None and self.left == None):
            return [lvl, scr, side] 
        c = cola()
        
        if self.up != None:
            c.enqueue([self.up, scr, "w"])
        if self.right != None:
            c.enqueue([self.right, scr, "d"])
        if self.down != None:
            c.enqueue([self.down, scr, "s"])
        if self.left != None:
            c.enqueue([self.left, scr, "a"])
        
        if kind:
            value = -21
            while c.empty() == False:
                const = c.dequeue()
                val = const[0].alphabeta(not kind, lvl-1, scr, const[2], alpha, beta)
                if value <= val[1]:
                    aux = const[2]
                value = max(value, val[1])
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return [lvl, value, aux]
        else:
            value = 21
           
            while c.empty() == False:
                const = c.dequeue()
                val = const[0].alphabeta(not kind, lvl-1, scr, const[2], alpha, beta)
                if value >= val[1]:
                    aux = const[2]
                value = min(value, val[1])
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return [lvl, value, aux]


    # Method: 
    # Constructor method for the posibilities tree
    # Variables:
    # self: Currend node
    # obj: Table object
    # rpos: Red player position (player)
    # bpos: Blue player position (CPU)
    # lvl: SIze of the tree
    # minimax: Minimax status for root node.
    def build(self, obj, rpos, bpos, lvl, minimax = False):
        if lvl == 0:
            return
        if minimax == False:
            if((bpos[0])-1 >= 0 and obj.data[bpos[0]-1][bpos[1]] != 0):
                bpos[0] = bpos[0] - 1
                self.up = node(obj.data[bpos[0]][bpos[1]])
                obj.data[bpos[0]][bpos[1]] = 0
                self.up.build(obj, rpos, bpos, lvl-1, not minimax)
                obj.data[bpos[0]][bpos[1]] = self.up.data
                bpos[0] = bpos[0] + 1
            if((bpos[1])+1 < obj.size and obj.data[bpos[0]][bpos[1]+1] != 0):
                bpos[1] = bpos[1] + 1
                self.right = node(obj.data[bpos[0]][bpos[1]])
                obj.data[bpos[0]][bpos[1]] = 0
                self.right.build(obj, rpos, bpos, lvl-1, not minimax)
                obj.data[bpos[0]][bpos[1]] = self.right.data
                bpos[1] = bpos[1] - 1
            if((bpos[0])+1 < obj.size and obj.data[bpos[0]+1][bpos[1]] != 0):
                bpos[0] = bpos[0] + 1
                self.down = node(obj.data[bpos[0]][bpos[1]])
                obj.data[bpos[0]][bpos[1]] = 0
                self.down.build(obj, rpos, bpos, lvl-1, not minimax)
                obj.data[bpos[0]][bpos[1]] = self.down.data
                bpos[0] = bpos[0] - 1
            if((bpos[1])-1 >= 0 and obj.data[bpos[0]][bpos[1]-1] != 0):
                bpos[1] = bpos[1] - 1
                self.left = node(obj.data[bpos[0]][bpos[1]])
                obj.data[bpos[0]][bpos[1]] = 0
                self.left.build(obj, rpos, bpos, lvl-1, not minimax)
                obj.data[bpos[0]][bpos[1]] = self.left.data
                bpos[1] = bpos[1] + 1
        if minimax == True:
            if((rpos[0])-1 >= 0 and obj.data[rpos[0]-1][rpos[1]] != 0):
                rpos[0] = rpos[0] - 1
                self.up = node(obj.data[rpos[0]][rpos[1]])
                obj.data[rpos[0]][rpos[1]] = 0
                self.up.build(obj, rpos, bpos, lvl-1, not minimax)
                obj.data[rpos[0]][rpos[1]] = self.up.data
                rpos[0] = rpos[0] + 1
            if((rpos[1])+1 < obj.size and obj.data[rpos[0]][rpos[1]+1] != 0):
                rpos[1] = rpos[1] + 1
                self.right = node(obj.data[rpos[0]][rpos[1]])
                obj.data[rpos[0]][rpos[1]] = 0
                self.right.build(obj, rpos, bpos, lvl-1, not minimax)
                obj.data[rpos[0]][rpos[1]] = self.right.data
                rpos[1] = rpos[1] - 1
            if((rpos[0])+1 < obj.size and obj.data[rpos[0]+1][rpos[1]] != 0):
                rpos[0] = rpos[0] + 1
                self.down = node(obj.data[rpos[0]][rpos[1]])
                obj.data[rpos[0]][rpos[1]] = 0
                self.down.build(obj, rpos, bpos, lvl-1, not minimax)
                obj.data[rpos[0]][rpos[1]] = self.down.data
                rpos[0] = rpos[0] - 1
            if((rpos[1])-1 >= 0 and obj.data[rpos[0]][rpos[1]-1] != 0):
                rpos[1] = rpos[1] - 1
                self.left = node(obj.data[rpos[0]][rpos[1]])
                obj.data[rpos[0]][rpos[1]] = 0
                self.left.build(obj, rpos, bpos, lvl-1, not minimax)  
                obj.data[rpos[0]][rpos[1]] = self.left.data
                rpos[1] = rpos[1] + 1
        return
        

### Table class and its functions ###
class table:
    
    # --Constructor--
    def __init__(self, s = 4):
        self.data = []
        self.size = s
        self.rpos = [self.size-1, self.size -1]
        self.bpos = [0, 0]
        self.points = 0
        self.status = True
    
    # Fills the table with uniform random integers between 1 and 2n 
    def newtable(self):
        self.data = np.random.randint(1, ((self.size*2)+1), size = (self.size, self.size))
        return self.data
   
    # Prints the content of the table. 
    def print(self):
        print(self.data)
        print("\nScore", self.points, "points\n")
    
    # User plays a turn
    # Variable
    # player: boolean for defining wich player's turn is.
    def turn(self, player):
        self.print()
        
        if player == True:
            # Variables with all positions possible.
            up = [(self.rpos[0])-1, self.rpos[1]]
            right = [self.rpos[0], (self.rpos[1])+1]
            down = [self.rpos[0]+1, self.rpos[1]]
            left = [self.rpos[0], self.rpos[1]-1]
            # list of list with the information of each available block
            choices = []
            print("\nYour turn\n")
            print("moves possible")
            # Availability of each adjacent block.
            if (up[0] >= 0 and self.data[up[0], up[1]] != 0):
                print("Up", self.data[up[0], up[1]])
                choices.append(('w', self.data[up[0], up[1]], up, True))
            else:
                choices.append(('w', 0, up, False))
            if (right[1] < self.size and self.data[right[0], right[1]] != 0):
                print("Right", self.data[right[0], right[1]])
                choices.append(('d', self.data[right[0], right[1]], right, True))
            else:
                choices.append(('d', 0, right, False))
            if (down[0] < self.size and self.data[down[0], down[1]] != 0):
                print("Down", self.data[down[0], down[1]])
                choices.append(('s', self.data[down[0], down[1]], down, True))
            else:
                choices.append(('s', 0, down, False))
            if (left[1] >= 0 and self.data[left[0], left[1]] != 0):
                print("Left", self.data[left[0], left[1]])
                choices.append(('a', self.data[left[0], left[1]], left, True))
            else:
                choices.append(('a', 0, left, False))
            # If there is no more options available, it returns False
            if choices[0][3] == False and choices[1][3] == False and choices[2][3] == False and choices[3][3] == False:
                return False
            else:
                # Variable with the player's selected option.
                choice = 'x'
                # Displays available options.
                print('Choose, then Enter.')
                for i in range(len(choices)):
                    if (choices[i][1] != 0):
                        print(choices[i][0])
                print("Choose a valid option")
                opc = False
                
                while opc == False:
                    choice = input()
                    # Looks for the option selected by the user.
                    for i in range(len(choices)):
                        if choices[i][0] == choice:
                            # If it's a fair movement, it moves to the new block and adds its number.
                            if choices[i][3] == True:
                                opc = True
                                self.rpos = choices[i][2]
                                self.points += self.data[self.rpos[0], self.rpos[1]]
                                self.data[self.rpos[0], self.rpos[1]] = 0
                                break
                            else:
                                print("Please choose an available option.")
                print("Your move")
                return True
        else:
            # Variables with all positions possible.
            print("CPU's move")
            up = [(self.bpos[0])-1, self.bpos[1]]
            right = [self.bpos[0], (self.bpos[1])+1]
            down = [self.bpos[0]+1, self.bpos[1]]
            left = [self.bpos[0], self.bpos[1]-1]
            alt = self
            choices = []
            # Availability of each adjacent block.
            if (up[0] >= 0 and self.data[up[0], up[1]] != 0):
                choices.append(('w', self.data[up[0], up[1]], up, True))
            else:
                choices.append(('w', 0, up, False))
            if (right[1] < self.size and self.data[right[0], right[1]] != 0):
                choices.append(('d', self.data[right[0], right[1]], right, True))
            else:
                choices.append(('d', 0, right, False))
            if (down[0] < self.size and self.data[down[0], down[1]] != 0):
                choices.append(('s', self.data[down[0], down[1]], down, True))
            else:
                choices.append(('s', 0, down, False))
            if (left[1] >= 0 and self.data[left[0], left[1]] != 0):
                choices.append(('a', self.data[left[0], left[1]], left, True))
            else:
                choices.append(('a', 0, left, False))
            # If there is no more options available, it returns False
            if choices[0][3] == False and choices[1][3] == False and choices[2][3] == False and choices[3][3] == False:
                return False
            n = node(alt.data[alt.bpos[0], alt.bpos[1]])
            n.build(alt, alt.rpos, alt.bpos, dif)
            result = n.alphabeta(False, dif, 0, "x")
            if result[2] == "w":
                self.bpos = up
            if result[2] == "d":
                self.bpos = right
            if result[2] == "s":
                self.bpos = down
            if result[2] == "a":
                self.bpos = left
            self.points -= self.data[self.bpos[0], self.bpos[1]]
            self.data[self.bpos[0], self.bpos[1]] = 0
        return True
            
# Let the game begin!
print("\nWelcome to Numtrail\n")
print("In order to play use the w, a, s, d keys.",
      "\nTheese are the videogame standard for:",
      "\nw: Up",
      "\na: Left",
      "\ns: Down",
      "\nd: Right\n")   
size = 0
dif = 0
# Until the user doesn't select a right table size...
while size < 4 or size > 10: 
    print("Please select a table size\n", "Min 4\n", "Max 10 \n")
    size = input()
    size = int(size)
# Until the user desn't select a right dificulty level...
while dif < 3 or dif > 15:
    print("Please select a dificulty level between 3 (extra easy) and 15 (extra hard)")
    dif = input()
    dif = int(dif)     
    print("\n")
t = table(size)
t.newtable()
t.data[t.bpos[0]][t.bpos[1]] = 0
t.data[t.rpos[0]][t.rpos[1]] = 0
t.points = 0 
gameon = True
player = False
#Mientras se pueda seguir jugando...
while gameon:
    gameon = t.turn(player)
    player = not player
print("\n          ***************")
print("          ***GAME OVER***")
print("          ***************")
if t.points > 0:
    print("             You win!")
elif t.points < 0:
    print("            You lose...")
else: 
    print("             Draw!")
print("\nFinal score:", t.points, "points")
print("Thanks for playing. Created by Miguel Solis.")