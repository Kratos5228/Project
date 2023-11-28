import pygame

# from game import playGame
from Asteroid import*
from Rocket import*
from Button import*
import os

time = pygame.time.Clock()

BASE = os.path.dirname(os.path.abspath(__file__))

class Handler:
    def __init__(self, display):
        self.display = display
        self.queueofEvent = []
        self.rocket1 = Rocket(350)
        self.rocket2 = Rocket(850)
        self.asteroid = Asteroid()
        self.count = 0
        self.exitOut_button_image = pygame.image.load(f"{BASE}/static/goBackButton.png")

    def listen(self, bg, rk):     
        for event in pygame.event.get():
            self.pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    print("T")
                    self.playGame(bg, rk)
                elif event.key == pygame.K_DOWN:
                    print("Down")
                    self.rocket2.yv += 5
                elif event.key == pygame.K_UP:
                    print("Up")
                    self.rocket2.yv -= 5
                elif event.key == pygame.K_w:
                    print("W")
                    self.rocket1.yv -= 5
                elif event.key == pygame.K_s:
                    print("S")
                    self.rocket1.yv += 5
                elif event.key == pygame.K_ESCAPE:
                    print("Esc")
                    self.running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    print("Down")
                    self.rocket2.yv = 0
                elif event.key == pygame.K_UP:
                    print("Up")
                    self.rocket2.yv = 0
                elif event.key  == pygame.K_w:
                    print("W")
                    self.rocket1.yv = 0
                elif event.key  == pygame.K_s:
                    print("S")
                    self.rocket1.yv = 0
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.exitOut_button.rect.collidepoint(self.pos):
                    self.running = False
            

    def text(self):
        font = pygame.font.SysFont('arial', 50)
        player1Text = font.render("Player 1", 1, (0, 0, 255))
        player2Text = font.render("Player 2", 1, (255, 0, 0))
        
        rocket1ScoreText = font.render(str(self.rocket1.score), 1, (100, 100, 100))
        rocket2ScoreText = font.render(str(self.rocket2.score), 1, (255, 255, 255))

        self.display.blit(rocket1ScoreText, (200 - rocket1ScoreText.get_width()/2, 740))
        self.display.blit(rocket2ScoreText, (700 - rocket2ScoreText.get_width() / 2, 740))
        self.display.blit(player1Text, (200 - rocket1ScoreText.get_width()/2, 50))
        self.display.blit(player2Text, (700 - rocket2ScoreText.get_width() / 2, 50))

    def gameOver(self):
        font = pygame.font.SysFont('arial', 50)
        player1WinsText = font.render("Player 1 Wins", 1, (0, 0, 255))
        player2WinsText = font.render("Player 2 Wins", 1, (255, 0, 0))
        playText = font.render("T - Play Again", 1, (255, 255, 255))

        self.exitOut_button = Button(1000, 50, self.exitOut_button_image, scale=0.4)

        if self.rocket1.score == 5:
            self.display.fill((0,0,0))
            self.display.blit(player1WinsText, (450, 200))
            self.display.blit(playText, (450, 400))
            self.exitOut_button.draw(self.display)
            self.rocket1.y = 790
            self.rocket2.y = 790
            
    
        if self.rocket2.score == 5:
            self.display.fill((0,0,0))
            self.display.blit(player2WinsText, (450, 200))
            self.display.blit(playText, (450, 400))
            self.exitOut_button.draw(self.display)
            self.rocket1.y = 790
            self.rocket2.y = 790

    
    def movingAsteroids(self, rocks, display):

        self.count += 1
        if self.count % 30 == 0:
            rocks.append(Asteroid())
            rocks.append(Asteroid())
        for a in rocks:
            a.move()   
            if a.xv > 0 and a.x > 1200:
                rocks.pop(rocks.index(a))
            if a.xv < 0 and a.x < -a.w:
                rocks.pop(rocks.index(a))
            if self.rocket1.isCollision(a):
                rocks.pop(rocks.index(a))
                self.rocket1.y = 790
            if self.rocket2.isCollision(a):
                rocks.pop(rocks.index(a))
                self.rocket2.y = 790
        
        for r in rocks:
            r.draw(display)    

    def playGame(self, background, rocks):
        
        pygame.display.set_caption('Space Race')
        self.rocket1.score = 0
        self.rocket2.score = 0
        
        self.running = True
        while self.running:  

            time = pygame.time.Clock()

            self.display.fill((0,0,0))
            self.display.blit(background, (0,0))

            self.listen(background, rocks)
            self.movingAsteroids(rocks, self.display)

            self.rocket1.checkPoint()
            self.rocket1.update()
            self.rocket1.draw(self.display)

            self.rocket2.checkPoint()
            self.rocket2.update()
            self.rocket2.draw(self.display)

            self.text() 
                
            self.gameOver()
                
            time.tick(30)

            pygame.display.update() 
             