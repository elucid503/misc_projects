from random import randint

# Exercise 1

name_list = ["Andrea", "Patrick", "Aaron", "David", "Lynn", "Oliver", "Grace", "Roman"]
for name in name_list:
    print("Hello, " + name + "!")

# Exercise 2

set_str = "You must cut down the mightiest tree in the forest with…a herring!"

count = 0
while (count < len(set_str)):
    count += 1

print(count)

# Exercise 3

num_list = [20, -3, -2, 42, 1, -66, 8, 30, -4, 76, 33, -16]
new_list = []

for num in num_list:

    if (num > 0):
        new_list.append(num)

print(new_list)

# Exercise 4

d = {"car": "ford", "age": 21, 42: "everything", "result": True, "animals": ["dog", "cat", "rat"], "negative": -10}

for item in list(d.items()):
    print(f"Key: {item[0]}; Value: {item[1]} Value Type: {type(item[1])}")

# Exercise 5

d_1 = {"3_positive": "NA", "4_positive": "NA", "2_negative": "NA", "1_positive": "NA", "5_negative": "NA", "6_negative": "NA"}

for key in d_1:

    if ("positive" in key): 
        d_1[key] = randint(1, 100)

    else:
        d_1[key] = randint(-100, -1)

print(d_1)
