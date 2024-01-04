#!/usr/bin/env python
# coding: utf-8

# #### Author: David Martinez Jaramillo
# #### Class: Algorithms and Data Structures
# #### Instructor: Mr. Haytock
# #### Description: Created a maze solving game using pygame along with different stack implementations to render the maze. Keep in mind that the screen of the game is small. The maze view is not supposed to move across the screen. The screen is static.

# # Maze Solver

# ## Installing necessary libraries

# In[123]:


# ==========================================================
# ==========================================================
# IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
# !!! Input the content of the next line in your command prompt in order for the game to work !!
# !!!!!!!!!!!!!!!!!!! ->
# pip install pygame
# <- !!!!!!!!!!!!!!!!!!!!!!!!!
# IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT
# ==========================================================

# You need to input this in your command prompt once you have installed python.
# You can also install Anaconda and open jupyter notebook and decomment the first line
# of this code box and open the .ipynb file I uploaded

# ==========================================================
# ==========================================================


# ## Import necessary libraries for graphics and player interface

# In[124]:


from pygame.locals import *
import pygame


# ## Stack implementation

# ### Array List implementation

# In[125]:


# Allows node use
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# In[126]:


# Create a Stack Array implementation
class StackArray:
    # Initializes array
    def __init__(self):
        self.head = Node("h")
        self.size = 0
        
    # Pop operation
    def pop(self):
        if (self.isEmpty()):
            print("You can't do that")
            
        
        else:
            self.head = self.head.next
            self.size = self.size - 1
            
    # Peek operation
    def peek(self):
        return self.head.value
    
    # Push operation
    def push(self, value):
        node = Node(value)
        
        node.next = self.head
        self.head = node
        
        self.size = self.size + 1
    
    # Checking if empty operation
    def isEmpty(self):
        return self.size == 0
    
    # Getting size operation
    def getSize(self):
        return self.size


# ### Partially filled array

# In[127]:


# Static implementation
class StackPartial:
    state = True
    
    # Initializing array
    def __init__(self, length):
        self.length = length
        self.list = [_ for _ in range(self.length)]
        self.size = -1
        self.state = True
        
    # Pop operation
    def pop(self):
        if self.isEmpty():
            print("Error: Stack underflow")
            return
        
        else:
            self.size = self.size - 1
    
    # Peek operation
    def peek(self):
        if (self.isEmpty()):
            print("Empty")
        
        return self.list[self.size]
        
    # Push operation
    def push(self, value):
        if self.isFull():
            self.state = False            
        else:
            self.list[self.size + 1] = value
            self.size = self.size + 1
    
    # Checking if empty operation
    def isEmpty(self):
        return self.size == -1
    
    # Checking if full operation
    def isFull(self):
        return self.length - 1 == self.size
    
    # Getting Size operation
    def getSize(self):
        return self.size


# ## Creating a Maze class

# In[128]:


class Maze:
    mazeSection = None
    # Maze has a height and a width. The maze input is for the maze. It is going to be a list of 1 and 0s. Initialization
    def __init__(self, width, heigth, maze, size):
       self.h = heigth
       self.w = width
       self.maze = maze
       self.size = size
    
    # Drawing maze by sections (To simulate limited sigth)
    def draw(self,display_surf,image_surf, position):
       self.mazeSection = [0, self.maze[position-self.w], 0, self.maze[position-1], self.maze[position], self.maze[position+1], 0, self.maze[position+self.w], 0]
        
       bx = 0
       by = 0 
       for i in range(0,9):
           if self.mazeSection[ bx + (by*3) ] == 1:
               display_surf.blit(image_surf,( bx * self.size , by * self.size))
      
           bx = bx + 1
           if bx > 3-1:
               bx = 0 
               by = by + 1


# In[129]:


