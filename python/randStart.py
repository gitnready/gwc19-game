# Based on code at:
# http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# 1 - Import pygame library ####################################################
import pygame, random
from pygame.locals import *

# 2 - Set game global variables ################################################
boardsize = (512, 512)
screen = pygame.display.set_mode(boardsize)
width, height, margin = 100, 100, 2
BLACK = (0, 0, 0)
WHITE = (255,255,255)
grid = [] # 2D array (list of lists) for board
player = pygame.image.load('../img/player.jpg').convert()
playerCoord = [0,0]
icon0 = pygame.image.load('../img/icon0.jpg').convert() 
icon1 = pygame.image.load('../img/icon1.jpg').convert()
icon2 = pygame.image.load('../img/icon2.jpg').convert()
icon3 = pygame.image.load('../img/icon3.jpg').convert()

xSize = 5
ySize = 5

# 3 - Define game functions ####################################################
## 3a - Initialize the game board
def initBoard(): 
  for row in range(ySize):
    grid.append([])
    for column in range(xSize):
        grid[row].append(0) # all values set to 0
  # Set hard-coded start location for player
  grid[0][0] = 1  # player icon; value of 1 is player location

  #Randomly set start location for icons
  i = 10 #starts loop at code for icon 0
  while i < 14: #loops until icon 3 code is reached
      x = random.randrange(0,xSize) #randomly assign x cord
      y = random.randrange(0,ySize) #randomly assign y cord
      print(x,y)
      if (grid[x][y] == 0): #if nothing is written to grid square already, assign it to icon i and continue
        grid[x][y] = i
        i += 1

## 3b - Draw player/icon on the board
def drawIcon(rw,cl,iconName):
  screen.blit(iconName,((margin+width)*cl + margin,(margin+height)*rw + margin))
  
## 3c - Update the grid for the board
def updateBoard():
  for row in range(5):
    for column in range(5):
      color = WHITE             
      pygame.draw.rect(screen,color,[(margin + width) * column + margin,
                                     (margin + height) * row + margin,
                                      width, height])
      if grid[row][column] == 10:  #icon0 location
        drawIcon(row,column,icon0)  
      if grid[row][column] == 11:  #icon1 location
        drawIcon(row,column,icon1)  
      if grid[row][column] == 12:  #icon2 location
        drawIcon(row,column,icon2)  
      if grid[row][column] == 13:  #icon3 location
        drawIcon(row,column,icon3)    
      if grid[row][column] == 1:  #player location
        drawIcon(row,column,player)  

## 3d - Adjust score and print out a message if increased
def adjustScore(scoreP):
  if grid[playerCoord[0]][playerCoord[1]] >= 10:
    scoreP += 1
    print("You have learned "+str(scoreP)+" of the Core 4")
  return scoreP

## 3e - Handle player movement
def movePlayer(scoreParam):
  # Based on how-to at:
  # https://opensource.com/article/17/12/game-python-moving-player
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True; pygame.quit()
        sys.exit(); numlitter == 0
      # only handle key releases for simplicity (KEYUP not KEYDOWN)
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == ord('a'):
          if playerCoord[1] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1          
        elif event.key == pygame.K_RIGHT or event.key == ord('d'):
          if playerCoord[1] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] += 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1
        elif event.key == pygame.K_UP or event.key == ord('w'):
          if playerCoord[0] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1          
        elif event.key == pygame.K_DOWN or event.key == ord('s'):
          if playerCoord[0] < 4:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] += 1
            scoreParam = adjustScore(scoreParam)    
            grid[playerCoord[0]][playerCoord[1]] = 1
        elif event.key == ord('q'):
          print('quit game'); pygame.quit()
          break          
  return scoreParam

# 4 - Define main game #########################################################
def gameFunct():
  ## 4a - Initialize game
  pygame.init()
  initBoard()
  clock = pygame.time.Clock()
  score = 0
  print("Collect all of the Core 4 to increase your knowledge!\n")
  ## 4b - keep looping until exit condition met
  while (score < 4):
    score = movePlayer(score)  # Handle player movement
    updateBoard() # Update the grid for the board
    clock.tick(60) # In milliseconds (https://www.pygame.org/docs/ref/time.html)
    pygame.display.flip() # Redraw the board
    if score == 4: # Check for exit condition congratulatory message
      print("Congratulations on learning all of the Core 4!")
      print("Now practice practice practice and create cool code!")
  pygame.quit() # Quit the game

# Run automatically upon load/F5 ###############################################
if __name__ == "__main__":
  gameFunct()
