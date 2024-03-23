def list1():
	listOriginal = []
	length = int(input('Enter Range: '))
	i=0
	for i in range(length):
		listOriginal.append(int(input("Enter Number: ")))
	return listOriginal
print(list1())