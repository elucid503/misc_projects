# Excercise 1 

inputted = False

while (not inputted): 

    try:

        inputted = int(input("Enter a number: "))

    except ValueError:
        
        print("Cannot enter a float, try again: ")

        inputted = int(input("Enter a number: "))

if (inputted % 2): 

    print("Odd")

else:

    print("Even")

# Excercise 2

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

inputted = False

while (not inputted or (inputted > 7 or inputted < 1)):

    try:
        inputted = int(input("Enter a number between 1 and 7: "))
    except ValueError:
        print("Cannot enter a float, try again: ")
        inputted = int(input("Enter a number between 1 and 7: "))

print(days_of_week[inputted - 1])

# Excercise 3

hours = float(input("Enter the number of hours: "))

rate = float(input("Enter the hourly pay: "))

pay = (hours * rate) 

# The worker now is paid 50% more for overtime

if (hours > 40): 

    overtime_pay = (hours - 40) * (rate * 1.5)

    pay += overtime_pay

print("The worker is paid $" + str(pay))

