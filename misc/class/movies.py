# Find all comedy movies

import csv 

path = "./movies.csv"

def main():

    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "Comedy" in row["Genre"]:
                print(row["Title"])

if __name__ == "__main__":
    main()