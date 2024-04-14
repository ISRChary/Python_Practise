# Date: 11 April 2024

# Try and Except in python




try:
    # answer = 10/0
    number = int (input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print (err)
except ValueError:
    print("Enter a valid number!")
