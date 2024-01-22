class Co_ordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def update_co_ord(self,distance,angle):
        if angle == 0:      # North
            y = y + distance
        if angle == 180:    # South
            y = y - distance
        if angle == 90:     # East
            x = x + distance
        if angle == 270:    # West
            x = x - distance
        if angle == 45:
            x

        

class Direction:
    def __init__(self,name,angle):
        self.name=name
        self.direc_angle=angle
    # North - 0
    # South - 180
    # East - 90
    # West - 270
    # North - East - 45
    # South - East - 135
    # South - West - 225
    # North - West - 315
    def get_angle(self):
        return self.direc_angle
    def __str__(self):
        return self.name