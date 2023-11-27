import pygame

from hangmanHandler import * 
pygame.init()

# generate a display

disp = pygame.display.set_mode((800,600))

# set window caption to hangman
pygame.display.set_caption("Hangman")

# create handler object and pass in display
handler = hangmanHandler(disp)

# create letter object
Letters = letters()

# create stick figure object
sFigure = StickFigure()

# create object to display words 
dispWord = guessingWords()

# create a loop to update the display 
while(True):
    # fill in display backgroung 
    disp.fill((255,255,255))
    
    gameClock = pygame.time.Clock()
    
    # call listen method in hangmanHandler to listen for events
    handler.listen(pygame.event.get(),dispWord,sFigure)
    
    # draw stick figure img onto screen
    sFigure.drawStickFigure(disp)
    
    # draw letters onto screen
    Letters.drawLetters(disp)
   
    # draw word onto the screen
    dispWord.printWord(disp)
    
    # draw the number of guesses onto the screen
    handler.printNumGuess()
    
    handler.printGuessedLetters()

    handler.Retry() 
    # update the display using flip
    pygame.display.flip()
    
    gameClock.tick(60) 
