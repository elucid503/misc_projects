import csv 

path = "./spotify.csv"

def main():

    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (row["track_name"]).lower() == "con la brisa":
                print(f"Track: {row['track_name']}, Artist: {row['artist(s)_name']}, Plays: {row['streams']}")
            
if __name__ == "__main__":
    main()