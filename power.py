# Date 11 April 2024

# Power of the given number

def raise_to_power(base_num,pow_num):
    result = 1
    for i in range (pow_num):
        result = result * base_num
    return result

base_num = int(input("Enter the Base number:"))
pow_num = int(input("Enter the power number: "))

print(raise_to_power(base_num,pow_num))
