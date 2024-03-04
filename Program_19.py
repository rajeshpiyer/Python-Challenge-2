#Write program for building restaurant menu using class in Python.

class Menu:
    starters=[]
    snacks=[]
    breads=[]
    south_indian=[]
    north_indian=[]
    chinese=[]
    juices=[]
    shakes=[]
    def __init__(self,title,price,cuisine,category) -> []:
        self.title=title
        self.price=price
        self.cuisine=cuisine
        if category==1:
            self.starters.append(self)
        elif category==2:
            self.snacks.append(self)
        elif category==3:
            self.breads.append(self)
        elif category==4:
            self.south_indian.append(self)
        elif category==5:
            self.north_indian.append(self)
        elif category==6:
            self.chinese.append(self)
        elif category==7:
            self.juices.append(self)
        elif category==8:
            self.shakes.append(self)

    def __str__(self) -> str:
        if self.cuisine==1:
            return f"{self.title} "+"\033[92m\u25CF\033[0m"+f"\t{self.price}"
        else:
            return f"{self.title} "+"\033[91m\u25CF\033[0m"+f"\t{self.price}"

def addItem():
    print("Add Item to Menu ")
    category = int(input("1.Starters\t\t2.Snacks\n3.Breads\t\t4.South Indian\n5.North Indian\t\t6.Chinese\n7.Juices\t\t8.Shakes\nChoose the category : "))
    cuisine = int(input("1.Vegetarian\t\t2.Non Vegetarian\nChoose the Cuisine : "))
    title = input("Item Title : ")
    price = input("Price : ")
    item = Menu(title,price,cuisine,category)
    print("Item Added Successfully!!")

def PrintMenu():
    print("-------------------------")
    print("---- Restaurant Menu ----")
    print("-------------------------")
    if not Menu.starters==[]:
        print("-- Starters --")
        for i in Menu.starters:
            print(i)
    if Menu.breads != []:
        print("-- Breads --")
        for i in Menu.breads:
            print(i)
    if Menu.snacks != []:
        print("-- Snacks --")
        for i in Menu.snacks:
            print(i)
    if Menu.south_indian != []:
        print("-- South Indian --")
        for i in Menu.south_indian:
            print(i)
    if Menu.north_indian != []:
        print("-- North Indian --")
        for i in Menu.north_indian:
            print(i)
    if Menu.chinese != []:
        print("-- Chinese --")
        for i in Menu.chinese:
            print(i)
    if Menu.juices != []:
        print("-- Juices --")
        for i in Menu.juices:
            print(i)
    if Menu.shakes != []:
        print("-- Shakes --")
        for i in Menu.shakes:
            print(i)

ch='y'
while(ch=='y' or ch=='Y'):
    print("\n1.Add Item\n2.View Menu")
    choice = int(input("Choice : "))
    if choice==1:
        addItem()
    elif choice==2:
        PrintMenu()
    ch = input("Do you wish to go again?(Y/N) : ")
        
        