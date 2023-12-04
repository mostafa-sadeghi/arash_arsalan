import pygame
pygame.init()


SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 60

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
myfont = pygame.font.Font("font.otf",48)
title = myfont.render("Wolf game", True, (255,0,0))
title_rect = title.get_rect(top = 0, centerx = SCREEN_WIDTH/2)


wolf_image = pygame.image.load("wolf.png")
wolf_rect = wolf_image.get_rect()
wolf_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)
# main loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        wolf_rect.y -= 5
    if keys[pygame.K_DOWN]:
        wolf_rect.y += 5
    if keys[pygame.K_LEFT]:
        wolf_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        wolf_rect.x += 5
    screen.fill((0,0,0))
    screen.blit(title, title_rect)
    screen.blit(wolf_image, wolf_rect)
    pygame.display.update()
    clock.tick(FPS)
# TODO

#  اضافه کردن تصویر غذا و متن امتیاز و جان گرگ به صفحه