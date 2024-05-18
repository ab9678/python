def main():
    num = int (input ("Enter a number: "))
    if evenodd(num) == 0:
        print("Even")
    else:
        print("Odd")
def evenodd(number):
    if number%2 == 0:
        return 0
    else:
        return 1
main()