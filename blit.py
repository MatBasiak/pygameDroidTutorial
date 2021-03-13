import pygame


def main():
    pygame.init()
    pygame.display.set_caption("blit")
    smiley = pygame.image.load("smiley.png")
    smiley.set_colorkey((255, 255, 255))
    smiley.set_alpha(250)
    background = pygame.image.load("background.png")
    screen = pygame.display.set_mode((600, 400))
    screen.fill((125, 163, 148))
    screen.blit(background, (0, 0))
    # screen.blit(smiley, (50, 50))

    screen_width = screen.get_width()

    xpos = 50
    ypos = 50
    step_x = 2
    step_y = 2

    screen.blit(smiley, (xpos, ypos))
    pygame.display.flip()
    clock = pygame.time.Clock()

    running = True
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        if xpos > screen_width - 300 or xpos < 0:
            step_x = -step_x
        if ypos > screen_width - 300 or ypos < 0:
            step_y = -step_y
        xpos += step_x  # move it to the right
        ypos += step_y  # move it down

        screen.blit(smiley, (xpos, ypos))
        pygame.display.flip()

        screen.blit(background, (0, 0))
        screen.blit(background, (300, 0))
        screen.blit(background, (300, 200))
        screen.blit(background, (0, 200))
        screen.blit(smiley, (xpos, ypos))

        pygame.display.flip()
        clock.tick(350)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
