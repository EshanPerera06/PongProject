# Import delle librerie
import pygame
import random as r

#Inizializzazione delle librerie di pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

#Variabili per la creazione della finestra di gioco
GAME_RES = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60
GAME_TITLE = "Pong"
dt = 1000 / FPS / 1000

#Creazione della finestra di gioco
window = pygame.display.set_mode(GAME_RES, pygame.HWACCEL|pygame.HWSURFACE|pygame.DOUBLEBUF)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

loops = 1

backgruond_img = pygame.image.load("assets/levels/bg1.png")
level1_img = pygame.image.load("assets/levels/bg2.png")
level2_img = pygame.image.load("assets/levels/bg3.png")
player1_img = pygame.image.load("assets/bricks/paddle1_2p.png")
player2_img = pygame.image.load("assets/bricks/paddle2_2p.png")
ball_img = pygame.image.load("assets/ball/ball.png")
ball_img = pygame.transform.scale(ball_img, (16, 16))

player1_rect = player1_img.get_rect(center=(8, 32))
player2_rect = player2_img.get_rect(center=(8, 32))
ball_rect = ball_img.get_rect(center=(8, 8))

player1_rect.x = 20
player1_rect.y = 300 - 32

player2_rect.x = 780 - 16
player2_rect.y = 300 - 32

ball_rect.x = WINDOW_WIDTH / 2
ball_rect.y = WINDOW_HEIGHT / 2

#Direzione iniziale della palla
if r.randint(1,2) == 1:
    ball_direction = -1
else:
    ball_direction = 1
    

player_speed = 5
ball_speed_v = 0
ball_speed_h = 7

game_ended = False

while not game_ended:
    #Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_ended = True
                
    keys_pressed = pygame.key.get_pressed()
    
    #movimento player 1
    if keys_pressed[pygame.K_w]:
        player1_rect.y -= 5
        player1_direction = 1
    if keys_pressed[pygame.K_s]:
        player1_rect.y += 5
        player1_direction = -1
    #movimento player 2
    if keys_pressed[pygame.K_UP]:
        player2_rect.y -= 5
        player2_direction = 1
    if keys_pressed[pygame.K_DOWN]:
        player2_rect.y += 5
        player2_direction = -1

    #movimento orizzontale ball
    if ball_direction == -1:
        ball_rect.x -= ball_speed_h
    if ball_direction == 1:
        ball_rect.x += ball_speed_h

    #movimento vertical ball
    
    #controllo la fuoriuscita dai bordi dei player
    if player1_rect.y < 0:
        player1_rect.y = 0
    if player1_rect.y > WINDOW_HEIGHT - player1_rect.height:
        player1_rect.y = WINDOW_HEIGHT - player1_rect.height
        
    if player2_rect.y < 0:
        player2_rect.y = 0
    if player2_rect.y > WINDOW_HEIGHT - player2_rect.height:
        player2_rect.y = WINDOW_HEIGHT - player2_rect.height
         
    #Update game logic
    if player1_rect.colliderect(ball_rect):
        ball_direction = 1
    
    if player2_rect.colliderect(ball_rect):
        ball_direction = -1
        if keys_pressed[pygame.K_UP]:
            ball_speed_v  = -7
        if keys_pressed[pygame.K_DOWN]:
            ball_speed_v = 7
        
    #Display draw and update
    window.blit(backgruond_img, (0, 0))
    
    #Disegno le due racchette
    window.blit(player1_img, player1_rect)
    window.blit(player2_img, player2_rect)
    window.blit(ball_img, ball_rect)
    
    pygame.display.update()
    dt = clock.tick(FPS)
    dt /= 1000
    
    

pygame.quit()
exit(0)