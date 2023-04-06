import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font =  pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('src/Sky.png').convert()
ground_surface =  pygame.image.load('src/ground.png').convert()
text_surface = test_font.render("Corre BERGE", False, 'black')

snail_surface = pygame.image.load('src/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('src/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #bringing the surface to the screen
    screen.blit(sky_surface,(0,0)) 
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,10))
    
    screen.blit(snail_surface,snail_rect)
    snail_rect.right -= 5
    
    screen.blit(player_surf,player_rect)
    
    pygame.display.update()
    #set the framerate of the game
    clock.tick(60)