def main():
    while True:
        
        try:
            a,b= input("Fraction: ").split('/')
            x = int(a)
            y = int (b)

            value = (x/y)*100
            if value<=1:
                print("E")
                break
            elif value>=99:
                print("F")
                break
            else:
                print(value)
                break
        except (ValueError , ZeroDivisionError):
           pass
main()