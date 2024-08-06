import pygame as py

py.init()

py.mixer.init()

mainMenuTheme = py.mixer.Sound("assets/sounds/mainMenuTheme.wav")

mainGameTheme = py.mixer.Sound("assets/sounds/mainGameTheme.wav")

playerWindupGrunt = py.mixer.Sound("assets/sounds/playerWindupGrunt.wav")

cpuWindup = py.mixer.Sound("assets/sounds/cpuWindup.wav")

roundWinSound = py.mixer.Sound("assets/sounds/roundWinSound.wav")

roundTieSound = py.mixer.Sound("assets/sounds/roundTieSound.wav")

roundLoseSound = py.mixer.Sound("assets/sounds/roundLoseSound.wav")

playerBreathing = py.mixer.Sound("assets/sounds/playerBreathing.wav")

#Game Endings
playerWinTheme = py.mixer.Sound("assets/sounds/playerWinTheme.wav")


#Intro Audio
introVoice1 = py.mixer.Sound("assets/sounds/introVoice/introVoice1.wav")

introVoice2 = py.mixer.Sound("assets/sounds/introVoice/introVoice2.wav")

introVoice3 = py.mixer.Sound("assets/sounds/introVoice/introVoice3.wav")

introVoice4 = py.mixer.Sound("assets/sounds/introVoice/introVoice4.wav")

introVoice5 = py.mixer.Sound("assets/sounds/introVoice/introVoice5.wav")

introVoice6 = py.mixer.Sound("assets/sounds/introVoice/introVoice6.wav")

introAudio = [introVoice1, introVoice2, introVoice3, introVoice4, introVoice5, introVoice6]

#Spill Audio
spillVoice1 = py.mixer.Sound("assets/sounds/spillVoice/spillVoice1.wav")

spillVoice2 = py.mixer.Sound("assets/sounds/spillVoice/spillVoice2.wav")

spillVoice3 = py.mixer.Sound("assets/sounds/spillVoice/spillVoice3.wav")

spillVoice4 = py.mixer.Sound("assets/sounds/spillVoice/spillVoice4.wav")

spillAudio = [spillVoice1, spillVoice2, spillVoice3, spillVoice4]