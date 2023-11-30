import csv

# file = open('./test.txt', 'w')

# file.write('Hello, world!')

# file.close()

with open('./test.txt', 'a') as file:
    file.write('\nHello, again!')

movies = [["Where the Crawdads Sing", 2022],["The Matrix", 1999],["The Shawshank Redemption", 1994], ["Die Hard", 1988]]

with open('./movies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(movies)