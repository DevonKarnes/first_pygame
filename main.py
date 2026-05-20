import pygame
import sys

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,100))
test_surface.fill((255,0,200))

x_speed = 0
y_speed = 0
x_pos = 0
y_pos = 0

test_rect = test_surface.get_rect(center = (100,100))

while True:
    pygame.display.set_caption("First Pygame Game")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y_speed = -1
                x_speed = 0
            if event.key == pygame.K_s:
                y_speed = 1
                x_speed = 0
            if event.key == pygame.K_a:
                x_speed = -1
                y_speed = 0
            if event.key == pygame.K_d:
                x_speed = 1
                y_speed = 0

    screen.fill((175,215,70))
    screen.blit(test_surface,(x_pos, y_pos))
    x_pos += x_speed
    y_pos += y_speed

    pygame.display.update()
    clock.tick(60)