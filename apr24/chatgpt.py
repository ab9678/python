def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # Check if the plate starts with at least two letters
    if len(plate) < 2 or not plate[0:2].isalpha():
        return False
    
    # Check if the length of the plate is between 2 and 6 characters
    if not (2 <= len(plate) <= 6):
        return False

    # Check for invalid characters
    if not plate.isalnum():
        return False

    # Check if numbers are in the middle or if the first number is '0'
    if check_num_middle(plate):
        return False

    return True

def check_num_middle(plate):
    number_started = False
    for i, char in enumerate(plate):
        if char.isdigit():
            if not number_started:
                if char == '0':  # The first number cannot be '0'
                    return True
                number_started = True
        elif number_started:
            # If a letter appears after numbers have started, it's invalid
            return True
    return False

main()
