# <------------------------------------------------------BASIC SETUP----------------------------------------------------------->

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
# <------------------------------------------------------GLOBAL VARIABLES------------------------------------------------------>
turn = 0
pawns = []

# Run until the user asks to quit
running = True
dragging = False
interim_pos = (0,0)

# <------------------------------------------------------HELPER FUNCTION------------------------------------------------------->

def check(coord,color):
    for pawn in pawns:
        if pawn[0] == coord:
            if color == pawn[1]:
                return 1
            else:
                return 0
    return 2

def getCoord():
    x, y = pygame.mouse.get_pos()
    if y > 547 and y < 573:
        if x > 489 and x < 515:
            return (502,560)
        if x > 280 and x < 306:
            return (293,560)
    
    elif y > 347 and y < 373:
        if x > 555 and x < 581:
            return (568,360)
        if x > 425 and x < 451:
            return (438,360)
        if x > 344 and x < 370:
            return (357,360)
        if x > 215 and x < 241:
            return (228,360)
    
    elif y > 423 and y < 449:
        if x > 450 and x < 476:
            return (463,436)
        if x > 319 and x < 345:
            return (332,436)
    
    elif x > 385 and x < 411:
        if y > 471 and y < 497:
            return (398,484)
        if y > 223 and y < 249:
            return (398,236)
    
    else:
        return None

def draw(circles):
    for circle in circles:
        pygame.draw.circle(screen, circle[1], circle[0], 12)


# <------------------------------------------------------GAME VARIABLES-------------------------------------------------------->

class crow:
    def __init__(self,color,count):
        self.color = color
        self.count = count

    def cr_movement(self,event):
        global dragging
        global interim_pos
        global turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = getCoord()
            static = check(pos,self.color)
            if static == 1:
                dragging = True
                interim_pos = pos
                pawns.remove((pos,self.color))
        if event.type == pygame.MOUSEBUTTONUP:
            pos = getCoord()
            static = check(pos,self.color)
            if dragging and pos != None:
                if static == 2:
                    temp = (pos,self.color)
                    pawns.append(temp)
                    turn = (turn + 1) % 2
                else:
                    temp = (interim_pos,self.color)
                    pawns.append(temp)
                dragging = False
            elif self.count < 7 and pos != None:
                if static == 2:
                    self.count = self.count + 1
                    temp = (pos,self.color)
                    pawns.append(temp)
                    turn = (turn + 1) % 2


class vulture:
    def __init__(self,color,count):
        self.color = color
        self.count = count

    def vr_movement(self,event):
        global dragging
        global interim_pos
        global turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = getCoord()
            static = check(pos,self.color)
            if static == 1:
                dragging = True
                interim_pos = pos
                pawns.remove((pos,self.color))
        if event.type == pygame.MOUSEBUTTONUP:
            pos = getCoord()
            static = check(pos,self.color)
            if dragging and pos != None:
                if static == 2:
                    temp = (pos,self.color)
                    pawns.append(temp)
                    turn = (turn + 1) % 2
                else:
                    temp = (interim_pos,self.color)
                    pawns.append(temp)
                dragging = False
            elif self.count < 1 and pos != None:
                if static == 2:
                    self.count = self.count + 1
                    temp = (pos,self.color)
                    pawns.append(temp)
                    turn = (turn + 1) % 2


opponent_1 = crow((127, 255, 212),0)
opponent_2 = vulture((255, 234, 0),0)


while running:

    screen.fill((255,140,0))
    # update background image
    screen.blit(backgorund,(150,150))
    screen.blit(text,textRect)

    for event in pygame.event.get():

        # Did the user click the window close button?
        if event.type == pygame.QUIT:
            running = False

        if(turn == 0):
            opponent_1.cr_movement(event)
        else:
            opponent_2.vr_movement(event)
    
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