class MazeApp:
    windowWidth = 800
    windowHeight = 600
    player = 0
    state = 0
    tracker = 0
    goal = None
    position = 0
    positionTracker = None 
    screenTracker = 0
    timer = 500
    movementTracker = StackArray()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    
    # Initializes the game and sets up the initial conditions
    def __init__(self, width, height, mazeMap, shortestPath):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.mazeMap = mazeMap
        self.width = width
        self.height = height
        self.shortestPath = shortestPath
        
        self.positionTracker = StackPartial(self.shortestPath)
        
        # Get entrance into maze
        x = 0
        for i in self.mazeMap:
            if (i == 0):
                self.tracker = x
                break
                
            x = x + 1  
            
        y = self.width*self.height - 1
        while(self.mazeMap[y] == 1):             
            y = y - 1  
        self.goal = y
        
        self.pathTracker = self.tracker
        self.positionTracker.push(self.tracker)
    
    # Performs more initializing operations, more related with the graphics
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Maze Solver')
        self._running = True
        
        self._block_surf = pygame.image.load("wall.png").convert()
        
        self._image_surf = pygame.image.load("character.png").convert()
        width = self._block_surf.get_rect().width
        height = self._block_surf.get_rect().height
        self._image_surf = pygame.transform.scale(self._image_surf, (width, height))
        
        self.maze = Maze(self.width, self.height, self.mazeMap, self._block_surf.get_rect().width)
        
    # Just an event function that controls the game window
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
     
    # A function that performs updates
    def on_loop(self):
        pass
    
    # Handles rendering according to conditions (if in game, or if in other game over screens)
    def on_render(self):
        self._display_surf.fill((0,0,0))

        if (self.screenTracker == 0):
            self.renderStartMenu()
            
        elif (self.screenTracker == 1):
            self._display_surf.blit(self._image_surf,((1%(self.width))*self._block_surf.get_rect().width, int(1%self.width)*self._block_surf.get_rect().width))
            self.maze.draw(self._display_surf, self._block_surf, self.positionTracker.peek())
            self.gameScreen()
            
            
        elif (self.screenTracker == 2):
            self.renderEndMenu()
            
        elif (self.screenTracker == 3):
            self.renderWinMenu()
                
        
        pygame.display.flip()
     
    # Closes game window
    def on_cleanup(self):
        pygame.quit()        
    
    # Renders the start menu to initiate playing
    def renderStartMenu(self):
        self.screen.fill((0,0,0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Maze Solver', True, (255, 255, 255))
        start_button = font.render('[SPACE] for starting the game', True, (255, 255, 255))
        self.screen.blit(title, (self.windowWidth/2 - title.get_width()/2, self.windowHeight/2 - title.get_height()/2))
        self.screen.blit(start_button, (self.windowWidth/2 - start_button.get_width()/2, self.windowHeight/2 + start_button.get_height()/2))
        
        keys = pygame.key.get_pressed()

        if (keys[K_SPACE]):
            self.screenTracker = 1
        
        pygame.display.update()
    
    # Renders the game over screen.
    def renderEndMenu(self):
        self.screen.fill((0,0,0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game over', True, (255, 255, 255))
        start_button = font.render('Too many moves.[Q] to restart', True, (255, 255, 255))
        self.screen.blit(title, (self.windowWidth/2 - title.get_width()/2, self.windowHeight/2 - title.get_height()/2))
        self.screen.blit(start_button, (self.windowWidth/2 - start_button.get_width()/2, self.windowHeight/2 + start_button.get_height()/2))
        
        keys = pygame.key.get_pressed()
        
        if (keys[K_q]):
            self.restart()
            
            
        pygame.display.update()
        
    # Renders the winning screen
    def renderWinMenu(self):
        self.screen.fill((0,0,0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('You have solved the Maze!', True, (255, 255, 255))
        start_button = font.render('press [Q] for starting again', True, (255, 255, 255))
        self.screen.blit(title, (self.windowWidth/2 - title.get_width()/2, self.windowHeight/2 - title.get_height()/2))
        self.screen.blit(start_button, (self.windowWidth/2 - start_button.get_width()/2, self.windowHeight/2 + start_button.get_height()/2))
        
        keys = pygame.key.get_pressed()

        if (keys[K_q]):
            self.restart()
        
        pygame.display.update()
    
    # Restarts game when going back to initial screen
    def restart(self):
        self.player = 0
        self.state = 0
        self.tracker = 0
        self.goal = None
        self.position = 0
        self.positionTracker = StackPartial(self.shortestPath)
        self.screenTracker = 0
        self.timer = 500
        self.movementTracker = StackArray()
        self.screen = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        
        # Get entrance into maze
        x = 0
        for i in self.mazeMap:
            if (i == 0):
                self.tracker = x
                break
                
            x = x + 1  
            
        y = self.width*self.height - 1
        while(self.mazeMap[y] == 1):             
            y = y - 1  
        self.goal = y
        
        self.pathTracker = self.tracker
        self.positionTracker.push(self.tracker)
        
        
        self.on_init()
    
    # User interface function for updating changes in inputs and handles cases.
    def gameScreen(self):        
        keys = pygame.key.get_pressed()
        if (self.timer == 500):
            last = self.movementTracker.peek()
                
            if (keys[K_RIGHT]):
                potential = self.positionTracker.peek() + 1
                if (self.mazeMap[potential] != 1):
                    self.tracker = potential
                    self.timer = self.timer-1
                        
                    if (last == 'l'):
                        self.movementTracker.pop()
                        self.positionTracker.pop()
                            
                    else:
                        self.movementTracker.push('r')
                        self.positionTracker.push(potential)
 
            elif (keys[K_LEFT]):
                potential = self.positionTracker.peek() - 1
                if (self.mazeMap[potential] != 1):
                    self.tracker = potential
                    self.timer = self.timer-1
                        
                    if (last == 'r'):
                        self.movementTracker.pop()
                        self.positionTracker.pop()
                            
                    else:
                        self.movementTracker.push('l')
                        self.positionTracker.push(potential)
            
 
            elif (keys[K_UP]):
                potential = self.positionTracker.peek() - self.width
                if (self.mazeMap[potential] != 1):
                    self.tracker = potential
                    self.timer = self.timer-1
                        
                    if (last == 'd'):
                        self.movementTracker.pop()
                        self.positionTracker.pop()
                            
                    else:
                        self.movementTracker.push('u')
                        self.positionTracker.push(potential)
 
            elif (keys[K_DOWN]):
                potential = self.positionTracker.peek() + self.width
                if (self.mazeMap[potential] != 1):
                    self.tracker = potential
                    self.timer = self.timer-1
                        
                    if (last == 'u'):
                        self.movementTracker.pop()   
                        self.positionTracker.pop()
                            
                    else:
                        self.movementTracker.push('d')
                        self.positionTracker.push(potential)
 
            elif (keys[K_ESCAPE]):
                self._running = False
            
            
        if (self.timer < 500 and self.timer > 0):
            self.timer = self.timer - 1
            
        if (self.timer == 0):
            self.timer = 500
                
        if (self.positionTracker.peek() == self.goal):
            self.screenTracker = 3
                
        if (self.positionTracker.state == False):
            self.screenTracker = 2
            
        pygame.display.update()
     
    # Function that executes while the program is active. Handles the whole program while on execution.
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            pygame.event.pump()
            
                        
            self.on_loop()
            self.on_render()
        self.on_cleanup()
        
     


# ## Read input file

# In[130]:


# Reads the custom text file format for Maze
def readMaze(filepath):
    """
    Reads maze with input file of 1 dimensional array.
    
    """
    with open(filepath) as file:
        mazeFile = file.read()
        
    a = ''
    b = ''
    c = 0
    d = 0
        
    for i in mazeFile:
        if (i == '\n'):
            c += 1
        if (c == 0 and i != '\n'):
            a += i
        if (c == 1 and i != '\n'):
            b += i
        if (c == 2):
            break
        d += 1
        
        
        
   
    return int(a), int(b), [int(i) for i in mazeFile[d:] if i != ' ' and i != '\n']


# ## Executing maze game

# In[131]:


if __name__ == "__main__":
    print('Welcome to the maze game! Please go to the README.txt to find how to create your own maze input.')
    print('In case you do not input a maze file, there will be a default maze.')
    filepath = input('Input the location of your maze file')
    maximum = input('What do you want the maximum number of moves to be?')
    width, height, maze = readMaze(filepath)
    mazeApp = MazeApp(width, height, maze, int(maximum))
    mazeApp.on_execute()


# In[ ]:




