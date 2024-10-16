print("Price of pizza are Mention Below:")
print("Small pizza: 100,Medium pizza:200,large Pizza:300 ")
takeorder=input("enter pizza size : ")
small=100
medium=200
large=300
if(takeorder==small):
   smallprice=100
elif(takeorder==medium):
    mediumprice=200
else:
   largeprice=300
print("Pepronnifor Small pizza: 20,PepronniforMedium pizza:50,Pepronniforlarge Pizza:70 ")
pepproni=input("you want pepproni yes or no: ")  
print("Cheese price 20")
cheese=input("you want cheese or no :")
if(pepproni=='yes' and takeorder=="small"):
    smallprice=130
    if(cheese=="yes"):
        smallprice=150
    print("Your Total Bill is ",smallprice)
elif(pepproni=='yes' and takeorder=="medium"):
    mediumprice=250
    if(cheese=="yes"):
        mediumprice=270
    print("Your Total Bill is ",mediumprice)
elif(pepproni=='yes' and takeorder=="large"):
    largeprice=370
    if(cheese=="yes"):
        largeprice=390
    print("your Total Bill is ",largeprice)
elif(pepproni=='no' and takeorder=="small"):
    smallprice=100
    if(cheese=="yes"):
        smallprice=120
    print("Your total Bill is  ",smallprice)
elif(pepproni=='no' and takeorder=="medium"):
    mediumprice=200
    if(cheese=="yes"):
        mediumprice=220
    print("Your Total Bill is ",mediumprice)
elif(pepproni=='no' and takeorder=="large"):
    largeprice=300
    if(cheese=="yes"):
        largeprice=320
    print("Your Total Bill is ",largeprice)
else:
    print("code not working")
        
    
    
        
        
    
    
          