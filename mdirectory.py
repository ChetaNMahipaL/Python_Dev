from prettytable import PrettyTable
import subprocess as sp

class Enteries:
    def __init__(self):
        self.rows = []
    
    def add_entry(self,info):
        self.rows.append(info)

    def display_data(self,table_rep):
        table = PrettyTable()
        table.field_names = ["First Name","Last Name","Roll Number","Course Name","Semester","Exam Type","Total Marks","Scored Marks"]
        for entry in table_rep:
            table.add_row([entry["FirstName"],entry["LastName"],entry["Roll_No"],entry["CourseName"],entry["Semester"],entry["ExamType"],entry["TotalMarks"],entry["ScoredMarks"]])
        print(table)
    
    def search(self,srch_param):
        search_results = []
        for entry in self.rows:
            match = all(entry[key] == value for key, value in srch_param.items())
            if match:
                search_results.append(entry)
        return search_results

    def edit(self,ed_param,key,nval):
        for ed_params in ed_param:
            for entry in self.rows:
                if all(entry[k] == v for k, v in ed_params.items()):
                    entry[key] = nval

    def remove_entry(self,rem_param):
        for entry in rem_param:
            self.rows.remove(entry)

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
    # print(dict)
    mdirect.add_entry(dict)

def params():
    print("Keys are as follow:\nFirstName, LastName, Roll_No, CourseName, Semester, ExamType, TotalMarks, ScoredMarks ")
    temp = input("Enter the parameters to query on: ") 
    # enter key first then value wihtout space and each parmater space separated
    # example FirstName,Rajat LastName,Garg and so on
    # only 1 value per key
    # search parameters will be in conjunction
    x = temp.split()
    search_dict = {}
    for val in x:
        peak = val.split(",")
        search_dict[peak[0]]=peak[1]
    return mdirect.search(search_dict)

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
    print("Enter 7 to store the database")
    print("Enter 0 to exit the menu")
    
    arg_input = input("Enter the command: ")
    arg_input = int(arg_input)

    if(arg_input == 1):
        add_entry()
    if(arg_input == 2):
        ans_search = params()
        mdirect.display_data(ans_search)
    if(arg_input == 3):
        ans_search = params()
        temp_1 = input("Enter key of the cell: ")
        temp_2 = input("Enter new value: ")
        mdirect.edit(ans_search,temp_1,temp_2)
    if(arg_input == 4):
        ans_search = params()
        mdirect.remove_entry(ans_search)
    if(arg_input == 5):
        mdirect.display_data(mdirect.rows)
    if(arg_input == 6):
        pass
    if(arg_input == 7):
        pass
    if(arg_input == 0):
        break
