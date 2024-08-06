import pygame as py
import sys
from settings import *

playerScore = 0
userScore = 0

#This function is meant to stall time for animations
def stall(stallTime):

    startTime = py.time.get_ticks()
    
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
        
        currentTime = py.time.get_ticks()

        if currentTime - startTime >= stallTime:
            return 
        
        py.display.update()

def pixelizer(image, width, height):
    
    image = py.transform.scale(image, (width // 4, height // 4))
    image = py.transform.scale(image, (width, height))

    return image

def refresh(screen, background, playerScore, cpuScore):

    screen.blit(background, (0, 0))

    displayScore(playerScore, cpuScore, screen)

    py.display.update()

def blankRefresh(screen, background):
    
    screen.blit(background, (0, 0))

    py.display.update()
                
def displayScore(playerScore, cpuScore, screen):

    scoreSurface = py.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))

    font = py.font.Font("assets/fonts/mainFont.ttf", fontSize - 5)

    playerText = font.render("Your Score: " + str(playerScore), False, "white")

    cpuText = font.render("Phil's Score: " + str(cpuScore), False, "white")

    screen.blit(cpuText, (10, 10))

    screen.blit(playerText, (650, 10))

    py.display.update()
    
def transitionBackground(screen, newColor):
    # Fade out the current screen
    fadeScreenOut(screen)

    py.display.update()

    # Fade in to the new background
    fadeScreenIn(screen)


def fadeScreenOut(screen):

    fadeSurface = py.Surface((WIDTH, HEIGHT))
    fadeSurface.fill("black")

    for alpha in range(0, 50, 1):
        print(alpha)
        fadeSurface.set_alpha(alpha)
        screen.blit(fadeSurface, (0, 0))
        py.display.update()
        py.time.delay(50)

def fadeScreenIn(screen):

    fadeSurface = py.Surface((WIDTH, HEIGHT))

    playerWinBackground = py.image.load("assets/backgrounds/playerEnding/playerWinSky.jpg")

    playerWinBackground = pixelizer(playerWinBackground, WIDTH, HEIGHT)
    
    fadeSurface.blit(playerWinBackground, (0, 0))

    for alpha in range(50 ,0, -1):
        print(alpha)
        fadeSurface.set_alpha(alpha)
        screen.blit(fadeSurface, (0, 0))
        py.display.update()
        py.time.delay(50)