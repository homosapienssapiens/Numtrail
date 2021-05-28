# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 23:28:50 2020

@author: Miguel
"""

import numpy as np

class cola:
    # Constructor
    def __init__(self, cap=100):
        self.data=[]
        self.capacity=cap

    # --Métodos--
    
    #Enqueue: Inserta un elemento en la cola
    def enqueue(self, x):
        if len(self.data) <= self.capacity:
            return self.data.append(x)
    
    # Dequeue: Quita y devuelve un elemento en la cola    
    def dequeue(self):
        return self.data.pop(0)
    
    # Peek: Devuelve el elemento al inicio de la cola
    def peek(self):
        return self.data[0]
    
    # Empty: Devuelve un booleano indicando si es verdad que la pila está vacía
    def empty(self):
        return self.data == []
    
    # Print: Imprime la pila en orden.
    def print(self):
            print(self.data)

### Clase nodo y sus funciones ###
class node:
    
    # Constructor
    def __init__(self, n=0):
        self.up = None
        self.right = None
        self.down = None
        self.left = None
        self.data = n
        
    # ---Métodos---            
           
    # Método alfa-beta para encontrar el camino más óptimo en el árbol de cuatro nodos dado.
    # Variables:
    # self (el nodo actual)
    # kind (si es Max o ens Min (True/False))
    # lvl (el nivel del árbol en cuestión)
    # alpha (el valor de alfa)
    # beta (el valor de beta)        
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


    # Método creador de arbol de posibilidades
    # Variables:
    # self: El nodo actual
    # obj: El objeto tablero de la partida
    # rpos: La posición del jugador rojo (jugador)
    # bpos: la posición del jugaro azul (CPU)
    # lvl: El nivel de profundidad del árbol a crear
    # minimax = Qué estatus de minimax es el nodo raiz
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
        

### Clase tabla y sus funciones ###
class table:
    
    # --Constructor--
    def __init__(self, s = 4):
        self.data = []
        self.size = s
        self.rpos = [self.size-1, self.size -1]
        self.bpos = [0, 0]
        self.points = 0
        self.status = True
    
    # Llenar la tabla de enteros al azar entre 1 y 2N
    def newtable(self):
        self.data = np.random.randint(1, ((self.size*2)+1), size = (self.size, self.size))
        return self.data
   
    # Imprime los datos de la tabla 
    def print(self):
        print(self.data)
        print("\nMarcador", self.points, "puntos\n")
    
    # Usuario juega un turno
    # Variable
    # player: booleano para saber a qué jugador le toca
    def turn(self, player):
        self.print()
        
        if player == True:
            # Variables con las rposiciones de cada opción rposible
            up = [(self.rpos[0])-1, self.rpos[1]]
            right = [self.rpos[0], (self.rpos[1])+1]
            down = [self.rpos[0]+1, self.rpos[1]]
            left = [self.rpos[0], self.rpos[1]-1]
            # lista de listas con la información necesaria de cada bloque contiguo
            choices = []
            print("\nSu turno\n")
            print("posibilidad de movimientos")
            # Ifs para revisar la disponibilidad de cada bloque
            if (up[0] >= 0 and self.data[up[0], up[1]] != 0):
                print("Arriba", self.data[up[0], up[1]])
                choices.append(('w', self.data[up[0], up[1]], up, True))
            else:
                choices.append(('w', 0, up, False))
            if (right[1] < self.size and self.data[right[0], right[1]] != 0):
                print("Derecha", self.data[right[0], right[1]])
                choices.append(('d', self.data[right[0], right[1]], right, True))
            else:
                choices.append(('d', 0, right, False))
            if (down[0] < self.size and self.data[down[0], down[1]] != 0):
                print("Abajo", self.data[down[0], down[1]])
                choices.append(('s', self.data[down[0], down[1]], down, True))
            else:
                choices.append(('s', 0, down, False))
            if (left[1] >= 0 and self.data[left[0], left[1]] != 0):
                print("Izquierda", self.data[left[0], left[1]])
                choices.append(('a', self.data[left[0], left[1]], left, True))
            else:
                choices.append(('a', 0, left, False))
            # Si no hay más opciones disponibles regresa False
            if choices[0][3] == False and choices[1][3] == False and choices[2][3] == False and choices[3][3] == False:
                return False
            else:
                # Variable con la opción señalada por el usuario
                choice = 'x'
                # Despliega las opciones disponibles.
                print('por favor usa solo una de las teclas de abajo y luego enter.')
                for i in range(len(choices)):
                    if (choices[i][1] != 0):
                        print(choices[i][0])
                print("Elige una opción válida")
                opc = False
                
                while opc == False:
                    choice = input()
                    # Busca la opción señalada por el usuario.
                    for i in range(len(choices)):
                        if choices[i][0] == choice:
                            # Si es un movimiento válido mueve de casilla y suma.
                            if choices[i][3] == True:
                                opc = True
                                self.rpos = choices[i][2]
                                self.points += self.data[self.rpos[0], self.rpos[1]]
                                self.data[self.rpos[0], self.rpos[1]] = 0
                                break
                            else:
                                print("Favor de poner una opción válida.")
                print("Tu movimiento")
                return True
        else:
            # Variables con las rposiciones de cada opción posible
            print("Movimiento CPU")
            up = [(self.bpos[0])-1, self.bpos[1]]
            right = [self.bpos[0], (self.bpos[1])+1]
            down = [self.bpos[0]+1, self.bpos[1]]
            left = [self.bpos[0], self.bpos[1]-1]
            alt = self
            choices = []
             # Ifs para revisar la disponibilidad de cada bloque
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
            # Si no hay más opciones disponibles regresa False
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
            
# Arranca el juego!
print("\nBienvenido al juego\n")
print("Para poder jugar usa las teclas w, a, s, d del teclado.",
      "\nEstas teclas son un estándar en los videojuegos de compurtadora para:",
      "\nw: arriba",
      "\na: izquierda",
      "\ns: abajo",
      "\nd: derecha\n")   
size = 0
dif = 0
# Mientras no diga un tamaño de tablero correcto...
while size < 4 or size > 10: 
    print("Por favor ingresa el tamaño del tablero\n", "Mínimo 4\n", "Máximo 10 \n")
    size = input()
    size = int(size)
# Mientras no diga un nivel de dificultado correcto...
while dif < 3 or dif > 15:
    print("Por favor ingresa una dificultad del 3 al 15")
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
    print("             ¡Tu ganas!")
elif t.points < 0:
    print("            Tu pierdes...")
else: 
    print("             ¡Empate!")
print("\nPuntuación final:", t.points, "puntos")
print("Gracias por jugar. Juego creado por Miguel Solis para la clase de IDI1.")