def whatis_it(string):
    if string.startswith('n') is True:
        return True
    else:
        return False


def main():
    string = input("Enter what is your processor: ").lower()
    if whatis_it(string) is True:
        print("It should be a chromebook")
    else:
        print("It might be something else(WINDOWS! o_o)")

main()


