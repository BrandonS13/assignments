#I used google to figure out the pygame code to help make the soccer ball move (I kinda knew it before just didn't know how to use it in pygame) you can use the arrow keys to move the soccer ball around

import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640, 480))
my_image = pygame.image.load("code_jam/media/soccerball.png")
image_rect = my_image.get_rect(center=(320, 240))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 150, 0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        image_rect.x += 3

    if keys[pygame.K_LEFT]:
        image_rect.x -= 3

    if keys[pygame.K_UP]:
        image_rect.y -= 3

    if keys[pygame.K_DOWN]:
        image_rect.y += 3

    screen.blit(my_image, image_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()