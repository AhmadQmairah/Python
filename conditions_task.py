import operator

ops = { "+": operator.add, "-": operator.sub ,"*" :operator.mul,"/": operator.truediv}

while (True):
    operand_1= input("Enter the first number: ").strip()
    if ( not operand_1.isdigit()):
        print("Please enter a valid number")
        continue
    break

while (True):
    operand_2= input("Enter the second number: ").strip()
    if ( not operand_2.isdigit()):
        print("Please enter a valid number")
        continue
    break

while(True):
    operation= input("Choose the operation (+, -, /, *): ").strip()
    if operation not in ops :
        print("Please enter a valid operation")
        continue
    break
   
            
print("The answer is",ops[operation](int(operand_1),int(operand_2)))
