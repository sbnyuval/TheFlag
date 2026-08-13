import pygame
import consts
import random
pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()

running = True

def create_grass(grass_img):
    grass = pygame.image.load(grass_img)
    return grass

def draw_grass(grass):
    grass = pygame.transform.scale(grass, (40, 40))
    screen.blit(grass, (random.choice(20,400),(random.choice(20,400))))
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
clock = pygame.time.Clock()
SOLDIER_IMG = pygame.image.load("bin\soldier.png")
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
   grass = create_grass("bin/grass.png")
   pygame.transform.scale(grass, (5, 2))
   draw_grass(grass)
   screen.blit(soldier_resized, (player_x, player_y))
   pygame.display.flip()
pygame.quit()








def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)

def draw_win_message():
        draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
                     consts.WIN_COLOR, consts.WIN_LOCATION)