import pygame 
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time = current_time//1000
    score_surf = test_font.render(f'Score: {current_time}',False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    pygame.draw.rect(screen, '#c0e8e6', score_rect)
    pygame.draw.rect(screen, '#c0e8e6', score_rect, 10)
    screen.blit(score_surf,score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font =  pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0

sky_surface = pygame.image.load('src/Sky.png').convert()
ground_surface =  pygame.image.load('src/ground.png').convert()

#text_surf = test_font.render("Corre BERGE", False, (64,64,64))
#text_rect = text_surf.get_rect(center = (400,50))

end_surf = test_font.render("Game Over", False, (64,64,64))
end_rect = end_surf.get_rect(center = (400,50))

restart_surf = test_font.render("Press SPACE to restart", False, (64,64,64))
restart_rect = restart_surf.get_rect(center = (400,350))

snail_surf = pygame.image.load('src/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('src/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#player in game over screen
player_stand = pygame.image.load('src/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = 800
                print('GAME RESTARTED')
                game_active = True
                start_time = pygame.time.get_ticks()
                
    if game_active:
        #bringing the surface to the screen
        screen.blit(sky_surface,(0,0)) 
        screen.blit(ground_surface,(0,300))
        display_score()
                    
        if snail_rect.x <= 0: snail_rect.left = 800
        snail_rect.right -= 5
        screen.blit(snail_surf,snail_rect)

        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        if player_rect.collidepoint((mouse_pos)):
            pygame.mouse.get_pressed()
            
        if snail_rect.colliderect(player_rect):
            print('GAME OVER')
            game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(end_surf,end_rect)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(restart_surf,restart_rect)
            
    
    pygame.display.update()
    #set the framerate of the game
    clock.tick(60)