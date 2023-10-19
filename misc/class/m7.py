obj = { "introduction": "hello world", 14: "fourteen", 9: "nine", "animal_1": "cat", "animal_2": "dog" }

items = list(obj.items())

i = 0

for item in items:
    print(f"Item {i} => Key: {item[0]}; Value: {item[1]}")
    i+= 1