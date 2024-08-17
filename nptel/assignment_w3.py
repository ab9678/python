def contracting(l):
    i=0
    while i+2 <= (len(l)-1):
        
        if abs(l[i] - l[i+1]) <= abs(l[i+1] - l[i+2]):
            return False
        
        i+=1
    return True
# print(contracting([9,3,5]))


# hill and valley
def counthv(l):
    i = 1
    hc = 0
    vc = 0
    while i+1 <= (len(l)-1):
        if l[i-1]<l[i]>l[i+1]:
            hc = hc+1
        elif l[i-1]>l[i]<l[i+1]:
            vc+=1
        
        i+=1
    list1= [hc,vc]

    return list1
# print(counthv([1,2,3,1]))


