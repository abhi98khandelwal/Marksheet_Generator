import os

def main_menu():
    #global choice_main 
    #Main_Menu
    """Displays the Main Menu and Takes Input of the suitable Choice"""

    print "_"*80
    print "-"*80
    print "\t \t \t \tMAIN-MENU"
    print "\t \t \t \t"+"~"*9
    print "1: New Data Entry"
    print "2: Update Stored Marks"
    print "3: Display Marksheet"
    print "4: Display Top 10 Students of a Class"
    print "5: Display Studens Eligible for Scholar Badge"
    #print "00000: Exit"
    print "_"*80
    print "-"*80
    print
    
    #Choice is Entered Here
    bridge = True
    while bridge:
        try:
            choice = int(raw_input("Enter the Choice:"))
            if choice > 6:
                print 1/0
        except:
            print "Only Integers between 1-6 allowed"
            bride = True
        else:
            bridge = False
            if choice == 1:
                entry = data_entry()
                entry.Input_record()
            elif choice == 2:
                update=update_entry()
            elif choice == 3:
                view_marksheet_obj=view_marksheet()
                view_marksheet_obj.det_student()
                view_marksheet_obj.select_data()
            elif choice == 4:
                t_ten= top_ten()
            elif choice == 5:
                sch_badge = scholar_badge()
            elif choice == 6:
                choice_main = "n"
                

class data_entry(object):
    """Class for dataentry"""
    
    def __init__(self):
        """Method to initialize the class"""
        self.name = ""
        self.f_name = ""
        self.m_name = ""
        self.dob = ""
        self.Class = 0
        self.sec = ""
        self.ad_no = ""
        self.myfile = ""
        self.mode = 1
        self.l_of_sub = []
        self.l_name_sub = [None,"English","Maths","Physics","Chemistry","Computer Science","E.G.","Economics","Biology","Biotechnology","Acountancy","Recodkepping","Bookkeeping","Taxation","Cost Analysis"]
                

    def Input_record(self):
        """Method to Input Record"""
        
        bridge = True        
        
        self.name = raw_input("Enter the Name of the Student:")
        if self.name == "":
            print "Please Enter a name"
            self.name = raw_input("Enter the Name of the Student:")

        self.f_name = raw_input("Enter Father's Name:")
        if self.f_name == "":
            print "Please Enter a name"
            self.f_name = raw_input("Enter Father's Name:")

        self.m_name = raw_input("Enter Mother's Name:")
        if self.m_name == "":
            print "Please Enter a name"
            self.m_name = raw_input("Enter Mother's Name:")

        self.dob = raw_input("Enter Date of Birth(DD/MM/YYYY):")
        self.date_checker()
        
        
        self.Class_checker()
        self.sec_checker()
        self.ad_no = raw_input("Enter the Admission Number ")
        self.ad_no_checker()
        self.file_select()
        self.sub_select()

    
    def file_select(self):
        """Method to select file"""
        
        if self.Class == "11":
            self.myfile=open("class_11\Record.txt","a")
        elif self.Class == "12":
            self.myfile=open("class_12\Record.txt","a")
    

    def sub_select(self):

        """Method to Select Subjet w.r.t. section"""
        
        if self.sec in ["a","b","c"]:           
            self.l_of_sub = [1,2,3,4,5]

        elif self.sec in ["c","d","e","f"]:
            #E.G.        
            self.l_of_sub = [1,2,3,4,6]

        elif self.sec == "g":
            #Economics
            self.l_of_sub = [1,2,3,4,7]
       
        elif self.sec == "h":
            #Bio - Maths
            self.l_of_sub = [1,2,3,4,8]
           
        elif self.sec == "i":
            # Bio-Biotech
            self.l_of_sub = [1,3,4,8,9] 
            
        elif self.sec == "j":
            #  j = "comm, maths"       
            self.l_of_sub = [1,10,11,12,13]           
            
        elif self.sec == "k":
            # k = "com, ip"
            self.l_of_sub = [1,11,12,13,14]

        if self.mode == 1:
            self.marks_input(self.l_of_sub,self.myfile)
    
            
    def sec_checker(self):
        """Method to Check Section and take input"""
        
        bridge_sec = True
        while bridge_sec:
            self.sec = raw_input("Enter the section:").lower()
            if self.sec not in ["a","b","c","d","e","f","g","h","i","j","k"]:
                print "Please Enter proper Section"
                bridge_sec = True
            else:
                bridge_sec = False


    def Class_checker(self):
        """Method to check Class and take Input"""
        
        bridge_class = True
        while bridge_class:
            self.Class = raw_input("Enter the class (11/12):")
            if self.Class == "11" or self.Class == "12":
                bridge_class = False
            else:
                print "Please Enter proper Class"
                bridge_class = True


    def ad_no_checker(self):
        """Method to Check Admission Number"""
        
        bridge = None
        try:
            check_len = self.ad_no[1]
        except:
            bridge = True
            
        while bridge or self.ad_no[1]!="-" or self.ad_no=="" :
            print "Enter Admission number(like-B-3212)"
            self.ad_no = raw_input("Enter the Admission Number ")
            
            try:
                tryy= int(self.ad_no[2::])
            except:
                bridge = True
            else:
                bridge = False

            if self.ad_no[0].lower()!="b":
                bridge = True


    def date_checker(self):
        """Method to check the date"""
        bridge = False
        try:
            while self.dob=="" or self.dob[-5]!= "/" or self.dob[-8] != "/" or bridge:
                #Date checker needs to be added
                print "Enter a valid date"
                self.dob = raw_input("Enter Date of Birth(DD/MM/YYYY):")
        except:
            print"Enter a Valid Date"

                
    def marks_input(self,l_of_sub,myfile):
        """Method to take Input from user and write data to file"""
        #Input_taker
        l_marks=[]
        l_name_sub = [None,"English","Maths","Physics","Chemistry","Computer Science","E.G.","Economics","Biology","Biotechnology","","","","",""]
        myfile.write(self.name+" ^\t"+self.f_name+" ^\t"+self.m_name+" ^\t"+self.dob+" ^\t"+self.Class+" ^\t"+self.sec+" ^\t"+self.ad_no+" ^\t")
        for i in range(1,16):
            if i in l_of_sub:
                subject_name ="print'Marks obtained in',l_name_sub[i],'out of 100'" 
                exec(subject_name)
                
                subject_mark = float(raw_input())
                while 100.0<subject_mark<0.0:
                    subject_mark = float(raw_input("Please Enter Marks out of 100"))
                l_marks.append(subject_mark)
            else:
                l_marks.append("~")
        for ii in l_marks:
            myfile.write(str(ii)+"^\t")
        myfile.write("\n")
        myfile.close()


