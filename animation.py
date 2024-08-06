import pygame as py
from system import *
from settings import *
from button import *
from sounds import *

py.init()

def cpuAnimateMove(screen, cpuMove):

    #creating surfaace
    cpuSurface = py.Surface((CPU_WIDTH * 1.15, CPU_HEIGHT * 1.15), py.SRCALPHA)
    
    #loading the image
    if cpuMove == "rock":
        cpuImage = py.image.load("assets/cpu/computerRock.png").convert_alpha()
        cpuImage = py.transform.scale(cpuImage, (CPU_WIDTH * 1.15, CPU_HEIGHT * 1.15))
        cpuSurface.blit(cpuImage, (10, 10))
        screen.blit(cpuSurface, (230, 275))
    elif cpuMove == "paper":
        cpuImage = py.image.load("assets/cpu/computerPaper.png").convert_alpha()
        cpuImage = py.transform.scale(cpuImage, (CPU_WIDTH * 1.15, CPU_HEIGHT * 1.15))
        cpuSurface.blit(cpuImage, (10, 10))
        screen.blit(cpuSurface, (201, 275))
    elif cpuMove == "scissors":
        cpuImage = py.image.load("assets/cpu/computerScissors.png").convert_alpha()
        cpuImage = py.transform.scale(cpuImage, (CPU_WIDTH * 1.15, CPU_HEIGHT * 1.15))
        cpuSurface.blit(cpuImage, (10, 10))
        screen.blit(cpuSurface, (228, 275))

    #updating the display so we can see changes
    py.display.update()

    stall(1000)

def playerAnimateMove(screen, playerMove):
    
    playerSurface = py.Surface((PLAYER_WIDTH, PLAYER_HEIGHT), py.SRCALPHA)
    
    if playerMove == "rock":
        playerImage = py.image.load("assets/player/playerMoves/playerRock.png").convert_alpha()
    elif playerMove == "paper":
        playerImage = py.image.load("assets/player/playerMoves/playerPaper.png").convert_alpha()
    elif playerMove == "scissors":
        playerImage = py.image.load("assets/player/playerMoves/playerScissors.png").convert_alpha()

    playerImage = pixelizer(playerImage, PLAYER_WIDTH, PLAYER_HEIGHT)

    playerSurface.blit(playerImage, (-80, -80))

    screen.blit(playerSurface, (400, 300))

#this function calls the "plyaerAnimateWindupFrame" function to animate each frame
#this method is mainly for code cleanup
def playerAnimateWindup(screen, background, playerScore, cpuScore):

    #animating the player's "windup"
    refresh(screen, background, playerScore, cpuScore)

    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame1.png", PLAYER_WIDTH, PLAYER_HEIGHT, -80, -80, 430, 229)
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame2.png", PLAYER_WIDTH, PLAYER_HEIGHT, -80, -80, 429, 229)
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame3.png", PLAYER_WIDTH, PLAYER_HEIGHT, -80, -80, 429, 229)
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame4.png", PLAYER_WIDTH, PLAYER_HEIGHT + 10, -40, -40, 389, 179)
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame5.png", PLAYER_WIDTH, PLAYER_HEIGHT, -40, -40, 409, 189)
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame4.png", PLAYER_WIDTH, PLAYER_HEIGHT + 10, -40, -40, 389, 179)
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame3.png", PLAYER_WIDTH, PLAYER_HEIGHT, -80, -80, 429, 229)
    refresh(screen, background, playerScore, cpuScore)

def playerAnimateWindDown(screen, background, playerScore, cpuScore):
    
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame2.png", PLAYER_WIDTH, PLAYER_HEIGHT, -80, -80, 430, 229)
    refresh(screen, background, playerScore, cpuScore)
    playerAnimateWindupFrame(screen, "assets/player/playerWindup/playerWindupFrame1.png", PLAYER_WIDTH, PLAYER_HEIGHT, -80, -80, 429, 229)
    refresh(screen, background, playerScore, cpuScore)

def playerAnimateWindupFrame(screen, file, surfaceWidth, surfaceHeight, imageX, imageY, screenX, screenY):
    
    playerWindupSurface = py.Surface((surfaceWidth, surfaceHeight), py.SRCALPHA)

    frame = py.image.load(file).convert_alpha()
    
    frame = pixelizer(frame, surfaceWidth, surfaceHeight)

    playerWindupSurface.blit(frame, (imageX, imageY))

    screen.blit(playerWindupSurface, (screenX, screenY))
    py.display.update()

    stall(100)

def winAnimation(result, screen):

    wins = "WINS"
    win = "WIN"
    tie = "TIE"

    font = py.font.Font("assets/fonts/mainFont.ttf", fontSize + 15)    

    if result == "cpu":
        roundLoseSound.set_volume(.1)
        roundLoseSound.play()
        winText2 = font.render("PHIL", False, "red")
        winText1 = font.render(wins, False, "white")
        screen.blit(winText2, (280, 100))
        screen.blit(winText1, (390, 100))
    elif result == "player":
        roundWinSound.set_volume(.1)
        roundWinSound.play()
        winText2 = font.render("YOU", False, "green")
        winText1 = font.render(win, False, "white")
        screen.blit(winText2, (300, 100))
        screen.blit(winText1, (400, 100))
    elif result == "tie":
        roundTieSound.set_volume(.1)
        roundTieSound.play()
        winText2 = font.render("TIE", False, "white")
        screen.blit(winText2, (350, 100))
        py.display.update()
        return
    
    

    
    
    py.display.update()

