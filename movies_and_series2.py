from datetime import datetime
from random import choice, randint

class Movie:
    def __init__(self, title, year, type, plays=0):
        """A class to represent a movie."""
        self.title = title
        self.year = year
        self.type = type
        self.plays = plays
    
    def play(self):
        """Increases the plays count by one."""
        self.plays += 1

    def display(self, show_views=False):
        """Displays information about the movie."""
        content = f"{self.title} ({self.year})"
        if show_views: content += f", {self.plays}" 
        print(content)

class Serial(Movie):
    """A class to represent a single episode of a serial."""
    def __init__(self, title, year, type, episode, season, plays=0):
        super(Serial, self).__init__(title, year, type, plays)
        self.episode = episode
        self.season = season

    def display(self, show_views=False):
        """Displays information about the episode."""
        content = f"{self.title} ({self.year}) S{self.episode:02d}E{self.season:02d}"
        if show_views: content += f", {self.plays}" 
        print(content)

def get_movies(library):
    """Returns instances of Movie in given list sorted alphabetically."""
    movies = []
    for video in library:
        if type(video) is Movie:
            movies.append(video)

    return sorted(movies, key=lambda m: m.title)

def get_series(library):
    """Returns instances of Serial in given list sorted alphabetically."""
    series = []
    for video in library:
        if type(video) is Serial:
            series.append(video)

    return sorted(series, key=lambda s: s.title)

def search(library, title):
    """Linearly searches for a movie or series by its title."""
    for video in library:
        if video.title.lower() == title.lower():
            return video

def generate_views(library):
    """Randomly selects an item from given list and adds to it a random number of plays."""
    item = choice(library)
    for i in range(randint(1, 100)):
        item.play()

def run_generate_views(library):
    """Runs generate_views 10 times."""
    for i in range(10):
        generate_views(library)

def top_titles(library, number, content_type=(Movie, Serial)):
    """Returns a selected number of the most popular titles from the given list."""
    content_type = content_type if type(content_type) is tuple else (content_type,)
    sorted_library = sort_by_views(library)
    filtered_library = []
    for video in sorted_library:
        if type(video) in content_type:
            filtered_library.append(video)
    return filtered_library[:number]

def sort_by_views(library):
    """Returns a sorted version of the given library, based on the number of views."""
    return sorted(library, key=lambda x: x.plays, reverse=True)

def fill_library():
    """Returns a library filled with content."""
    return [
        Movie("Avengers", 2012, "fiction"),
        Movie("Tenet", 2020, "fiction"),
        Movie("Spider-Man: Homecoming", 2017, "fiction"),
        Movie("Titanic", 1997, "romance"),
        Movie("Beautiful Mind", 2001, "biographical"),
        Serial("The Simpsons", 2019, "comedy", 3, 31),
        Serial("Rick and Morty", 2013, "sitcom", 5, 1),
        Serial("Mr. Robot", 2016, "drama", 10, 2),
        Serial("Stranger Things", 2016, "thriller", 4, 1),
        Serial("Breaking Bad", 2008, "drama", 7, 1)
    ]

def display_library(library, show_views=False):
    """Displays each item in library."""
    for video in library:
        video.display(show_views)

def display_separator(length=20):
    print("-" * length)

def main():
    curr_day = datetime.now().strftime("%d.%m.%Y")
    print(f"Movie Library {curr_day}")
    display_separator()

    library = fill_library()
    display_library(library)

    run_generate_views(library)
    sorted_library = sort_by_views(library)
    display_separator()

    print("Sorted by views:")
    display_library(sorted_library, show_views=True)
    display_separator()

    print(f"Most popular movies and series: ")
    for video in top_titles(library, 3):
        video.display()

if __name__ == "__main__":
    main()
