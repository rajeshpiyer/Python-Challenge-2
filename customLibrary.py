def intInput() ->int:
    num=None
    while(num==None):
        try:
            num = int(input("Enter a number : "))
        except Exception as e:
            print("Error : ",e)
            continue
    return num

def floatInput()->float:
    num=None
    while(num==None):
        try:
            num = float(input("Enter a number : "))
        except Exception as e:
            print("Error : ",e)
            continue
    return num



