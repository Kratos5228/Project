import pygame
# create letters class

class letters:
    def __init__(self):
        # create font for letters using pygame.font
            # instead of None you can use a different font style 
            # used None for default
            # 36 represents the Font Size 
        self.letterFont = pygame.font.Font(None,50)
        
        # create height and width of letters 
            # make a perfect square around the letter
        self.lHeight = 40
        self.lWidth = 40 
        
        # create a margin for letter spacing
        self.margin = 10
        
        # get the total width that is occupied by the 13 columns
        # and get the total height occupied by the 2 rows
        self.totalWidth = 13 * (self.lWidth + self.margin)
        self.totalHeight = 2 * (self.lHeight + self.margin)
        
        # create the starting position for x, and y
        self.xPos = (800 - self.totalWidth) / 2 # center the lettrs to the middle of the screen
        self.yPos = (450 - self.totalHeight) # Letters are close to the bottom of the display
        
        
    def drawLetters(self,display):
        # use a for loop to iterate all letters
        for i in range(26):
            
            # generate the row of letters using integer division
                # Integer division returns the largest number less than or equal to the result.
                # Ex. 0 / 13 = 0 - > 0 
                # Ex. 1 / 13 = 0.076... -> 0 
                # Ex. 14 / 13 = 1.076... -> 1 
                    # places numbers from 0 - 12 in the first row 
                    # places numbers from 13 - 25 in the second row 
            self.row = i // 13
            
            # generate the columns using modulus
            self.column = i % 13
            
            # Create the placements for the letters in a grid layout (make (x,y) Coordinates for every letter)
                # calculates the width that all columns take up 
                # then places the letter in the current column by adding this width to the xPos
            self.xPlacement = self.xPos + self.column * (self.lWidth + self.margin)
            
                # calculates the height that all rows take up 
                # then places the letter in the current row by adding this height to the yPos 
            self.yPlacement = self.yPos + self.row * (self.lHeight + self.margin)
            
            # create rect for each button using pygame.draw.rect
                # draws a button onto the screen at (x,y) coordinates with the dimensions of Letter Width, and Height
                    # (x,y) coordinates are self.xPos and self.yPos created above 
            pygame.draw.rect(display,(255,255,255),(self.xPlacement,self.yPlacement,self.lWidth,self.lHeight))
            
            # render the letter onto the display using .render
                # chr converts the ASCII value to a character
                # ord gets the ASCII value of the character A
                # adding i enables iteration through characters up to Z 
                # True is to enable Anti-aliasing for smoother edges on displayed text
            self.printLetter = self.letterFont.render(chr(ord('A') + i ), True, (0,0,0))
          
            # blit the letter to the screen
            display.blit(self.printLetter,(self.xPlacement, self.yPlacement))
            
        
