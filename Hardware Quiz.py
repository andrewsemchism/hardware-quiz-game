# Andrew Semchism
# A hardware quiz
# June 16 2017

import pygame, sys, random
from pygame.locals import *


pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock() # create clock object
# set the size of the display window in pixels
Display_Surface = pygame.display.set_mode((800, 600))
# change the caption of the display window
pygame.display.set_caption('Hardware Quiz')
# Load images
titleImg = pygame.image.load('homelogo.png')
backroundImg = pygame.image.load('backround.png')
playImg = pygame.image.load('play.png')
custom1Img = pygame.image.load('custom1.png')
custom2Img = pygame.image.load('custom2.png')
custom3Img = pygame.image.load('custom3.png')
custom4Img = pygame.image.load('custom4.png')
custom5Img = pygame.image.load('custom5.png')
custom1miniImg = pygame.image.load('custom1mini.png')
custom2miniImg = pygame.image.load('custom2mini.png')
custom3miniImg = pygame.image.load('custom3mini.png')
custom4miniImg = pygame.image.load('custom4mini.png')
custom5miniImg = pygame.image.load('custom5mini.png')
arrowright = pygame.image.load('arrowright.png')
arrowleft = pygame.image.load('arrowleft.png')
nextImg = pygame.image.load('next.png')
questionImg = pygame.image.load('Questions.png')
ramImg = pygame.image.load('ram.png')
cpuImg = pygame.image.load('cpu.png')
keyboardImg = pygame.image.load('keyboard.png')
byteImg = pygame.image.load('byte.png')
scannerImg = pygame.image.load('scanner.png')


# Homescreen
def homescreen():
    Display_Surface.blit(backroundImg, (0, 0))
    Display_Surface.blit(playImg, (270, 400))
    Display_Surface.blit(titleImg, (20, 100))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN: # check if mouse button is pressed down
            if event.button == 1: # check if the left mouse button is pressed down
                # get the position of the mouse
                mouseX, mouseY = pygame.mouse.get_pos()
                # determine if the position of the mouse is on play button
                if mouseX > 270 and mouseX < 500 and mouseY > 400 and mouseY < 540:
                    global screen
                    screen = 1

                
# Player 1 Character
def player1Create():
    global character
    Display_Surface.blit(backroundImg, (0, 0))
    font = pygame.font.SysFont("monospace", 39)
    choosePlayerText = font.render("Player 1, choose your character!", 1, (230,66,66))
    Display_Surface.blit(choosePlayerText, (32, 15))
    Display_Surface.blit(arrowright, (495, 200))
    Display_Surface.blit(arrowleft, (80, 200))
    Display_Surface.blit(nextImg, (550, 500))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN: # check if mouse button is pressed down
            if event.button == 1: # check if the left mouse button is pressed down
                # get the position of the mouse
                mouseX, mouseY = pygame.mouse.get_pos()
                # determine if the position of the mouse is on play button
                if mouseX > 110 and mouseX < 290 and mouseY > 200 and mouseY < 420:
                    character -= 1
                    if character == 0:
                        character = 5
                if mouseX > 540 and mouseX < 710 and mouseY > 200 and mouseY < 420:
                    character += 1
                    if character == 6:
                        character = 1
                if mouseX > 550 and mouseX < 800 and mouseY > 500 and mouseY < 600:
                    global player1Img
                    global player1miniImg
                    if character == 1:
                        player1Img = Display_Surface.blit(custom1Img, (250, 100))
                        player1miniImg = pygame.image.load('custom1mini.png')
                    elif character == 2:
                        player1Img = Display_Surface.blit(custom2Img, (250, 100))
                        player1miniImg = pygame.image.load('custom2mini.png')
                    elif character == 3:
                        player1Img = Display_Surface.blit(custom3Img, (250, 100))
                        player1miniImg = pygame.image.load('custom3mini.png')
                    elif character == 4:
                        player1Img = Display_Surface.blit(custom4Img, (250, 100))
                        player1miniImg = pygame.image.load('custom4mini.png')
                    elif character == 5:
                        player1Img = Display_Surface.blit(custom5Img, (250, 100))
                        player1Img = pygame.image.load('custom5mini.png')
                    global currentPlayerminiImg
                    currentPlayerminiImg = player1miniImg
                    global screen
                    screen = 2


    if character == 1:
        Display_Surface.blit(custom1Img, (250, 100))
    elif character == 2:
        Display_Surface.blit(custom2Img, (250, 100))
    elif character == 3:
        Display_Surface.blit(custom3Img, (250, 100))
    elif character == 4:
        Display_Surface.blit(custom4Img, (250, 100))
    elif character == 5:
        Display_Surface.blit(custom5Img, (250, 100))

