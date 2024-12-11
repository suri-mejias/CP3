class Movie:
    def __init__(self, title, year, director, rating, genre, cast):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return (f"Title: {self.title}\nYear: {self.year}\nDirector: {self.director}\n"
                f"Rating: {self.rating}\nGenre: {self.genre}\nCast: {', '.join(self.cast)}")

class MovieManager:
    def __init__(self, movies):
        self.movies = movies

    def sort_movies_alpha(self):
        def get_title(movie):
            return movie.title
        return sorted(self.movies, key=get_title)

    def sort_movies_chrono(self):
        def get_year(movie):
            return movie.year
        return sorted(self.movies, key=get_year)

    def search_by_genre(self, genre):
        return [movie for movie in self.movies if movie.genre.lower() == genre.lower()]

    def search_by_director(self, director):
        return [movie for movie in self.movies if movie.director.lower() == director.lower()]

    def search_by_cast(self, actor):
        return [movie for movie in self.movies if actor.lower() in [member.lower() for member in movie.cast]]


movies = [
    Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),
    Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),
    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),
    Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]),
    Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]),
    Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Movie("Schindler's List", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]),
    Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]),
    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta", "Joe Pesci"]),
    Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]),
    Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]),
    Movie("The Lord of the Rings: The Fellowship of the Ring", 2001, "Peter Jackson", "PG-13", "Fantasy", ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]),
    Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]),
    Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]),
    Movie("Saving Private Ryan", 1998, "Steven Spielberg", "R", "War", ["Tom Hanks", "Matt Damon", "Tom Sizemore"]),
    Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"]),
    Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]),
    Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]),
    Movie("Eternal Sunshine of the Spotless Mind", 2004, "Michel Gondry", "R", "Romance", ["Jim Carrey", "Kate Winslet", "Kirsten Dunst"]),
]

manager = MovieManager(movies)

print("Movies sorted alphabetically:")
for movie in manager.sort_movies_alpha():
    print(movie, "\n")

print("Movies sorted chronologically:")
for movie in manager.sort_movies_chrono():
    print(movie, "\n")

print("Search by genre (Crime):")
for movie in manager.search_by_genre("Crime"):
    print(movie, "\n")

print("Search by director (Francis Ford Coppola):")
for movie in manager.search_by_director("Francis Ford Coppola"):
    print(movie, "\n")

print("Search by cast (Morgan Freeman):")
for movie in manager.search_by_cast("Morgan Freeman"):
    print(movie, "\n")