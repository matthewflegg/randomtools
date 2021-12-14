from functools import reduce

def pipe_iterable (data, *functions): 
    
    ''' Takes a variable/object and any amount of functions as
        arguments. Processes a value through a chain of functions, 
        passing the result of the previous one into the next one. '''
    
    return list (map (lambda data: pipe (data, *functions), data))
    
''' 1. [a, *f] puts a at the start of a list, 
    and unpacks all of the functions in f.

    2. Reduce assigns the first value in the
    list, g the value of a. It assigns the second, 
    h the value of the first function. 

    3. It evaluates the function applied to the 
    expression, the result gets assigned to g. 
    The second function then gets assigned to h. 

    3. Repeats step 2 until it can't continue, 
    then returns the result. '''

pipe = lambda a, *f: reduce (lambda g, h: h (g), [a, *f])

        

    
    
    
    

