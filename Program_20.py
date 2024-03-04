#Create a Python library with the function to input the values with expectation handling and demonstrate with the example.

import customLibrary as lib

def displayNumbers():
    print("Integer Check")
    a = lib.intInput()
    print("Floating Point Check")
    b = lib.floatInput()
    print(f"The numbers are : {a} and {b}.")
displayNumbers()