def main():
    time = input("What time is it? ")
    time=convert(time)
    # meal time decision
    if 7.0<=time<=8.0:
        print("It breakfast time")
    elif 12.0<=time<=13.0:
        print("Lunch time")
    elif 18.0<=time<=19.0:
        print("Dinner time")
    else:
        print()
    

def convert(time):
    h,m = time.split(':')
    # m=int(m)/6
    # m=str(m)
    h,m=int(h),float(m)
    time = h+m/60
    return time


if __name__ == "main":
    main()

main()
