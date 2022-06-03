
from datetime import datetime
import re
print("\n<<~~~~~ Welcome to Crowd-Funding console app ~~~~>>\n")
def authuser():
    ch = input("   [1] REGISTER   ..or..    [2] LOGIN   ..or..   [3] EXIT  \n")
    if ch == "1" :    
        register()
    elif ch == "2" :
        login()
    elif ch == "3" :
        exit()
    else:
        print("Invalid input!!")
        authuser()    
def register():
    fname = input(" >> First name: ")
    valname(fname)
    lname = input(" >> Last name: ")
    valname(lname)
    eml = input(" >> Email: ")
    emlval(eml)
    passwd = input(" >> Pasword: ")
    passval(passwd)
    confpasswd = input(" >> Confirm Password: ")
    confpas(passwd,confpasswd)
    phone = input(" >> Mobile: ")
    phoneval(phone)
    user_data = f"{fname}:{lname}:{eml}:{passwd}:{phone}\n"
    #user_data = {"fname":fname,"lname":lname,"email":eml,"password":passwd,"phone":phone}
    print(" >> Welcome ",fname ,"You have registered successfully ")
    usersfile= open("users.txt","a")
    usersfile.write(user_data)
    usersfile.close()
    projects(eml)
    ###### redirect user to projects #######
########### validation Functions ####### 
def valname(name):
        if name.isdigit() or not name or len(name) < 3:
            print(">> invalid name!!  , please Enter valid name ")
            name = input()
            valname(name)
        else:
            return name
def emlval(eml):
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, eml)):
            usersfile = open("users.txt", "r")
            usersdata = usersfile.readlines()  #read file content into a list
            for i in usersdata:
                i = i.strip("\n")  # remove chars from the beginning and the end of the string
                user = i.split(":")  # split string into parts ---> according to seperator
                # save content into a list
                #print(user)
                # print(usersdata)
                if eml == user[0] :
                    eml = input(" this Email already Exist , Enter another one or Press [1] to login: ")
                    if eml == "1":
                        authuser()
                    else:
                        emlval(eml)
                
            return eml
        else:
            print(">> invalid email!! ,  please enter valid one:  ")
            eml = input()
            emlval(eml)
def passval(passwd):
        reg = "^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])"
        pat = re.compile(reg)
        mat = re.search(pat, passwd)
        if mat:
            return passwd
        else:
            print(">> invalid password!! ,  please enter valid one:  ")
            passwd = input()
            passval(passwd)
def confpas(passwd,confpasswd):
    
    if passwd == confpasswd:
        return confpasswd
    else:
        print(">> invalid confirmed password !!  Enter Again:  ")
        confpasswd = input()
        reg = "^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])"
        pat = re.compile(reg)
        mat = re.search(pat, confpasswd)
        if mat:
            passwd = confpasswd
            confpas(passwd,confpasswd)
        else:
            print(">> invalid password!! ,  please enter valid one:  ")
            confpasswd = input()
            confpas(passwd,confpasswd)           
def phoneval(phone):
    regex = r'00201[0125]+[0-9]{8}'
    if(re.fullmatch(regex, phone)):
        return phone
    else:
        print(">> Invalid phone number !! Enter valid one: ")
        phone = input()
        phoneval(phone)
def login():
    while True:
        user_mail = input(">> Email:  ")
        user_pass = input(">> Password:  ")
        usersfile = open("users.txt", "r")
        usersdata = usersfile.readlines()  #read file content into a list
        ##
        auth = False
        ##
        user = []
        for i in usersdata:
            i = i.strip("\n")  # remove chars from the beginning and the end of the string
            user = i.split(":")  # split string into parts ---> according to seperator
            # save content into a list
            #print(user)
            # print(usersdata)
            if user_mail == user[2] and user_pass == user[3] :
                auth = True
                
        if auth:
            print(" Welcome back !")
            break
        else:
            print("Email or Password isn't correct 'try again'")
            
        usersfile.close()
    projects(user_mail)
def projects(user_mail):
    print("\n<<--- Welcome to PROJECTS section --->>\n")
    ch = input("""
      [1] Create project
      [2] View projects
      [3] Edit project
      [4] Delete project
      [5] Search for project
      [6] Back to Main Menu
      \n
      >> Press choice number 
      """)
    if ch == "1":
        create_projects(user_mail)
    elif ch == "2":
        view_projects(user_mail)
    elif ch == "3":
        edit_project(user_mail)
    elif ch == "4":
        delete_project(user_mail)
    elif ch == "5":
        search_project(user_mail)
    elif ch == "6":
        authuser()
    else:
        print("Invalid Input , choose from list: ")
        projects(user_mail)      
