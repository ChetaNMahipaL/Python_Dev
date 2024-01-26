# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode((800, 800))

#Title and Icon
pygame.display.set_caption("Board Game")

# background
backgorund = pygame.image.load('bg.png')

# Adding heading
font = pygame.font.Font('freesansbold.ttf', 84)
 
# create a text surface object,
# on which text is drawn on it.
text = font.render('KAOOA', True, (255,255,255))
 
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (400, 75)

# Run until the user asks to quit
running = True
while running:

    screen.fill((255,140,0))
    # update background image
    screen.blit(backgorund,(150,150))
    screen.blit(text,textRect)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # must to make changes visible
    pygame.display.update()




# Done! Time to quit.
pygame.quit()