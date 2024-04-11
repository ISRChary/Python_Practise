# Write a program to accept the marks of n students and return them in sorted order

# Taking number of students
students = int(input("\nEnter the number of students: "))

# Initializing the list
marks_list = []

# Creating loop to take input for the given number of students
print("\nEnter the marks of each student: ")
for i in range(students):
    marks = int(input())
    marks_list.append(marks)

# Sorting the marks
sorted_marks = sorted(marks_list)
print("The Sorted order is",sorted_marks)


#-------------------------------------------------
# To count the number of zeros
count = marks_list.count(0)
print("THe number of zeros are",count)
#-------------------------------------------------



#----------------------------------------------------
# Addition of all marks in the list
sum = sum(marks_list)
print("The sum of the marks in the list is:",sum)
#----------------------------------------------------