# Player 2 Character
def player2Create():
    global character
    Display_Surface.blit(backroundImg, (0, 0))
    font = pygame.font.SysFont("monospace", 39)
    choosePlayerText = font.render("Player 2, choose your character!", 1, (230,66,66))
    Display_Surface.blit(choosePlayerText, (32, 15))
    Display_Surface.blit(arrowright, (495, 200))
    Display_Surface.blit(arrowleft, (80, 200))
    Display_Surface.blit(nextImg, (550, 500))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN: # check if mouse button is pressed down
            if event.button == 1: # check if the left mouse button is pressed down
                # get the position of the mouse
                mouseX, mouseY = pygame.mouse.get_pos()
                # determine if the position of the mouse is on play button
                if mouseX > 110 and mouseX < 290 and mouseY > 200 and mouseY < 420:
                    character -= 1
                    if character == 0:
                        character = 5
                if mouseX > 540 and mouseX < 710 and mouseY > 200 and mouseY < 420:
                    character += 1
                    if character == 6:
                        character = 1
                if mouseX > 550 and mouseX < 800 and mouseY > 500 and mouseY < 600:
                    global player2Img
                    global player2miniImg
                    if character == 1:
                        player2Img = Display_Surface.blit(custom1Img, (250, 100))
                        player2miniImg = pygame.image.load('custom1mini.png')
                    elif character == 2:
                        player2Img = Display_Surface.blit(custom2Img, (250, 100))
                        player2miniImg = pygame.image.load('custom2mini.png')
                    elif character == 3:
                        player2Img = Display_Surface.blit(custom3Img, (250, 100))
                        player2miniImg = pygame.image.load('custom3mini.png')
                    elif character == 4:
                        player2Img = Display_Surface.blit(custom4Img, (250, 100))
                        player2miniImg = pygame.image.load('custom4mini.png')
                    elif character == 5:
                        player2Img = Display_Surface.blit(custom5Img, (250, 100))
                        player2miniImg = pygame.image.load('custom5mini.png')
                    global screen
                    screen = 3


    if character == 1:
        Display_Surface.blit(custom1Img, (250, 100))
    elif character == 2:
        Display_Surface.blit(custom2Img, (250, 100))
    elif character == 3:
        Display_Surface.blit(custom3Img, (250, 100))
    elif character == 4:
        Display_Surface.blit(custom4Img, (250, 100))
    elif character == 5:
        Display_Surface.blit(custom5Img, (250, 100))

def quiz(List, player, playerminiImg):
    if currentQuestion in allQuestions:
        allQuestions.remove(currentQuestion)
    Display_Surface.blit(backroundImg, (0, 0))
    Display_Surface.blit(questionImg, (0, 0))
    Display_Surface.blit(playerminiImg,(610, 110))
    Display_Surface.blit(List[6],(100, 70))
    font = pygame.font.SysFont("Arial", 28)
    question = font.render(List[0], 1, (230,66,66))
    Display_Surface.blit(question, (55, 20))
    playernumber = font.render(player, 1, (230,66,66))
    Display_Surface.blit(playernumber, (620, 20))
    a = font.render(List[1], 1, (230,66,66))
    Display_Surface.blit(a, (50, 385))
    b = font.render(List[2], 1, (230,66,66))
    Display_Surface.blit(b, (430, 385))
    c = font.render(List[3], 1, (230,66,66))
    Display_Surface.blit(c, (50, 510))
    d = font.render(List[4], 1, (230,66,66))
    Display_Surface.blit(d, (430, 510))
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN: # check if mouse button is pressed down
            if event.button == 1: # check if the left mouse button is pressed down
                # get the position of the mouse
                mouseX, mouseY = pygame.mouse.get_pos()
                # determine if the position of the mouse is on a
                if mouseX > 30 and mouseX < 375 and mouseY > 360 and mouseY < 460:
                    if currentQuestion[5] == "a":
                        correct(player)
                    else:
                        wrong(player)
                # determine if the position of the mouse is on b
                if mouseX > 430 and mouseX < 775 and mouseY > 360 and mouseY < 460:
                    if currentQuestion[5] == "b":
                        correct(player)
                    else:
                        wrong(player)
                # determine if the position of the mouse is on c
                if mouseX > 30 and mouseX < 375 and mouseY > 490 and mouseY < 575:
                    if currentQuestion[5] == "c":
                        correct(player)
                    else:
                        wrong(player)
                # determine if the position of the mouse is on d
                if mouseX > 430 and mouseX < 775 and mouseY > 490 and mouseY < 575:
                    if currentQuestion[5] == "d":
                        correct(player)
                    else:
                        wrong(player)

