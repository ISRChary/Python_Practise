# Date : 11 April 2024
#  substitute any vowels with the s in the given string

def translate(phrase):
    translated_text = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translated_text = translated_text + "s"
        else:
            translated_text = translated_text + letter
    return translated_text

print(translate(input("Enter any String: ")))