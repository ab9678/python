#  create largest palindrome of a string
NTR = int(input())
word = input()
ans = str()
for i in range(len(word)):
    for j in range(len(word)-1,i-1,-1):
         if word[i] == word[j]:
              m = word[i:j+1]
              if m == m[::-1]:
                  if len(ans) <= len(m):
                        ans = m 
print(len(ans))
print(ans)

    