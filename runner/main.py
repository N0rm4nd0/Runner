import pygame 
from sys import exit
from random import randint

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time = current_time//1000
    score_surf = test_font.render(f'Score: {current_time}',False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    pygame.draw.rect(screen, '#c0e8e6', score_rect)
    pygame.draw.rect(screen, '#c0e8e6', score_rect, 10)
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            
            if obstacle_rect.bottom == 300:screen.blit(snail_surf, obstacle_rect)
            else:screen.blit(fly_surf,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles: 
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surf,player_index
    #player walking animation if the plauer is on the floor
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]
    #player jump if it not in the floor
    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font =  pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('src/Sky.png').convert()
ground_surface =  pygame.image.load('src/ground.png').convert()

#text_surf = test_font.render("Corre BERGE", False, (64,64,64))
#text_rect = text_surf.get_rect(center = (400,50))

#text
end_surf = test_font.render("Game Over", False, (64,64,64))
end_rect = end_surf.get_rect(center = (400,50))

restart_surf = test_font.render("Press SPACE to restart", False, (64,64,64))
restart_rect = restart_surf.get_rect(center = (400,350))

#stail
snail_frame_1 = pygame.image.load('src/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('src/snail/snail2.png').convert_alpha()
snail_frame = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frame[snail_frame_index]

#fly

fly_frame_1 = pygame.image.load('src/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('src/Fly/Fly2.png').convert_alpha()
fly_frame = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frame[fly_frame_index]

obstacle_rect_list = []

#player
player_walk1 = pygame.image.load('src/Player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('src/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_jump = pygame.image.load('src/Player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#player in game over screen
player_stand = pygame.image.load('src/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#Timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1200)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer,200)

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
                print('GAME RESTARTED')
                game_active = True
                start_time = pygame.time.get_ticks()
        if game_active:
            if event.type ==  obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),200)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frame[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frame[fly_frame_index]

    if game_active:
        #bringing the surface to the screen
        screen.blit(sky_surface,(0,0)) 
        screen.blit(ground_surface,(0,300))
        score = display_score()
                    
        #if snail_rect.x <= 0: snail_rect.left = 800
        #snail_rect.right -= 5
        #screen.blit(snail_surf,snail_rect)
        
        #player
        player_gravity += 1 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf,player_rect)
        
        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #obstacles
        game_active = collisions(player_rect, obstacle_rect_list)
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint((mouse_pos)):
        #    pygame.mouse.get_pressed()
        #    
        #if snail_rect.colliderect(player_rect):
        #    print('GAME OVER')
         #   game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = test_font.render(f"Your score: {score}", False, (64,64,64))
        score_message_rect =  score_message.get_rect(center = (400,350))
        screen.blit(end_surf,end_rect)
        
        if score == 0: screen.blit(restart_surf,restart_rect)
        else: screen.blit(score_message, score_message_rect)
        
    pygame.display.update()
    #set the framerate of the game
    clock.tick(60)