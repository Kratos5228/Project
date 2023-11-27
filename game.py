import pygame
import os

from Button import*
from handler import*
from hangmanHandler import*

BASE = os.path.dirname(os.path.abspath(__file__))

pygame.init()

# Initialize an empty Pong leaderboard list, outside of any function definitions to declare it as global
leaderboard = [] #this will allow the leaderboard to stay saved even when switching to other games

print(BASE)

backgroundimage = pygame.image.load(f"{BASE}/static/background.png")
background = pygame.transform.scale(backgroundimage, (1250,900))

mainDisplay = pygame.display.set_mode((1250,900)) #(X,Y)

space_race_img = pygame.image.load(f"{BASE}/static/NEWBUTTON.png").convert_alpha()
space_racer_button = Button(460, 75, space_race_img, 0.7)

pong_img = pygame.image.load(f"{BASE}/static/pongMenu.png").convert_alpha()
pong_button = Button(435, 225, pong_img, 0.6)

hangman_img = pygame.image.load(f"{BASE}/static/HangManButton.png").convert_alpha()
hangman_button = Button(480, 600, hangman_img, 0.5)

exit_image = pygame.image.load(f"{BASE}/static/EXITBUTTON.png").convert_alpha()
exit_image_button = Button(1050, 800, exit_image, 0.4)

time = pygame.time.Clock()

rocks = []

