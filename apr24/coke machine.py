'''
shows the user the amount due of the 50 cents which is the price of the coke
every time he inserts a coin
'''
amountDue = 50
amount = 0
while amountDue != 0:
    print("Amount due: ",amountDue)
    usertCoin = int(input("Insert your coin: "))
    if usertCoin in [10,25,5]:
        amount += usertCoin
        amountDue -= usertCoin       
    else:
        print("Amount due: ",amountDue)
print("Change owed: 0")