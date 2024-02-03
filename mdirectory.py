from prettytable import PrettyTable
import subprocess as sp

class Enteries:
    def __init__(self):
        self.rows = []
    
    def add_entry(self,info):
        self.rows.append(info)

    def display_data(self):
        table = PrettyTable()
        table.field_names = ["First Name","Last Name","Roll Number","Course Name","Semester","Exam Type","Total Marks","Scored Marks"]
        for entry in self.rows:
            table.add_row([entry["FirstName"],entry["LastName"],entry["Roll_No"],entry["CourseName"],entry["Semester"],entry["ExamType"],entry["TotalMarks"],entry["ScoredMarks"]])
        print(table)
    
    def search(self,srch_param):
        pass

    def edit(self,ed_param):
        pass

    def remove(self,rem_param):
        pass

mdirect = Enteries()
# Menu based input

def add_entry():
    dict = {}
    temp = input("Enter First Name: ")
    dict["FirstName"] = temp
    temp = input("Enter Last Name: ")
    dict["LastName"] = temp
    temp = input("Enter Roll Number: ")
    dict["Roll_No"] = temp
    temp = input("Enter name of the course: ")
    dict["CourseName"] = temp
    temp = input("Enter semester in which it was taken: ")
    dict["Semester"] = temp
    temp = input("Enter type of examination: ")
    dict["ExamType"] = temp
    temp = input("Enter maximum marks of examination: ")
    dict["TotalMarks"] = temp
    temp = input("Enter marks obtained: ")
    dict["ScoredMarks"] = temp
    print(dict)
    mdirect.add_entry(dict)






flag = 0

while(1):
    if flag > 0:
        temp_1 = input("Press Enter to Continue")
        tmp = sp.call('clear', shell=True)
    flag = flag + 1
    print("Enter 1 to add new entry")
    print("Enter 2 for searching entry")
    print("Enter 3 for editing entry")
    print("Enter 4 for removing entry")
    print("Enter 5 to display directory")
    print("Enter 6 to load csv file")
    print("enter 0 to exit the menu")
    
    arg_input = input("Enter the command: ")
    arg_input = int(arg_input)

    if(arg_input == 1):
        add_entry()
    if(arg_input == 2):
        pass
    if(arg_input == 3):
        pass
    if(arg_input == 4):
        pass
    if(arg_input == 5):
        mdirect.display_data()
    if(arg_input == 6):
        pass
    if(arg_input == 0):
        break
