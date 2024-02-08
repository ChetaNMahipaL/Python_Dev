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
dead_crow = 0

# Run until the user asks to quit
running = True
dragging = False
cr_interim_pos = (0,0)
vr_interim_pos = (0,0)

# <------------------------------------------------------Position Decleration and Data Sets--------------------------------------->
pos_1 = (398,236)
pos_2 = (228,360)
pos_3 = (357,360)
pos_4 = (438,360)
pos_5 = (568,360)
pos_6 = (332,436)
pos_7 = (463,436)
pos_8 = (398,484)
pos_9 = (293,560)
pos_10 = (502,560)

adj_dict = {
    pos_1: [pos_3, pos_4],
    pos_2: [pos_3, pos_6],
    pos_3: [pos_2, pos_4, pos_6, pos_1],
    pos_4: [pos_3, pos_5, pos_7, pos_1],
    pos_5: [pos_4, pos_7],
    pos_6: [pos_2, pos_3, pos_8, pos_9],
    pos_7: [pos_4, pos_5, pos_8, pos_10],
    pos_8: [pos_10, pos_9, pos_6, pos_7],
    pos_9: [pos_6, pos_8],
    pos_10: [pos_7, pos_8]
}

lines = [[] for _ in range(5)]

lines[0] = [pos_1, pos_3, pos_6, pos_9]
lines[1] = [pos_1, pos_4, pos_7, pos_10]
lines[2] = [pos_2, pos_3, pos_4, pos_5]
lines[3] = [pos_2, pos_6, pos_8, pos_10]
lines[4] = [pos_5, pos_7, pos_8, pos_9]

# <------------------------------------------------------HELPER FUNCTION------------------------------------------------------->

def cr_check(coord,color):
    for pawn in pawns:
        if pawn[0] == coord:
            if color == pawn[1]:
                return 1
            else:
                return 0
    if cr_interim_pos == (0,0):
        return 2
    if dragging:
        if coord in adj_dict[cr_interim_pos]:
            return 2
        else:
            return -1
    return 2

def find_list_with_points(lines, point1, point2):
    for i, line in enumerate(lines):
        if point1 in line and point2 in line:
            index_point1 = line.index(point1)
            index_point2 = line.index(point2)
            return line, index_point1, index_point2
    return -1

def vr_check(coord,color,drag):
    global dead_crow
    for pawn in pawns:
        if pawn[0] == coord:
            if color == pawn[1]:
                return 1
            else:
                return 0
    if drag == True:
        return -1
    if vr_interim_pos == (0,0):
        return 2
    result = find_list_with_points(lines,coord,vr_interim_pos)
    if result == (-1):
        return -1
    else:
        req_line,index_1,index_2= find_list_with_points(lines,coord,vr_interim_pos)
        if (abs(index_1 - index_2 ) == 3):
            return -1
        else:
            if (index_1 + index_2) % 2 == 0:
                if cr_check(req_line[int((index_1+index_2)/2)],opponent_1.color) == 1:
                    dead_crow = dead_crow + 1
                    pawns.remove((req_line[int((index_1+index_2)/2)],opponent_1.color))
                else:
                    return -1
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

def check_win():
    global running
    if dead_crow >= 4:      
        font_1 = pygame.font.Font(None, 36)
        text_1 = font_1.render("Opponent_2 Wins!", True, (0, 0, 0))
        textRect_1 = text_1.get_rect()
        textRect_1.center = (400, 150)
        screen.blit(text_1,textRect_1)
        pygame.display.update()
        pygame.time.delay(2000)
        running = False
    else:
        win_flag = 0
        for i, line in enumerate(lines):
            if vr_interim_pos in line:
                index = line.index(vr_interim_pos)
                if index == 1 or index == 2:
                    win_flag = all(cr_check(line_point, opponent_1.color) == 1 and line_point != vr_interim_pos for line_point in line[1:])
                    if not win_flag:
                        break
                else:
                    win_flag = cr_check(line[1], opponent_1.color) == cr_check(line[2], opponent_1.color) == 1
                    if not win_flag:
                        break

        if win_flag == 1:
            # print("Yes")
            font_1 = pygame.font.Font(None, 36)
            text_1 = font_1.render("Opponent_1 Wins!", True, (0, 0, 0))
            textRect_1 = text_1.get_rect()
            textRect_1.center = (400, 150)
            screen.blit(text_1,textRect_1)
            pygame.display.update()
            pygame.time.delay(2000)
            running = False



# <------------------------------------------------------GAME VARIABLES-------------------------------------------------------->

class crow:
    def __init__(self,color,count):
        self.color = color
        self.count = count

    def cr_movement(self,event):
        global dragging
        global cr_interim_pos
        global turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = getCoord()
            static = cr_check(pos,self.color)
            if static == 1:
                dragging = True
                cr_interim_pos = pos
                pawns.remove((pos,self.color))
        if event.type == pygame.MOUSEBUTTONUP:
            pos = getCoord()
            static = cr_check(pos,self.color)
            if dragging and pos != None:
                if static == 2 and self.count >= 7:
                    temp = (pos,self.color)
                    pawns.append(temp)
                    turn = (turn + 1) % 2
                else:
                    temp = (cr_interim_pos,self.color)
                    pawns.append(temp)
                dragging = False
            elif self.count < 7 and pos != None and dragging == False:
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
        global vr_interim_pos
        global turn
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = getCoord()
            static = vr_check(pos,self.color,True)
            # print(static)
            if static == 1:
                dragging = True
                vr_interim_pos = pos
                pawns.remove((pos,self.color))
        if event.type == pygame.MOUSEBUTTONUP:
            pos = getCoord()
            if dragging and pos != None:
                static = vr_check(pos,self.color,False)
                # print(static)
                if static == 2:
                    temp = (pos,self.color)
                    pawns.append(temp)
                    vr_interim_pos = pos
                    turn = (turn + 1) % 2
                else:
                    temp = (vr_interim_pos,self.color)
                    pawns.append(temp)
                dragging = False
            elif self.count < 1 and pos != None:
                static = vr_check(pos,self.color,False)
                if static == 2:
                    self.count = self.count + 1
                    temp = (pos,self.color)
                    pawns.append(temp)
                    turn = (turn + 1) % 2
                    vr_interim_pos = pos


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
        
        # print(turn)
        if(turn == 0):
            opponent_1.cr_movement(event)
        else:
            opponent_2.vr_movement(event)
        # set the center of the rectangular object.vement(event)
    
    if dragging:
        continue
    
    draw(pawns)
    pygame.display.update()
    check_win()
    # # get pawns co-ordinate
    # x, y = pygame.mouse.get_pos()
    # print(x)
    # print(y)
            
    
    # must to make changes visible

# Done! Time to quit.
pygame.quit()