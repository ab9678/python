#fix price is 50
fix_price=50
print("Amount due:",fix_price)

while fix_price >=0:
    print(fix_price)
    amount=int(input("Insert coin:"))
    
    fix_price = fix_price - amount

    