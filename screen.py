import pygame
import consts
pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
flag_image = pygame.image.load("flag.png")
flag_resized = pygame.transform.scale(flag_image, (consts.FLAG_WIDTH, consts.FLAG_WIDTH))
flag_x = (consts.WINDOW_WIDTH - consts.FLAG_WIDTH)
flag_y = (consts.WINDOW_HEIGHT - consts.FLAG_HEIGHT)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("Dark green")
    screen.blit(flag_resized, (flag_x, flag_y))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
