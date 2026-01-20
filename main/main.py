import pygame
from particles import Transition
from data import width, height, pixels_frame, pixels_user
import data
from pathlib import Path


folder = Path("frames")
count_folder = len(list(folder.iterdir()))

pygame.init()

screen = pygame.display.set_mode((width,height))

pixels_frame = data.load(0, width, height)

running = True
start_hold = 0
hold = 100
holding = False
particles = []
clock = pygame.time.Clock()

for i in range(0, len(pixels_user), 10):
    particles.append(Transition(pixels_user[i]["coords"][0],
                                pixels_user[i]["coords"][1],
                                pixels_frame[i]["coords"][0],
                                pixels_frame[i]["coords"][1],
                                pixels_user[i]["color"]))

while running:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False

    arrived = True

    screen.fill("black")
    for particle in particles:
        particle.draw(screen)

        if not holding:
            particle.math()
        
        if not particle.finished():
            arrived = False

    if arrived and not holding:
        holding = True
        start_hold = pygame.time.get_ticks()

    if holding:
        if pygame.time.get_ticks() - start_hold >= hold:
            holding = False
            data.frame_count += 1

            if data.frame_count < count_folder:
                
                pixels_frame = data.load(data.frame_count, width, height)
                pixels_frame = pixels_frame[::10]


                for i, particle in enumerate(particles):
                    particle.target_next(
                        pixels_frame[i]["coords"][0],
                        pixels_frame[i]["coords"][1]
                    )
            else:
                data.frame_count = 0


    pygame.display.flip()

pygame.quit()