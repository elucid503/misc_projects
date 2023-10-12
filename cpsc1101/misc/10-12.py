# multidim = [3, 67, "cat", [ 56, 57, "dog"], [], 3.14, False]

# print(multidim[2])
# print(multidim[3][2])
# print(multidim[4])

# print("Finding sublist using negative accessor ", multidim[-2:len(multidim)])

# print("String functions are available to string elements ", multidim[2].upper(), multidim[2][0])

# print("student" in ["teacher", "student", "principal"])

# print([1,2] + [3,4])

# print(["go"] * 4)

# print("Slicing a list: ", multidim[1:3])
# print("Slicing a list: ", multidim[:4])
# print("Slicing a list: ", multidim[3:])

from math import floor

integers = []
inputted = False

while (inputted == False and len(integers) < 6):
    try:
        inputted = int(input("Enter an integer smaller than 42: "))
        if (inputted >= 42):
            print("You must enter a valid integer smaller than 42.")
            inputted = False
        else:
            integers.append(inputted)
            inputted = False
    except ValueError:
        print("You must enter a valid integer.")
        inputted = False

sortedints = integers.sort()

sumoflist = 0

for num in integers:
    sumoflist += num

print(f"Avg mean is {floor(sumoflist / len(integers))}")

medianindex = len(integers) / 2

median = 0

if ((medianindex % 2) == 1):
    median = floor((integers[floor(medianindex)] + integers[floor(medianindex) + 1]) / 2)
else:
    median = floor(integers[medianindex])

print(f"Median is {median}")

# From class 

for i in range(6):
    inp = input("Enter a number: ")