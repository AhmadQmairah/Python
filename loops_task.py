Cart={"Items":[],"Price":[],"Quantity":[]}


Item=input("""item (enter "done" when finished): """)

while(Item.lower()!="done"):
    try:
        Price=float(input("price: "))
        Quantity=int(input("Qunatity: "))
    except:
        print("Enter valid Number")
        Item=input("""item (enter "done" when finished): """)
        continue

    Cart["Items"].append(Item)
    Cart["Quantity"].append(Quantity)
    Cart["Price"].append(Price * Quantity)
    Item=input("""item (enter "done" when finished): """)
    

if(len(Cart["Items"])!=0):
    print ("-"*20+"\nreceipt\n"+"-"*20)
    for (i,items) in enumerate(Cart["Items"]):
        print("{}     {}     {}".format(Cart["Quantity"][i],Cart["Items"][i],Cart["Price"][i]))
        
    print ("-"*20)
    print("Total Price :   {}".format(sum(Cart["Price"])))     
else:
    print("The Cart is empty")

    
