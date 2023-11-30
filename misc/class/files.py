# file = open('./test.txt', 'w')

# file.write('Hello, world!')

# file.close()

with open('./test.txt', 'a') as file:
    file.write('\nHello, again!')