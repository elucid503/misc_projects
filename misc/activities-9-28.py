# # Excercise 1 

# inputted = False

# while (not inputted): 

#     try:

#         inputted = int(input("Enter a number: "))

#     except ValueError:
        
#         print("Cannot enter a float, try again: ")

#         inputted = int(input("Enter a number: "))

# if (inputted % 2): 

#     print("Odd")

# else:

#     print("Even")

# # Excercise 2

# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# inputted = False

# while (not inputted or (inputted > 7 or inputted < 1)):

#     try:
#         inputted = int(input("Enter a number between 1 and 7: "))
#     except ValueError:
#         print("Cannot enter a float, try again: ")
#         inputted = int(input("Enter a number between 1 and 7: "))

# print(days_of_week[inputted - 1])

# Excercise 3

# hours = float(input("Enter the number of hours: "))

# rate = float(input("Enter the hourly pay: "))

# pay = (hours * rate) 

# # The worker now is paid 50% more for overtime

# if (hours > 40): 

#     overtime_pay = (hours - 40) * (rate * 0.5)

#     pay += overtime_pay

# print("The worker is paid $" + str(pay))

n1=20
n2=2
n3=42

# if n1 < n2:
#     if n2 < n3:
#         print (n1, " ", n2, " ", n3)
#     else:
#         if n1 < n3:
#             print (n1, " ", n3, " ", n2)
#         else: 
#             print(n3, " ", n1, " ", n2)
# else:
#     if n3 < n2:
#         print (n3, " ", n2, " ", n1)
#     else:
#         if n3 < n1:
#             print (n2 , " " , n3 , " " , n1)
#         else: 
#             print (n2 , " " , n1 , " " , n3)

# Better fix 

numbers = [n1, n2, n3]
numbers.sort()

print(numbers)

# Using logical operators 

if n1 < n2 and n2 < n3:
    print (n1, " ", n2, " ", n3)
elif n1 < n3 and n3 < n2:
    print (n1, " ", n3, " ", n2)
elif n3 < n2 and n2 < n1:
    print (n3, " ", n2, " ", n1)
elif n3 < n1 and n1 < n2:
    print (n3, " ", n1, " ", n2)
elif n2 < n3 and n3 < n1:
    print (n2, " ", n3, " ", n1)
else:
    print (n2, " ", n1, " ", n3)

# Alternate solution

if n1 <= n2 and n1 <= n3:
    smallest = n1
    if n2 <= n3:
        middle = n2
        largest = n3
    else:
        middle = n3
        largest = n2
elif n2 <= n1 and n2 <= n3:
    smallest = n2
    if n1 <= n3:
        middle = n1
        largest = n3
    else:
        middle = n3
        largest = n1
else:
    smallest = n3
    if n1 <= n2:
        middle = n1
        largest = n2
    else:
        middle = n2
        largest = n1

print(smallest, middle, largest)