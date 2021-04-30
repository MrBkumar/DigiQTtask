from core.models import Movie

def MovieData():
    movie_data_list = [
    {'movie_description': 'The Shawshank Redemption is a movie starring Tim '
                            'Robbins, Morgan Freeman, and Bob Gunton. Two '
                            'imprisoned men bond over a number of years, '
                            'finding solace and eventual redemption through '
                            'acts of common decency.',
        'movie_duration': 'PT2H22M',
        'movie_name': 'The Shawshank Redemption',
        'movie_rating': '9.2',
        'release_date': '1994-09-23'},
    {'movie_description': 'The Godfather is a movie starring Marlon Brando, '
                            'Al Pacino, and James Caan. An organized crime '
                            "dynasty's aging patriarch transfers control of "
                            'his clandestine empire to his reluctant son.',
        'movie_duration': 'PT2H55M',
        'movie_name': 'The Godfather',
        'movie_rating': '9.1',
        'release_date': '1972-03-24'},
    {'movie_description': 'The Godfather: Part II is a movie starring Al '
                            'Pacino, Robert De Niro, and Robert Duvall. The '
                            'early life and career of Vito Corleone in 1920s '
                            'New York City is portrayed, while his son, '
                            'Michael, expands and tightens his grip on the...',
        'movie_duration': 'PT3H22M',
        'movie_name': 'The Godfather: Part II',
        'movie_rating': '9.0',
        'release_date': '1974-12-18'},
    {'movie_description': 'The Dark Knight is a movie starring Christian '
                            'Bale, Heath Ledger, and Aaron Eckhart. When the '
                            'menace known as the Joker wreaks havoc and chaos '
                            'on the people of Gotham, Batman must accept one '
                            'of the greatest psychological and...',
        'movie_duration': 'PT2H32M',
        'movie_name': 'The Dark Knight',
        'movie_rating': '9.0',
        'release_date': '2008-07-16'},
    {'movie_description': '12 Angry Men is a movie starring Henry Fonda, '
                            'Lee J. Cobb, and Martin Balsam. A jury holdout '
                            'attempts to prevent a miscarriage of justice by '
                            'forcing his colleagues to reconsider the '
                            'evidence.',
        'movie_duration': 'PT1H36M',
        'movie_name': '12 Angry Men',
        'movie_rating': '8.9',
        'release_date': '1957-04-10'},
    {'movie_description': "Schindler's List is a movie starring Liam "
                            'Neeson, Ralph Fiennes, and Ben Kingsley. In '
                            'German-occupied Poland during World War II, '
                            'industrialist Oskar Schindler gradually becomes '
                            'concerned for his Jewish workforce after '
                            'witnessing...',
        'movie_duration': 'PT3H15M',
        'movie_name': "Schindler's List",
        'movie_rating': '8.9',
        'release_date': '1993-12-15'},
    {'movie_description': 'The Lord of the Rings: The Return of the King is '
                            'a movie starring Elijah Wood, Viggo Mortensen, '
                            'and Ian McKellen. Gandalf and Aragorn lead the '
                            "World of Men against Sauron's army to draw his "
                            'gaze from Frodo and Sam as they approach...',
        'movie_duration': 'PT3H21M',
        'movie_name': 'The Lord of the Rings: The Return of the King',
        'movie_rating': '8.9',
        'release_date': '2003-12-17'},
    {'movie_description': 'Pulp Fiction is a movie starring John Travolta, '
                            'Uma Thurman, and Samuel L. Jackson. The lives of '
                            'two mob hitmen, a boxer, a gangster and his '
                            'wife, and a pair of diner bandits intertwine in '
                            'four tales of violence and redemption.',
        'movie_duration': 'PT2H34M',
        'movie_name': 'Pulp Fiction',
        'movie_rating': '8.8',
        'release_date': '1994-09-10'},
    {'movie_description': 'Il buono, il brutto, il cattivo is a movie '
                            'starring Clint Eastwood, Eli Wallach, and Lee '
                            'Van Cleef. A bounty hunting scam joins two men '
                            'in an uneasy alliance against a third in a race '
                            'to find a fortune in gold buried in a remote...',
        'movie_duration': 'PT2H58M',
        'movie_name': 'Il buono, il brutto, il cattivo',
        'movie_rating': '8.8',
        'release_date': '1966-12-23'},
    {'movie_description': 'The Lord of the Rings: The Fellowship of the '
                            'Ring is a movie starring Elijah Wood, Ian '
                            'McKellen, and Orlando Bloom. A meek Hobbit from '
                            'the Shire and eight companions set out on a '
                            'journey to destroy the powerful One Ring and '
                            'save...',
        'movie_duration': 'PT2H58M',
        'movie_name': 'The Lord of the Rings: The Fellowship of the Ring',
        'movie_rating': '8.8',
        'release_date': '2001-12-19'},
    {'movie_description': 'Fight Club is a movie starring Brad Pitt, '
                            'Edward Norton, and Meat Loaf. An insomniac '
                            'office worker and a devil-may-care soap maker '
                            'form an underground fight club that evolves '
                            'into much more.',
        'movie_duration': 'PT2H19M',
        'movie_name': 'Fight Club',
        'movie_rating': '8.8',
        'release_date': '1999-10-15'},
    {'movie_description': 'Forrest Gump is a movie starring Tom Hanks, '
                            'Robin Wright, and Gary Sinise. The presidencies '
                            'of Kennedy and Johnson, the Vietnam War, the '
                            'Watergate scandal and other historical events '
                            'unfold from the perspective of an Alabama man...',
        'movie_duration': 'PT2H22M',
        'movie_name': 'Forrest Gump',
        'movie_rating': '8.8',
        'release_date': '1994-06-23'},
    {'movie_description': 'Inception is a movie starring Leonardo '
                            'DiCaprio, Joseph Gordon-Levitt, and Elliot '
                            'Page. A thief who steals corporate secrets '
                            'through the use of dream-sharing technology is '
                            'given the inverse task of planting an idea into '
                            'the mind of...',
        'movie_duration': 'PT2H28M',
        'movie_name': 'Inception',
        'movie_rating': '8.7',
        'release_date': '2010-07-14'},
    {'movie_description': 'The Lord of the Rings: The Two Towers is a '
                            'movie starring Elijah Wood, Ian McKellen, and '
                            'Viggo Mortensen. While Frodo and Sam edge '
                            'closer to Mordor with the help of the shifty '
                            'Gollum, the divided fellowship makes a stand '
                            'against...',
        'movie_duration': 'PT2H59M',
        'movie_name': 'The Lord of the Rings: The Two Towers',
        'movie_rating': '8.7',
        'release_date': '2002-12-18'},
    {'movie_description': 'Star Wars: Episode V - The Empire Strikes Back '
                            'is a movie starring Mark Hamill, Harrison Ford, '
                            'and Carrie Fisher. After the Rebels are '
                            'brutally overpowered by the Empire on the ice '
                            'planet Hoth, Luke Skywalker begins Jedi '
                            'training...',
        'movie_duration': 'PT2H4M',
        'movie_name': 'Star Wars: Episode V - The Empire Strikes Back',
        'movie_rating': '8.7',
        'release_date': '1980-05-21'},
    {'movie_description': 'The Matrix is a movie starring Keanu Reeves, '
                            'Laurence Fishburne, and Carrie-Anne Moss. When '
                            'a beautiful stranger leads computer hacker Neo '
                            'to a forbidding underworld, he discovers the '
                            'shocking truth--the life he knows is the...',
        'movie_duration': 'PT2H16M',
        'movie_name': 'The Matrix',
        'movie_rating': '8.6',
        'release_date': '1999-03-31'},
    {'movie_description': 'Goodfellas is a movie starring Robert De Niro, '
                            'Ray Liotta, and Joe Pesci. The story of Henry '
                            'Hill and his life in the mob, covering his '
                            'relationship with his wife Karen Hill and his '
                            'mob partners Jimmy Conway and Tommy DeVito in '
                            'the...',
        'movie_duration': 'PT2H26M',
        'movie_name': 'Goodfellas',
        'movie_rating': '8.6',
        'release_date': '1990-09-12'},
    {'movie_description': "One Flew Over the Cuckoo's Nest is a movie "
                            'starring Jack Nicholson, Louise Fletcher, and '
                            'Michael Berryman. A criminal pleads insanity '
                            'and is admitted to a mental institution, where '
                            'he rebels against the oppressive nurse and '
                            'rallies...',
        'movie_duration': 'PT2H13M',
        'movie_name': "One Flew Over the Cuckoo's Nest",
        'movie_rating': '8.6',
        'release_date': '1975-11-19'},
    {'movie_description': 'Shichinin no samurai is a movie starring '
                            'Toshirô Mifune, Takashi Shimura, and Keiko '
                            'Tsushima. A poor village under attack by '
                            'bandits recruits seven unemployed samurai to '
                            'help them defend themselves.',
        'movie_duration': 'PT3H27M',
        'movie_name': 'Shichinin no samurai',
        'movie_rating': '8.6',
        'release_date': '1954-04-26'},
    {'movie_description': 'Se7en is a movie starring Morgan Freeman, Brad '
                            'Pitt, and Kevin Spacey. Two detectives, a '
                            'rookie and a veteran, hunt a serial killer who '
                            'uses the seven deadly sins as his motives.',
        'movie_duration': 'PT2H7M',
        'movie_name': 'Se7en',
        'movie_rating': '8.6',
        'release_date': '1995-09-22'},
    {'movie_description': 'La vita è bella is a movie starring Roberto '
                            'Benigni, Nicoletta Braschi, and Giorgio '
                            'Cantarini. When an open-minded Jewish librarian '
                            'and his son become victims of the Holocaust, he '
                            'uses a perfect mixture of will, humor, and...',
        'movie_duration': 'PT1H56M',
        'movie_name': 'La vita è bella',
        'movie_rating': '8.6',
        'release_date': '1997-12-20'},
    {'movie_description': 'Cidade de Deus is a movie starring Alexandre '
                            'Rodrigues, Leandro Firmino, and Matheus '
                            "Nachtergaele. In the slums of Rio, two kids' "
                            'paths diverge as one struggles to become a '
                            'photographer and the other a kingpin.',
        'movie_duration': 'PT2H10M',
        'movie_name': 'Cidade de Deus',
        'movie_rating': '8.6',
        'release_date': '2002-08-30'},
    {'movie_description': 'The Silence of the Lambs is a movie starring '
                            'Jodie Foster, Anthony Hopkins, and Lawrence A. '
                            'Bonney. A young F.B.I. cadet must receive the '
                            'help of an incarcerated and manipulative '
                            'cannibal killer to help catch another serial '
                            'killer,...',
        'movie_duration': 'PT1H58M',
        'movie_name': 'The Silence of the Lambs',
        'movie_rating': '8.6',
        'release_date': '1991-02-14'},
    {'movie_description': "It's a Wonderful Life is a movie starring James "
                            'Stewart, Donna Reed, and Lionel Barrymore. An '
                            'angel is sent from Heaven to help a desperately '
                            'frustrated businessman by showing him what life '
                            'would have been like if he had never...',
        'movie_duration': 'PT2H10M',
        'movie_name': "It's a Wonderful Life",
        'movie_rating': '8.6',
        'release_date': '1947-01-07'},
    {'movie_description': 'Saving Private Ryan is a movie starring Tom '
                            'Hanks, Matt Damon, and Tom Sizemore. Following '
                            'the Normandy Landings, a group of U.S. soldiers '
                            'go behind enemy lines to retrieve a paratrooper '
                            'whose brothers have been killed in action.',
        'movie_duration': 'PT2H49M',
        'movie_name': 'Saving Private Ryan',
        'movie_rating': '8.6',
        'release_date': '1998-07-24'},
    {'movie_description': 'Star Wars is a movie starring Mark Hamill, '
                            'Harrison Ford, and Carrie Fisher. Luke '
                            'Skywalker joins forces with a Jedi Knight, a '
                            'cocky pilot, a Wookiee and two droids to save '
                            "the galaxy from the Empire's world-destroying "
                            'battle...',
        'movie_duration': 'PT2H1M',
        'movie_name': 'Star Wars',
        'movie_rating': '8.6',
        'release_date': '1977-05-25'},
    {'movie_description': 'The Green Mile is a movie starring Tom Hanks, '
                            'Michael Clarke Duncan, and David Morse. The '
                            'lives of guards on Death Row are affected by '
                            'one of their charges: a black man accused of '
                            'child murder and rape, yet who has a mysterious '
                            'gift.',
        'movie_duration': 'PT3H9M',
        'movie_name': 'The Green Mile',
        'movie_rating': '8.5',
        'release_date': '1999-12-10'},
    {'movie_description': 'Sen to Chihiro no kamikakushi is a movie '
                            'starring Daveigh Chase, Suzanne Pleshette, and '
                            "Miyu Irino. During her family's move to the "
                            'suburbs, a sullen 10-year-old girl wanders into '
                            'a world ruled by gods, witches, and spirits, '
                            'and...',
        'movie_duration': 'PT2H5M',
        'movie_name': 'Sen to Chihiro no kamikakushi',
        'movie_rating': '8.5',
        'release_date': '2001-07-20'},
    {'movie_description': 'Interstellar is a movie starring Matthew '
                            'McConaughey, Anne Hathaway, and Jessica '
                            'Chastain. A team of explorers travel through a '
                            'wormhole in space in an attempt to ensure '
                            "humanity's survival.",
        'movie_duration': 'PT2H49M',
        'movie_name': 'Interstellar',
        'movie_rating': '8.5',
        'release_date': '2014-11-05'},
    {'movie_description': 'Gisaengchung is a movie starring Kang-ho Song, '
                            'Sun-kyun Lee, and Yeo-jeong Cho. Greed and '
                            'class discrimination threaten the newly formed '
                            'symbiotic relationship between the wealthy Park '
                            'family and the destitute Kim clan.',
        'movie_duration': 'PT2H12M',
        'movie_name': 'Gisaengchung',
        'movie_rating': '8.5',
        'release_date': '2019-05-30'},
    {'movie_description': 'Léon is a movie starring Jean Reno, Gary '
                            'Oldman, and Natalie Portman. Mathilda, a '
                            '12-year-old girl, is reluctantly taken in by '
                            'Léon, a professional assassin, after her family '
                            'is murdered. An unusual relationship forms as '
                            'she becomes...',
        'movie_duration': 'PT1H50M',
        'movie_name': 'Léon',
        'movie_rating': '8.5',
        'release_date': '1994-09-14'},
    {'movie_description': 'Seppuku is a movie starring Tatsuya Nakadai, '
                            'Akira Ishihama, and Shima Iwashita. When a '
                            "ronin requesting seppuku at a feudal lord's "
                            'palace is told of the brutal suicide of another '
                            'ronin who previously visited, he reveals how '
                            'their...',
        'movie_duration': 'PT2H13M',
        'movie_name': 'Seppuku',
        'movie_rating': '8.5',
        'release_date': '1962-09-16'},
    {'movie_description': 'The Lion King is a movie starring Matthew '
                            'Broderick, Jeremy Irons, and James Earl Jones. '
                            'Lion prince Simba and his father are targeted '
                            'by his bitter uncle, who wants to ascend the '
                            'throne himself.',
        'movie_duration': 'PT1H28M',
        'movie_name': 'The Lion King',
        'movie_rating': '8.5',
        'release_date': '1994-06-23'},
    {'movie_description': 'The Usual Suspects is a movie starring Kevin '
                            'Spacey, Gabriel Byrne, and Chazz Palminteri. A '
                            'sole survivor tells of the twisty events '
                            'leading up to a horrific gun battle on a boat, '
                            'which began when five criminals met at a '
                            'seemingly...',
        'movie_duration': 'PT1H46M',
        'movie_name': 'The Usual Suspects',
        'movie_rating': '8.5',
        'release_date': '1995-07-19'},
    {'movie_description': 'The Pianist is a movie starring Adrien Brody, '
                            'Thomas Kretschmann, and Frank Finlay. A Polish '
                            'Jewish musician struggles to survive the '
                            'destruction of the Warsaw ghetto of World War '
                            'II.',
        'movie_duration': 'PT2H30M',
        'movie_name': 'The Pianist',
        'movie_rating': '8.5',
        'release_date': '2002-09-25'},
    {'movie_description': 'Terminator 2: Judgment Day is a movie starring '
                            'Arnold Schwarzenegger, Linda Hamilton, and '
                            'Edward Furlong. A cyborg, identical to the one '
                            'who failed to kill Sarah Connor, must now '
                            'protect her ten year old son, John Connor, from '
                            'a...',
        'movie_duration': 'PT2H17M',
        'movie_name': 'Terminator 2: Judgment Day',
        'movie_rating': '8.5',
        'release_date': '1991-07-03'},
    {'movie_description': 'Back to the Future is a movie starring Michael '
                            'J. Fox, Christopher Lloyd, and Lea Thompson. '
                            'Marty McFly, a 17-year-old high school student, '
                            'is accidentally sent thirty years into the past '
                            'in a time-traveling DeLorean invented by his...',
        'movie_duration': 'PT1H56M',
        'movie_name': 'Back to the Future',
        'movie_rating': '8.5',
        'release_date': '1985-07-03'},
    {'movie_description': 'American History X is a movie starring Edward '
                            "Norton, Edward Furlong, and Beverly D'Angelo. A "
                            'former neo-nazi skinhead tries to prevent his '
                            'younger brother from going down the same wrong '
                            'path that he did.',
        'movie_duration': 'PT1H59M',
        'movie_name': 'American History X',
        'movie_rating': '8.5',
        'release_date': '1998-07-01'},
    {'movie_description': 'Modern Times is a movie starring Charles '
                            'Chaplin, Paulette Goddard, and Henry Bergman. '
                            'The Tramp struggles to live in modern '
                            'industrial society with the help of a young '
                            'homeless woman.',
        'movie_duration': 'PT1H27M',
        'movie_name': 'Modern Times',
        'movie_rating': '8.5',
        'release_date': '1936-02-11'},
    {'movie_description': 'Gladiator is a movie starring Russell Crowe, '
                            'Joaquin Phoenix, and Connie Nielsen. A former '
                            'Roman General sets out to exact vengeance '
                            'against the corrupt emperor who murdered his '
                            'family and sent him into slavery.',
        'movie_duration': 'PT2H35M',
        'movie_name': 'Gladiator',
        'movie_rating': '8.5',
        'release_date': '2000-05-04'},
    {'movie_description': 'Psycho is a movie starring Anthony Perkins, '
                            'Janet Leigh, and Vera Miles. A Phoenix '
                            "secretary embezzles $40,000 from her employer's "
                            'client, goes on the run, and checks into a '
                            'remote motel run by a young man under the '
                            'domination of...',
        'movie_duration': 'PT1H49M',
        'movie_name': 'Psycho',
        'movie_rating': '8.5',
        'release_date': '1960-08-17'},
    {'movie_description': 'The Departed is a movie starring Leonardo '
                            'DiCaprio, Matt Damon, and Jack Nicholson. An '
                            'undercover cop and a mole in the police attempt '
                            'to identify each other while infiltrating an '
                            'Irish gang in South Boston.',
        'movie_duration': 'PT2H31M',
        'movie_name': 'The Departed',
        'movie_rating': '8.5',
        'release_date': '2006-10-04'},
    {'movie_description': 'City Lights is a movie starring Charles '
                            'Chaplin, Virginia Cherrill, and Florence Lee. '
                            'With the aid of a wealthy erratic tippler, a '
                            'dewy-eyed tramp who has fallen in love with a '
                            'sightless flower girl accumulates money to be '
                            'able to...',
        'movie_duration': 'PT1H27M',
        'movie_name': 'City Lights',
        'movie_rating': '8.5',
        'release_date': '1931-03-07'},
    {'movie_description': 'Whiplash is a movie starring Miles Teller, J.K. '
                            'Simmons, and Melissa Benoist. A promising young '
                            'drummer enrolls at a cut-throat music '
                            'conservatory where his dreams of greatness are '
                            'mentored by an instructor who will stop at '
                            'nothing...',
        'movie_duration': 'PT1H46M',
        'movie_name': 'Whiplash',
        'movie_rating': '8.5',
        'release_date': '2014-10-15'},
    {'movie_description': 'Intouchables is a movie starring François '
                            'Cluzet, Omar Sy, and Anne Le Ny. After he '
                            'becomes a quadriplegic from a paragliding '
                            'accident, an aristocrat hires a young man from '
                            'the projects to be his caregiver.',
        'movie_duration': 'PT1H52M',
        'movie_name': 'The Intouchables',
        'movie_rating': '8.5',
        'release_date': '2011-11-02'},
    {'movie_description': 'Hotaru no haka is a movie starring Tsutomu '
                            'Tatsumi, Ayano Shiraishi, and Akemi Yamaguchi. '
                            'A young boy and his little sister struggle to '
                            'survive in Japan during World War II.',
        'movie_duration': 'PT1H29M',
        'movie_name': 'Hotaru no haka',
        'movie_rating': '8.5',
        'release_date': '1988-04-16'},
    {'movie_description': 'The Prestige is a movie starring Christian '
                            'Bale, Hugh Jackman, and Scarlett Johansson. '
                            'After a tragic accident, two stage magicians '
                            'engage in a battle to create the ultimate '
                            'illusion while sacrificing everything they have '
                            'to outwit...',
        'movie_duration': 'PT2H10M',
        'movie_name': 'The Prestige',
        'movie_rating': '8.5',
        'release_date': '2006-10-19'},
    {'movie_description': "C'era una volta il West is a movie starring "
                            'Henry Fonda, Charles Bronson, and Claudia '
                            'Cardinale. A mysterious stranger with a '
                            'harmonica joins forces with a notorious '
                            'desperado to protect a beautiful widow from a '
                            'ruthless assassin...',
        'movie_duration': 'PT2H45M',
        'movie_name': 'Once Upon a Time in the West',
        'movie_rating': '8.4',
        'release_date': '1968-12-21'},
    {'movie_description': 'Casablanca is a movie starring Humphrey Bogart, '
                            'Ingrid Bergman, and Paul Henreid. A cynical '
                            'expatriate American cafe owner struggles to '
                            'decide whether or not to help his former lover '
                            'and her fugitive husband escape the Nazis in...',
        'movie_duration': 'PT1H42M',
        'movie_name': 'Casablanca',
        'movie_rating': '8.4',
        'release_date': '1943-01-23'},
    {'movie_description': 'Nuovo Cinema Paradiso is a movie starring '
                            'Philippe Noiret, Enzo Cannavale, and Antonella '
                            'Attili. A filmmaker recalls his childhood when '
                            'falling in love with the pictures at the cinema '
                            'of his home village and forms a deep '
                            'friendship...',
        'movie_duration': 'PT2H35M',
        'movie_name': 'Nuovo Cinema Paradiso',
        'movie_rating': '8.4',
        'release_date': '1988-11-17'},
    {'movie_description': 'Rear Window is a movie starring James Stewart, '
                            'Grace Kelly, and Wendell Corey. A '
                            'wheelchair-bound photographer spies on his '
                            'neighbors from his apartment window and becomes '
                            'convinced one of them has committed murder.',
        'movie_duration': 'PT1H52M',
        'movie_name': 'Rear Window',
        'movie_rating': '8.4',
        'release_date': '1954-09-01'},
    {'movie_description': 'Alien is a movie starring Sigourney Weaver, Tom '
                            'Skerritt, and John Hurt. After a space merchant '
                            'vessel receives an unknown transmission as a '
                            'distress call, one of the crew is attacked by a '
                            'mysterious life form and they soon realize...',
        'movie_duration': 'PT1H57M',
        'movie_name': 'Alien',
        'movie_rating': '8.4',
        'release_date': '1979-05-28'},
    {'movie_description': 'Apocalypse Now is a movie starring Martin '
                            'Sheen, Marlon Brando, and Robert Duvall. A U.S. '
                            'Army officer serving in Vietnam is tasked with '
                            'assassinating a renegade Special Forces Colonel '
                            'who sees himself as a god.',
        'movie_duration': 'PT2H27M',
        'movie_name': 'Apocalypse Now',
        'movie_rating': '8.4',
        'release_date': '1979-08-15'},
    {'movie_description': 'Memento is a movie starring Guy Pearce, '
                            'Carrie-Anne Moss, and Joe Pantoliano. A man '
                            'with short-term memory loss attempts to track '
                            "down his wife's murderer.",
        'movie_duration': 'PT1H53M',
        'movie_name': 'Memento',
        'movie_rating': '8.4',
        'release_date': '2000-10-11'},
    {'movie_description': 'The Great Dictator is a movie starring Charles '
                            'Chaplin, Paulette Goddard, and Jack Oakie. '
                            'Dictator Adenoid Hynkel tries to expand his '
                            'empire while a poor Jewish barber tries to '
                            "avoid persecution from Hynkel's regime.",
        'movie_duration': 'PT2H5M',
        'movie_name': 'The Great Dictator',
        'movie_rating': '8.4',
        'release_date': '1941-01-01'},
    {'movie_description': 'Raiders of the Lost Ark is a movie starring '
                            'Harrison Ford, Karen Allen, and Paul Freeman. '
                            'In 1936, archaeologist and adventurer Indiana '
                            'Jones is hired by the U.S. government to find '
                            "the Ark of the Covenant before Adolf Hitler's...",
        'movie_duration': 'PT1H55M',
        'movie_name': 'Raiders of the Lost Ark',
        'movie_rating': '8.4',
        'release_date': '1981-06-12'},
    {'movie_description': 'Django Unchained is a movie starring Jamie '
                            'Foxx, Christoph Waltz, and Leonardo DiCaprio. '
                            'With the help of a German bounty-hunter, a '
                            'freed slave sets out to rescue his wife from a '
                            'brutal plantation-owner in Mississippi.',
        'movie_duration': 'PT2H45M',
        'movie_name': 'Django Unchained',
        'movie_rating': '8.4',
        'release_date': '2012-12-25'},
    {'movie_description': 'Das Leben der Anderen is a movie starring '
                            'Ulrich Mühe, Martina Gedeck, and Sebastian '
                            'Koch. In 1984 East Berlin, an agent of the '
                            'secret police, conducting surveillance on a '
                            'writer and his lover, finds himself becoming '
                            'increasingly...',
        'movie_duration': 'PT2H17M',
        'movie_name': 'The Lives of Others',
        'movie_rating': '8.4',
        'release_date': '2006-03-23'},
    {'movie_description': 'Paths of Glory is a movie starring Kirk '
                            'Douglas, Ralph Meeker, and Adolphe Menjou. '
                            'After refusing to attack an enemy position, a '
                            'general accuses the soldiers of cowardice and '
                            'their commanding officer must defend them.',
        'movie_duration': 'PT1H28M',
        'movie_name': 'Paths of Glory',
        'movie_rating': '8.4',
        'release_date': '1957-10-25'},
    {'movie_description': 'WALL·E is a movie starring Ben Burtt, Elissa '
                            'Knight, and Jeff Garlin. In the distant future, '
                            'a small waste-collecting robot inadvertently '
                            'embarks on a space journey that will ultimately '
                            'decide the fate of mankind.',
        'movie_duration': 'PT1H38M',
        'movie_name': 'WALL·E',
        'movie_rating': '8.4',
        'release_date': '2008-06-26'},
    {'movie_description': 'Hamilton is a movie starring Lin-Manuel '
                            'Miranda, Phillipa Soo, and Leslie Odom Jr.. The '
                            "real life of one of America's foremost founding "
                            'fathers and first Secretary of the Treasury, '
                            'Alexander Hamilton. Captured live on Broadway '
                            'from...',
        'movie_duration': 'PT2H40M',
        'movie_name': 'Hamilton',
        'movie_rating': '8.4',
        'release_date': '2020-07-03'},
    {'movie_description': 'Joker is a movie starring Joaquin Phoenix, '
                            'Robert De Niro, and Zazie Beetz. In Gotham '
                            'City, mentally troubled comedian Arthur Fleck '
                            'is disregarded and mistreated by society. He '
                            'then embarks on a downward spiral of revolution '
                            'and...',
        'movie_duration': 'PT2H2M',
        'movie_name': 'Joker',
        'movie_rating': '8.4',
        'release_date': '2019-10-01'},
    {'movie_description': 'The Shining is a movie starring Jack Nicholson, '
                            'Shelley Duvall, and Danny Lloyd. A family heads '
                            'to an isolated hotel for the winter where a '
                            'sinister presence influences the father into '
                            'violence, while his psychic son sees horrific...',
        'movie_duration': 'PT2H26M',
        'movie_name': 'The Shining',
        'movie_rating': '8.4',
        'release_date': '1980-06-13'},
    {'movie_description': 'Avengers: Infinity War is a movie starring '
                            'Robert Downey Jr., Chris Hemsworth, and Mark '
                            'Ruffalo. The Avengers and their allies must be '
                            'willing to sacrifice all in an attempt to '
                            'defeat the powerful Thanos before his blitz '
                            'of...',
        'movie_duration': 'PT2H29M',
        'movie_name': 'Avengers: Infinity War',
        'movie_rating': '8.4',
        'release_date': '2018-04-25'},
    {'movie_description': 'Sunset Blvd. is a movie starring William '
                            'Holden, Gloria Swanson, and Erich von Stroheim. '
                            'A screenwriter develops a dangerous '
                            'relationship with a faded film star determined '
                            'to make a triumphant return.',
        'movie_duration': 'PT1H50M',
        'movie_name': 'Sunset Blvd.',
        'movie_rating': '8.4',
        'release_date': '1950-09-29'},
    {'movie_description': 'Witness for the Prosecution is a movie starring '
                            'Tyrone Power, Marlene Dietrich, and Charles '
                            'Laughton. A veteran British barrister must '
                            'defend his client in a murder trial that has '
                            'surprise after surprise.',
        'movie_duration': 'PT1H56M',
        'movie_name': 'Witness for the Prosecution',
        'movie_rating': '8.4',
        'release_date': '1958-02-06'},
    {'movie_description': 'Spider-Man: Into the Spider-Verse is a movie '
                            'starring Shameik Moore, Jake Johnson, and '
                            'Hailee Steinfeld. Teen Miles Morales becomes '
                            'the Spider-Man of his universe, and must join '
                            'with five spider-powered individuals from '
                            'other...',
        'movie_duration': 'PT1H57M',
        'movie_name': 'Spider-Man: Into the Spider-Verse',
        'movie_rating': '8.3',
        'release_date': '2018-12-12'},
    {'movie_description': 'Oldeuboi is a movie starring Choi Min-sik, Yoo '
                            'Ji-Tae, and Kang Hye-jeong. After being '
                            'kidnapped and imprisoned for fifteen years, Oh '
                            'Dae-Su is released, only to find that he must '
                            'find his captor in five days.',
        'movie_duration': 'PT2H',
        'movie_name': 'Oldeuboi',
        'movie_rating': '8.3',
        'release_date': '2003-11-21'},
    {'movie_description': 'Mononoke-hime is a movie starring Yôji Matsuda, '
                            'Yuriko Ishida, and Yûko Tanaka. On a journey to '
                            "find the cure for a Tatarigami's curse, "
                            'Ashitaka finds himself in the middle of a war '
                            'between the forest gods and Tatara, a mining...',
        'movie_duration': 'PT2H14M',
        'movie_name': 'Mononoke-hime',
        'movie_rating': '8.3',
        'release_date': '1997-07-12'},
    {'movie_description': 'Dr. Strangelove or: How I Learned to Stop '
                            'Worrying and Love the Bomb is a movie starring '
                            'Peter Sellers, George C. Scott, and Sterling '
                            'Hayden. An insane general triggers a path to '
                            'nuclear holocaust that a War Room full of '
                            'politicians...',
        'movie_duration': 'PT1H35M',
        'movie_name': 'Dr. Strangelove or: How I Learned to Stop Worrying and '
                        'Love the Bomb',
        'movie_rating': '8.3',
        'release_date': '1964-01-29'},
    {'movie_description': 'The Dark Knight Rises is a movie starring '
                            'Christian Bale, Tom Hardy, and Anne Hathaway. '
                            "Eight years after the Joker's reign of anarchy, "
                            'Batman, with the help of the enigmatic '
                            'Catwoman, is forced from his exile to save '
                            'Gotham City...',
        'movie_duration': 'PT2H44M',
        'movie_name': 'The Dark Knight Rises',
        'movie_rating': '8.3',
        'release_date': '2012-07-19'},
    {'movie_description': 'Once Upon a Time in America is a movie starring '
                            'Robert De Niro, James Woods, and Elizabeth '
                            'McGovern. A former Prohibition-era Jewish '
                            'gangster returns to the Lower East Side of '
                            'Manhattan over thirty years later, where he '
                            'once again...',
        'movie_duration': 'PT3H49M',
        'movie_name': 'Once Upon a Time in America',
        'movie_rating': '8.3',
        'release_date': '1984-05-23'},
    {'movie_description': 'Kimi no na wa. is a movie starring Ryûnosuke '
                            'Kamiki, Mone Kamishiraishi, and Ryô Narita. Two '
                            'strangers find themselves linked in a bizarre '
                            'way. When a connection forms, will distance be '
                            'the only thing to keep them apart?',
        'movie_duration': 'PT1H46M',
        'movie_name': 'Kimi no na wa.',
        'movie_rating': '8.3',
        'release_date': '2016-08-26'},
    {'movie_description': 'Aliens is a movie starring Sigourney Weaver, '
                            'Michael Biehn, and Carrie Henn. Fifty-seven '
                            'years after surviving an apocalyptic attack '
                            'aboard her space vessel by merciless space '
                            'creatures, Officer Ripley awakens from '
                            'hyper-sleep and...',
        'movie_duration': 'PT2H17M',
        'movie_name': 'Aliens',
        'movie_rating': '8.3',
        'release_date': '1986-07-18'},
    {'movie_description': 'Coco is a movie starring Anthony Gonzalez, Gael '
                            'García Bernal, and Benjamin Bratt. Aspiring '
                            "musician Miguel, confronted with his family's "
                            'ancestral ban on music, enters the Land of the '
                            'Dead to find his great-great-grandfather, a...',
        'movie_duration': 'PT1H45M',
        'movie_name': 'Coco',
        'movie_rating': '8.3',
        'release_date': '2017-10-27'},
    {'movie_description': 'Avengers: Endgame is a movie starring Robert '
                            'Downey Jr., Chris Evans, and Mark Ruffalo. '
                            'After the devastating events of Avengers: '
                            'Infinity War (2018), the universe is in ruins. '
                            'With the help of remaining allies, the '
                            'Avengers...',
        'movie_duration': 'PT3H1M',
        'movie_name': 'Avengers: Endgame',
        'movie_rating': '8.3',
        'release_date': '2019-04-24'},
    {'movie_description': 'Capharnaüm is a movie starring Zain Al Rafeea, '
                            'Yordanos Shiferaw, and Boluwatife Treasure '
                            'Bankole. While serving a five-year sentence for '
                            'a violent crime, a 12-year-old boy sues his '
                            'parents for neglect.',
        'movie_duration': 'PT2H6M',
        'movie_name': 'Capharnaüm',
        'movie_rating': '8.3',
        'release_date': '2018-09-20'},
    {'movie_description': 'American Beauty is a movie starring Kevin '
                            'Spacey, Annette Bening, and Thora Birch. A '
                            'sexually frustrated suburban father has a '
                            'mid-life crisis after becoming infatuated with '
                            "his daughter's best friend.",
        'movie_duration': 'PT2H2M',
        'movie_name': 'American Beauty',
        'movie_rating': '8.3',
        'release_date': '1999-10-01'},
    {'movie_description': 'Braveheart is a movie starring Mel Gibson, '
                            'Sophie Marceau, and Patrick McGoohan. Scottish '
                            'warrior William Wallace leads his countrymen in '
                            'a rebellion to free his homeland from the '
                            'tyranny of King Edward I of England.',
        'movie_duration': 'PT2H58M',
        'movie_name': 'Braveheart',
        'movie_rating': '8.3',
        'release_date': '1995-05-24'},
    {'movie_description': 'Tengoku to jigoku is a movie starring Toshirô '
                            'Mifune, Yutaka Sada, and Tatsuya Nakadai. An '
                            'executive of a shoe company becomes a victim of '
                            "extortion when his chauffeur's son is kidnapped "
                            'and held for ransom.',
        'movie_duration': 'PT2H23M',
        'movie_name': 'Tengoku to jigoku',
        'movie_rating': '8.3',
        'release_date': '1963-03-01'},
    {'movie_description': 'Toy Story is a movie starring Tom Hanks, Tim '
                            'Allen, and Don Rickles. A cowboy doll is '
                            'profoundly threatened and jealous when a new '
                            'spaceman figure supplants him as top toy in a '
                            "boy's room.",
        'movie_duration': 'PT1H21M',
        'movie_name': 'Toy Story',
        'movie_rating': '8.3',
        'release_date': '1995-11-22'},
    {'movie_description': 'Das Boot is a movie starring Jürgen Prochnow, '
                            'Herbert Grönemeyer, and Klaus Wennemann. The '
                            'claustrophobic world of a WWII German U-boat; '
                            'boredom, filth and sheer terror.',
        'movie_duration': 'PT2H29M',
        'movie_name': 'Das Boot',
        'movie_rating': '8.3',
        'release_date': '1981-09-17'},
    {'movie_description': '3 Idiots is a movie starring Aamir Khan, '
                            'Madhavan, and Mona Singh. Two friends are '
                            'searching for their long lost companion. They '
                            'revisit their college days and recall the '
                            'memories of their friend who inspired them to '
                            'think...',
        'movie_duration': 'PT2H50M',
        'movie_name': '3 Idiots',
        'movie_rating': '8.3',
        'release_date': '2009-12-24'},
    {'movie_description': 'Amadeus is a movie starring F. Murray Abraham, '
                            'Tom Hulce, and Elizabeth Berridge. The life, '
                            'success and troubles of Wolfgang Amadeus '
                            'Mozart, as told by Antonio Salieri, the '
                            'contemporaneous composer who was insanely '
                            'jealous of...',
        'movie_duration': 'PT2H40M',
        'movie_name': 'Amadeus',
        'movie_rating': '8.3',
        'release_date': '1984-09-19'},
    {'movie_description': 'Inglourious Basterds is a movie starring Brad '
                            'Pitt, Diane Kruger, and Eli Roth. In '
                            'Nazi-occupied France during World War II, a '
                            'plan to assassinate Nazi leaders by a group of '
                            'Jewish U.S. soldiers coincides with a theatre '
                            "owner's...",
        'movie_duration': 'PT2H33M',
        'movie_name': 'Inglourious Basterds',
        'movie_rating': '8.3',
        'release_date': '2009-08-19'},
    {'movie_description': 'Good Will Hunting is a movie starring Robin '
                            'Williams, Matt Damon, and Ben Affleck. Will '
                            'Hunting, a janitor at M.I.T., has a gift for '
                            'mathematics, but needs help from a psychologist '
                            'to find direction in his life.',
        'movie_duration': 'PT2H6M',
        'movie_name': 'Good Will Hunting',
        'movie_rating': '8.3',
        'release_date': '1998-01-09'},
    {'movie_description': 'Star Wars: Episode VI - Return of the Jedi is a '
                            'movie starring Mark Hamill, Harrison Ford, and '
                            'Carrie Fisher. After a daring mission to rescue '
                            'Han Solo from Jabba the Hutt, the Rebels '
                            'dispatch to Endor to destroy the second Death...',
        'movie_duration': 'PT2H11M',
        'movie_name': 'Star Wars: Episode VI - Return of the Jedi',
        'movie_rating': '8.3',
        'release_date': '1983-05-25'},
    {'movie_description': 'Taare Zameen Par is a movie starring Darsheel '
                            'Safary, Aamir Khan, and Tisca Chopra. An '
                            'eight-year-old boy is thought to be a lazy '
                            'trouble-maker, until the new art teacher has '
                            'the patience and compassion to discover the '
                            'real problem...',
        'movie_duration': 'PT2H45M',
        'movie_name': 'Taare Zameen Par',
        'movie_rating': '8.3',
        'release_date': '2007-12-21'},
    {'movie_description': 'Reservoir Dogs is a movie starring Harvey '
                            'Keitel, Tim Roth, and Michael Madsen. When a '
                            'simple jewelry heist goes horribly wrong, the '
                            'surviving criminals begin to suspect that one '
                            'of them is a police informant.',
        'movie_duration': 'PT1H39M',
        'movie_name': 'Reservoir Dogs',
        'movie_rating': '8.3',
        'release_date': '1992-09-02'},
    {'movie_description': '2001: A Space Odyssey is a movie starring Keir '
                            'Dullea, Gary Lockwood, and William Sylvester. '
                            'After discovering a mysterious artifact buried '
                            'beneath the Lunar surface, mankind sets off on '
                            'a quest to find its origins with help from...',
        'movie_duration': 'PT2H29M',
        'movie_name': '2001: A Space Odyssey',
        'movie_rating': '8.3',
        'release_date': '1968-04-11'},
    {'movie_description': 'Requiem for a Dream is a movie starring Ellen '
                            'Burstyn, Jared Leto, and Jennifer Connelly. The '
                            'drug-induced utopias of four Coney Island '
                            'people are shattered when their addictions run '
                            'deep.',
        'movie_duration': 'PT1H42M',
        'movie_name': 'Requiem for a Dream',
        'movie_rating': '8.3',
        'release_date': '2000-11-03'},
    {'movie_description': 'Jagten is a movie starring Mads Mikkelsen, '
                            'Thomas Bo Larsen, and Annika Wedderkopp. A '
                            'teacher lives a lonely life, all the while '
                            "struggling over his son's custody. His life "
                            'slowly gets better as he finds love and '
                            'receives good news...',
        'movie_duration': 'PT1H55M',
        'movie_name': 'Jagten',
        'movie_rating': '8.3',
        'release_date': '2012-10-25'},
    {'movie_description': 'Vertigo is a movie starring James Stewart, Kim '
                            'Novak, and Barbara Bel Geddes. A former police '
                            'detective juggles wrestling with his personal '
                            'demons and becoming obsessed with a hauntingly '
                            'beautiful woman.',
        'movie_duration': 'PT2H8M',
        'movie_name': 'Vertigo',
        'movie_rating': '8.3',
        'release_date': '1958-05-22'},
    {'movie_description': 'M - Eine Stadt sucht einen Mörder is a movie '
                            'starring Peter Lorre, Ellen Widmann, and Inge '
                            'Landgut. When the police in a German city are '
                            'unable to catch a child-murderer, other '
                            'criminals join in the manhunt.',
        'movie_duration': 'PT1H39M',
        'movie_name': 'M - Eine Stadt sucht einen Mörder',
        'movie_rating': '8.3',
        'release_date': '1931-08-31'},
    {'movie_description': 'Eternal Sunshine of the Spotless Mind is a '
                            'movie starring Jim Carrey, Kate Winslet, and '
                            'Tom Wilkinson. When their relationship turns '
                            'sour, a couple undergoes a medical procedure to '
                            'have each other erased from their memories.',
        'movie_duration': 'PT1H48M',
        'movie_name': 'Eternal Sunshine of the Spotless Mind',
        'movie_rating': '8.3',
        'release_date': '2004-03-19'},
    {'movie_description': 'Citizen Kane is a movie starring Orson Welles, '
                            'Joseph Cotten, and Dorothy Comingore. Following '
                            'the death of publishing tycoon Charles Foster '
                            'Kane, reporters scramble to uncover the meaning '
                            "of his final utterance; 'Rosebud'.",
        'movie_duration': 'PT1H59M',
        'movie_name': 'Citizen Kane',
        'movie_rating': '8.3',
        'release_date': '1941-06-06'},
    {'movie_description': 'Dangal is a movie starring Aamir Khan, Sakshi '
                            'Tanwar, and Fatima Sana Shaikh. Former wrestler '
                            'Mahavir Singh Phogat and his two wrestler '
                            'daughters struggle towards glory at the '
                            'Commonwealth Games in the face of societal '
                            'oppression.',
        'movie_duration': 'PT2H41M',
        'movie_name': 'Dangal',
        'movie_rating': '8.3',
        'release_date': '2016-12-21'},
    {'movie_description': 'Idi i smotri is a movie starring Aleksey '
                            'Kravchenko, Olga Mironova, and Liubomiras '
                            'Laucevicius. After finding an old rifle, a '
                            'young boy joins the Soviet resistance movement '
                            'against ruthless German forces and experiences '
                            'the horrors...',
        'movie_duration': 'PT2H22M',
        'movie_name': 'Idi i smotri',
        'movie_rating': '8.2',
        'release_date': '1985-10-17'},
    {'movie_description': "Singin' in the Rain is a movie starring Gene "
                            "Kelly, Donald O'Connor, and Debbie Reynolds. A "
                            'silent film production company and cast make a '
                            'difficult transition to sound.',
        'movie_duration': 'PT1H43M',
        'movie_name': "Singin' in the Rain",
        'movie_rating': '8.2',
        'release_date': '1952-04-11'},
    {'movie_description': 'The Kid is a movie starring Charles Chaplin, '
                                'Edna Purviance, and Jackie Coogan. The Tramp '
                                'cares for an abandoned child, but events put '
                                'that relationship in jeopardy.',
        'movie_duration': 'PT1H8M',
        'movie_name': 'The Kid',
        'movie_rating': '8.2',
        'release_date': '1921-02-06'},
    {'movie_description': 'Ladri di biciclette is a movie starring '
                                'Lamberto Maggiorani, Enzo Staiola, and '
                                'Lianella Carell. In post-war Italy, a '
                                "working-class man's bicycle is stolen. He and "
                                'his son set out to find it.',
        'movie_duration': 'PT1H29M',
        'movie_name': 'Ladri di biciclette',
        'movie_rating': '8.2',
        'release_date': '1948-11-24'},
    {'movie_description': 'Full Metal Jacket is a movie starring Matthew '
                                "Modine, R. Lee Ermey, and Vincent D'Onofrio. A "
                                'pragmatic U.S. Marine observes the '
                                'dehumanizing effects the Vietnam War has on '
                                'his fellow recruits from their brutal boot '
                                'camp training to...',
        'movie_duration': 'PT1H56M',
        'movie_name': 'Full Metal Jacket',
        'movie_rating': '8.2',
        'release_date': '1987-06-26'},
    {'movie_description': 'Ikiru is a movie starring Takashi Shimura, '
                                "Nobuo Kaneko, and Shin'ichi Himori. A "
                                'bureaucrat tries to find a meaning in his life '
                                'after he discovers he has terminal cancer.',
        'movie_duration': 'PT2H23M',
        'movie_name': 'Ikiru',
        'movie_rating': '8.2',
        'release_date': '1952-10-09'},
    {'movie_description': 'Snatch is a movie starring Jason Statham, Brad '
                                'Pitt, and Benicio Del Toro. Unscrupulous '
                                'boxing promoters, violent bookmakers, a '
                                'Russian gangster, incompetent amateur robbers '
                                'and supposedly Jewish jewelers fight to track '
                                'down a...',
        'movie_duration': 'PT1H42M',
        'movie_name': 'Snatch',
        'movie_rating': '8.2',
        'release_date': '2000-09-01'},
    {'movie_description': 'North by Northwest is a movie starring Cary '
                                'Grant, Eva Marie Saint, and James Mason. A New '
                                'York City advertising executive goes on the '
                                'run after being mistaken for a government '
                                'agent by a group of foreign spies.',
        'movie_duration': 'PT2H16M',
        'movie_name': 'North by Northwest',
        'movie_rating': '8.2',
        'release_date': '1959-09-08'},
    {'movie_description': 'Scarface is a movie starring Al Pacino, '
                                'Michelle Pfeiffer, and Steven Bauer. In 1980 '
                                'Miami, a determined Cuban immigrant takes over '
                                'a drug cartel and succumbs to greed.',
        'movie_duration': 'PT2H50M',
        'movie_name': 'Scarface',
        'movie_rating': '8.2',
        'release_date': '1983-12-09'},
    {'movie_description': 'A Clockwork Orange is a movie starring Malcolm '
                                'McDowell, Patrick Magee, and Michael Bates. In '
                                'the future, a sadistic gang leader is '
                                'imprisoned and volunteers for a '
                                "conduct-aversion experiment, but it doesn't go "
                                'as planned.',
        'movie_duration': 'PT2H16M',
        'movie_name': 'A Clockwork Orange',
        'movie_rating': '8.2',
        'release_date': '1972-01-13'},
    {'movie_description': '1917 is a movie starring Dean-Charles Chapman, '
                                'George MacKay, and Daniel Mays. April 6th, '
                                '1917. As a regiment assembles to wage war deep '
                                'in enemy territory, two soldiers are assigned '
                                'to race against time and deliver a message '
                                'that...',
        'movie_duration': 'PT1H59M',
        'movie_name': '1917',
        'movie_rating': '8.2',
        'release_date': '2020-01-02'},
    {'movie_description': 'Incendies is a movie starring Lubna Azabal, '
                                'Mélissa Désormeaux-Poulin, and Maxim Gaudette. '
                                'Twins journey to the Middle East to discover '
                                'their family history and fulfill their '
                                "mother's last wishes.",
        'movie_duration': 'PT2H11M',
        'movie_name': 'Incendies',
        'movie_rating': '8.2',
        'release_date': '2011-01-12'},
    {'movie_description': 'Taxi Driver is a movie starring Robert De '
                                'Niro, Jodie Foster, and Cybill Shepherd. A '
                                'mentally unstable veteran works as a nighttime '
                                'taxi driver in New York City, where the '
                                'perceived decadence and sleaze fuels his urge '
                                'for violent...',
        'movie_duration': 'PT1H54M',
        'movie_name': 'Taxi Driver',
        'movie_rating': '8.2',
        'release_date': '1976-02-08'},
    {'movie_description': 'Jodaeiye Nader az Simin is a movie starring '
                                'Payman Maadi, Leila Hatami, and Sareh Bayat. A '
                                'married couple are faced with a difficult '
                                'decision - to improve the life of their child '
                                'by moving to another country or to stay in '
                                'Iran and...',
        'movie_duration': 'PT2H3M',
        'movie_name': 'Jodaeiye Nader az Simin',
        'movie_rating': '8.2',
        'release_date': '2011-03-16'},
    {'movie_description': 'Toy Story 3 is a movie starring Tom Hanks, Tim '
                                'Allen, and Joan Cusack. The toys are '
                                'mistakenly delivered to a day-care center '
                                'instead of the attic right before Andy leaves '
                                "for college, and it's up to Woody to convince "
                                'the other toys...',
        'movie_duration': 'PT1H43M',
        'movie_name': 'Toy Story 3',
        'movie_rating': '8.2',
        'release_date': '2010-06-16'},
    {'movie_description': 'The Sting is a movie starring Paul Newman, '
                                'Robert Redford, and Robert Shaw. Two grifters '
                                'team up to pull off the ultimate con.',
        'movie_duration': 'PT2H9M',
        'movie_name': 'The Sting',
        'movie_rating': '8.2',
        'release_date': '1973-12-25'},
    {'movie_description': 'Lawrence of Arabia is a movie starring Peter '
                                "O'Toole, Alec Guinness, and Anthony Quinn. The "
                                'story of T.E. Lawrence, the English officer '
                                'who successfully united and led the diverse, '
                                'often warring, Arab tribes during World War I '
                                'in...',
        'movie_duration': 'PT3H48M',
        'movie_name': 'Lawrence of Arabia',
        'movie_rating': '8.2',
        'release_date': '1962-12-11'},
    {'movie_description': "Le fabuleux destin d'Amélie Poulain is a movie "
                                'starring Audrey Tautou, Mathieu Kassovitz, and '
                                'Rufus. Amélie is an innocent and naive girl in '
                                'Paris with her own sense of justice. She '
                                'decides to help those around her and, along '
                                'the...',
        'movie_duration': 'PT2H2M',
        'movie_name': 'Amélie',
        'movie_rating': '8.2',
        'release_date': '2001-04-25'},
    {'movie_description': 'Metropolis is a movie starring Brigitte Helm, '
                                'Alfred Abel, and Gustav Fröhlich. In a '
                                'futuristic city sharply divided between the '
                                'working class and the city planners, the son '
                                "of the city's mastermind falls in love with "
                                'a...',
        'movie_duration': 'PT2H33M',
        'movie_name': 'Metropolis',
        'movie_rating': '8.2',
        'release_date': '1927-02-06'},
    {'movie_description': 'The Apartment is a movie starring Jack Lemmon, '
                                'Shirley MacLaine, and Fred MacMurray. A man '
                                'tries to rise in his company by letting its '
                                'executives use his apartment for trysts, but '
                                'complications and a romance of his own ensue.',
        'movie_duration': 'PT2H5M',
        'movie_name': 'The Apartment',
        'movie_rating': '8.2',
        'release_date': '1960-06-29'},
    {'movie_description': 'The Father is a movie starring Anthony '
                                'Hopkins, Olivia Colman, and Mark Gatiss. A man '
                                'refuses all assistance from his daughter as he '
                                'ages. As he tries to make sense of his '
                                'changing circumstances, he begins to doubt his '
                                'loved ones,...',
        'movie_duration': 'PT1H37M',
        'movie_name': 'The Father',
        'movie_rating': '8.2',
        'release_date': '2020-12-23'},
    {'movie_description': 'Per qualche dollaro in più is a movie starring '
                                'Clint Eastwood, Lee Van Cleef, and Gian Maria '
                                'Volontè. Two bounty hunters with the same '
                                'intentions team up to track down a Western '
                                'outlaw.',
        'movie_duration': 'PT2H12M',
        'movie_name': 'Per qualche dollaro in più',
        'movie_rating': '8.2',
        'release_date': '1965-12-20'},
    {'movie_description': 'Double Indemnity is a movie starring Fred '
                                'MacMurray, Barbara Stanwyck, and Edward G. '
                                'Robinson. An insurance representative lets '
                                'himself be talked by a seductive housewife '
                                'into a murder/insurance fraud scheme that '
                                'arouses the...',
        'movie_duration': 'PT1H47M',
        'movie_name': 'Double Indemnity',
        'movie_rating': '8.2',
        'release_date': '1944-04-24'},
    {'movie_description': 'To Kill a Mockingbird is a movie starring '
                                'Gregory Peck, John Megna, and Frank Overton. '
                                'Atticus Finch, a lawyer in the Depression-era '
                                'South, defends a black man against an '
                                'undeserved rape charge, and his children '
                                'against prejudice.',
        'movie_duration': 'PT2H9M',
        'movie_name': 'To Kill a Mockingbird',
        'movie_rating': '8.2',
        'release_date': '1962-12-20'},
    {'movie_description': 'Up is a movie starring Edward Asner, Jordan '
                                'Nagai, and John Ratzenberger. 78-year-old Carl '
                                'Fredricksen travels to Paradise Falls in his '
                                'house equipped with balloons, inadvertently '
                                'taking a young stowaway.',
        'movie_duration': 'PT1H36M',
        'movie_name': 'Up',
        'movie_rating': '8.2',
        'release_date': '2009-05-28'},
    {'movie_description': 'Indiana Jones and the Last Crusade is a movie '
                                'starring Harrison Ford, Sean Connery, and '
                                'Alison Doody. In 1938, after his father '
                                'Professor Henry Jones, Sr. goes missing while '
                                'pursuing the Holy Grail, Professor Henry '
                                '"Indiana" Jones,...',
        'movie_duration': 'PT2H7M',
        'movie_name': 'Indiana Jones and the Last Crusade',
        'movie_rating': '8.2',
        'release_date': '1989-05-24'},
    {'movie_description': 'Heat is a movie starring Al Pacino, Robert De '
                                'Niro, and Val Kilmer. A group of professional '
                                'bank robbers start to feel the heat from '
                                'police when they unknowingly leave a clue at '
                                'their latest heist.',
        'movie_duration': 'PT2H50M',
        'movie_name': 'Heat',
        'movie_rating': '8.2',
        'release_date': '1995-12-15'},
    {'movie_description': 'L.A. Confidential is a movie starring Kevin '
                                'Spacey, Russell Crowe, and Guy Pearce. As '
                                'corruption grows in 1950s Los Angeles, three '
                                'policemen - one strait-laced, one brutal, and '
                                'one sleazy - investigate a series of murders '
                                'with their...',
        'movie_duration': 'PT2H18M',
        'movie_name': 'L.A. Confidential',
        'movie_rating': '8.2',
        'release_date': '1997-09-19'},
    {'movie_description': 'Green Book is a movie starring Viggo '
                                'Mortensen, Mahershala Ali, and Linda '
                                'Cardellini. A working-class Italian-American '
                                'bouncer becomes the driver of an '
                                'African-American classical pianist on a tour '
                                'of venues through the 1960s...',
        'movie_duration': 'PT2H10M',
        'movie_name': 'Green Book',
        'movie_rating': '8.2',
        'release_date': '2018-11-16'},
    {'movie_description': 'Die Hard is a movie starring Bruce Willis, '
                                'Alan Rickman, and Bonnie Bedelia. An NYPD '
                                'officer tries to save his wife and several '
                                'others taken hostage by German terrorists '
                                'during a Christmas party at the Nakatomi Plaza '
                                'in Los Angeles.',
        'movie_duration': 'PT2H12M',
        'movie_name': 'Die Hard',
        'movie_rating': '8.2',
        'release_date': '1988-07-20'},
    {'movie_description': 'Batman Begins is a movie starring Christian '
                                'Bale, Michael Caine, and Ken Watanabe. After '
                                'training with his mentor, Batman begins his '
                                'fight to free crime-ridden Gotham City from '
                                'corruption.',
        'movie_duration': 'PT2H20M',
        'movie_name': 'Batman Begins',
        'movie_rating': '8.2',
        'release_date': '2005-06-15'},
    {'movie_description': 'Yojinbo is a movie starring Toshirô Mifune, '
                                'Eijirô Tôno, and Tatsuya Nakadai. A crafty '
                                'ronin comes to a town divided by two criminal '
                                'gangs and decides to play them against each '
                                'other to free the town.',
        'movie_duration': 'PT1H50M',
        'movie_name': 'Yojinbo',
        'movie_rating': '8.2',
        'release_date': '1961-04-25'},
    {'movie_description': 'Rashomon is a movie starring Toshirô Mifune, '
                                'Machiko Kyô, and Masayuki Mori. The rape of a '
                                'bride and the murder of her samurai husband '
                                'are recalled from the perspectives of a '
                                "bandit, the bride, the samurai's ghost and a "
                                'woodcutter.',
        'movie_duration': 'PT1H28M',
        'movie_name': 'Rashomon',
        'movie_rating': '8.2',
        'release_date': '1950-08-26'},
    {'movie_description': 'Monty Python and the Holy Grail is a movie '
                                'starring Graham Chapman, John Cleese, and Eric '
                                'Idle. King Arthur and his Knights of the Round '
                                'Table embark on a surreal, low-budget search '
                                'for the Holy Grail, encountering many, very '
                                'silly...',
        'movie_duration': 'PT1H31M',
        'movie_name': 'Monty Python and the Holy Grail',
        'movie_rating': '8.2',
        'release_date': '1975-05-25'},
    {'movie_description': 'Der Untergang is a movie starring Bruno Ganz, '
                                'Alexandra Maria Lara, and Ulrich Matthes. '
                                'Traudl Junge, the final secretary for Adolf '
                                "Hitler, tells of the Nazi dictator's final "
                                'days in his Berlin bunker at the end of WWII.',
        'movie_duration': 'PT2H36M',
        'movie_name': 'Der Untergang',
        'movie_rating': '8.2',
        'release_date': '2004-09-16'},
    {'movie_description': 'Bacheha-Ye aseman is a movie starring Mohammad '
                                'Amir Naji, Amir Farrokh Hashemian, and Bahare '
                                "Seddiqi. After a boy loses his sister's pair "
                                'of shoes, he goes on a series of adventures in '
                                "order to find them. When he can't, he tries "
                                'a...',
        'movie_duration': 'PT1H29M',
        'movie_name': 'Bacheha-Ye aseman',
        'movie_rating': '8.2',
        'release_date': '1999-01-22'},
    {'movie_description': 'Ran is a movie starring Tatsuya Nakadai, Akira '
                                'Terao, and Jinpachi Nezu. In Medieval Japan, '
                                'an elderly warlord retires, handing over his '
                                'empire to his three sons. However, he vastly '
                                'underestimates how the new-found power will...',
        'movie_duration': 'PT2H42M',
        'movie_name': 'Ran',
        'movie_rating': '8.2',
        'release_date': '1985-06-01'},
    {'movie_description': 'Unforgiven is a movie starring Clint Eastwood, '
                                'Gene Hackman, and Morgan Freeman. Retired Old '
                                'West gunslinger William Munny reluctantly '
                                'takes on one last job, with the help of his '
                                'old partner Ned Logan and a young man, The '
                                '"Schofield...',
        'movie_duration': 'PT2H10M',
        'movie_name': 'Unforgiven',
        'movie_rating': '8.2',
        'release_date': '1992-08-07'},
    {'movie_description': 'Some Like It Hot is a movie starring Marilyn '
                                'Monroe, Tony Curtis, and Jack Lemmon. After '
                                'two male musicians witness a mob hit, they '
                                'flee the state in an all-female band disguised '
                                'as women, but further complications set in.',
        'movie_duration': 'PT2H1M',
        'movie_name': 'Some Like It Hot',
        'movie_rating': '8.2',
        'release_date': '1959-03-19'},
    {'movie_description': 'Hauru no ugoku shiro is a movie starring '
                                'Chieko Baishô, Takuya Kimura, and Tatsuya '
                                'Gashûin. When an unconfident young woman is '
                                'cursed with an old body by a spiteful witch, '
                                'her only chance of breaking the spell lies '
                                'with a...',
        'movie_duration': 'PT1H59M',
        'movie_name': 'Hauru no ugoku shiro',
        'movie_rating': '8.2',
        'release_date': '2004-11-20'},
    {'movie_description': 'All About Eve is a movie starring Bette Davis, '
                                'Anne Baxter, and George Sanders. A seemingly '
                                'timid but secretly ruthless ingénue insinuates '
                                'herself into the lives of an aging Broadway '
                                'star and her circle of theater friends.',
        'movie_duration': 'PT2H18M',
        'movie_name': 'All About Eve',
        'movie_rating': '8.2',
        'release_date': '1950-10-27'},
    {'movie_description': 'Casino is a movie starring Robert De Niro, '
                                'Sharon Stone, and Joe Pesci. A tale of greed, '
                                'deception, money, power, and murder occur '
                                'between two best friends: a mafia enforcer and '
                                'a casino executive compete against each other '
                                'over a...',
        'movie_duration': 'PT2H58M',
        'movie_name': 'Casino',
        'movie_rating': '8.2',
        'release_date': '1995-11-22'},
    {'movie_description': 'The Wolf of Wall Street is a movie starring '
                                'Leonardo DiCaprio, Jonah Hill, and Margot '
                                'Robbie. Based on the true story of Jordan '
                                'Belfort, from his rise to a wealthy '
                                'stock-broker living the high life to his fall '
                                'involving crime,...',
        'movie_duration': 'PT3H',
        'movie_name': 'The Wolf of Wall Street',
        'movie_rating': '8.2',
        'release_date': '2013-12-25'},
    {'movie_description': 'A Beautiful Mind is a movie starring Russell '
                                'Crowe, Ed Harris, and Jennifer Connelly. After '
                                'John Nash, a brilliant but asocial '
                                'mathematician, accepts secret work in '
                                'cryptography, his life takes a turn for the '
                                'nightmarish.',
        'movie_duration': 'PT2H15M',
        'movie_name': 'A Beautiful Mind',
        'movie_rating': '8.2',
        'release_date': '2002-01-04'},
    {'movie_description': 'The Great Escape is a movie starring Steve '
                                'McQueen, James Garner, and Richard '
                                'Attenborough. Allied prisoners of war plan for '
                                'several hundred of their number to escape from '
                                'a German camp during World War II.',
        'movie_duration': 'PT2H52M',
        'movie_name': 'The Great Escape',
        'movie_rating': '8.2',
        'release_date': '1963-07-04'},
    {'movie_description': 'El laberinto del fauno is a movie starring '
                                'Ivana Baquero, Ariadna Gil, and Sergi López. '
                                'In the Falangist Spain of 1944, the bookish '
                                'young stepdaughter of a sadistic army officer '
                                'escapes into an eerie but captivating fantasy '
                                'world.',
        'movie_duration': 'PT1H58M',
        'movie_name': "Pan's Labyrinth",
        'movie_rating': '8.2',
        'release_date': '2006-10-11'},
    {'movie_description': 'There Will Be Blood is a movie starring Daniel '
                                'Day-Lewis, Paul Dano, and Ciarán Hinds. A '
                                'story of family, religion, hatred, oil and '
                                'madness, focusing on a turn-of-the-century '
                                'prospector in the early days of the business.',
        'movie_duration': 'PT2H38M',
        'movie_name': 'There Will Be Blood',
        'movie_rating': '8.2',
        'release_date': '2008-01-25'},
    {'movie_description': 'El secreto de sus ojos is a movie starring '
                                'Ricardo Darín, Soledad Villamil, and Pablo '
                                'Rago. A retired legal counselor writes a novel '
                                'hoping to find closure for one of his past '
                                'unresolved homicide cases and for his '
                                'unreciprocated...',
        'movie_duration': 'PT2H9M',
        'movie_name': 'El secreto de sus ojos',
        'movie_rating': '8.1',
        'release_date': '2009-08-13'},
    {'movie_description': 'Judgment at Nuremberg is a movie starring '
                                'Spencer Tracy, Burt Lancaster, and Richard '
                                'Widmark. In 1948, an American court in '
                                'occupied Germany tries four Nazis judged for '
                                'war crimes.',
        'movie_duration': 'PT2H59M',
        'movie_name': 'Judgment at Nuremberg',
        'movie_rating': '8.1',
        'release_date': '1961-12-18'},
    {'movie_description': 'Lock, Stock and Two Smoking Barrels is a movie '
                                'starring Jason Flemyng, Dexter Fletcher, and '
                                'Nick Moran. Eddy persuades his three pals to '
                                'pool money for a vital poker game against a '
                                'powerful local mobster, Hatchet Harry. Eddy '
                                'loses,...',
        'movie_duration': 'PT1H47M',
        'movie_name': 'Lock, Stock and Two Smoking Barrels',
        'movie_rating': '8.1',
        'release_date': '1998-08-28'},
    {'movie_description': 'Raging Bull is a movie starring Robert De '
                                'Niro, Cathy Moriarty, and Joe Pesci. The life '
                                'of boxer Jake LaMotta, whose violence and '
                                'temper that led him to the top in the ring '
                                'destroyed his life outside of it.',
        'movie_duration': 'PT2H9M',
        'movie_name': 'Raging Bull',
        'movie_rating': '8.1',
        'release_date': '1980-12-19'},
    {'movie_description': 'Tonari no Totoro is a movie starring Hitoshi '
                                'Takagi, Noriko Hidaka, and Chika Sakamoto. '
                                'When two girls move to the country to be near '
                                'their ailing mother, they have adventures with '
                                'the wondrous forest spirits who live nearby.',
        'movie_duration': 'PT1H26M',
        'movie_name': 'Tonari no Totoro',
        'movie_rating': '8.1',
        'release_date': '1988-04-16'},
    {'movie_description': 'The Treasure of the Sierra Madre is a movie '
                                'starring Humphrey Bogart, Walter Huston, and '
                                'Tim Holt. Two Americans searching for work in '
                                'Mexico convince an old prospector to help them '
                                'mine for gold in the Sierra Madre Mountains.',
        'movie_duration': 'PT2H6M',
        'movie_name': 'The Treasure of the Sierra Madre',
        'movie_rating': '8.1',
        'release_date': '1948-01-24'},
    {'movie_description': 'Dial M for Murder is a movie starring Ray '
                                'Milland, Grace Kelly, and Robert Cummings. A '
                                'former tennis player tries to arrange his '
                                "wife's murder after learning of her affair.",
        'movie_duration': 'PT1H45M',
        'movie_name': 'Dial M for Murder',
        'movie_rating': '8.1',
        'release_date': '1954-05-29'},
    {'movie_description': 'Shutter Island is a movie starring Leonardo '
                                'DiCaprio, Emily Mortimer, and Mark Ruffalo. In '
                                '1954, a U.S. Marshal investigates the '
                                'disappearance of a murderer who escaped from a '
                                'hospital for the criminally insane.',
        'movie_duration': 'PT2H18M',
        'movie_name': 'Shutter Island',
        'movie_rating': '8.1',
        'release_date': '2010-02-18'},
    {'movie_description': 'Three Billboards Outside Ebbing, Missouri is a '
                                'movie starring Frances McDormand, Woody '
                                'Harrelson, and Sam Rockwell. A mother '
                                'personally challenges the local authorities to '
                                "solve her daughter's murder when they fail to "
                                'catch the...',
        'movie_duration': 'PT1H55M',
        'movie_name': 'Three Billboards Outside Ebbing, Missouri',
        'movie_rating': '8.1',
        'release_date': '2017-12-01'},
    {'movie_description': 'The Gold Rush is a movie starring Charles '
                                'Chaplin, Mack Swain, and Tom Murray. A '
                                'prospector goes to the Klondike in search of '
                                'gold and finds it and more.',
        'movie_duration': 'PT1H35M',
        'movie_name': 'The Gold Rush',
        'movie_rating': '8.1',
        'release_date': '1925-07-13'},
    {'movie_description': 'Babam ve Oglum is a movie starring Eser '
                                'Sariyar, Çetin Tekindor, and Fikret Kuskan. '
                                'The family of a left-wing journalist is torn '
                                'apart after the military coup of Turkey in '
                                '1980.',
        'movie_duration': 'PT1H52M',
        'movie_name': 'Babam ve Oglum',
        'movie_rating': '8.1',
        'release_date': '2005-11-18'},
    {'movie_description': 'Chinatown is a movie starring Jack Nicholson, '
                                'Faye Dunaway, and John Huston. A private '
                                'detective hired to expose an adulterer finds '
                                'himself caught up in a web of deceit, '
                                'corruption, and murder.',
        'movie_duration': 'PT2H10M',
        'movie_name': 'Chinatown',
        'movie_rating': '8.1',
        'release_date': '1974-06-20'},
    {'movie_description': 'No Country for Old Men is a movie starring '
                                'Tommy Lee Jones, Javier Bardem, and Josh '
                                'Brolin. Violence and mayhem ensue after a '
                                'hunter stumbles upon a drug deal gone wrong '
                                'and more than two million dollars in cash near '
                                'the Rio Grande.',
        'movie_duration': 'PT2H2M',
        'movie_name': 'No Country for Old Men',
        'movie_rating': '8.1',
        'release_date': '2007-11-21'},
    {'movie_description': 'V for Vendetta is a movie starring Hugo '
                                'Weaving, Natalie Portman, and Rupert Graves. '
                                'In a future British tyranny, a shadowy freedom '
                                'fighter, known only by the alias of "V", plots '
                                'to overthrow it with the help of a young woman.',
        'movie_duration': 'PT2H12M',
        'movie_name': 'V for Vendetta',
        'movie_rating': '8.1',
        'release_date': '2006-03-15'},
    {'movie_description': 'The Thing is a movie starring Kurt Russell, '
                                'Wilford Brimley, and Keith David. A research '
                                'team in Antarctica is hunted by a '
                                'shape-shifting alien that assumes the '
                                'appearance of its victims.',
        'movie_duration': 'PT1H49M',
        'movie_name': 'The Thing',
        'movie_rating': '8.1',
        'release_date': '1982-06-25'},
    {'movie_description': 'Inside Out is a movie starring Amy Poehler, '
                                'Bill Hader, and Lewis Black. After young Riley '
                                'is uprooted from her Midwest life and moved to '
                                'San Francisco, her emotions - Joy, Fear, '
                                'Anger, Disgust and Sadness - conflict on how '
                                'best to...',
        'movie_duration': 'PT1H35M',
        'movie_name': 'Inside Out',
        'movie_rating': '8.1',
        'release_date': '2015-06-17'},
    {'movie_description': 'The Elephant Man is a movie starring Anthony '
                                'Hopkins, John Hurt, and Anne Bancroft. A '
                                'Victorian surgeon rescues a heavily disfigured '
                                'man who is mistreated while scraping a living '
                                'as a side-show freak. Behind his monstrous '
                                'façade,...',
        'movie_duration': 'PT2H4M',
        'movie_name': 'The Elephant Man',
        'movie_rating': '8.1',
        'release_date': '1980-10-10'},
    {'movie_description': 'Det sjunde inseglet is a movie starring Max '
                                'von Sydow, Gunnar Björnstrand, and Bengt '
                                'Ekerot. A man seeks answers about life, death, '
                                'and the existence of God as he plays chess '
                                'against the Grim Reaper during the Black '
                                'Plague.',
        'movie_duration': 'PT1H36M',
        'movie_name': 'Det sjunde inseglet',
        'movie_rating': '8.1',
        'release_date': '1957-02-16'},
    {'movie_description': 'The Sixth Sense is a movie starring Bruce '
                                'Willis, Haley Joel Osment, and Toni Collette. '
                                'A boy who communicates with spirits seeks the '
                                'help of a disheartened child psychologist.',
        'movie_duration': 'PT1H47M',
        'movie_name': 'The Sixth Sense',
        'movie_rating': '8.1',
        'release_date': '1999-08-06'},
    {'movie_description': 'Warrior is a movie starring Tom Hardy, Nick '
                                'Nolte, and Joel Edgerton. The youngest son of '
                                'an alcoholic former boxer returns home, where '
                                "he's trained by his father for competition in "
                                'a mixed martial arts tournament - a path that '
                                'puts...',
        'movie_duration': 'PT2H20M',
        'movie_name': 'Warrior',
        'movie_rating': '8.1',
        'release_date': '2011-09-09'},
    {'movie_description': 'Jurassic Park is a movie starring Sam Neill, '
                                'Laura Dern, and Jeff Goldblum. A pragmatic '
                                'paleontologist visiting an almost complete '
                                'theme park is tasked with protecting a couple '
                                'of kids after a power failure causes the '
                                "park's cloned...",
        'movie_duration': 'PT2H7M',
        'movie_name': 'Jurassic Park',
        'movie_rating': '8.1',
        'release_date': '1993-06-11'},
    {'movie_description': 'Klaus is a movie starring Jason Schwartzman, '
                                'J.K. Simmons, and Rashida Jones. A simple act '
                                'of kindness always sparks another, even in a '
                                "frozen, faraway place. When Smeerensburg's new "
                                'postman, Jesper, befriends toymaker Klaus, '
                                'their...',
        'movie_duration': 'PT1H36M',
        'movie_name': 'Klaus',
        'movie_rating': '8.1',
        'release_date': '2019-11-08'},
    {'movie_description': 'Trainspotting is a movie starring Ewan '
                                'McGregor, Ewen Bremner, and Jonny Lee Miller. '
                                'Renton, deeply immersed in the Edinburgh drug '
                                'scene, tries to clean up and get out, despite '
                                'the allure of the drugs and influence of '
                                'friends.',
        'movie_duration': 'PT1H33M',
        'movie_name': 'Trainspotting',
        'movie_rating': '8.1',
        'release_date': '1996-02-23'},
    {'movie_description': 'The Truman Show is a movie starring Jim '
                                'Carrey, Ed Harris, and Laura Linney. An '
                                'insurance salesman discovers his whole life is '
                                'actually a reality TV show.',
        'movie_duration': 'PT1H43M',
        'movie_name': 'The Truman Show',
        'movie_rating': '8.1',
        'release_date': '1998-06-05'},
    {'movie_description': 'Gone with the Wind is a movie starring Clark '
                                'Gable, Vivien Leigh, and Thomas Mitchell. A '
                                'manipulative woman and a roguish man conduct a '
                                'turbulent romance during the American Civil '
                                'War and Reconstruction periods.',
        'movie_duration': 'PT3H58M',
        'movie_name': 'Gone with the Wind',
        'movie_rating': '8.1',
        'release_date': '1940-01-17'},
    {'movie_description': 'Finding Nemo is a movie starring Albert '
                                'Brooks, Ellen DeGeneres, and Alexander Gould. '
                                'After his son is captured in the Great Barrier '
                                'Reef and taken to Sydney, a timid clownfish '
                                'sets out on a journey to bring him home.',
        'movie_duration': 'PT1H40M',
        'movie_name': 'Finding Nemo',
        'movie_rating': '8.1',
        'release_date': '2003-05-30'},
    {'movie_description': 'Salinui chueok is a movie starring Kang-ho '
                                'Song, Kim Sang-kyung, and Roe-ha Kim. In a '
                                'small Korean province in 1986, two detectives '
                                'struggle with the case of multiple young women '
                                'being found raped and murdered by an unknown '
                                'culprit.',
        'movie_duration': 'PT2H12M',
        'movie_name': 'Salinui chueok',
        'movie_rating': '8.1',
        'release_date': '2003-05-02'},
    {'movie_description': 'Stalker is a movie starring Alisa Freyndlikh, '
                                'Aleksandr Kaydanovskiy, and Anatoliy '
                                'Solonitsyn. A guide leads two men through an '
                                'area known as the Zone to find a room that '
                                'grants wishes.',
        'movie_duration': 'PT2H42M',
        'movie_name': 'Stalker',
        'movie_rating': '8.1',
        'release_date': '1980-04-17'},
    {'movie_description': 'Kill Bill: Vol. 1 is a movie starring Uma '
                                'Thurman, David Carradine, and Daryl Hannah. '
                                'After awakening from a four-year coma, a '
                                'former assassin wreaks vengeance on the team '
                                'of assassins who betrayed her.',
        'movie_duration': 'PT1H51M',
        'movie_name': 'Kill Bill: Vol. 1',
        'movie_rating': '8.1',
        'release_date': '2003-10-10'},
    {'movie_description': 'Smultronstället is a movie starring Victor '
                                'Sjöström, Bibi Andersson, and Ingrid Thulin. '
                                'After living a life marked by coldness, an '
                                'aging professor is forced to confront the '
                                'emptiness of his existence.',
        'movie_duration': 'PT1H31M',
        'movie_name': 'Smultronstället',
        'movie_rating': '8.1',
        'release_date': '1957-12-26'},
    {'movie_description': 'Blade Runner is a movie starring Harrison '
                                'Ford, Rutger Hauer, and Sean Young. A blade '
                                'runner must pursue and terminate four '
                                'replicants who stole a ship in space, and have '
                                'returned to Earth to find their creator.',
        'movie_duration': 'PT1H57M',
        'movie_name': 'Blade Runner',
        'movie_rating': '8.1',
        'release_date': '1982-06-25'},
    {'movie_description': 'Fargo is a movie starring William H. Macy, '
                                'Frances McDormand, and Steve Buscemi. Jerry '
                                "Lundegaard's inept crime falls apart due to "
                                "his and his henchmen's bungling and the "
                                'persistent police work of the quite pregnant '
                                'Marge Gunderson.',
        'movie_duration': 'PT1H38M',
        'movie_name': 'Fargo',
        'movie_rating': '8.1',
        'release_date': '1996-04-05'},
    {'movie_description': 'The Bridge on the River Kwai is a movie '
                                'starring William Holden, Alec Guinness, and '
                                'Jack Hawkins. British POWs are forced to build '
                                'a railway bridge across the river Kwai for '
                                'their Japanese captors, not knowing that the '
                                'allied forces...',
        'movie_duration': 'PT2H41M',
        'movie_name': 'The Bridge on the River Kwai',
        'movie_rating': '8.1',
        'release_date': '1957-10-11'},
    {'movie_description': 'Relatos salvajes is a movie starring Darío '
                                'Grandinetti, María Marull, and Mónica Villa. '
                                'Six short stories that explore the extremities '
                                'of human behavior involving people in distress.',
        'movie_duration': 'PT2H2M',
        'movie_name': 'Relatos salvajes',
        'movie_rating': '8.1',
        'release_date': '2014-08-21'},
    {'movie_description': 'Tôkyô monogatari is a movie starring Chishû '
                                'Ryû, Chieko Higashiyama, and Sô Yamamura. An '
                                'old couple visit their children and '
                                'grandchildren in the city, but receive little '
                                'attention.',
        'movie_duration': 'PT2H16M',
        'movie_name': 'Tôkyô monogatari',
        'movie_rating': '8.1',
        'release_date': '1953-11-03'},
    {'movie_description': 'Gran Torino is a movie starring Clint '
                                'Eastwood, Bee Vang, and Christopher Carley. '
                                'Disgruntled Korean War veteran Walt Kowalski '
                                'sets out to reform his neighbor, Thao Lor, a '
                                "Hmong teenager who tried to steal Kowalski's "
                                'prized...',
        'movie_duration': 'PT1H56M',
        'movie_name': 'Gran Torino',
        'movie_rating': '8.1',
        'release_date': '2009-01-09'},
    {'movie_description': 'Room is a movie starring Brie Larson, Jacob '
                                'Tremblay, and Sean Bridgers. Held captive for '
                                '7 years in an enclosed space, a woman and her '
                                'young son finally gain their freedom, allowing '
                                'the boy to experience the outside world for '
                                'the...',
        'movie_duration': 'PT1H58M',
        'movie_name': 'Room',
        'movie_rating': '8.1',
        'release_date': '2015-12-10'},
    {'movie_description': 'The Third Man is a movie starring Orson '
                                'Welles, Joseph Cotten, and Alida Valli. Pulp '
                                'novelist Holly Martins travels to shadowy, '
                                'postwar Vienna, only to find himself '
                                'investigating the mysterious death of an old '
                                'friend, Harry Lime.',
        'movie_duration': 'PT1H33M',
        'movie_name': 'The Third Man',
        'movie_rating': '8.1',
        'release_date': '1949-10-12'},
    {'movie_description': 'On the Waterfront is a movie starring Marlon '
                                'Brando, Karl Malden, and Lee J. Cobb. An '
                                'ex-prize fighter turned longshoreman struggles '
                                'to stand up to his corrupt union bosses.',
        'movie_duration': 'PT1H48M',
        'movie_name': 'On the Waterfront',
        'movie_rating': '8.1',
        'release_date': '1954-06-22'},
    {'movie_description': 'The Deer Hunter is a movie starring Robert De '
                                'Niro, Christopher Walken, and John Cazale. An '
                                'in-depth examination of the ways in which the '
                                'U.S. Vietnam War impacts and disrupts the '
                                'lives of people in a small industrial town '
                                'in...',
        'movie_duration': 'PT3H3M',
        'movie_name': 'The Deer Hunter',
        'movie_rating': '8.1',
        'release_date': '1979-02-22'},
    {'movie_description': 'In the Name of the Father is a movie starring '
                                'Daniel Day-Lewis, Pete Postlethwaite, and '
                                "Alison Crosbie. A man's coerced confession to "
                                'an I.R.A. bombing he did not commit results in '
                                'the imprisonment of his father as well. An '
                                'English...',
        'movie_duration': 'PT2H13M',
        'movie_name': 'In the Name of the Father',
        'movie_rating': '8.1',
        'release_date': '1993-12-27'},
    {'movie_description': 'Before Sunrise is a movie starring Ethan '
                                'Hawke, Julie Delpy, and Andrea Eckert. A young '
                                'man and woman meet on a train in Europe, and '
                                'wind up spending one evening together in '
                                'Vienna. Unfortunately, both know that this '
                                'will probably...',
        'movie_duration': 'PT1H41M',
        'movie_name': 'Before Sunrise',
        'movie_rating': '8.1',
        'release_date': '1995-01-27'},
    {'movie_description': 'The Grand Budapest Hotel is a movie starring '
                                'Ralph Fiennes, F. Murray Abraham, and Mathieu '
                                'Amalric. A writer encounters the owner of an '
                                'aging high-class hotel, who tells him of his '
                                'early years serving as a lobby boy in the '
                                "hotel's...",
        'movie_duration': 'PT1H39M',
        'movie_name': 'The Grand Budapest Hotel',
        'movie_rating': '8.1',
        'release_date': '2014-02-26'},
    {'movie_description': 'Mary and Max is a movie starring Toni '
                                'Collette, Philip Seymour Hoffman, and Eric '
                                'Bana. A tale of friendship between two '
                                'unlikely pen pals: Mary, a lonely, '
                                'eight-year-old girl living in the suburbs of '
                                'Melbourne, and Max, a...',
        'movie_duration': 'PT1H32M',
        'movie_name': 'Mary and Max',
        'movie_rating': '8.1',
        'release_date': '2009-04-09'},
    {'movie_description': 'Catch Me If You Can is a movie starring '
                                'Leonardo DiCaprio, Tom Hanks, and Christopher '
                                'Walken. Barely 21 yet, Frank is a skilled '
                                'forger who has passed as a doctor, lawyer and '
                                'pilot. FBI agent Carl becomes obsessed with '
                                'tracking down...',
        'movie_duration': 'PT2H21M',
        'movie_name': 'Catch Me If You Can',
        'movie_rating': '8.1',
        'release_date': '2002-12-25'},
    {'movie_description': 'Gone Girl is a movie starring Ben Affleck, '
                                'Rosamund Pike, and Neil Patrick Harris. With '
                                "his wife's disappearance having become the "
                                'focus of an intense media circus, a man sees '
                                "the spotlight turned on him when it's "
                                'suspected that he...',
        'movie_duration': 'PT2H29M',
        'movie_name': 'Gone Girl',
        'movie_rating': '8.1',
        'release_date': '2014-10-01'},
    {'movie_description': 'Hacksaw Ridge is a movie starring Andrew '
                                'Garfield, Sam Worthington, and Luke Bracey. '
                                'World War II American Army Medic Desmond T. '
                                'Doss, who served during the Battle of Okinawa, '
                                'refuses to kill people, and becomes the first '
                                'man in...',
        'movie_duration': 'PT2H19M',
        'movie_name': 'Hacksaw Ridge',
        'movie_rating': '8.1',
        'release_date': '2016-11-03'},
    {'movie_description': 'Prisoners is a movie starring Hugh Jackman, '
                                'Jake Gyllenhaal, and Viola Davis. When Keller '
                                "Dover's daughter and her friend go missing, he "
                                'takes matters into his own hands as the police '
                                'pursue multiple leads and the pressure mounts.',
        'movie_duration': 'PT2H33M',
        'movie_name': 'Prisoners',
        'movie_rating': '8.1',
        'release_date': '2013-09-19'},
    {'movie_description': 'Persona is a movie starring Bibi Andersson, '
                                'Liv Ullmann, and Margaretha Krook. A nurse is '
                                'put in charge of a mute actress and finds that '
                                'their personae are melding together.',
        'movie_duration': 'PT1H23M',
        'movie_name': 'Persona',
        'movie_rating': '8.1',
        'release_date': '1966-10-18'},
    {'movie_description': 'Sherlock Jr. is a movie starring Buster '
                                'Keaton, Kathryn McGuire, and Joe Keaton. A '
                                'film projectionist longs to be a detective, '
                                'and puts his meagre skills to work when he is '
                                'framed by a rival for stealing his '
                                "girlfriend's father's...",
        'movie_duration': 'PT45M',
        'movie_name': 'Sherlock Jr.',
        'movie_rating': '8.1',
        'release_date': '1924-05-11'},
    {'movie_description': 'Andhadhun is a movie starring Ayushmann '
                                'Khurrana, Tabu, and Radhika Apte. A series of '
                                'mysterious events change the life of a blind '
                                'pianist, who must now report a crime that he '
                                'should technically know nothing of.',
        'movie_duration': 'PT2H19M',
        'movie_name': 'Andhadhun',
        'movie_rating': '8.1',
        'release_date': '2018-10-04'},
    {'movie_description': 'The Big Lebowski is a movie starring Jeff '
                                'Bridges, John Goodman, and Julianne Moore. '
                                'Jeff "The Dude" Lebowski, mistaken for a '
                                'millionaire of the same name, seeks '
                                'restitution for his ruined rug and enlists his '
                                'bowling buddies to help...',
        'movie_duration': 'PT1H57M',
        'movie_name': 'The Big Lebowski',
        'movie_rating': '8.1',
        'release_date': '1998-03-06'},
    {'movie_description': "Barry Lyndon is a movie starring Ryan O'Neal, "
                                'Marisa Berenson, and Patrick Magee. An Irish '
                                'rogue wins the heart of a rich widow and '
                                "assumes her dead husband's aristocratic "
                                'position in 18th-century England.',
        'movie_duration': 'PT3H5M',
        'movie_name': 'Barry Lyndon',
        'movie_rating': '8.1',
        'release_date': '1975-12-18'},
    {'movie_description': 'To Be or Not to Be is a movie starring Carole '
                                'Lombard, Jack Benny, and Robert Stack. During '
                                'the Nazi occupation of Poland, an acting '
                                "troupe becomes embroiled in a Polish soldier's "
                                'efforts to track down a German spy.',
        'movie_duration': 'PT1H39M',
        'movie_name': 'To Be or Not to Be',
        'movie_rating': '8.1',
        'release_date': '1942-03-06'},
    {'movie_description': 'The General is a movie starring Buster Keaton, '
                                'Marion Mack, and Glen Cavender. When Union '
                                "spies steal an engineer's beloved locomotive, "
                                'he pursues it single-handedly and straight '
                                'through enemy lines.',
        'movie_duration': 'PT1H7M',
        'movie_name': 'The General',
        'movie_rating': '8.1',
        'release_date': '1927-01-02'},
    {'movie_description': 'Ford v Ferrari is a movie starring Matt Damon, '
                                'Christian Bale, and Jon Bernthal. American car '
                                'designer Carroll Shelby and driver Ken Miles '
                                'battle corporate interference and the laws of '
                                'physics to build a revolutionary race car '
                                'for...',
        'movie_duration': 'PT2H32M',
        'movie_name': 'Ford v Ferrari',
        'movie_rating': '8.1',
        'release_date': '2019-11-13'},
    {'movie_description': 'How to Train Your Dragon is a movie starring '
                                'Jay Baruchel, Gerard Butler, and Christopher '
                                'Mintz-Plasse. A hapless young Viking who '
                                'aspires to hunt dragons becomes the unlikely '
                                'friend of a young dragon himself, and learns '
                                'there may...',
        'movie_duration': 'PT1H38M',
        'movie_name': 'How to Train Your Dragon',
        'movie_rating': '8.1',
        'release_date': '2010-03-18'},
    {'movie_description': '12 Years a Slave is a movie starring Chiwetel '
                                'Ejiofor, Michael Kenneth Williams, and Michael '
                                'Fassbender. In the antebellum United States, '
                                'Solomon Northup, a free black man from upstate '
                                'New York, is abducted and sold into slavery.',
        'movie_duration': 'PT2H14M',
        'movie_name': '12 Years a Slave',
        'movie_rating': '8.1',
        'release_date': '2013-11-08'},
    {'movie_description': 'Eskiya is a movie starring Sener Sen, Ugur '
                                'Yücel, and Sermin Hürmeriç. Baran the Bandit, '
                                'released from prison after 35 years, searches '
                                'for vengeance and his lover.',
        'movie_duration': 'PT2H8M',
        'movie_name': 'Eskiya',
        'movie_rating': '8.1',
        'release_date': '1996-11-29'},
    {'movie_description': 'Mr. Smith Goes to Washington is a movie '
                                'starring James Stewart, Jean Arthur, and '
                                'Claude Rains. A naive man is appointed to fill '
                                'a vacancy in the United States Senate. His '
                                'plans promptly collide with political '
                                'corruption, but he...',
        'movie_duration': 'PT2H9M',
        'movie_name': 'Mr. Smith Goes to Washington',
        'movie_rating': '8.1',
        'release_date': '1939-10-19'},
    {'movie_description': 'Höstsonaten is a movie starring Ingrid '
                                'Bergman, Liv Ullmann, and Lena Nyman. A '
                                "married daughter who longs for her mother's "
                                'love is visited by the latter, a successful '
                                'concert pianist.',
        'movie_duration': 'PT1H39M',
        'movie_name': 'Höstsonaten',
        'movie_rating': '8.1',
        'release_date': '1978-10-08'},
    {'movie_description': 'Mad Max: Fury Road is a movie starring Tom '
                                'Hardy, Charlize Theron, and Nicholas Hoult. In '
                                'a post-apocalyptic wasteland, a woman rebels '
                                'against a tyrannical ruler in search for her '
                                'homeland with the aid of a group of female...',
        'movie_duration': 'PT2H',
        'movie_name': 'Mad Max: Fury Road',
        'movie_rating': '8.1',
        'release_date': '2015-05-13'},
    {'movie_description': 'Dead Poets Society is a movie starring Robin '
                                'Williams, Robert Sean Leonard, and Ethan '
                                'Hawke. Maverick teacher John Keating uses '
                                'poetry to embolden his boarding school '
                                'students to new heights of self-expression.',
        'movie_duration': 'PT2H8M',
        'movie_name': 'Dead Poets Society',
        'movie_rating': '8.1',
        'release_date': '1989-06-09'},
    {'movie_description': 'Million Dollar Baby is a movie starring Hilary '
                                'Swank, Clint Eastwood, and Morgan Freeman. A '
                                'determined woman works with a hardened boxing '
                                'trainer to become a professional.',
        'movie_duration': 'PT2H12M',
        'movie_name': 'Million Dollar Baby',
        'movie_rating': '8.1',
        'release_date': '2004-12-15'},
    {'movie_description': 'Harry Potter and the Deathly Hallows: Part 2 '
                                'is a movie starring Daniel Radcliffe, Emma '
                                'Watson, and Rupert Grint. Harry, Ron, and '
                                "Hermione search for Voldemort's remaining "
                                'Horcruxes in their effort to destroy the Dark '
                                'Lord as the...',
        'movie_duration': 'PT2H10M',
        'movie_name': 'Harry Potter and the Deathly Hallows: Part 2',
        'movie_rating': '8.1',
        'release_date': '2011-07-12'},
    {'movie_description': 'Ben-Hur is a movie starring Charlton Heston, '
                                'Jack Hawkins, and Stephen Boyd. After a Jewish '
                                'prince is betrayed and sent into slavery by a '
                                'Roman friend, he regains his freedom and comes '
                                'back for revenge.',
        'movie_duration': 'PT3H32M',
        'movie_name': 'Ben-Hur',
        'movie_rating': '8.1',
        'release_date': '1959-11-18'},
    {'movie_description': 'Stand by Me is a movie starring Wil Wheaton, '
                                'River Phoenix, and Corey Feldman. After the '
                                'death of one of his friends, a writer recounts '
                                'a childhood journey with his friends to find '
                                'the body of a missing boy.',
        'movie_duration': 'PT1H29M',
        'movie_name': 'Stand by Me',
        'movie_rating': '8.1',
        'release_date': '1986-08-22'},
    {'movie_description': 'Network is a movie starring Faye Dunaway, '
                                'William Holden, and Peter Finch. A television '
                                'network cynically exploits a deranged former '
                                "anchor's ravings and revelations about the "
                                'news media for its own profit.',
        'movie_duration': 'PT2H1M',
        'movie_name': 'Network',
        'movie_rating': '8.1',
        'release_date': '1976-11-27'},
    {'movie_description': "Hachi: A Dog's Tale is a movie starring "
                                'Richard Gere, Joan Allen, and Cary-Hiroyuki '
                                'Tagawa. A college professor bonds with an '
                                'abandoned dog he takes into his home.',
        'movie_duration': 'PT1H33M',
        'movie_name': "Hachi: A Dog's Tale",
        'movie_rating': '8.1',
        'release_date': '2009-08-08'},
    {'movie_description': 'Ah-ga-ssi is a movie starring Kim Min-hee, '
                                'Jung-woo Ha, and Cho Jin-woong. A woman is '
                                'hired as a handmaiden to a Japanese heiress, '
                                'but secretly she is involved in a plot to '
                                'defraud her.',
        'movie_duration': 'PT2H25M',
        'movie_name': 'Ah-ga-ssi',
        'movie_rating': '8.1',
        'release_date': '2016-06-01'},
    {'movie_description': 'Cool Hand Luke is a movie starring Paul '
                                'Newman, George Kennedy, and Strother Martin. A '
                                'laid back Southern man is sentenced to two '
                                'years in a rural prison, but refuses to '
                                'conform.',
        'movie_duration': 'PT2H7M',
        'movie_name': 'Cool Hand Luke',
        'movie_rating': '8.1',
        'release_date': '1967-11-01'},
    {'movie_description': 'Logan is a movie starring Hugh Jackman, '
                                'Patrick Stewart, and Dafne Keen. In a future '
                                'where mutants are nearly extinct, an elderly '
                                'and weary Logan leads a quiet life. But when '
                                'Laura, a mutant child pursued by scientists, '
                                'comes to him...',
        'movie_duration': 'PT2H17M',
        'movie_name': 'Logan',
        'movie_rating': '8.1',
        'release_date': '2017-02-28'},
    {'movie_description': 'Anand is a movie starring Rajesh Khanna, '
                                'Amitabh Bachchan, and Sumita Sanyal. The story '
                                'of a terminally ill man who wishes to live '
                                'life to the fullest before the inevitable '
                                'occurs, as told by his best friend.',
        'movie_duration': 'PT2H2M',
        'movie_name': 'Anand',
        'movie_rating': '8.0',
        'release_date': '1971-03-12'},
    {'movie_description': 'Platoon is a movie starring Charlie Sheen, Tom '
                                'Berenger, and Willem Dafoe. Chris Taylor, a '
                                'neophyte recruit in Vietnam, finds himself '
                                'caught in a battle of wills between two '
                                'sergeants, one good and the other evil. A '
                                'shrewd...',
        'movie_duration': 'PT2H',
        'movie_name': 'Platoon',
        'movie_rating': '8.0',
        'release_date': '1987-02-06'},
    {'movie_description': 'Le salaire de la peur is a movie starring Yves '
                                'Montand, Charles Vanel, and Peter van Eyck. In '
                                'a decrepit South American village, four men '
                                'are hired to transport an urgent '
                                'nitroglycerine shipment without the equipment '
                                'that would make...',
        'movie_duration': 'PT2H11M',
        'movie_name': 'Le salaire de la peur',
        'movie_rating': '8.0',
        'release_date': '1953-04-22'},
    {'movie_description': 'Rush is a movie starring Daniel Brühl, Chris '
                                'Hemsworth, and Olivia Wilde. The merciless '
                                '1970s rivalry between Formula One rivals James '
                                'Hunt and Niki Lauda.',
        'movie_duration': 'PT2H3M',
        'movie_name': 'Rush',
        'movie_rating': '8.0',
        'release_date': '2013-09-12'},
    {'movie_description': 'Into the Wild is a movie starring Emile '
                                'Hirsch, Vince Vaughn, and Catherine Keener. '
                                'After graduating from Emory University, top '
                                'student and athlete Christopher McCandless '
                                'abandons his possessions, gives his entire '
                                '$24,000 savings...',
        'movie_duration': 'PT2H28M',
        'movie_name': 'Into the Wild',
        'movie_rating': '8.0',
        'release_date': '2007-09-28'},
    {'movie_description': 'La haine is a movie starring Vincent Cassel, '
                                'Hubert Koundé, and Saïd Taghmaoui. 24 hours in '
                                'the lives of three young men in the French '
                                'suburbs the day after a violent riot.',
        'movie_duration': 'PT1H38M',
        'movie_name': 'La haine',
        'movie_rating': '8.0',
        'release_date': '1995-05-31'},
    {'movie_description': 'Les quatre cents coups is a movie starring '
                                'Jean-Pierre Léaud, Albert Rémy, and Claire '
                                'Maurier. A young boy, left without attention, '
                                'delves into a life of petty crime.',
        'movie_duration': 'PT1H39M',
        'movie_name': 'Les quatre cents coups',
        'movie_rating': '8.0',
        'release_date': '1959-06-03'},
    {'movie_description': "La passion de Jeanne d'Arc is a movie starring "
                                'Maria Falconetti, Eugene Silvain, and André '
                                "Berley. In 1431, Jeanne d'Arc is placed on "
                                'trial on charges of heresy. The ecclesiastical '
                                'jurists attempt to force Jeanne to recant '
                                'her...',
        'movie_duration': 'PT1H54M',
        'movie_name': "La passion de Jeanne d'Arc",
        'movie_rating': '8.0',
        'release_date': '1928-04-21'},
    {'movie_description': 'Life of Brian is a movie starring Graham '
                                'Chapman, John Cleese, and Michael Palin. Born '
                                'on the original Christmas in the stable next '
                                'door to Jesus Christ, Brian of Nazareth spends '
                                'his life being mistaken for a messiah.',
        'movie_duration': 'PT1H34M',
        'movie_name': 'Life of Brian',
        'movie_rating': '8.0',
        'release_date': '1979-08-17'},
    {'movie_description': 'Spotlight is a movie starring Mark Ruffalo, '
                                'Michael Keaton, and Rachel McAdams. The true '
                                'story of how the Boston Globe uncovered the '
                                'massive scandal of child molestation and '
                                'cover-up within the local Catholic '
                                'Archdiocese, shaking...',
        'movie_duration': 'PT2H9M',
        'movie_name': 'Spotlight',
        'movie_rating': '8.0',
        'release_date': '2015-11-20'},
    {'movie_description': 'Hotel Rwanda is a movie starring Don Cheadle, '
                                'Sophie Okonedo, and Joaquin Phoenix. Paul '
                                'Rusesabagina, a hotel manager, houses over a '
                                'thousand Tutsi refugees during their struggle '
                                'against the Hutu militia in Rwanda, Africa.',
        'movie_duration': 'PT2H1M',
        'movie_name': 'Hotel Rwanda',
        'movie_rating': '8.0',
        'release_date': '2005-01-20'},
    {'movie_description': 'Gangs of Wasseypur is a movie starring Manoj '
                                'Bajpayee, Richa Chadha, and Nawazuddin '
                                'Siddiqui. A clash between Sultan and Shahid '
                                'Khan leads to the expulsion of Khan from '
                                'Wasseypur, and ignites a deadly blood feud '
                                'spanning three...',
        'movie_duration': 'PT5H21M',
        'movie_name': 'Gangs of Wasseypur',
        'movie_rating': '8.0',
        'release_date': '2012-06-22'},
    {'movie_description': 'Amores perros is a movie starring Emilio '
                                'Echevarría, Gael García Bernal, and Goya '
                                'Toledo. A horrific car accident connects three '
                                'stories, each involving characters dealing '
                                "with loss, regret, and life's harsh realities, "
                                'all in the...',
        'movie_duration': 'PT2H34M',
        'movie_name': 'Amores perros',
        'movie_rating': '8.0',
        'release_date': '2000-06-16'},
    {'movie_description': 'Monsters, Inc. is a movie starring Billy '
                                'Crystal, John Goodman, and Mary Gibbs. In '
                                'order to power the city, monsters have to '
                                'scare children so that they scream. However, '
                                'the children are toxic to the monsters, and '
                                'after a child gets...',
        'movie_duration': 'PT1H32M',
        'movie_name': 'Monsters, Inc.',
        'movie_rating': '8.0',
        'release_date': '2001-11-02'},
    {'movie_description': 'Rocky is a movie starring Sylvester Stallone, '
                                'Talia Shire, and Burt Young. A small-time '
                                'boxer gets a supremely rare chance to fight a '
                                'heavyweight champion in a bout in which he '
                                'strives to go the distance for his '
                                'self-respect.',
        'movie_duration': 'PT2H',
        'movie_name': 'Rocky',
        'movie_rating': '8.0',
        'release_date': '1976-12-03'},
    {'movie_description': 'Andrey Rublev is a movie starring Anatoliy '
                                'Solonitsyn, Ivan Lapikov, and Nikolay Grinko. '
                                'The life, times and afflictions of the '
                                'fifteenth-century Russian iconographer St. '
                                'Andrei Rublev.',
        'movie_duration': 'PT3H25M',
        'movie_name': 'Andrei Rublev',
        'movie_rating': '8.0',
        'release_date': '1971-12-24'},
    {'movie_description': 'Kaze no tani no Naushika is a movie starring '
                                'Sumi Shimamoto, Mahito Tsujimura, and Hisako '
                                'Kyôda. Warrior and pacifist Princess Nausicaä '
                                'desperately struggles to prevent two warring '
                                'nations from destroying themselves and their '
                                'dying...',
        'movie_duration': 'PT1H57M',
        'movie_name': 'Kaze no tani no Naushika',
        'movie_rating': '8.0',
        'release_date': '1984-03-11'},
    {'movie_description': 'Soul is a movie starring Jamie Foxx, Tina Fey, '
                                'and Graham Norton. After landing the gig of a '
                                'lifetime, a New York jazz pianist suddenly '
                                'finds himself trapped in a strange land '
                                'between Earth and the afterlife.',
        'movie_duration': 'PT1H40M',
        'movie_name': 'Soul',
        'movie_rating': '8.0',
        'release_date': '2020-12-24'},
    {'movie_description': 'Rebecca is a movie starring Laurence Olivier, '
                                'Joan Fontaine, and George Sanders. A '
                                'self-conscious woman juggles adjusting to her '
                                "new role as an aristocrat's wife and avoiding "
                                "being intimidated by his first wife's spectral "
                                'presence.',
        'movie_duration': 'PT2H10M',
        'movie_name': 'Rebecca',
        'movie_rating': '8.0',
        'release_date': '1940-04-12'},
    {'movie_description': 'Before Sunset is a movie starring Ethan Hawke, '
                                'Julie Delpy, and Vernon Dobtcheff. Nine years '
                                'after Jesse and Celine first met, they '
                                'encounter each other again on the French leg '
                                "of Jesse's book tour.",
        'movie_duration': 'PT1H20M',
        'movie_name': 'Before Sunset',
        'movie_rating': '8.0',
        'release_date': '2004-06-17'},
    {'movie_description': 'Fa yeung nin wah is a movie starring Tony '
                                'Chiu-Wai Leung, Maggie Cheung, and Ping Lam '
                                'Siu. Two neighbors, a woman and a man, form a '
                                'strong bond after both suspect extramarital '
                                'activities of their spouses. However, they '
                                'agree to keep...',
        'movie_duration': 'PT1H38M',
        'movie_name': 'Fa yeung nin wah',
        'movie_rating': '8.0',
        'release_date': '2000-09-29'},
    {'movie_description': 'Dom za vesanje is a movie starring Davor '
                                'Dujmovic, Bora Todorovic, and Ljubica Adzovic. '
                                'In this luminous tale set in the area around '
                                'Sarajevo and in Italy, Perhan, an engaging '
                                'young Romany (gypsy) with telekinetic powers, '
                                'is seduced...',
        'movie_duration': 'PT2H22M',
        'movie_name': 'Dom za vesanje',
        'movie_rating': '8.0',
        'release_date': '1989-11-15'},
    {'movie_description': 'Rang De Basanti is a movie starring Aamir '
                                'Khan, Soha Ali Khan, and Siddharth. The story '
                                'of six young Indians who assist an English '
                                'woman to film a documentary on the freedom '
                                'fighters from their past, and the events that '
                                'lead them to...',
        'movie_duration': 'PT2H47M',
        'movie_name': 'Rang De Basanti',
        'movie_rating': '8.0',
        'release_date': '2006-01-26'},
    {'movie_description': 'Paris, Texas is a movie starring Harry Dean '
                                'Stanton, Nastassja Kinski, and Dean Stockwell. '
                                'Travis Henderson, an aimless drifter who has '
                                'been missing for four years, wanders out of '
                                'the desert and must reconnect with society, '
                                'himself,...',
        'movie_duration': 'PT2H25M',
        'movie_name': 'Paris, Texas',
        'movie_rating': '8.0',
        'release_date': '1984-08-23'},
    {'movie_description': 'Du rififi chez les hommes is a movie starring '
                                'Jean Servais, Carl Möhner, and Robert Manuel. '
                                'Four men plan a technically perfect crime, but '
                                'the human element intervenes...',
        'movie_duration': 'PT1H58M',
        'movie_name': 'Du rififi chez les hommes',
        'movie_rating': '8.0',
        'release_date': '1955-04-13'},
    {'movie_description': 'Ratsasan is a movie starring Vishnu Vishal, '
                                'Amala Paul, and Radha Ravi. A sub-inspector '
                                'sets out in pursuit of a mysterious serial '
                                'killer who targets teen school girls and '
                                'murders them brutally.',
        'movie_duration': 'PT2H50M',
        'movie_name': 'Ratsasan',
        'movie_rating': '8.0',
        'release_date': '2018-10-05'},
    {'movie_description': 'Drishyam is a movie starring Mohanlal, Meena, '
                                'and Asha Sharath. A man goes to extreme '
                                'lengths to save his family from punishment '
                                'after the family commits an accidental crime.',
        'movie_duration': 'PT2H40M',
        'movie_name': 'Drishyam',
        'movie_rating': '8.0',
        'release_date': '2013-12-19'},
    {'movie_description': 'Portrait de la jeune fille en feu is a movie '
                                'starring Noémie Merlant, Adèle Haenel, and '
                                'Luàna Bajrami. On an isolated island in '
                                'Brittany at the end of the eighteenth century, '
                                'a female painter is obliged to paint a wedding '
                                'portrait...',
        'movie_duration': 'PT2H2M',
        'movie_name': 'Portrait de la jeune fille en feu',
        'movie_rating': '8.0',
        'release_date': '2019-09-18'},
    {'movie_description': 'It Happened One Night is a movie starring '
                                'Clark Gable, Claudette Colbert, and Walter '
                                'Connolly. A renegade reporter and a crazy '
                                'young heiress meet on a bus heading for New '
                                'York, and end up stuck with each other when '
                                'the bus leaves...',
        'movie_duration': 'PT1H45M',
        'movie_name': 'It Happened One Night',
        'movie_rating': '8.0',
        'release_date': '1934-02-22'},
    {'movie_description': 'Mandariinid is a movie starring Lembit Ulfsak, '
                                'Elmo Nüganen, and Giorgi Nakashidze. In 1992, '
                                'war rages in Abkhazia, a breakaway region of '
                                'Georgia. An Estonian man Ivo has decided to '
                                'stay behind and harvest his crops of '
                                'tangerines....',
        'movie_duration': 'PT1H27M',
        'movie_name': 'Mandariinid',
        'movie_rating': '8.0',
        'release_date': '2013-10-17'},
    {'movie_description': 'Drishyam is a movie starring Ajay Devgn, '
                                'Shriya Saran, and Tabu. Desperate measures are '
                                'taken by a man who tries to save his family '
                                'from the dark side of the law, after they '
                                'commit an unexpected crime.',
        'movie_duration': 'PT2H43M',
        'movie_name': 'Drishyam',
        'movie_rating': '8.0',
        'release_date': '2015-07-30'},
    {'movie_description': 'La battaglia di Algeri is a movie starring '
                                'Brahim Hadjadj, Jean Martin, and Yacef Saadi. '
                                'In the 1950s, fear and violence escalate as '
                                'the people of Algiers fight for independence '
                                'from the French government.',
        'movie_duration': 'PT2H1M',
        'movie_name': 'La battaglia di Algeri',
        'movie_rating': '8.0',
        'release_date': '1966-09-09'},
    {'movie_description': 'Swades: We, the People is a movie starring '
                                'Shah Rukh Khan, Gayatri Joshi, and Kishori '
                                'Ballal. A successful Indian scientist returns '
                                'to an Indian village to take his nanny to '
                                'America with him and in the process '
                                'rediscovers his roots.',
        'movie_duration': 'PT3H9M',
        'movie_name': 'Swades: We, the People',
        'movie_rating': '8.0',
        'release_date': '2004-12-17'},
    {'movie_description': 'Koe no katachi is a movie starring Miyu Irino, '
                                'Saori Hayami, and Aoi Yûki. A young man is '
                                'ostracized by his classmates after he bullies '
                                'a deaf girl to the point where she moves away. '
                                'Years later, he sets off on a path for '
                                'redemption.',
        'movie_duration': 'PT2H10M',
        'movie_name': 'Koe no katachi',
        'movie_rating': '8.0',
        'release_date': '2016-09-17'}
    ]

    for movie in movie_data_list:
        movie_obj = Movie.objects.create(name=movie['movie_name'], description=movie['movie_description'],
            rating = movie['movie_rating'], release_date=movie['release_date'], duration=movie['movie_duration']
        )        

