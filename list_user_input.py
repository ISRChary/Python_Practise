# List program to take input from the user

# initializing the empty list
fruits_list = []

while True:
    fruits = input("\nEnter the fruit name or \nEnter stop to finish: ")

    if(fruits.lower()=="stop"):
        break
    fruits_list.append(fruits)

# Printing the list of fruits
print("\nThe fruits in the list are:")
for i in fruits_list:
    print(i)