# Main Menu Loop
run = True
while run:

    mainDisplay.fill((0, 0, 0))
    pygame.display.set_caption('Game Menu')
    
    if space_racer_button.draw(mainDisplay):
        disp1 = pygame.display.set_mode((1250, 900))
        handler = Handler(disp1)
        handler.playGame(background, rocks)

    if pong_button.draw(mainDisplay):
        pygame.init()

        # Game window dimensions and display setup
        WIDTH, HEIGHT = 700, 500
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")

        # Constants for game settings
        FPS = 60
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
        BALL_RADIUS = 7
        SCORE_FONT = pygame.font.SysFont("comicsans", 50)
        WINNING_SCORE = 5

        # Loading images for the game's UI elements
        title_image = pygame.image.load(f'{BASE}/static/pongImg.png')

        oneplayer_button_image = pygame.image.load(f"{BASE}/static/player1.png")
        twoplayer_button_image = pygame.image.load(f"{BASE}/static/player2.png")
        leaderboard_button_image = pygame.image.load(f"{BASE}/static/leaderboard.png")

        play_again_image = pygame.image.load(f"{BASE}/static/retry.png")
        main_menu_image = pygame.image.load(f"{BASE}/static/menu.png")

        # ImageButton class for creating and managing interactive image buttons
        class ImageButton:
            def __init__(self, x, y, image, scale=1):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)

            def draw(self, win):
                win.blit(self.image, (self.rect.x, self.rect.y))

            def is_over(self, pos):
                return self.rect.collidepoint(pos)
            
        # Paddle class representing the player's paddle in the game
        class Paddle:
            COLOR = WHITE
            VEL = 4

            def __init__(self, x, y, width, height):
            # Initialize paddle properties
                self.x = self.original_x = x
                self.y = self.original_y = y
                self.width = width
                self.height = height

            def draw(self, win):
            # Draw the paddle
                pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

            def move(self, up=True):
            # move the paddle up/down
                if up:
                    self.y -= self.VEL
                else:
                    self.y += self.VEL

            def reset(self):
            # Reset the paddle to its original position
                self.x = self.original_x
                self.y = self.original_y
            
        # Ball class representing the ball in the game
        class Ball:
            MAX_VEL = 5
            COLOR = WHITE

            def __init__(self, x, y, radius):
            # Initialize ball properties
                self.x = self.original_x = x
                self.y = self.original_y = y
                self.radius = radius
                self.x_vel = self.MAX_VEL
                self.y_vel = 0

            def draw(self, win):
            # Draw the ball
                pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

            def move(self):
            # Move the ball
                self.x += self.x_vel
                self.y += self.y_vel

            def reset(self):
            # Reset the ball to its original position
                self.x = self.original_x
                self.y = self.original_y
                self.y_vel = 0
                self.x_vel *= -1
            
            # Draws the game window, scores, paddles, and the ball
        def draw(win, paddles, ball, left_score, right_score):
            win.fill(BLACK)
            left_score_text = SCORE_FONT.render(f"{left_score}", 1, WHITE)
            right_score_text = SCORE_FONT.render(f"{right_score}", 1, WHITE)
            win.blit(left_score_text, (WIDTH//4 - left_score_text.get_width()//2, 20))
            win.blit(right_score_text, (WIDTH * (3/4) - right_score_text.get_width()//2, 20))

            for paddle in paddles:
                paddle.draw(win)

            for i in range(10, HEIGHT, HEIGHT//20):
                if i % 2 == 1:
                    continue
                pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))

            ball.draw(win)
            pygame.display.update()

        # Handles the collision of the ball with paddles and walls
        def handle_collision(ball, left_paddle, right_paddle):
            if ball.y + ball.radius >= HEIGHT or ball.y - ball.radius <= 0:
                ball.y_vel *= -1

            if ball.x_vel < 0 and left_paddle.y < ball.y < left_paddle.y + left_paddle.height:
                if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                    ball.x_vel *= -1

                    middle_y = left_paddle.y + left_paddle.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (left_paddle.height / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel

            elif ball.x_vel > 0 and right_paddle.y < ball.y < right_paddle.y + right_paddle.height:
                if ball.x + ball.radius >= right_paddle.x:
                    ball.x_vel *= -1

                    middle_y = right_paddle.y + right_paddle.height / 2
                    difference_in_y = middle_y - ball.y
                    reduction_factor = (right_paddle.height / 2) / ball.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    ball.y_vel = -1 * y_vel

        # Handles movement of the paddles based on player input
        def handle_paddle_movement(keys, left_paddle, right_paddle, ball, player_mode):
            if player_mode == 2:
                if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
                    right_paddle.move(up=True)
                if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
                    right_paddle.move(up=False)

            else:
                if ball.y > right_paddle.y + right_paddle.height/2 and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
                    right_paddle.move(up=False)
                elif ball.y < right_paddle.y + right_paddle.height/2 and right_paddle.y - right_paddle.VEL >= 0:
                    right_paddle.move(up=True)

            if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
                left_paddle.move(up=True)
            if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
                left_paddle.move(up=False)

            # Displays the main menu screen
        def menu_screen(win):
            
            title_image_y = .09 # Adjust this value as needed for proper title placement

            single_player_button = ImageButton(WIDTH // 2 - 125, 50, oneplayer_button_image, scale=0.6)
            two_player_button = ImageButton(WIDTH // 2 - 125, 150, twoplayer_button_image, scale=0.6)
            leaderboard_button = ImageButton(WIDTH // 2 - 125, 250, leaderboard_button_image, scale=0.6)
            menu_button = ImageButton(WIDTH // 2 - 125, 350, main_menu_image, scale=0.6)

            run = True
            while run:
                win.fill(BLACK)

                # Draw the title image
                win.blit(title_image, (WIDTH // 2 - title_image.get_width() // 2, title_image_y))

                # Draw the buttons
                single_player_button.draw(win)
                two_player_button.draw(win)
                leaderboard_button.draw(win)
                menu_button.draw(win)


                pygame.display.update()

                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()

                    if event.type == pygame.QUIT:
                        mainDisplay = pygame.display.set_mode((1250,900)) #(X,Y)
                        run = False
                    elif event.type == pygame.K_q:
                        mainDisplay = pygame.display.set_mode((1250,900)) #(X,Y)
                        run = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if single_player_button.is_over(pos):
                            return 1
                        if two_player_button.is_over(pos):
                            return 2
                        if leaderboard_button.is_over(pos):
                            display_leaderboard(WIN, leaderboard)
                            pygame.time.delay(5000)  # Display for 5 seconds
                        if menu_button.is_over(pos):
                            mainDisplay = pygame.display.set_mode((1250,900)) #(X,Y)
                            run = False

        # Captures the winner's name for the leaderboard
        def get_winner_name(win, winner):
            input_box = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
            color_inactive = pygame.Color('lightskyblue3')
            color_active = pygame.Color('dodgerblue2')
            color = color_inactive
            active = False
            text = ''
            font = pygame.font.Font(None, 32)
            done = False

            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return None
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_box.collidepoint(event.pos):
                            active = True
                        else:
                            active = False
                        color = color_active if active else color_inactive
                    if event.type == pygame.KEYDOWN:
                        if active:
                            if event.key == pygame.K_RETURN:
                                done = True
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode

                win.fill((30, 30, 30))
                txt_surface = font.render(text, True, color)
                width = max(200, txt_surface.get_width()+10)
                input_box.w = width
                win.blit(txt_surface, (input_box.x+5, input_box.y+5))
                pygame.draw.rect(win, color, input_box, 2)

                title_font = pygame.font.SysFont("comicsans", 50)
                label = title_font.render(f"{winner} Player Enter Your Name", 1, WHITE)
                win.blit(label, (WIDTH//2 - label.get_width()//2, 20))

                pygame.display.flip()

            return text

            # Displays the leaderboard
        def display_leaderboard(win, leaderboard):
            win.fill(BLACK)
            title_font = pygame.font.SysFont("comicsans", 50)
            label = title_font.render("Leaderboard", 1, WHITE)
            win.blit(label, (WIDTH//2 - label.get_width()//2, 20))

            for i, (name, wins) in enumerate(leaderboard):
                win_text = "win" if wins == 1 else "wins"
                score_text = SCORE_FONT.render(f"{i+1}. {name} - {wins} {win_text}", 1, WHITE)
                win.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 100 + i * 50))

            pygame.display.update()
            pygame.time.delay(5000)

        # Shows options after a game has finished
        def post_game_options(win):
            play_again_button = ImageButton(WIDTH // 2 - 125, 150, play_again_image, scale=0.6)
            main_menu_button = ImageButton(WIDTH // 2 - 125, 250, main_menu_image, scale=0.6)

            while True:
                win.fill(BLACK)
                play_again_button.draw(win)
                main_menu_button.draw(win)

                pygame.display.update()

                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return None

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if play_again_button.is_over(pos):
                            return 1  # Play again
                        if main_menu_button.is_over(pos):
                            return 2  # Main menu

                    # Handle mouse over button color change
                    if event.type == pygame.MOUSEMOTION:
                        if play_again_button.is_over(pos):
                            play_again_button.color = (170, 170, 170)
                        else:
                            play_again_button.color = WHITE

                        if main_menu_button.is_over(pos):
                            main_menu_button.color = (170, 170, 170)
                        else:
                            main_menu_button.color = WHITE



        # Updates the leaderboard with the winner's name and score
        def update_leaderboard(leaderboard, winner_name):
            for i in range(len(leaderboard)):
                if leaderboard[i][0] == winner_name:
                    leaderboard[i] = (winner_name, leaderboard[i][1] + 1)
                    break
            else:
                leaderboard.append((winner_name, 1))

            #sort the leaderboard by score in descending order
            leaderboard.sort(key=lambda x: x[1], reverse=True)

        # Main function containing the game loop
        def main():
            global leaderboard
        
            # Loop for handling game start, gameplay, and post-game actions
            running = True
            while running:
                player_mode = menu_screen(WIN)

                if player_mode in [1, 2]:
                    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
                    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
                    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

                    left_score = 0
                    right_score = 0

                    run = True
                    clock = pygame.time.Clock()

                    while run:
                        clock.tick(FPS)
                        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                                pygame.quit()
                                return

                        keys = pygame.key.get_pressed()
                        handle_paddle_movement(keys, left_paddle, right_paddle, ball, player_mode)

                        ball.move()
                        handle_collision(ball, left_paddle, right_paddle)

                        if ball.x < 0:
                            right_score += 1
                            ball.reset()
                            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)
                        elif ball.x > WIDTH:
                            left_score += 1
                            ball.reset()
                            draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

                        if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:
                            if player_mode == 1 and right_score >= WINNING_SCORE:
                                winner_name = "AI"
                            else:
                                winner = "Left" if left_score >= WINNING_SCORE else "Right"
                                winner_name = get_winner_name(WIN, winner)

                            if winner_name:
                                update_leaderboard(leaderboard, winner_name)
                            display_leaderboard(WIN, leaderboard)
                            break

                    option = post_game_options(WIN)
                    if option == 1:
                        continue  # Play again
                    elif option == 2:
                        continue  # Return to main menu
                    else:
                        break

                if player_mode is None:
                    break

        main()

    if hangman_button.draw(mainDisplay):
        disp = pygame.display.set_mode((800,600))

        # set window caption to hangman
        pygame.display.set_caption("Hangman")

        # create handler object and pass in display
        handler = hangmanHandler(disp)

        # create stick figure object
        sFigure = StickFigure()

        # create object to display words 
        dispWord = guessingWords()

        handler.playGame(disp, dispWord, sFigure)
            
    if exit_image_button.draw(mainDisplay):
        run = False
        
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    pygame.display.update() 
