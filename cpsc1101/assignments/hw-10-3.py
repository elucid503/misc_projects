# Exercise 1
num1 = input("Enter the first decimal number: ")
num2 = input("Enter the second decimal number: ")

# Remove the decimal point for comparison
num1_digits = len(num1.replace(".", ""))
num2_digits = len(num2.replace(".", ""))

if num1_digits > num2_digits:
    print(f"The number with the most digits is: {num1}")
elif num1_digits < num2_digits:
    print(f"The number with the most digits is: {num2}")
else:
    print("Both numbers have the same number of digits.")

# Exercise 2

# Exercise 2
n1, n2, n3 = 5, 4, 7

if n1 < n2 and n2 < n3:
    print(n1, n2, n3)
elif n1 < n3 and n3 < n2:
    print(n1, n3, n2)
elif n3 < n1 and n1 < n2:
    print(n3, n1, n2)
elif n3 < n2 and n2 < n1:
    print(n3, n2, n1)
elif n2 < n3 and n3 < n1:
    print(n2, n3, n1)
else:
    print(n2, n1, n3)

# Exercise 3

num = input("Enter a decimal number: ")

# Remove the decimal and join the digits with a hash

result = "#".join(num.replace(".", ""))
print(result)

# Exercise 4

correct_password = "youshallnotpass"
attempts = 0

while attempts < 3:
    entered_password = input("Enter the password: ")
    
    if entered_password == correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")
        attempts += 1

if attempts == 3:
    print("Access denied. You've used all attempts.")

