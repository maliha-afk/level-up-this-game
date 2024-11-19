import random
import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("space invador")
game_over_text=False
game_over=False
fire_rad=10
fire_x=250
fire_y=10
fire_color=(255,69,0)

bg_color=(0,0,0)

rc_color=(255,0,0)
rc_h=50
rc_w=25
rc_x=250
rc_y=400

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    if fire_y > 520:
        fire_y=-20
        fire_x=random.randint(10,490)

    else:
        fire_y=fire_y+5

    
    key=pygame.key.get_pressed()

    if (key[pygame.K_LEFT]):
        rc_x=rc_x-5

    if (key[pygame.K_RIGHT]):
        rc_x=rc_x+5

    if (key[pygame.K_UP]):
        rc_x=rc_x-5

    if (key[pygame.K_DOWN]):
        rc_x=rc_x=5

    
    fire_rect=pygame.Rect(fire_x-fire_rad,fire_y-fire_rad,fire_rad*2,fire_rad*2)
    rc_rect=pygame.Rect(rc_x,rc_y,rc_w,rc_h)
    
    if fire_rect.colliderect(rc_rect):
        rc_color=(0,0,0)
        fire_color=(0,0,0)
        game_over=True

        if game_over==True:
          pygame.draw.circle(screen,fire_color,(fire_x,fire_y),fire_rad)
          pygame.draw.rect(screen,rc_color,(rc_x,rc_y,rc_w,rc_h))
          game_over_text=True
          

          if game_over_text==True:
           font=pygame.font.SysFont(None,60)
           text=font.render("!GAME OVER!",True,(255,255,255))
           screen.blit(text,(100,250))
        

    screen.fill(bg_color)
    
    pygame.draw.circle(screen,fire_color,(fire_x,fire_y),fire_rad)
    pygame.draw.rect(screen,rc_color,(rc_x,rc_y,rc_w,rc_h))
    
    pygame.time.delay(15)
    
    pygame.display.update()

    