############### start  Create Project section ##################
def create_projects(user_mail):
    print("\n<<--- Welcome to Create PROJECTS section --->>\n",user_mail)
    print("\nEnter project data:\n")
    title = input("Title:  ")
    details = input("Details:  ")
    total_target = input("Total target:  ")
    start_time = input("Start Date (mm/dd/yyyy): ")
    end_time = input("End Date (mm/dd/yyyy): ")
    P_data = f"{user_mail}:{title}:{details}:{total_target}:{start_time}:{end_time}\n"
    #print(P_data)
    format = "%d/%m/%Y"
    try:
        
        v_start_date = datetime.strptime(start_time,format)
        v_end_date   = datetime.strptime(end_time,format)
        if v_start_date and v_end_date :
            project_file = open("project_data.txt", "r")
            project_data = project_file.readlines() 
            for i in project_data:
                i = i.strip("\n")  
                pr = i.split(":") 
                if title == pr[1] :
                    print("this project already Exist")
                    projects(user_mail)
                    #create_projects(user_mail)
                else:
                    project = open("project_data.txt","a")
                    project.write(P_data)
                    project.close()
                print("Data inserted successfully")
                projects(user_mail)
        else:
            print("invalid date !! ")
            create_projects(user_mail)
    except ValueError:
        print("invalid date !! ")
        create_projects(user_mail)   
############### end  Create Project section ##################
############### start  view Project section ##################
def view_projects(user_mail):
    list = []
    main_file = open("project_data.txt","r")
    for line in main_file:
        line = line.strip("\n")  
        pr = line.split(":") 
        list.append(pr)
        
    main_file.close()
    #print(list)
    for record in list:
        if record[0] == user_mail:
            print(record,"\n")
        else:
            print(" ")
    projects(user_mail)
############### end  view Project section ##################
############### start  edit Project section ##################
def edit_project(user_mail):
    nameofproject = input("\nEnter project name:  ")
    list = []
    main_file = open("project_data.txt","r")
    for line in main_file:
        line = line.strip("\n")  
        pr = line.split(":") 
        list.append(pr)
        
    main_file.close()
    #print(list)
    
    main_file = open("project_data.txt","w")
    main_file.write("")
    main_file.close()
    f=1
    for record in list:
        if record[0] == user_mail and record[1] == nameofproject :
            column = input("choose number of column to update [1-Title] [2-Details] [3-Total target] [4-start date] [5-End date] :  ")
            if column == "1":
                recval = input("Enter new value to update: ")
                record[1]=recval
                f=0
                break
            elif column == "2":
                recval = input("Enter new value to update: ")
                record[2]=recval
                f=0
                break
            elif column == "3":
                recval = input("Enter new value to update: ")
                record[3]=recval
                f=0
                break
            elif column == "4":
                recval = input("Enter new value to update: ")
                record[4]=recval
                f=0
                break
            elif column == "5":
                recval = input("Enter new value to update: ")
                record[5]=recval
                f=0
                break
            else:
                print("Invalid choice!!!")
                edit_project(user_mail)
    if f == 1:   
        print("project doesn't exist!!!")
    for add_data in list:
        n_data = open("project_data.txt","a")
        x = ":".join(add_data)
     #   print("value of x",x)
        n_data.write(x)
        n_data.write("\n")
        n_data.close()
    #print("\n new list :" ,list)
    projects(user_mail)
############### end  edit Project section ##################
############### start  delete Project section ##################
def delete_project(user_mail):
    
    nameofproject = input("\nEnter project name:  ")
    list = []
    main_file = open("project_data.txt","r")
    for line in main_file:
        line = line.strip("\n")  
        pr = line.split(":") 
        list.append(pr)
        
    main_file.close()
    #print(list)
    
    main_file = open("project_data.txt","w")
    main_file.write("")
    main_file.close()
    f=1
    for record in list:
        if record[0] == user_mail and record[1]==nameofproject :
            list.remove(record)
            f = 0
            break
    if f == 1:
        print("project doesn't exist!!!")
        
            
    for add_data in list:
        n_data = open("project_data.txt","a")
        x = ":".join(add_data)
    #   print("value of x",x)
        n_data.write(x)
        n_data.write("\n")
        n_data.close()
    #print("\n new list :" ,list)
    projects(user_mail)
############### end  delete Project section ##################
############### start  search Project section ##################
def search_project(user_mail):
    nameofproject = input("\nEnter project name:  ")
    list = []
    main_file = open("project_data.txt","r")
    for line in main_file:
        line = line.strip("\n")  
        pr = line.split(":") 
        list.append(pr)
        
    main_file.close()
    #print(list)
    for record in list:
        if record[0] == user_mail and record[1] == nameofproject:
            print(record,"\n")
        else:
            print("you haven't any projects to display! ")
    projects(user_mail)
############### end  search Project section ##################
authuser()