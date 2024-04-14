# Date:- 14 April 2024
# Program to sort the words alphabetically from the string given by the user


def sort_words_alphabetically(string):

    words = string.split()

    sorted_words = sorted(words)

    sorted_string = ' '.join(sorted_words)

    return sorted_string

str1 = input("Enter a string to arrange in alphabetical order: ")
print("The sorted order of the given string is: ")

print(sort_words_alphabetically(str1))