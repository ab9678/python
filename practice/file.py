fh = open("abc.py","r")
res=fh.read()
fh = open ("abc.py","a")
s = "\ntalent"
fh.write(s)
fh.close()