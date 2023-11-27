import pygame
import random

from stickFigure import *

class guessingWords:
    def __init__(self):
        # create a list of words
        self.listOfWords = ["Gameboy", "Nintendo", "Tetris", "Galaga", "Pac Man", "Mega Man", "Donkey Kong", "Super Mario", 
                            "Gamecube", "Luigi", "Bowser", "Zelda", "Link","Star Fox","FZero","Metroid","Arcade","Dr Wylie", "Ganondorf",
                            "sonic"]
        
        # converts the words inside listOfWords to upper case letters
        self.listOfWordsUpper = [word.upper() for word in self.listOfWords]
        
        # select a word at random
        self.selectedWord = random.choice(self.listOfWordsUpper)
      
        # create empty list of guessed variables
        self.guessedLetters = []
        
        # create font for the selected words
        self.wordFont = pygame.font.Font(None,75)
        
        # test selected word
        print(f"Selected Word: {self.selectedWord}")

    # create a method to display the selected word onto the screen.
    def printWord(self, display):
        # create variable to display word
        self.displayWord = ""
        
        # word will first display nothing since word is hidden
        # create a loop to create " _ " characters for each letter in the word
        for i in self.selectedWord:
            # add spaces in bewteen words 
            # for words like Donkey Kong 
            if i == ' ':
                self.displayWord += ' '
            elif i in self.guessedLetters:
                self.displayWord += i + " "
            else:
                self.displayWord += "_ "
        self.wordText = self.wordFont.render(self.displayWord, True, (0,0,0))
        display.blit(self.wordText,(225,250))

    # add the letters chosen by the player to the guessedLetters list
    def guessLetters(self, letter):
        if letter not in self.guessedLetters: 
            # append upper case letters to the list
            self.guessedLetters.append(letter.upper())
        else:
            print(f"You've already guessed the letter {letter}")
            
    # create a method to check if all letters are guessed from the selected word
    def checkWin(self):
        for letter in self.selectedWord:
            # checks to see if upper case letters and if the charaters are alphabetic charactesr such as 'A'
            if letter.isalpha() and letter.upper() not in self.guessedLetters:
             return False
        else:   
            return True
    
    # create a method to determine if the player has guessed incorrectly
    def wrongGuess(self,letter): 
      # checks to see if the letter is not in the selected word
      if letter.upper() not in self.selectedWord:
          return True 
      else:
        return False
  
    def resetGW(self):
        # clear guessed letters
        self.guessedLetters.clear()
        
        # select a new random word from the list
        self.selectedWord = random.choice(self.listOfWordsUpper) 
        
        print(f"Selected word: {self.selectedWord}")
            
            
    

  
    
