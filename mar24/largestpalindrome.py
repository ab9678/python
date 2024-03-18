

def reverse_number(number):
    # Convert the number to a string
    number_str = str(number)
    # Reverse the string
    reversed_str = number_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)
    
    return reversed_number


for i in range (0,100):
    number= i

    reversed_number = reverse_number(number)
    # print("Original number:", number)
    # print("Reversed number:", reversed_number)
    if(reversed_number == i):
        largestPalindrome=reversed_number


print(largestPalindrome)

