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


#<------------------------------------------------------HELPER FUNCTION------------------------------------------------------->

pawns = []

def app_rem_pawns(coord,flag):
    if coord in pawns and flag:
        pawns.remove(coord)
    elif not flag:
        pawns.append(coord)

def drawCircle(flag):
    x, y = pygame.mouse.get_pos()
    if y > 547 and y < 573:
        if x > 489 and x < 515:
            app_rem_pawns((502,560),flag)
        if x > 280 and x < 306:
            app_rem_pawns((293,560),flag)
    
    elif y > 347 and y < 373:
        if x > 555 and x < 581:
            app_rem_pawns((568,360),flag)
        if x > 425 and x < 451:
            app_rem_pawns((438,360),flag)
        if x > 344 and x < 370:
            app_rem_pawns((357,360),flag)
        if x > 215 and x < 241:
            app_rem_pawns((228,360),flag)
    
    elif y > 423 and y < 449:
        if x > 450 and x < 476:
            app_rem_pawns((463,436),flag)
        if x > 319 and x < 345:
            app_rem_pawns((332,436),flag)
    
    elif x > 385 and x < 411:
        if y > 471 and y < 497:
            app_rem_pawns((398,484),flag)
        if y > 223 and y < 249:
            app_rem_pawns((398,236),flag)

def draw(circles):
    for circle in circles:
        pygame.draw.circle(screen, (127, 255, 212), circle, 12) 




# Run until the user asks to quit
running = True
dragging = False
flag = True
while running:

    screen.fill((255,140,0))
    # update background image
    screen.blit(backgorund,(150,150))
    screen.blit(text,textRect)

    for event in pygame.event.get():

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = True
            drawCircle(flag)
            dragging = True

        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            flag = False
            drawCircle(flag)
            pygame.display.update()

        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False
    
    if dragging:
        continue
    draw(pawns)
    # # get pawns co-ordinate
    # x, y = pygame.mouse.get_pos()
    # print(x)
    # print(y)
            
    
    # must to make changes visible
    pygame.display.update()




# Done! Time to quit.
pygame.quit()