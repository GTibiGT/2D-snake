import pygame
import time
import random

#snake speed
speed = 12

#window size
scrn_x = 480
scrn_y = 480

#color
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

#intialize pygame
pygame.init()

#intialize game window
pygame.display.set_caption('Snake 2D')
game_scrn = pygame.display.set_mode((scrn_x, scrn_y))

#frames
fps = pygame.time.Clock()

#default snake position
snake_pos = [100, 50]

#define snake body
snake_body = [ [100, 50],
               [90, 50],
               [80, 50],
               [70, 50]
            ]

#fruit position 
fruit_pos = [random.randrange(1, (scrn_x//10)) * 10,
             random.randrange(1, (scrn_y//10)) * 10]
fruit_appear = True

#setting snake default direction
#goes right
direction = 'RIGHT'
change_to = direction

#score display
#intialize score
score = 0

#display score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_scrn.blit(score_surface, score_rect)

#game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (scrn_x/2, scrn_y/2)
    game_scrn.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main Function
while True:
  
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously 
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism 
    # if fruits and snakes collide then scores will be 
    # incremented by 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_appear = False
    else:
        snake_body.pop()
        
    if not fruit_appear:
        fruit_pos = [random.randrange(1, (scrn_x//10)) * 10, 
                          random.randrange(1, (scrn_y//10)) * 10]
        
    fruit_appear = True
    game_scrn.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_scrn, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_scrn, white, pygame.Rect(
      fruit_pos[0], fruit_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > scrn_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > scrn_y-10:
        game_over()
    
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    # displaying score continuously
    show_score(1, white, 'times new roman', 20)
    
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(speed)
