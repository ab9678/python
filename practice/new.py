def sayhello(theysay):
    if theysay == "hello":
        print("Hello sir")
    elif theysay == "hi":
        print("Hi sir")
    else:
        print("Greetings monsieur!")


def main():
    theysay = input("").lower()
    sayhello(theysay) 
 
main()