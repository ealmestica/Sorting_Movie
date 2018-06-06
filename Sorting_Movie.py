# SNHU - CS200
# Elijah Almestica
# Program name: Sorting Movie

# Dictionary of movie collection
Movie_Collection = {
  1:[2005, 'Munich','Steven Spielberg'],
  2:[2006, 'The Prestige','Christopher Nolan' ],
  3:[2006, 'The Departed', 'Martin Scorsese'],
  4:[2007, 'Into the Wild', 'Sean Penn'],
  5:[2008, 'The Dark Knight', 'Christopher Nolan'],
  6:[2009, 'Mary and Max', 'Adam Elliot'],
  7:[2010, "The King's Speech", 'Tom Hooper'],
  8:[2011, 'The Artist', 'Michel Hazanavicius'],
  9:[2011,'The Help', 'Tate Taylor'],
  10:[2012, 'Argo', 'Ben Affleck'],
  11:[2013, '12 Years a Slave','Steve McQueen'],
  12:[2014, 'Birdman','Alejandro G. Inarritu'],
  13:[2015, 'Spotlight','Tom McCarthy'],
  14:[2016, 'The BFG','Steven Spielberg'],
}

prompt = int(input('Enter a year between 2005 and 2016:\n'))

while (not (2004 < prompt < 2017)):
  print ("N/A")
  prompt = int(input('Enter a year between 2005 and 2016:\n'))

for key, movies in Movie_Collection.items():
  if prompt ==  movies[0]:
    print (movies[1]+", "+movies[2])
 
# Initial List
movie_list = list(Movie_Collection.values())


user_choice = 's'

while user_choice != "q":
  print ("\nMENU")
  print ("Sort by:")
  print ("y - Year")
  print ("d - Director")
  print ("t - Movie title")
  print ("q - Quit")

  user_choice = input('\nChoose an option:')

  # User Chose y  
  if user_choice == 'y':
    prev_years =[]
    for movie in Movie_Collection.values():
      if movie[0] in prev_years:
        print ("\t"+movie[1]+", "+movie[2])
      else:  
        print ("\n"+str(movie[0])+":")
        print ("\t"+movie[1]+", "+movie[2])
      prev_years.append (movie[0])
  
  # User Chose d
  elif user_choice == 'd':
    def sort_director(x): # sort by director
      return x[2]
  
    # prints list sorted by director
    sorted_director = sorted(movie_list, key=sort_director)
    prev_directors = []
    for director in sorted_director:
      if director[2] in prev_directors:
        print ("\t"+director[1]+", "+str(director[0]))
      else:
        print ("\n"+director[2]+":")
        print ("\t"+director[1]+", "+str(director[0]))
      prev_directors.append (director[2])
    
  # User Chose t
  elif user_choice == 't':
    def sort_title(x):  # sort by title
      return x[1]
    
    # prints list sorted by title
    sorted_title = sorted(movie_list, key=sort_title)  
    for title in sorted_title:
      print ("\n"+title[1]+":")  
      print ("\t"+title[2]+", "+str(title[0]))
print ()
