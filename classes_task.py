from datetime import date
class Employee:

    def __init__(self,name,age,salary,employment_date):
        self.name=name
        self.age=age
        self.salary=salary
        self.employment_date=employment_date

    def get_working_years(self):
        return (date.today().year- self.employment_date)

    
    def __str__(self):
        DisplayText= "Name:{}\nAge:{}\nsalary:{}\nWorking Years:{}".format(self.name,self.age,self.salary,self.get_working_years())
        return DisplayText;
        


class Manager(Employee):

    def __init__(self,name, age,salary,employment_date,bonus_percentage):
      Employee.__init__(self, name, age,salary,employment_date)
      self.bonus_percentage=bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    
    def __str__(self):
        DisplayText= "Name:{}\nAge:{}\nsalary:{}\nWorking Years:{}\nBonus:{} ".format(self.name,self.age,self.salary,self.get_working_years(),self.get_bonus())
        return DisplayText;


def add_user(Type):

    try:
         Name= input("name: ")
         
         if(not Name.isalpha()):
             raise Exception
            
         age= int (input("age: "))
         salary=int(input("salary: "))
         employement_year= int(input("employement year: "))

         if( Type==1):
             bonus_percentage= float(input("bonus percentage: "))
             managers.append(Manager(Name,age,salary,employement_year,bonus_percentage))
         else:
             employees.append(Employee(Name,age,salary,employement_year))
         
    except:
        print("Invalid Input")
        
        
         
         
    


    
managers=[]      
employees =[]  




print("   Welcome to HR Pro 2019")

while True:
    print("""
        Choose an action to do:
            1. show employees
            2. show managers
            3. add an employee
            4. add a manager
            5. exit
    """)

    Input=input("what would you like to do? ")
    if(Input=="1"):
        print("-"*20)
        for employee in employees:
            print(employee)
            print("-"*20)

        print("\nFinisehd listing  all employees")
    elif(Input=="2"):
        print("-"*20)
        for manager in managers:
            print(manager)
            print("-"*20)
        
        print("\nFinisehd listing  all managers")

    elif(Input=="3"):
        add_user(0)
        
                         
    elif(Input == "4"):
        add_user(1)

    elif(Input =="5"):
        print("GoodBye")
        break
    else:
        print("Invalid Input")
        continue
                         
                         

                    
        
                         
     
     
                     
                     
                    