def correct(player):
    click = False
    while click == False:
        Display_Surface.blit(backroundImg, (0, 0))
        font = pygame.font.SysFont("Arial", 200)
        text = font.render("Correct!", 1, (230, 66, 66))
        font1 = pygame.font.SysFont("Arial", 60)
        text1 = font1.render("Click anywhere to continue.", 1, (230, 66, 66))
        Display_Surface.blit(text1, (105, 500))
        Display_Surface.blit(text, (100, 200))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:  # check if mouse button is pressed down
                if event.button == 1:  # check if the left mouse button is pressed down
                    click = True
                    global screen
                    screen += 1
        pygame.display.update()
        # check frame rate
        fpsClock.tick(FPS)
    filename = player + " score.txt"
    outFile = open(filename, "a")
    outFile.write("Correct" + "\n")
    outFile.close()
    global currentQuestion
    currentQuestion = random.choice(allQuestions)

def wrong(player):
    click = False
    while click == False:
        Display_Surface.blit(backroundImg, (0, 0))
        font = pygame.font.SysFont("Arial", 200)
        text = font.render("Wrong!", 1, (230, 66, 66))
        font1 = pygame.font.SysFont("Arial", 60)
        text1 = font1.render("Click anywhere to continue.", 1, (230, 66, 66))
        Display_Surface.blit(text1, (105, 500))
        Display_Surface.blit(text, (130, 200))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:  # check if mouse button is pressed down
                if event.button == 1:  # check if the left mouse button is pressed down
                    click = True
                    global screen
                    screen += 1
        pygame.display.update()
        # check frame rate
        fpsClock.tick(FPS)
    filename = player + " score.txt"
    outFile = open(filename, "a")
    outFile.write("Wrong" + "\n")
    outFile.close()
    global currentPlayer
    global currentPlayerminiImg
    if currentPlayer == "Player 1":
        currentPlayer = "Player 2"
        currentPlayerminiImg = player2miniImg
    elif currentPlayer == "Player 2":
        currentPlayer = "Player 1"
        currentPlayerminiImg = player1miniImg
    global currentQuestion
    currentQuestion = random.choice(allQuestions)

# List of questions. You can easily add or remove questions from the game here!
# Format: Name = ["Question", "A", "B", "C", "D", "answer", image]

RAM = ["What is this computer component?", "A) Motherboard", "B) RAM", "C) CPU", "D) Hard Drive", "b", ramImg]
CPU = ["What is this computer component?", "A) CPU", "B) Power Supply", "C) Video Card", "D) DVD Drive", "a", cpuImg]
Keyboard = ["What is this computer component?", "A) Mouse", "B) Speakers", "C) Router", "D) Keyboard", "d", keyboardImg]
Byte = ["Memory conversion question!", "A) 1,000", "B) 1,000,000", "C) 10,000", "D) 100,000", "b", byteImg]
Scanner = ["What is this computer accessory?", "A) Scanner", "B) Speakers", "C) Monitor", "D) USB", "d", scannerImg]
# List of all questions. If you add a question above, make sure to add it to this list too!
allQuestions = [RAM, CPU, Keyboard, Byte]

# Variables defined before main loop
currentPlayer = "Player 1"
currentQuestion = random.choice(allQuestions)
open("Player 1 score.txt", "w")
open("Player 2 score.txt", "w")
character = 1
screen = 0
while True: # main loop
    if screen == 0:
        homescreen()
    if screen == 1:
        player1Create()
    if screen == 2:
        player2Create()
    if screen == 3:
        quiz(currentQuestion, currentPlayer, currentPlayerminiImg)
    if screen == 4:
        quiz(currentQuestion, currentPlayer, currentPlayerminiImg)
    if screen == 5:
        quiz(currentQuestion, currentPlayer, currentPlayerminiImg)
    if screen == 6:
        quiz(currentQuestion, currentPlayer, currentPlayerminiImg)





    # check events that occur
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # update the display window
    pygame.display.update()
    # check frame rate
    fpsClock.tick(FPS)
