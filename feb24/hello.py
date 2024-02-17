import math
n1 = 22
n2 = 33
print(n1+n1 , n1*n2 , n1/n2)
diff = n1-n2
if diff<0:
    diff = n2-n1
print(diff)

i=0

while diff!=0:
    diff=n2-(n1+i)
    i=i+1
    print(diff)





