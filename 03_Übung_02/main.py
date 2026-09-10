### Übung_01 Kreis Bewegung ###
import pygame

"""----- Setup -----"""
pygame.init()
window = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
running = True
# Variablen
circle_01_x = window.width / 2
circle_01_y = window.height / 2
circle_02_x = window.width / 2
circle_02_y = window.height / 2
circle_01_movement = 10
circle_02_movement = 6

"""----- Gameloop -----"""
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Circle Movement
    circle_01_x += circle_01_movement
    circle_02_y += circle_02_movement

    # Screen Fill
    window.fill("#985899")

    """----- Rendern -----"""
    # Circle
    circle_01 = pygame.draw.circle(window, "#1d2e4d", (circle_01_x, circle_01_y), 50)
    circle_02 = pygame.draw.circle(window, "#306669", (circle_02_x, circle_02_y), 25)
    if circle_01.right >= window.width and circle_01_movement > 0:
        circle_01_movement = -circle_01_movement
    elif circle_01.left <= 0 and circle_01_movement < 0:
        circle_01_movement = -circle_01_movement
    if circle_02.top <= 0 and circle_02_movement < 0:
        circle_02_movement = -circle_02_movement
    elif circle_02.bottom >= window.height and circle_02_movement > 0:
        circle_02_movement = -circle_02_movement
    # print(circle_02.top, circle_02.bottom, circle_02_movement)

    # Screen Flip
    pygame.display.flip()

    # FPS Limit
    clock.tick(60)

pygame.quit()
