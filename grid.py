import pygame
import numpy as np
import random
 

class Grid:
    def __init__(self, width, height, scale, offset):#paramaters for window
        self.scale = scale    
        self.columns = int(height/scale)  
        self.rows = int(width/scale)     
        self.size = (self.rows , self.columns)
        self.grid_array = np.ndarray( shape=(self.size))
        self.offset = offset
        

    def random2D_array(self):
        for a in range(self.rows):
            for b in range(self.columns):
                self.grid_array[a][b] = random.randint(0,1)

    def Game(self, off_color, on_color, surface):
        for a in range(self.rows):
            for b in range(self.columns):
                b_pos = b*(self.scale)
                a_pos = a*(self.scale)

                if (self.grid_array[a][b] == 1):
                    pygame.draw.rect(surface, on_color, [a_pos, b_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [a_pos, b_pos, self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        for a in range(self.rows):
            for b in range(self.columns):
                state = self.grid_array[a][b]
                neighbours = self.get_neighbours(a,b)
                # provided rule or condition 
                if (state ==0  and neighbours == 3):
                    next[a][b]= 1
                elif (state ==1  and (neighbours < 2 or neighbours > 3)):
                    next[a][b]= 0 
                else:
                     next[a][b]= state

        self.grid_array = next

    def get_neighbours(self, a, b):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                a_edg = (a+n+self.rows) % self.rows
                b_edg = (b+n+self.columns) % self.columns
                total += self.grid_array[a_edg][b_edg]

        total += self.grid_array[a][b]
        
        return total

    
           
                

                


            






            


    

