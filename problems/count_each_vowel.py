# Date:- 14 Apr 2024
# program to count the number of each vowel in a string with explanation

# Defining a method to implement the logic
def count_vowels(string):
    # creating a dictionary to keep count of vowels
    vowels_count = {"a":0 , "e":0, "i":0, "o":0, "u":0}
    
    # converting the string into lower case. This is in case insensitive
    string = string.lower()

    # Loop to traverse through the string
    for char in string:
        if char in vowels_count:
            vowels_count[char] += 1

    # return the disctionary with updated count values
    return vowels_count

str1 = input("Enter a String to count the number of each vowel: ")
# print(count_vowels(str1))              printing dictionary directly

# printing method 2
result = count_vowels(str1)
print("The count of each vowel int he given string is:\n")

for vowel, count in result.items():
    print(vowel + " : " + str(count))