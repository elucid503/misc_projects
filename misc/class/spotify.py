import csv 

path = "./spotify.csv"

def main():

    with open(path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["track_name"] == "":
                print(f"Track: {row['track_name']}, Artist: {row['artist_name']}, Plays: {row['streams']}")
            

if __name__ == "__main__":
    main()