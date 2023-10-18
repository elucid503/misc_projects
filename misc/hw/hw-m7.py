# Exercise 1 

elements = []
while True:
    element = input("Enter an element (type 'done' to stop): ")
    if element == 'done':
        break
    elements.append(element)

print("Your list:", elements)

# Exercise 2

numbers = [4, 7, 15, 9, 2, 11]
smallest = largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"Smallest number: {smallest}")
print(f"Largest number: {largest}")

# Exercise 3

quote = "Bones of full fifty men lie strewn about its lair. So, brave knights, if you do doubt your courage or your strength, come no further, for death awaits you all with nasty, big, pointy teeth."
cleaned_quote = quote.replace(',', '').replace('.', '')
tokens = cleaned_quote.split()

print("Tokens:", tokens)

# Exercise 4

shopping_list = {}

while True:
    product = input("Enter a product (type 'done' to stop): ")
    if product == 'done':
        break
    count = int(input(f"How many {product} would you like? "))
    shopping_list[product] = count

print("Your shopping list:", shopping_list)
