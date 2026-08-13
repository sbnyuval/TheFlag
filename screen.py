import pygame
import consts
pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
SOLDIER_IMG = pygame.image.load("soldier.png")
player_size = 50
soldier_resized = pygame.transform.scale(SOLDIER_IMG, (player_size, player_size))
DARK_GREEN = (0, 100, 0)
player_x = 0
player_y = 0
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5
    screen.fill(DARK_GREEN)
    screen.blit(soldier_resized, (player_x, player_y))
    pygame.display.flip()
pygame.quit()

