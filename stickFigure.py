import pygame

# create a class to draw Stick Figure
class StickFigure:
    def __init__(self):
        # Create an empty list to hold stick figure images
        self.sfImages = [] 
        
        # create a for loop to iterate through images
        for i in range(7):  # Player is allowed up to 6 guesses before losing, meaning there will be 6 images
            # Searches through images of hangman 
            sf_image = pygame.image.load("/Users/ramonbernal/Desktop/FallProject/static/hangman" + str(i) + ".png")
            # Rescale the image drawn onto the screen
            sf_image = pygame.transform.scale(sf_image,(300,300))
            # append the images to the empty list
            self.sfImages.append(sf_image)
        
        # start off with the first image due to no incorret answer being given yet
        self.hangmanImage = 0
        # create a Rect object for positioning on the display 
        self.rect = self.sfImages[self.hangmanImage].get_rect()
            
    # method to draw stick figure
    def drawStickFigure(self, display):
        display.blit(self.sfImages[self.hangmanImage], self.rect.topleft)


    # create method to reload the other images onto screen when guess is wrong
    def reloadSF(self):
        # increment hangman image if it is less than amount of hangman Images
        # keeps the hangman images from incrementing above the 7 images being used.
        if self.hangmanImage < len(self.sfImages):
            self.hangmanImage += 1
            
    def resetSF(self):
        # set the hangman image back to 0 when called
        self.hangmanImage = 0