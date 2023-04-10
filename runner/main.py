import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font =  pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('src/Sky.png').convert()
ground_surface =  pygame.image.load('src/ground.png').convert()

text_surf = test_font.render("Corre BERGE", False, (64,64,64))
text_rect = text_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('src/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('src/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    #bringing the surface to the screen
    screen.blit(sky_surface,(0,0)) 
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen, '#c0e8eC', text_rect)
    pygame.draw.rect(screen, '#c0e8eC', text_rect, 10)
    screen.blit(text_surf,text_rect)
    
    if snail_rect.x <= 0: snail_rect.left = 800
    snail_rect.right -= 5
    screen.blit(snail_surf,snail_rect)

    player_gravity = 1
    player_rect.y += player_gravity
    screen.blit(player_surf,player_rect)

    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')
    
    #if player_rect.colliderect(snail_rect):
    #    snail_rect.right = 0
    
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        pygame.mouse.get_pressed()
    
    pygame.display.update()
    #set the framerate of the game
    clock.tick(60)