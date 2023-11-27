import pygame

from stickFigure import *
from letters import *
from words import * 


# create a class to handle events
class hangmanHandler():
    
    # pass in display in handler 
    def __init__(self,display):
        self.display = display
        # Initialize guesses the player has
            # the player will have 6 guesses
        self.incorrectGuesses = 6 
        # Initialize the number of guesses allowed
            # the player will start off with 0 guessed attempts
        self.numGuesses = 0
        
        self.guessedLetters = []
        
        # initialize font to print on pygame window
        self.gameFont = pygame.font.Font(None, 40)

        # create letter object
        self.Letters = letters()
   

    # create a method to listen for events being called
    def listen(self,qoe,guessingWordsObj,hangmanImg): # qoe A.K.A Queue Of Events
        for event in qoe:
            if event.type == pygame.QUIT:
                mainDisplay = pygame.display.set_mode((1250,900)) #(X,Y)
                self.run = False
               
            # create event type to register button being clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                #  get the x, and y position of when the event occurs
                x,y = event.pos
                # use a for loop to create a button for every letter on screen
                    # for loop will be similar to letters.py 
                for i in range(26):
                    # create the row and coulmns for the buttons
                    row = i // 13
                    column = i % 13
                    # generate the buttons for the letters 
                    totalWidth = 13 * (40 + 10)
                    totalHeight = 2 * (40 + 10)
                    # center the buttons to the center of the screen
                    # column * (40 + 10) is used to calculate the x position based on the column idex
                    xButton = ((800 - totalWidth) / 2) + column * (40 + 10)
                    # position the buttons near the bottom of the screen
                    # row * (40 + 10) is used to calculate the y position based on the row idex
                    yButton = (450 - totalHeight) + row * (40 + 10)
                    
                    # check if the event happens
                    if xButton <= x <= xButton + 40 and yButton <= y <= yButton + 40:
                        print(f"You clicked: {chr(ord('A') + i)}")
                        # Update guessed letters
                        guessingWordsObj.guessLetters(chr(ord('A') + i))
                        
                        guessedLetters = chr(ord('A') + i)
                        
                        self.guessedLetters.append(guessedLetters)
                        # Redraw the word
                        guessingWordsObj.printWord(self.display)
                        # Update the display
                        pygame.display.update()
                        # Check to see if the player guessed the word.
                        # if the player guessed wrong, reload hangman Imag
                        # decrement 
                        if guessingWordsObj.wrongGuess(guessedLetters):
                             hangmanImg.reloadSF() 
                             self.incorrectGuesses -= 1
                        if guessingWordsObj.checkWin():
                            print("You did it you won the game! Would you like to play again?")
                        if self.incorrectGuesses == self.numGuesses:
                            print("Better luck next time")
                            self.run = False
                            mainDisplay = pygame.display.set_mode((1250,900)) #(X,Y)

            if event.type == pygame.KEYDOWN:
                # if the user presses r 
                if event.key == pygame.K_r:  
                    # reset number of guesses 
                    self.resetGuessCount()
                    # reset the hangman image back to starting image
                    hangmanImg.resetSF() 
                    # reset guessing word
                    guessingWordsObj.resetGW()
                    # re-print the word onto the screen
                    guessingWordsObj.printWord(self.display)
                 # if the user presses q
                elif event.key == pygame.K_q:  
                    # close the game
                    self.run = False
                    mainDisplay = pygame.display.set_mode((1250,900)) #(X,Y)

    # print the number of guesses onto the screen
    def printNumGuess(self):
        # converts incorrect guesses from an int to a string 
        self.printGuess = self.gameFont.render(str(self.incorrectGuesses),True,(0,0,0))
        # message that will be rendered and displayed on screen
        self.guessDisplay = f"Number of guesses remaining: {self.incorrectGuesses}"
        # render guessDisplay
        self.guessDisplayRender = self.gameFont.render(self.guessDisplay,True,(0,0,0))
        # blit guessDisplay render to the screen
        self.display.blit(self.guessDisplayRender,(3,520))
        # update display when called 
        

    # method to print guessed letters to the screen 
    def printGuessedLetters(self):
        self.chosenLetters = f"Chosen Letters {self.guessedLetters}"
        
        self.printGL = self.gameFont.render(self.chosenLetters,True,(0,0,0))
        
        self.display.blit(self.printGL,(3,550))
        
    # method to print retry message to the screen 
    def Retry(self):
        self.Retrymsg  = f"Reset game by pressing r, or quit by pressing q"
        
        self.printRetrymsg = self.gameFont.render(self.Retrymsg,True,(0,0,0))
        
        self.display.blit(self.printRetrymsg,(3,490))
        
    # method to reset the number of incorrect guesses back to 6 and clear the guessedLetters list
    def resetGuessCount(self):
        self.incorrectGuesses = 6  
        
        self.guessedLetters.clear()

    def playGame(self, disp, dispWord, sFigure):
        self.run = True
        while self.run:
            # fill in display backgroung 
            disp.fill((255,255,255))
            
            gameClock = pygame.time.Clock()
            
            # call listen method in hangmanHandler to listen for events
            self.listen(pygame.event.get(),dispWord,sFigure)
            
            # draw stick figure img onto screen
            sFigure.drawStickFigure(disp)
            
            # draw letters onto screen
            self.Letters.drawLetters(disp)
        
            # draw word onto the screen
            dispWord.printWord(disp)
            
            # draw the number of guesses onto the screen
            self.printNumGuess()
            
            self.printGuessedLetters()

            self.Retry() 
            # update the display using flip
            pygame.display.flip()

            gameClock.tick(60)
        
            
        
