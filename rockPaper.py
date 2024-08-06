import pygame as py
import random as rd
import sys
from settings import *
from button import * 
from system import *
from animation import *
from sounds import *
from collections import Counter

py.init()

#MAIN GAME BUTTONS
#---------------------------------------------------------------------------------------
#creating buttons
buttons = [
    Button("Rock", (BUTTON_X - BUTTON_OFFSET, BUTTON_Y), 150, 75, "gray", "white"),
    Button("Paper", ((BUTTON_X + BUTTON_PADDING) - BUTTON_OFFSET, BUTTON_Y), 150, 75, "gray", "white"),
    Button("Scissors", ((BUTTON_X + (BUTTON_PADDING * 2)) - BUTTON_OFFSET, BUTTON_Y), 150, 75, "gray", "white"),
    Button("spill", (360, 265), 20, 70, "white", "white")
]
#---------------------------------------------------------------------------------------

#MAIN MENU BUTTON
#---------------------------------------------------------------------------------------
titleButtons = [
    Button("Play", (550, 450), 175, 50, "gray", "white"),
    Button("Quit", (550, 525), 175, 50, "gray", "white")
]
#---------------------------------------------------------------------------------------

#storing move possibilities
moves = ["rock", "paper", "scissors"]

screen = py.display.set_mode((WIDTH, HEIGHT))

#setting a title for the window
py.display.set_caption("rockPaperP̷͎͕͚̲̞͎͈͚̍̇̇́͌͛́̓͊͑̃̇̾̈́̽̽͒͗̈͆͘̚͘͠h̶͚͓̤̠͍̣̤̣̪͖̘̦̒̇̈́͆̈́͛̄͑̓̍̍̈̿̀͘͠͝i̵̡̛̝͎̯̗̖̭͒̂́̿͆̂͊̈͊̂̎͒̓͑͘͜͝l̷̢̡̞͓͎̖̞̼͍͙͇̭͎͈͉̬̰̠̞̪̪̀̐̆͜")

#GAME BACKGROUND
#---------------------------------------------------------------------------------------
#assigning an image as the background
background = py.image.load("assets/backgrounds/mainGame/backgroundRighty.jpg").convert_alpha()

#editing the image clarity
background.set_alpha(None)

#adjusting the background to fit within the bounds of the game window
background = pixelizer(background, WIDTH, HEIGHT)
#---------------------------------------------------------------------------------------

#MAIN MENU BACKGROUND
#---------------------------------------------------------------------------------------
mainMenuBackground = py.image.load("assets/backgrounds/mainMenu/mainMenu.jpg").convert_alpha()

mainMenuBackground = pixelizer(mainMenuBackground, WIDTH, HEIGHT)
#---------------------------------------------------------------------------------------

#MAIN MENU OVERLAY
#---------------------------------------------------------------------------------------
#creating a surface to put the title overlay on
mainMenuOverlaySurface = py.Surface((WIDTH, HEIGHT), py.SRCALPHA)

mainMenuOverlay = py.image.load("assets/backgrounds/mainMenu/mainMenuOverlay.png").convert_alpha()

mainMenuOverlay = pixelizer(mainMenuOverlay, WIDTH, HEIGHT)

mainMenuOverlaySurface.blit(mainMenuOverlay, (0, 0))
#---------------------------------------------------------------------------------------

#shows which action dominates the other
#the keys "beat" the values
wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

#storing the player's and the computer's score
playerScore = 0
cpuScore = 0

#storing the intro repeat
introDone = False

playerMoves = [0, 0, 0]

def intro():

    screen.blit(background, (0, 0))
    
    font = py.font.Font("assets/fonts/mainFont.ttf", fontSize)

    messages = [
                "You don't really know how you got here...",
                "That doesn't really matter though...",
                "This thing in front of you is named Phil...",
                "Phil wants to play Rock Paper Scissors...",
                "So good luck...",
                "You're going to need it..."]
    
    for index, message in enumerate(messages):

        messageText = font.render(message, False, "white")
        screen.blit(messageText, (25, 25))
        introAudio[index].set_volume(.1)
        introAudio[index].play()
        stall(3000)
        blankRefresh(screen, background)

