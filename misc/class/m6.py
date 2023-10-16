from math import floor

integers = []

while (len(integers) < 6):
    try:
        inputted = int(input("Enter an integer smaller than 42: "))
        if (inputted < 42):
            integers.append(inputted)
        else:
            print("Input was not less than 42. Please try again.")
            pass
    except ValueError:
        print("Invalid decimal input. Please try again.")
        pass

integers.sort()

# Find the mean 

avg_mean = floor(sum(integers) // len(integers))
print(f"Mean is {avg_mean}")

# Find the median

median = 0

if (len(integers) % 2 == 0):
    median = floor((integers[len(integers) // 2] + integers[len(integers) // 2 - 1]) / 2)
else:
    median = integers[len(integers) // 2]

print(f"Median is {median}")