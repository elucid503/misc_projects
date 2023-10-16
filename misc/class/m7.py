obj = { "hello": "hello world" }

obj[14] = "rat"
obj[9] = "cat"

# print(obj["hello"])

# print(obj[14])
# print(obj[9])

obj["animal_14"] = "rat"
obj["animal_9"] = "cat"

# print(obj["animal_14"])
# print(obj["animal_9"])

# print("animal_9" in obj)
# print("animal_10" in obj)

keys = obj.keys()

# for key in keys:
#     print(key)

values = list(obj.values())

print(values[0]) 