#main game loop
#the game will run as long as the player and cpu haven't reach a 
#certain score
def mainGame():

    global introDone
    global playerScore
    global cpuScore

    playerScore = 0
    cpuScore = 0

    running = True

    #stopping the ending themes
    playerWinTheme.stop()

    mainMenuTheme.set_volume(.1)
    mainMenuTheme.play(loops = -1)
    mainMenu()

    if not introDone:
        mainMenuTheme.stop()
        intro()

    mainMenuTheme.stop()

    mainGameTheme.set_volume(.1)
    mainGameTheme.play(loops = -1)

    displayScore(playerScore, cpuScore, screen)

    while cpuScore < 3 and playerScore < 3:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

        #gathering the player/cpu movess
        playerMove = playerTurn()

        while playerMove == "spill":
            playerMove = playerTurn()
        
        cpuMove = cpuTurn()

        playerWindupGrunt.set_volume(.1)
        playerWindupGrunt.play()

        playerAnimateWindup(screen, background, playerScore, cpuScore)

        #sending the player move to animate
        playerAnimateMove(screen, playerMove)

        cpuWindup.set_volume(.05)
        cpuWindup.play()
        
        #sending the cpu move to animate
        cpuAnimateMove(screen, cpuMove)

        roundResult = determineWinner(playerMove, cpuMove)

        stall(1000)

        winAnimation(roundResult, screen)

        stall(3000)

        playerAnimateWindDown(screen, background, playerScore, cpuScore)

        displayScore(playerScore, cpuScore, screen)
    
    mainGameTheme.stop()

    if playerScore == 3:
        playAgain = playerEnding(screen, background)
        if playAgain:
            introDone = True
            mainGame()
    elif cpuScore == 3:
        playAgain = cpuEnding(screen, background)
        if playAgain:
            introDone = True
            mainGame()


#takes in the player's turn as input from various buttons
def playerTurn():

    global playerMoves

    screen.blit(background, (0, 0))
    
    while True:
        
        #polls for all pygame events
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            #checks if the left mouse button is pressed
            if event.type == py.MOUSEBUTTONDOWN:
                for button in buttons:
                    clickedButton, text = button.handleEvent(event)

                    if clickedButton:

                        if button.text == "spill":
                            spill()
                        elif button.text.lower() == "rock":
                            playerMoves[0] += 1
                        elif button.text.lower() == "paper":
                            playerMoves[1] += 1
                        elif button.text.lower() == "scissors":
                            playerMoves[2] += 1
                        
                        screen.blit(background, (0, 0))


                        return text.lower()
                    
                    
        #drawing buttons
        for button in buttons:
            if button.text != "spill":
                button.draw(screen)

        displayScore(playerScore, cpuScore, screen)

        py.display.update()

#generates the computer's move
#current option is RANDOM
#later implemenation will "predict" the player's next choice
def cpuTurn():
    
    global playerMoves

    maxMove = playerMoves.index(max(playerMoves))

    if moves[maxMove] == "rock":
        return moves[1]
    elif moves[maxMove] == "paper":
        return moves[2]
    else:
        return moves[0]

#iterates through winning possibilites to determine the winner
def determineWinner(playerMove, cpuMove):

    global playerScore, cpuScore

    #Checking for a tie
    if playerMove == cpuMove:
        return "tie"
    
    if wins[playerMove] == cpuMove:
        playerScore += 1
        return "player"
    
    if wins[cpuMove] == playerMove:
        cpuScore += 1
        return "cpu"

def mainMenu():
    running = True

    screen.blit(mainMenuBackground, (0, 0))
    screen.blit(mainMenuOverlaySurface, (0, 0))

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            
            if event.type == py.MOUSEBUTTONDOWN:
                for button in titleButtons:
                    clickedButton, text = button.handleEvent(event)

                    if clickedButton:
                        if text.lower() == "quit":
                            py.quit()
                            sys.exit()
                        else:
                            return
        
        for button in titleButtons:
            button.draw(screen)

        py.display.update()

def spill():

    font = py.font.Font("assets/fonts/mainFont.ttf", fontSize - 2)

    blankRefresh(screen, background)

    stall(1000)

    messages = ["There's no escape...   ", 
                "You are merely a puppet...", 
                "and I am the one pulling the strings..." , 
                "Your fate was sealed the moment you stepped into my world..."]
    
    for index, message in enumerate(messages):

        messageText = font.render(message, False, "white")
        screen.blit(messageText, (25, 25))
        spillAudio[index].set_volume(.1)
        spillAudio[index].play()
        stall(3000)
        blankRefresh(screen, background)

#calling the main game loop to start game
mainGame()

