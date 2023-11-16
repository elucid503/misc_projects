# Exercise 1

ListToBePrinted = [ "Hello", "World" ]

def PrintList(InputtedList: list): 
    for item in InputtedList:
        print(item)

PrintList(ListToBePrinted)

# Exercise 2

Entered = int(input("Enter a number: "))

def IsDivisible(Num: int, Divisors: list): 
    for item in Divisors:
        if Num % item == 0:
            print(f"{Num} is divisible by {item}")
        else:
            print(f"{Num} is not divisible by {item}")


IsDivisible(Entered, [2, 5, 6, 7])