# Date:- 12 April 2024

# appending 
employee_file = open("employee_list.txt","a")
print(employee_file.write("\nToby - Human resources"))
employee_file.close()


# writing

# employee_file = open("employee_list.txt","w")         if we use thi all the existing data in the file will be created and new data we enter will be added
employee_file = open("employee_list1.txt","a")    #creating a new file
print(employee_file.write("This is the new file created with the 'write' "))