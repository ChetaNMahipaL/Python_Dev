from prettytable import PrettyTable

class Enteries:
    def __init___(self):
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

while(1):
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
        pass
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
