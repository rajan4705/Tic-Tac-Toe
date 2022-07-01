import pygame,sys,time
from pygame.locals import *
from tkinter import *
from tkinter import messagebox

#initialize global variables
X_or_O = 'x'

#Dimensions of the board
width = 400
height = 400
grey = (205, 205, 205)


winner = None
draw = False

#Getting the board ready
TTT = [[None]*3,[None]*3,[None]*3]

pygame.init()
fps = 30
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((width, height),0,32)
pygame.display.set_caption("Tic-Tac-Toe")

img_X = pygame.image.load('X.png')
img_O = pygame.image.load('O.png')

#rezing them inacc to the board size
img_X = pygame.transform.scale(img_X, (80,80))
img_O = pygame.transform.scale(img_O, (80,80))


def mainPage():  
    screen.fill(grey) 
    # Drawing vertical lines
    pygame.draw.line(screen,(125,100,165),(width/3,0),(width/3, height),2)
    pygame.draw.line(screen,(125,100,165),(width/3*2,0),(width/3*2, height),2)
    # Drawing horizontal lines
    pygame.draw.line(screen,(125,100,165),(0,height/3),(width, height/3),2)
    pygame.draw.line(screen,(125,100,165),(0,height/3*2),(width, height/3*2),2)            

def check_win():
    global TTT,winner,draw
    #Winning rows
    for row in range (0,3):
        if ((TTT [row][0] == TTT[row][1] == TTT[row][2]) and(TTT [row][0] is not None)):
            # this row won
            winner = TTT[row][0]          
            break
    #Winning columns
    for col in range (0, 3):
        if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):
            winner = TTT[0][col]       
            break
    #Diagonal winners
        if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
            winner = TTT[0][0]
       
        if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
         winner = TTT[0][2]
    
    if(all([all(row) for row in TTT]) and winner is None ):
        draw = True
    pop_up()

def drawX_or_O(row,col):
    global TTT,X_or_O
    if row==1:
        pos_x = 30
    if row==2:
        pos_x = width/3 + 30
    if row==3:
        pos_x = (width/3)*2 + 30

    if col==1:
        pos_y = 30
    if col==2:
        pos_y = height/3 + 30
    if col==3:
        pos_y = (height/3)*2 + 30
    TTT[row-1][col-1] = X_or_O
    if(X_or_O == 'x'):
        screen.blit(img_X,(pos_y,pos_x))
        X_or_O= 'o'
    else:
        screen.blit(img_O,(pos_y,pos_x))
        X_or_O = 'x'
    pygame.display.update()
    
def mouse_input():
    x,y = pygame.mouse.get_pos()
    if(x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif(x<width):
        col = 3
    else:
        col = None
        

    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None

    if(row and col and TTT[row-1][col-1] is None):
        global X_or_O
        drawX_or_O(row,col)
        check_win()

def pop_up():
        global switch
        switch = False
        if winner:
            message = "The Winner is "+ winner+"!!!"
            messagebox.showinfo("Tic-Tac-Toe", message)
            switch = True
              
        elif draw:
            message = 'DRAWWWWW!'
            messagebox.showinfo("Tic-Tac-Toe", message)
            switch = True
            
        if switch:
            message = 'Do you want to play again?'
            messagebox.askyesno("Tic-Tac-Toe", message)
            if messagebox.askyesno("Tic-Tac-Toe", message):
                reset_game()
            else:
                pygame.quit()
                sys.exit()              

def reset_game():
    global TTT, winner,X_or_O, draw
    time.sleep(1)
    X_or_O = 'x'
    mainPage()
    draw = False
    winner=False
    TTT = [[None]*3,[None]*3,[None]*3]
    
mainPage()

while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouse_input()
            if(winner or draw):
                reset_game()
    pygame.display.update()
    CLOCK.tick(fps)
