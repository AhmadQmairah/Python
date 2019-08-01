skills= ["python","c++","javascript","Java","NodeJs","C#"]
cv={"skills":[]}
order=1

while True:
    try:
        cv["name"]=input("name: ")
        if( not cv["name"].isalpha()):
            raise Exception ("Please enter a valid name\n\n")
        cv["age"]=input("age: ")
        
        if(not cv["age"].isdigit() or int(cv["age"]) <=0):
            raise Exception ("Please enter a valid age\n\n")
            
            
        cv["experience"]=input("how many years of experience do you have? ")
        if(not cv["experience"].isdigit() or int(cv["experience"]) < 0 or int(cv["experience"]) >=  int(cv["age"])  ):
            raise Exception ("Please enter a valid experience\n\n")
        break
        
    except Exception as err:
        print(err)
        
        continue
           
        

print("\n-------------------------------------------")
for skill in skills:
    print (str(order)+"-",skill)
    order+=1
while True:
    try:
        skill_1=int(input("choose a skill from above: "))
        
        skill_2=int(input("choose another skill from above: "))
        if( 1<skill_1 , skill_2<6 ):
             cv["skills"].append(skills[skill_1-1])
             cv["skills"].append(skills[skill_2-1])
             break
        else:
            raise Exception
            
       
    except:
        print("Please enter a valid skill\n\n")
        continue
        

    


if( 22<=int(cv["age"])<=40 and int(cv["experience"]) >=5 and "C#" in cv["skills"]):
    print("you have been accepted, %s" %(cv["name"].title()))
else:
    print(" you are not accepted , %s" %(cv["name"].title()))





