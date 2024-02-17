# write a program to calculate area of a shape 
def area():
    print("Select shape \n(1)square\n(2)Triangle\n(3)Rectangle\n(4)circle\n(5)Cube")
    shape = int(input())

    if(shape == 1):
        l=int(input("length: "))
        area=l**2
        print(area,"sq. units")
    elif(shape == 2):
        b=int(input("Base: "))
        h=int (input("Height: "))
        area = (b*h)/2
        print(area,"sq. units")
    elif(shape == 3 ):
        l=int(input("length: "))
        b=int(input("Breadth: "))
        area = l*b
        print(area,"sq. units")
    elif(shape == 4):
        r=int(input("Radius: "))
        area = 3.14*r*r
        print(area,"sq. units")
    elif(shape == 5):
        l=int(input("length: "))
        area = 6*(l**2)
        print(area,"sq. units")
    else:
        print("Invalid Input")

##
        

area()


