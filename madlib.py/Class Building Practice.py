# Started class with keyboard class and then named it using Pascal Case
class Movie:
    def __init__(self, title, release_year, director, rating, genre, cast):
        self.title = title
        self.release_year = release_year
        self.director = director
        self.rating = rating
        self.genre = genre
        self.cast = cast

    def __str__(self):
        return f"Title: {self.title}\nRelease_Year: {self.release_year}\n Director: {self.director}\nRating: {self.rating}\nGenre: {self.genre}\nCast: {self.cast}"


Mov1 = Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R" , "Drama" , ["Tim Robbins", "Morgan Freeman"])

Mov2 = Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", [John Travolta, Uma Thurman, Samuel L. Jackson])

Mov3 = Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", [Marlon Brando, Al Pacino, James Caan])

Mov4 = Movie("Inception", 2010, "Christopher Nolan", "PG-13", "Sci-Fi", [Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page])

Mov5 = Movie("The Matrix, (1999), Lana Wachowski, Lilly Wachowski, R, Sci-Fi, [Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss])

Forrest Gump, (1994), Robert Zemeckis, PG-13, Drama, [Tom Hanks, Robin Wright, Gary Sinise]

The Dark Knight, (2008), Christopher Nolan, PG-13, Action, [Christian Bale, Heath Ledger, Aaron Eckhart]

Schindler's List, (1993), Steven Spielberg, R, Drama, [Liam Neeson, Ben Kingsley, Ralph Fiennes]

Fight Club, (1999), David Fincher, R, Drama, [Brad Pitt, Edward Norton, Helena Bonham Carter]

Goodfellas, (1990), Martin Scorsese, R, Crime, [Robert De Niro, Ray Liotta, Joe Pesci]

The Silence of the Lambs, (1991), Jonathan Demme, R, Thriller, [Jodie Foster, Anthony Hopkins, Scott Glenn]

Forrest Gump, (1994), Robert Zemeckis, PG-13, Drama, [Tom Hanks, Robin Wright, Gary Sinise]

Titanic, (1997), James Cameron, PG-13, Romance, [Leonardo DiCaprio, Kate Winslet, Billy Zane]

The Lord of the Rings: The Fellowship of the Ring, (2001), Peter Jackson, PG-13, Fantasy, [Elijah Wood, Ian McKellen, Orlando Bloom]

Gladiator, (2000), Ridley Scott, R, Action, [Russell Crowe, Joaquin Phoenix, Connie Nielsen]

The Green Mile, (1999), Frank Darabont, R, Drama, [Tom Hanks, Michael Clarke Duncan, David Morse]

Saving Private Ryan, (1998), Steven Spielberg, R, War, [Tom Hanks, Matt Damon, Tom Sizemore]

Jurassic Park, (1993), Steven Spielberg, PG-13, Adventure, [Sam Neill, Laura Dern, Jeff Goldblum]

The Departed, (2006), Martin Scorsese, R, Crime, [Leonardo DiCaprio, Matt Damon, Jack Nicholson]

The Lion King, (1994), Roger Allers, Rob Minkoff, G, Animation, [Matthew Broderick, Jeremy Irons, James Earl Jones]