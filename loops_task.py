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
    

print ("-"*20+"\nreceipt\n"+"-"*20)


for (i,items) in enumerate(Cart["Items"]):
    print("{}     {}     {}".format(Cart["Quantity"][i],Cart["Items"][i],Cart["Price"][i]))
    


    
print ("-"*20)
