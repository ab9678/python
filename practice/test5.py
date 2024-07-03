def main():
    i = input ("Enter your name: ").lower().strip()
    if "abhigyan" in i:
        print("Welcome back", i)
    else:
        print("Looks like a new user, who are you? ")
        new = input()
        print("Hello,", new)

main()