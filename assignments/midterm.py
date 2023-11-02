# Exercise 1 

print("------- Excersise 1 -------")

stag_id = 292859 # without the 0's 

print(f"My Fairfield ID (Without 0's): {stag_id}")

if (stag_id % 13 == 0):
    print(f"{stag_id} is divisible by 13")
else:
    print(f"{stag_id} is not divisible by 13")

print("------- Excersise 2 -------")

# Excersise 2 

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

first_last = first_name + " " + last_name 

print(first_last) # first and last name
print(first_last[:3]) # first three chars 
print(first_last[len(first_last) - 3:]) # last three chars 
print(len(first_last)) # total number of characters 

print("------- Excersise 3 --------")

# Excersise 3 

products = ["apple", 0.5, "orange", 0.9, "milk", 1.25, "chocolate bar", 3.25]
amounts = { "chocolate bar": 1, "milk": 1, "orange": 3, "apple": 2 }

total_amt = 0

for product in products: 

    if (product in amounts):

        amount = amounts[product]
        price = products[products.index(product) + 1]

        total_amt += amount * price 

print(f"Total Price: {total_amt}$") 

# An object/dictionary would be better to implement this method as creating two lists and assuming
# that the other index will always be a price / a type we can work with represents bad type safety
# Also, this could lead to buffer overflow in lower level langs like C. Finally, an object would
# greatly simplify this process. Usage of an object within the amounts variable helps avoid an 
# otherwise lengthy (and in production, unfortunate) declaration of 4 other extraneous variables.

print("------- Excersise 4 --------")

# Excersise 4

import requests 

url = "https://newsapi.org/v2/everything?q=cybersecurity&searchin=title&from=2023-11-1&to=2023-11-1&sortBy=publishedAt&apiKey=0694092bb933442e861b65b330f6a1a9"

http_resp = requests.get(url)

try: 

    json_resp = http_resp.json()

except: 

    print("Request Failed")

articles = json_resp["articles"]

for article in articles:
    print(f"Title: {article['title']}\nAuthor: {article['author']}\nDescription: {article['description']}")