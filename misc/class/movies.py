def ListMovies(movies):
    if len(movies) > 0:
        print("\nList of Movies:")
        for title, year in movies.items():
            print(f"- {title} ({year})")
    else:
        print("\nNo movies in the list.")

def AddMovie(movies):
    title = input("Enter the movie title: ")
    year = input("Enter the movie year: ")
    movies[title] = year
    print(f"{title} added to the list.")

def DeleteMovie(movies):
    title = input("Enter the movie title to delete: ")
    if title in movies:
        del movies[title]
        print(f"{title} has been deleted.")
    else:
        print("Movie not found.")

def main():
    movies = {}

    while True:
        print("\nMovie List Program")
        print("1. List all movies")
        print("2. Add a movie")
        print("3. Delete a movie")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            ListMovies(movies)
        elif choice == '2':
            AddMovie(movies)
        elif choice == '3':
            DeleteMovie(movies)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
