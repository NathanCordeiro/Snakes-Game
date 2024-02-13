import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set playable region dimensions
playable_width = 600
playable_height = 400

# Create fullscreen display
dis = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Get fullscreen display dimensions
fullscreen_width, fullscreen_height = dis.get_width(), dis.get_height()

# Calculate playable region offset
offset_x = (fullscreen_width - playable_width) // 2
offset_y = (fullscreen_height - playable_height) // 2

# Define game parameters
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 36)

# Initialize score
score = 0

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(fullscreen_width - mesg.get_width()) // 2, (fullscreen_height - mesg.get_height()) // 2])

def show_score():
    score_text = font_style.render("Score: " + str(score), True, black)
    dis.blit(score_text, (10, 10))

def gameLoop():
    global score

    game_over = False

    # Initialize clock object
    clock = pygame.time.Clock()

    while not game_over:
        game_close = False

        x1 = offset_x + (playable_width / 2)
        y1 = offset_y + (playable_height / 2)

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        foodx = round(random.randrange(offset_x, offset_x + playable_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(offset_y, offset_y + playable_height - snake_block) / 10.0) * 10.0

        while not game_close and not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= offset_x + playable_width or x1 < offset_x or y1 >= offset_y + playable_height or y1 < offset_y:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)

            # Draw white border around the window
            pygame.draw.rect(dis, white, [offset_x - 4, offset_y - 4, playable_width + 6, playable_height + 6], 8)

            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            our_snake(snake_block, snake_list)

            # Check if snake eats food
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(offset_x, offset_x + playable_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(offset_y, offset_y + playable_height - snake_block) / 10.0) * 10.0
                length_of_snake += 1
                score += 1  # Increase score when snake eats food

            show_score()  # Display score

            pygame.display.update()

            clock.tick(snake_speed)

        while game_close and not game_over:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_close = False

    pygame.quit()
    quit()

# Start the game loop
gameLoop()
