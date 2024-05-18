# Write a program to calculate the th nerm of a fibonacci sequence if available
# next = first + second

flag = 0
def fibonacci(nth,reslist):
    global flag
    first = 0
    second = 1
    next = 0

    while True:
        next = first + second
        first = second
        second = next
        reslist.append(next)

        if next > nth:
            flag = 1
            break
        elif next == nth:
            break

    return reslist


def main():
    global flag 
    term = int(input("Enter the Fibonacci Term : "))
    res = [0,1]
    res = fibonacci(term , res)
    print(res)
    if flag == 0:
        print("THE SPECIFIED ELEMENT IS IN THE FIBONACCI SEQUENCE")
    elif flag == 1:
        print("THE SPECIFIED ELEMENT IS NOT IN THE FIBONACCI SEQUENCE")
main()
