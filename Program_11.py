#Write a Python function called calculate_discounted_price that takes the 
#original price of an item and a discount percentage as input. The function 
#should return the discounted price after applying the discount. Ensure that 
#the function handles the case where the discount percentage is negative 
#and raises a custom exception called InvalidDiscountError with an 
#appropriate error message. 

class InvalidDiscountError(Exception):
    def __init__(self, discount):
        self.discount = discount

    def __str__(self) -> str:
        return f"\nInvalid Discount: {self.discount}. Discount must not be negative!."

def calculate_discounted_price():
    price = int(input("-- Calculate Discount --\n\nEnter original Price : "))
    discount_percentage = int(input("Enter discount percentage : "))
    if discount_percentage<0:
        raise InvalidDiscountError(discount_percentage)
    else:
        discount = price * (discount_percentage/100)
    print("Particulars\t\tAmount")
    print(f"------------------------------")
    print(f"Item Price\t\t{price}")
    print(f"Discount\t\t{discount}")
    print(f"------------------------------")
    print(f"Total   \t\t{price-discount}")

ch='y'
while(ch=='y' or ch=='Y'):
    try:
        calculate_discounted_price()
    except Exception as e:
        print(e)
        continue
    ch=input("Do you want to calculate another discount?(Y/N) : ")