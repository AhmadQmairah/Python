from datetime import date,timedelta
from math import ceil
def check_birthday(year,month,day):
    
    users_date=date(year,month,day)
    if(date.today() < users_date):
        
        return False
    return True


def calculate_Age(year,month,day):
    
    users_date=date(year,month,day)
    
    year= (date.today()-users_date).days/365.245
    month= (year %1) *12
    day= (month%1) *  30
    print("you are %d years, %d months and %d days" %(year,month,ceil(day)))



while(True):
    try :
        year= int(input("Enter year of birth: "))
        month=int(input("Enter month of birth: "))
        day=int(input("Enter day of birth: "))
        
        if(check_birthday(year,month,day)):
            calculate_Age(year,month,day)
            break
        else:
            print("please enter a valid date\n%s" %("-"*30))
        

    except:
         print("please enter a valid date\n%s" %("-"*30))
         continue
    
      
     

    



   





   

