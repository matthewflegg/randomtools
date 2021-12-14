''' Checks if a predicate is true for any x, given a set and a predicate as parameters. 
The predicate must be a function that returns either true or false based on a condition. '''
existential = lambda predicate, set : True if any (map (predicate, set)) == True else False

''' Checks if a predicate is true for all x, given a set and a predicate as parameters. 
The predicate must be a function that returns either true or false based on a condition. '''
universal = lambda predicate, set : True if all (map (predicate, set)) == True else False