class view_marksheet(data_entry):
    """Class for Marksheet display"""
    def __init__(self):
        data_entry.__init__(self)
        self.percent = 0
        self.mode = 3

    def det_student(self):
        """Method to Determine the Student"""
        
        self.Class_checker()
        self.sec_checker()
        self.ad_no = raw_input("Enter the Admission Number ")
        self.ad_no_checker()
        self.file_open()
        
    def file_open(self):
        """Method to select file"""
        if self.Class == "11":
            self.myfile=open("class_11\Record.txt","r")
        elif self.Class == "12":
            self.myfile=open("class_12\Record.txt","r")

  
    def select_data(self):
        """Method to select data that needs to be displayed"""
        
        

        bridge_read_data = True
        record_raw = ["None"]
        r = 1
        while record_raw[0]!="" and bridge_read_data:
            record_raw = self.myfile.readline().split("^")
            record = []
            for i in  record_raw:
                temp_data = i.strip()
                record.append(temp_data)
                
            if record[0]!="" and record[6]== self.ad_no:
                r = 0
                self.l_name_sub = [None,"English","Maths","Physics","Chemistry","Computer Science","E.G.","Economics","Biology","Biotechnology","Acountancy","Recodkepping","Bookkeeping","Taxation","Cost Analysis"]
                bridge_read_data = False
                record_new= []
                for i in record:
                    if i != "~":
                        record_new.append(i)

                self.sub_select()
                index = 7
                sr_no = 1

                print "Name:",record_new[0],"\t "
                print "Class:",record_new[4]+"-"+record_new[5]
                print "Date of Birth",record_new[3]
                print "Father Name:",record_new[1]
                print "Mother Name:",record_new[2]
                
                print "-"*40
                print "-"*40
                print "%-5s\t%-20s\t%0s"%("S.no.","Subject","Marks")
                print "-"*40

                for j in self.l_of_sub:
                    print "%5s\t%-20s\t%-2s"%(sr_no,self.l_name_sub[j],record_new[index])
                    self.percent+=float(record_new[index])
                    index+=1
                    sr_no+=1
                print "-"*40

                self.percent = (self.percent/5.0)
                print "Percentage obtained",self.percent
                print "-"*40
                break
        if r == 1:
            print "Record not found in database"

                
class update_entry(view_marksheet,data_entry):
    """Class for Updating the record or entry"""
    def __init__(self):
        self.mode = 0
        self.tempfile = ""
        view_marksheet.__init__(self)
        view_marksheet.det_student(self)
        self.temp_file()
        

    def temp_file(self):
        """Method to open a temp file used for editing the record"""
        if self.Class == 11:
            self.myfile1=open("class_11\\temp.txt","w")
            self.update_menu()
        else:
            self.myfile1=open("class_12\\temp.txt","w")
            self.update_menu()
            

    def update_menu(self):
        """Method to display the Update menu"""
        data_entry.sub_select(self)
        print
        print "Select proper index to update marks in a subject:"
        for i in range(1,len(self.l_name_sub)):
            if i in self.l_of_sub:
                print str(i)+")",self.l_name_sub[i]

        print       
        self.index_change = int(raw_input("Enter the index:"))
        while self.index_change not in self.l_of_sub:
            self.index_change = int(raw_input("Please enter proper the index:"))

        self.change()

    def change(self):
        """Method that changes the record for the given student"""

        bridge_read_data = True
        record_raw = ["None"]
        r = 1

        while record_raw[0]!="" and bridge_read_data:
            record_raw= self.myfile.readline().split("^")
            if record_raw[0]!="":
                record = []
                for i in  record_raw:
                    temp_data = i.strip()
                    if temp_data!="":
                        record.append(temp_data)
                
                    
                if record[0]!="" and record[6]== self.ad_no:
                    self.marks_new = float(raw_input("Enter the new Marks out of 100:"))
                    while 100.0<self.marks_new<0.0:
                        self.marks_new = float(raw_input("Enter the new Marks out of 100:"))
                        
                    record_raw[6+self.index_change] = "\t"+str(self.marks_new)
                
                    r = 0
                
                temp_l=[]
                for kk in record_raw:
                    if kk!="":
                        temp_l.append(kk+" ^")
                        
                for z in temp_l:
                    self.myfile1.write(z)

        if r ==1:
            print "Record not found."
        else:
            print "Changes Done."
        self.myfile.close()
        self.myfile1.close()
            
        if self.Class == 11:
            os.remove("class_11\Record.txt")
            os.rename("class_11\\temp.txt","Record.txt")
        else:
            os.remove("class_12\Record.txt")
            os.rename("class_12\\temp.txt","class_12\Record.txt")
        

