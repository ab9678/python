# def h(n):
#     s = 0
#     for i in range(2,n):
#         if n%i == 0:
#            s = s+i
#     return(s)


# diff = h(60)-h(45)

# print(diff)


# def g(m,n):
#     res = 0
#     while m >= n:
#         (res,m) = (res+1,m/n)
#     return(res)

# dipti=g(375,4)

# print(dipti)

def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)

print(f(27182818))

