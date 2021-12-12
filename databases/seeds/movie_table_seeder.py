"""MovieTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Movie import Movie

class MovieTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Movie.create({"title": "The Godfather", "description": "The Godfather is an American film series that consists of three crime films directed by Francis Ford Coppola inspired by the 1969 novel of the same name by Italian American author Mario Puzo.", "year": "1972", "poster": "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg"})
        Movie.create({"title": "Parasite", "description": "All unemployed, Ki-taek’s family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident.", "year": "2019", "poster": "https://m.media-amazon.com/images/I/91sustfojBL._AC_SL1500_.jpg"})
        Movie.create({"title": "Once Upon a Time… in Hollywood", "description": "Los Angeles, 1969. TV star Rick Dalton, a struggling actor specializing in westerns, and stuntman Cliff Booth, his best friend, try to survive in a constantly changing movie industry. Dalton is the neighbor of the young and promising actress and", "year": "2019", "poster": "https://m.media-amazon.com/images/M/MV5BOTg4ZTNkZmUtMzNlZi00YmFjLTk1MmUtNWQwNTM0YjcyNTNkXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_FMjpg_UX1000_.jpg"})
        Movie.create({"title": "Climax", "description": "Young dancers gather in a remote and empty school building to rehearse on a cold and wintry night. The all-night celebration soon turns into a hallucinatory nightmare when they learn that their sangria is laced with LSD.", "year": "2018", "poster": "https://m.media-amazon.com/images/I/61z4mC8Zf5L._AC_SL1360_.jpg"})
        Movie.create({"title": "Another Round", "description": "Four high school teachers launch a drinking experiment: upholding a constant low level of intoxication.", "year": "2020", "poster": "https://m.media-amazon.com/images/M/MV5BOTNjM2Y2ZjgtMDc5NS00MDQ1LTgyNGYtYzYwMTAyNWQwYTMyXkEyXkFqcGdeQXVyMjE4NzUxNDA@._V1_.jpg"})
        Movie.create({"title": "Minari", "description": "It’s the 1980s, and David, a seven-year-old Korean American boy, is faced with new surroundings and a different way of life when his father, Jacob, moves their family from the West Coast to rural Arkansas. His mother, Monica, is aghast that they live", "year": "2020", "poster": "https://lh3.googleusercontent.com/proxy/yCYkg-AZ850p1VrTldkyLJ546PqBy3cGEV8iQJx_HdlwJq40C9F8a7gDbfuK5FBl1StXPPDjuzKBMALgxHeTj_lz6LyAl_oHNGcB3JoYmDpE"})
        Movie.create({"title": "Midsommar", "description": "Several friends travel to Sweden to study as anthropologists a summer festival that is held every ninety years in the remote hometown of one of them. What begins as a dream vacation in a place where the sun never sets, gradually turns into a dark ...", "year": "2019", "poster": "https://m.media-amazon.com/images/M/MV5BMzQxNzQzOTQwM15BMl5BanBnXkFtZTgwMDQ2NTcwODM@._V1_.jpg"})
        Movie.create({"title": "Soul", "description": "Joe Gardner is a middle school teacher with a love for jazz music. After a successful audition at the Half Note Club, he suddenly gets into an accident that separates his soul from his body and is transported to the You Seminar, a center in which ", "year": "2020", "poster": "https://1.bp.blogspot.com/-pG9x85OBW1o/XmkmpG-_-II/AAAAAAAAX-Q/9W0JXTUhOuQW-NmzEo4bvn_7S92TV18fACLcBGAsYHQ/s1600/Pixar-Soul-Poster.jpg"})
        Movie.create({"title": "Lost in Translation", "description": "Two lost souls visiting Tokyo – the young, neglected wife of a photographer and a washed-up movie star shooting a TV commercial – find an odd solace and pensive freedom to be real in each other’s company, away from their lives in America.", "year": "2003", "poster": "https://hdgoperahouse.org/wp-content/uploads/2018/12/Lost-in-Trans.jpg"})
        Movie.create({"title": "Vice", "description": "George W. Bush picks Dick Cheney, the CEO of Halliburton Co., to be his Republican running mate in the 2000 presidential election. No stranger to politics, Cheney’s impressive résumé includes stints as White House chief of staff, House Minority Whip and defense secretary. When Bush wins by a narrow margin, Cheney begins to use his newfound power to help reshape the country and the world.", "year": "2018", "poster": "https://m.media-amazon.com/images/M/MV5BMTY1NjM0MzgxMV5BMl5BanBnXkFtZTgwNDc4NTY0NjM@._V1_.jpg"})
        Movie.create({"title": "American Psycho", "description": "A wealthy New York investment banking executive hides his alternate psychopathic ego from his co-workers and friends as he escalates deeper into his illogical, gratuitous fantasies.", "year": "2000", "poster": "https://cdn.shopify.com/s/files/1/0057/3728/3618/products/f85ee5ef68c6266f73cf11f6c599cffd_9c1132bb-9c5f-41c8-bd6f-f35db9a6a1a6_480x.progressive.jpg?v=1573653978"})
        Movie.create({"title": "The Big Short", "description": "The men who made millions from a global economic meltdown.", "year": "2015", "poster": "https://m.media-amazon.com/images/I/91dC4o8mScL._AC_SY679_.jpg"})
        Movie.create({"title": "Scarface", "description": "After getting a green card in exchange for assassinating a Cuban government official, Tony Montana stakes a claim on the drug trade in Miami. Viciously murdering anyone who stands in his way, Tony eventually becomes the biggest drug lord in the state", "year": "1983", "poster": "https://m.media-amazon.com/images/I/61luAu5kqTL._AC_SY550_.jpg"})
        Movie.create({"title": "Good Will Hunting", "description": "Will Hunting has a genius-level IQ but chooses to work as a janitor at MIT. When he solves a difficult graduate-level math problem, his talents are discovered by Professor Gerald Lambeau, who decides to help the misguided youth reach his potential. ", "year": "1997", "poster": "https://m.media-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg"})
        Movie.create({"title": "Ratatoulie", "description": "A rat named Remy dreams of becoming a great French chef despite his family’s wishes and the obvious problem of being a rat in a decidedly rodent-phobic profession. When fate places Remy in the sewers of Paris, he finds himself ideally situated", "year": "2007", "poster": "https://lumiere-a.akamaihd.net/v1/images/p_ratatouille_19736_0814231f.jpeg"})
        Movie.create({"title": "Django", "description": "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.", "year": "2012", "poster": "https://cdn.shopify.com/s/files/1/1057/4964/products/django-unchained-vintage-movie-poster-original-1-sheet-27x41_b32fb297-3108-4d8c-a08b-eb5f6babab34_800x.progressive.jpg?v=1621314325"})
        Movie.create({"title": "Ex Machina", "description": "Caleb, a 26 year old coder at the world’s largest internet company, wins a competition to spend a week at a private mountain retreat belonging to Nathan, the reclusive CEO of the company. But when Caleb arrives at the remote location...", "year": "2014", "poster": "https://m.media-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_.jpg"})
        Movie.create({"title": "Arrival", "description": "Taking place after alien crafts land around the world, an expert linguist is recruited by the military to determine whether they come in peace or are a threat.", "year": "2016", "poster": "https://m.media-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_.jpg"})
        Movie.create({"title": "The Wolf of Wall Street", "description": "A New York stockbroker refuses to cooperate in a large securities fraud case involving corruption on Wall Street, corporate banking world and mob infiltration. Based on Jordan Belfort’s autobiography.", "year": "2013", "poster": "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_.jpg"})