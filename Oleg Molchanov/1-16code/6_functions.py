"""#movie = 'The good, the bad, and the ugly'
#rating = 100
#result = f'Movie: "{movie}", rating: {rating}'
#print(result)


#movie = 'Alien'
#rating = 200
#result = f'Movie: "{movie}", rating: {rating}'
#print(result)
greeting = 'Hello'
to = 'world'

def greet(message, name='world'):
    #print('Hello', name)
    result = f'{message}, {name}'
    return result
    #print(result)

#g = greet('Hello', name='asdf')

# message = greetin = 'hello'

g = greet('                    hello').title().strip()
print(g)
"""

#movie = 'Friends'
#rating = 998

def rating_movie(movie, rating = 998):
    result = f'"{movie}, {rating}'
    return result
    
#g = greet('Hello', name='asdf')

# message = greetin = 'hello'

g = rating_movie('Friends').upper()
print(g)