class top_ten(view_marksheet,data_entry):
    """Class to display the Top ten students of a class"""
    def __init__(self):
        """Initializer"""
        
        self.marks = 0
        self.list_per= []
        data_entry.__init__(self)
        self.myfile = ""
        self.Class_checker()
        self.calc_per()
        

    def calc_per(self):
        """Method to calculate the Percentage and display the student details"""
        view_marksheet.file_open(self)
        bridge_read_data = True
        record_raw = ["None"]
        r = 1
        while record_raw[0]!="" and bridge_read_data:
            self.marks = 0
            record_raw = self.myfile.readline().split("^")
            record = []
            for i in  record_raw:
                temp_data = i.strip()
                record.append(temp_data)
            
            if record !=[""]:
                for j in range(7,22):
                    if record[j]!="~":
                        self.marks+=float(record[j])
                    
            self.list_per.append(self.marks/5.0)

        self.list_per.sort()
        self.list_per = self.list_per[-11:-1]
        

        bridge_read_data = True
        record_raw = ["None"]
        r = 1
        print
        print "---------------------------------Top Ten-------------------------------------"
        print
        view_marksheet.file_open(self)
        rawlist =[]
        while record_raw[0]!="" and bridge_read_data:
            self.marks = 0
            record_raw = self.myfile.readline().split("^")
            record = []
            for i in  record_raw:
                temp_data = i.strip()
                record.append(temp_data)
            self.name = record[0]
            if record !=[""]:
                for j in range(7,22):
                    if record[j]!="~":
                        self.marks+=float(record[j])
            self.per = (self.marks/5.0)
            if self.per in self.list_per:
                rawlist.append(self.name+":"+"0"+str(self.per))
                r+=1
                
        for j in range(len(rawlist)):
            for k in range(len(rawlist)):
                if float(rawlist[j][-5::]) > float(rawlist[k][-5::]):
                    rawlist[j],rawlist[k]=rawlist[k],rawlist[j]


        print "-"*45
        print "%-5s\t%-20s\t%0s"%("Rank","Name","Percentage")
        print "-"*45
        index = 1

        for m in range(len(rawlist)):
            name,per = rawlist[m].split(":")
            print "%5s\t%-20s\t%-2s"%(index,name,float(per))
            index+=1
        print "-"*45


class scholar_badge(view_marksheet,data_entry):
    """Class for displaying the Students eligible for Scholar badge"""
    def __init__(self):
        self.sch_list = []
        self.Class_checker()
        self.det_stud_scholar_badge()



    def det_stud_scholar_badge(self):
        bridge_read_data = True
        view_marksheet.file_open(self)
        rawlist =[]
        record_raw = ["           "]
        while record_raw[0]!="" and bridge_read_data:
            
            self.marks = 0
            record_raw = self.myfile.readline().split("^")
            if record_raw[0]!="":
                record = []
                for i in  record_raw:
                    temp_data = i.strip()
                    record.append(temp_data)
                self.name = record[0]
                if record !=[""]:
                    for j in range(7,22):
                        if record[j]!="~":
                            self.marks+=float(record[j])
                self.per = (self.marks/5.0)
                
                rawlist.append(self.name+":"+"0"+str(self.per))


        print "-"*45
        print "%-5s\t%-20s\t%0s"%("Sr. No.","Name","Percentage")
        print "-"*45
        index = 1
        for m in range(len(rawlist)):
            if float(rawlist[m][-5::])>=90.0:
                name,per = rawlist[m].split(":")
                print "%5s\t%-20s\t%-2s"%(index,name,float(per))
                index+=1
            
            

#-----------------------------------Main Program---------------------------------------
            
"""Main Program"""

#-----------------------------------Main Program---------------------------------------
"""Main Program"""

choice_main = "y"
while choice_main == "y":
    clear = lambda: os.system('cls')
    clear()
    main_menu()
    print
    choice_main = raw_input("Want to continue(y/n)")