def playerEnding(screen, background):

    playerWinTheme.set_volume(.05)
    playerWinTheme.play(loops = -1)

    blankRefresh(screen, background)

    transitionBackground(screen, "green")
    
    stall(2000)

    messageFont = py.font.Font("assets/fonts/playerEndingFont.ttf", 26)
    messageFontSurface = messageFont.render("YOU HAVE SURVIVED!", True, "black")

    messageSurface = py.Surface((400, 150), py.SRCALPHA)

    messageFontX = (messageSurface.get_width() - messageFontSurface.get_width()) // 2
    messageFontY = (messageSurface.get_height() - messageFontSurface.get_height()) // 2

    scrollImage = py.image.load("assets/backgrounds/playerEnding/winMessage.png").convert_alpha()

    scrollImage = pixelizer(scrollImage,400, 150)

    
    messageSurface.blit(scrollImage, (0, 0))
    messageSurface.blit(messageFontSurface, (messageFontX, messageFontY))

    screen.blit(messageSurface, (200, 200))

    py.display.update()

    stall(2000)

    item = playAgainPlayer(screen)
    return True


def cpuEnding(screen, background):
    blankRefresh(screen, background)
    item = cpuEndingAnimation(screen)
    return item

def cpuEndingAnimation(screen):

    playerBreathing.set_volume(.1)
    playerBreathing.play(loops = -1)

    for i in range(1,6):

        endingImage = py.image.load(f"assets/backgrounds/cpuEnding/backgroundRightyFrame{i}.png").convert_alpha()

        endingImage = pixelizer(endingImage, WIDTH, HEIGHT)

        screen.blit(endingImage, (0, 0))

        py.display.update()
        stall(10//i)
    
    item = cpuEndingFace(screen)

    return item

def cpuEndingFace(screen):
    
    #creating font for Phil's ending
    font = py.font.Font("assets/fonts/mainFont.ttf", fontSize)
    
    #displaying Phil close up with eyes closed
    screen.fill("black")

    py.display.update()

    stall(1000)

    #showing Phil with just his eyes
    endingFace = py.image.load("assets/cpu/cpuEyes.png").convert_alpha()

    endingFace = pixelizer(endingFace, endingFace.get_width(), endingFace.get_height())

    screen.blit(endingFace, (300, 100))

    py.display.update()

    stall(3000)

    #Phil speaking with just his eyes open
    firstLine = font.render("It seems that you've lost...", False, "white")

    screen.blit(firstLine, (75, 50))

    py.display.update()

    stall(3000) 

    #Phil showing his eyes and teeth

    screen.fill("black")

    teeth = py.image.load("assets/cpu/cpuSmile.png")

    teeth = pixelizer(teeth, teeth.get_width(), teeth.get_height())

    teeth = pixelizer(teeth, teeth.get_width(), teeth.get_height())

    teeth = pixelizer(teeth, teeth.get_width(), teeth.get_height())

    screen.blit(teeth, (250, 300))

    screen.blit(endingFace, (300, 100))

    py.display.update()

    stall(3000)

    #Phil speaking with his eyes and teeth
    secondLine = font.render("Your death will be swift...", False, "white")
    
    screen.blit(secondLine, (75, 50))

    py.display.update()

    stall(3000)

    playerBreathing.stop()

    cpuWindup.set_volume(.1)
    cpuWindup.play()

    #filling the screen with red
    bloodBackground = py.image.load("assets/backgrounds/cpuEnding/bloodBackground.jpg")

    bloodBackground = py.transform.scale(bloodBackground, (WIDTH, HEIGHT))

    screen.blit(bloodBackground, (0, 0))

    py.display.update()

    stall(500)

    #displaying the "you died" screen
    deathLineFont = py.font.Font("assets/fonts/mainFont.ttf", 40)

    deathLine = deathLineFont.render("YOU DIED", False, "white")

    screen.blit(deathLine, (300, 250))

    py.display.update()

    stall(500)

    return playAgainCPU(screen)


def playAgainCPU(screen):
    
    yesNoButtons = [
        Button("Play Again", (325, 400), 150, 50, "gray", "black"),
        Button("Quit", (325, 475), 150, 50, "gray", "black")
    ]

    while True:

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.MOUSEBUTTONDOWN:
                for button in yesNoButtons:
                    clickedButton, text = button.handleEvent(event)

                    if clickedButton:
                        if text.lower() == "play again":
                            return True
                        
                        else:
                            py.quit()
                            sys.exit()

        for button in yesNoButtons:
            button.draw(screen)

        py.display.update()

def playAgainPlayer(screen):
    
    yesNoButtons = [
        Button("Play Again", (325, 400), 150, 50, "gray", "black"),
        Button("Quit", (325, 475), 150, 50, "gray", "black")
    ]

    while True:

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()

            if event.type == py.MOUSEBUTTONDOWN:
                for button in yesNoButtons:
                    clickedButton, text = button.handleEvent(event)

                    if clickedButton:
                        if text.lower() == "play again":
                            return True
                        
                        else:
                            py.quit()
                            sys.exit()

        for button in yesNoButtons:
            button.draw(screen)

        py.display.update()
    