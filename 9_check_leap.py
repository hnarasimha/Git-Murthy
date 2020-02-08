def check_leap(year):
    if year % 4 == 0 and year % 400 == 0:
        return "leap"
    elif year % 4 == 0 and year % 100 != 0:
        return "leap"
    else:
        return "not leap"

def take_input(n):
    # returns a list of size n
    years=[]
    for i in range (n):
        # year.append(int(input("Enter year {} :".format(i))))
        years.append(int(input(f"Enter year {i + 1} : ")))
    return years


n = int(input("Enter the number of years you want to check leap of : "))
for i in take_input(n):
    print(i, check_leap(i))
    