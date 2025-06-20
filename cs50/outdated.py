months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

user = input("DATE: ")
month=day=year=""
month,day,year=user.split("/")

try:
    test=int(month)
except ValueError:

    if month in months:
        for i in range(len(months)):
            if months[i]==month:
                month = i 
                print("hello")

print(f"{int(year)}/{(month):02}/{int(day):02}")

