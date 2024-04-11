# Date:- 11 April 2024



month_conversion ={
    "jan" : "January",
    "feb" : "February",
    "mar" : "March",
    "apr" : "April",
    "may" : "May",
    "jun" : "June",
    "jul" : "July",
    "aug" : "August",
    "sep" : "September",
    "oct" : "October",
    "nov" : "November",
    "dec" : "December"
}

print(month_conversion["nov"])
print(month_conversion["jan"])
# or
print(month_conversion.get("apr"))
print(month_conversion.get("apr","not a valid key"))
# Use default value if the key is not present
print(month_conversion.get("asdfghj","Not a valid key"))