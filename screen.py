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
    screen.fill((0, 0, 0))
    screen.blit(grass, (random.choice(0,200)))
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("Dark green")

    grass = create_grass("bin/grass.png")
    pygame.transform.scale(grass, (5,2))
    draw_grass(grass)
    pygame.display.flip()
    clock.tick(60)
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