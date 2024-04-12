# Date:- 12 April 2024

# Reading files using python

# r- read , w-write, r+ -read and write 

employee_file = open ("employee_list.txt", "r")
print(employee_file.read())   #reads whole file
print(employee_file.readline())   #reads first line in the file
print(employee_file.readline())   #reads second line in the file
print(employee_file.readline())   #reads third line in the file

print("----------------------------------")
print(employee_file.readlines())   #reads all linews one after the other and save them in a list
#print(employee_file.readlines()[1]) #reads the second line

# using for loop and readlines 

print("----------------------------------")
for employee in employee_file.readlines():
    print(employee)





# close the file after reading
employee_file.close()