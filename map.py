import math
import matplotlib.pyplot as plt
import subprocess as sp

class Co_ordinate:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    def update_co_ord(self, distance, angle):
        if angle == 90:      # North
            self.y = self.y + distance
        elif angle == 270:   # South
            self.y = self.y - distance
        elif angle == 0:    # East
            self.x = self.x + distance
        elif angle == 180:   # West
            self.x = self.x - distance
        elif angle == 45:    # North-East
            self.x = self.x + distance / math.sqrt(2)
            self.y = self.y + distance / math.sqrt(2)
        elif angle == 315:   # South-East
            self.x = self.x + distance / math.sqrt(2)
            self.y = self.y - distance / math.sqrt(2)
        elif angle == 225:   # South-West
            self.x = self.x - distance / math.sqrt(2)
            self.y = self.y - distance / math.sqrt(2)
        elif angle == 135:   # North-West
            self.x = self.x - distance / math.sqrt(2)
            self.y = self.y + distance / math.sqrt(2)

    def total_dist(self, distance):
        self.dist = self.dist + distance

    def ret_tdist(self):
        return self.dist
    
    def loc_from_S(self):
        angle_S = math.atan2(self.y, self.x) / math.pi * 180
        if self.y == 0 and self.x == 0:
            return "On S"
        elif angle_S == 90:      # North
            return "North of S"
        elif angle_S == -90:   # South
            return "South of S"
        elif angle_S == 0:    # East
            return "East of S"
        elif angle_S == 180:   # West
            return "West of S"
        elif angle_S == 45:    # North-East
            return "North-East of S"
        elif angle_S == -45:   # South-East
            return "South-East of S"
        elif angle_S == -135:   # South-West
            return "South-West of S"
        elif angle_S == 135:   # North-West
            return "North-West of S"
        elif angle_S > 0 and angle_S < 90:    # North-East
            return (f"{angle_S} North of East from S")
        elif angle_S > -90 and angle_S < 0:   # South-East
            angle_S = angle_S * (-1)
            return (f"{angle_S} South of East from S")
        elif angle_S > -180 and angle_S < -90:   # South-West
            angle_S = angle_S + 180;
            return (f"{angle_S} South of West from S")
        elif angle_S > 90 and angle_S < 180 :   # North-West
            angle_S = 180 - angle_S
            return (f"{angle_S} North of West from S")

class path_diag:
    def __init__(self,x,y):
        self.x_coord = []
        self.y_coord = []
        self.x_coord.append(x)
        self.y_coord.append(y)
    
    def update_loc(self,x,y):
        self.x_coord.append(x)
        self.y_coord.append(y)
    
    def print_plot(self):
        plt.plot(self.x_coord,self.y_coord)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title("Movement of Person")
        plt.show()
    


#intialization
person_p = Co_ordinate(0,0,0)
line_graph = path_diag(0,0)

# Few assumptions:
# 1. Person will always start from origin
# 2. Distance can be in m.m. or c.m. both as input but result will be in c.m.

def process_input():
    print("The codes for direction are:\nNorth - N\nSouth - S\nEast - E\nWest - W\nNorth-East - NE\nNorth-West - NW\nSouth-East - SE\nSouth-West - SW")
    dist_in = input("Enter the input in specified format: ") # space between units , magnitude and direction
    x = dist_in.split()                           # Example input 2.5 mm N
    mag_dist = float(x[0])
        
    if( x[1] == "mm"):
        mag_dist = mag_dist / 10
    if(x[2] == "N"):
        person_p.update_co_ord(mag_dist,90)
    elif(x[2] == "S"):
        person_p.update_co_ord(mag_dist,270)
    elif(x[2] == "E"):
        person_p.update_co_ord(mag_dist,0)
    elif(x[2] == "W"):
        person_p.update_co_ord(mag_dist,180)
    elif(x[2] == "NE"):
        person_p.update_co_ord(mag_dist,45)
    elif(x[2] == "NW"):
        person_p.update_co_ord(mag_dist,135)
    elif(x[2] == "SE"):
        person_p.update_co_ord(mag_dist,315)
    elif(x[2] == "SW"):
        person_p.update_co_ord(mag_dist,225)
    person_p.total_dist(mag_dist)
    line_graph.update_loc(person_p.x,person_p.y)
    return


# Menu based input
# 1. For taking input.
# 2. For having 2D-Plot
# 3. For getting relative position
# 4. For getting total distance travelled
# 5. For exiting program
flag = 0

while(1):
    if flag > 0:
        temp = input("Press Enter to Continue")
        tmp = sp.call('clear', shell=True)
    flag = flag + 1
    print("Enter 1 to give input")
    print("Enter 2 for obtaining path of P")
    print("Enter 3 for current location of P with respect to S")
    print("Enter 4 for retrieving total distance travelled")
    print("Enter 5 to exit the program")
    
    arg_input = input("Enter the command: ")
    arg_input = int(arg_input)

    if(arg_input == 1):
        process_input()
    if(arg_input == 2):
        line_graph.print_plot()
    if(arg_input == 3):
        print(person_p.loc_from_S())
    if(arg_input == 4):
        print(person_p.ret_tdist())
    if(arg_input == 5):
        break

