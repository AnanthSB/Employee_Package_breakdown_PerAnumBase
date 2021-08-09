#python OOP program to breakdown an Employee Compensation details in Per Anum Format,
# in Anexure format of an offer letter 
# just by taking E.name and fixed pay PA in the below format

#Ex: chandan,100000
"""
              ANNEXURE-II
           COMPENSATION DETAILS
_______________________________________________________________________
Company Name                    XYZ India PVT lim.
Name                            chandan
Band                            5A
Designation                     Process Associate
Location                        India>Hyderabad>Hyderabad Gachibowli - xyzOffice
Basic Pay                       66000
Employer Contribution to PF     7920
House Rent Allowence            26079
Fixed Pay                       100000
_________________________________________________________________________________________________________________"""
class Per_Anum_salary():
    Cname = "XYZ India PVT lim."       #Company name as Cname
    basic_pay =      0                
    employer_contribution_to_PF    = 0
    house_Rent_Allowence   =         0
    # fixed_pay   =   0                    

    def __init__(self,Ename,Eband,Edesign,Elocation):
        self.Ename = Ename
        self.Eband = Eband
        self.Edesign = Edesign
        self.Elocation = Elocation

    @property
    def fixed_pay(self):
        return  (self.basic_pay + self.employer_contribution_to_PF + self.house_Rent_Allowence)

    @fixed_pay.setter
    def fixed_pay(self,fp):                                         
        self.basic_pay =   ((66/100)*fp)                            #Basic Pay is 66% 
        self.employer_contribution_to_PF = ((7.9203/100)*fp)        #Employer PF is (7.9203%)
        self.house_Rent_Allowence       =   ((26.08/100)*fp)        #House rent (26.08)%

    @property
    def Ecompensation_details(self):
        return f"""\n\t      ANNEXURE-II\n\t   COMPENSATION DETAILS\n________________________________________________________________________________
Company Name\t\t\t{self.Cname}\nName\t\t\t\t{self.Ename}\nBand\t\t\t\t{self.Eband}\nDesignation\t\t\t{self.Edesign}\nLocation\t\t\t{self.Elocation}
Basic Pay\t\t\t{int(self.basic_pay)}\nEmployer Contribution to PF\t{int(self.employer_contribution_to_PF)}\nHouse Rent Allowence\t\t{int(self.house_Rent_Allowence)}\nFixed Pay\t\t\t{int(self.fixed_pay)}\n"""

while 1:
    try:
        inpu = input("Select\n1 = Give employee E.C data\n2 = Fetch EC data\n3 = Exit\n_")
        if int(inpu) == 3:
            print("____Have a nice day____")
            print(exit())
        elif int(inpu) == 1: 
            Ename = input("Enter Employee name\n>> ")
            Eband = "5A"
            Edesign = "Process Associate"
            Elocation   = "India>Hyderabad>Hyderabad Gachibowli - xyzOffice"
            
            #This changes will be impletementd soon
            #can chang later below properties
            # BP =       int(input("Enter the Basic salary per anum__"))                #191400    #BP as Basic Pay
            # ECPF =    int(input("Enter the Employer Contribution to PF__"))           #22968     #ECPF as Employer Contribution to PF
            # HRA =     int(input("Enter the  Housing Rent Allowence__"))               #75632     #HRA as House Rent Allowence
            # FP = 290000                                                                          # FP as Fixed Pay 

            #instatiating an object guest as a user 
            guest = Per_Anum_salary(Ename,Eband,Edesign,Elocation)
            guest.fixed_pay = int(input("Enter the Fixed Pay of Emolyee PerAnum>> "))  #290000
            
            #This function will be implented soon
            #for monthly salary
            # print(sharath.Per_month_salary)
            # print(sharath.Per_day_salary)
            EC = guest.Ecompensation_details
            print(f"The {Ename} EC data stored as below:\n{EC}")
            with open(f"C:\\Users\\91967\\Desktop\\codeisfun\\Learnings\\1_python\\My_completed_Projects\\5_Employee_offer_letter_format_of_compensation\\employee_Data\\{Ename}.txt","w") as w:
                w.write(f"{EC}")
        else:
            if int(inpu) == 2:
                filename = input("Enter Employee name to fetch his E.C\n_")    
                try:
                    filename = filename.lower()
                    with open(f"C:\\Users\\91967\\Desktop\\codeisfun\\Learnings\\1_python\\My_completed_Projects\\5_Employee_offer_letter_format_of_compensation\\employee_Data\\{filename}.txt","r") as r:
                        R = r.read()
                        print(f"{filename} Compensetion details:\n{R}")
                except Exception as e:
                    print(f"\nOop!No such file found\n{filename}'s E.C file doesn't exist in our Data Base\n")
    except Exception as e:
        print("Oop!, select the right option\n_")

"""_____________________________________________________THE_END_____________________________________________________"""