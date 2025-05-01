names = []
prices = []

#========================================================
def add () :
     name = input ("please enter the name of the book you want to add :")
     price = int(input("please enter the price of the book you want to add :"))
     names.append(name)
     prices.append(price)
#========================================================
def delete () :
    name = input("Enetr the name of the book you want to delete :")
    a= False
    for i in names :
        if i == name:
            names.remove(i)
            print (f"{name} deleted successfully.")
            a = True
            break
    if a == False :
        print(f"{name} is not here to delete.")
#=============================================================
def search () :
    name = input("please enter the name of the book you search for :")
    a = False 
    for i in names :
        if i == name :
            inde = i.index()
            print("here is the book you search for.") 
            print (f" name : {name}")
            print (f"price : {prices[inde]}")
            a = True
            break
    if a == False :
        print (f"{name} is not here to search for.")
#==========================
def display () :
    for i in names :
        inde = i.index()
        print (f"name : {i}")
        print(f"price : {prices[inde]}")
        print ("=========================")










print ("welcome at Dr/ahmed hany 's library.")
print ("1_Add a book.")
print ("2_Delete a book.")
print ("3_Search for a book.")
print ("4_Display all the books")
print ("5_Exit.")
choice = int (input("please enter your choice :"))
