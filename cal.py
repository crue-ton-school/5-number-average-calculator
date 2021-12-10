import sys

def average(a, b, x, y, z):
    return a + b + x + y + z
def divide(average):
    return average / 5


def print_titles():
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Start
2. Exit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Created by crue-ton on github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
print_titles()

while True:
    choice = input ("Enter choice(1/2): ")

    if choice in ('1'):
        num1 = float(input("Enter your number: "))
        num2 = float(input("Enter your number: "))
        num3 = float(input("Enter your number: "))
        num4 = float(input("Enter your number: "))
        num5 = float(input("Enter your number: "))
        print(divide(average(num1, num2, num3, num4, num5)))
    if choice in ('2'):
        sys.exit('Program Stopped!')


        break