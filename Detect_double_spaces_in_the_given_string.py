#Detect double spaces in the given string

str =input("Enter a string: ")
print(str.__contains__("  "))
if(str.__contains__("  ")==True):
    print(str.index("  "))
str=str.replace("  ","   ")
print(str)
