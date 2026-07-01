day = int(input("Enter a day (1-31): "))
while day < 1 or day > 31:
    print("Error. Day must be between 1 and 31.")
    day = int(input("Enter a day (1-31): "))
month = int(input("Enter a month (1-12): "))
while (month == 4 or month == 6 or month == 9 or month == 11) and day >30 :
    print("Error. Day must be within the month.")
    month = int(input("Enter a month (1-12): "))
while month < 1 or month > 12:
    print("Error. Month must be between 1 and 12.")
    month = int(input("Enter a month (1-12): "))
year = int(input("Enter the year you were born: "))
if year < 1000 or year > 9999 :
    print("Error. Year must have four digits.")
else:
    print("Yayy, all the information above is correct!")
if (month == 4 or month == 6 or month == 9 or month == 11) and day >30 :
    print("Error. Day must be within the month.")

if month < 1 or month > 12:
    print("Error. Month must be between 1 and 12.")
