from copy import deepcopy
    
def pass_by_value (function):
    
    ''' Decorator that takes a function as a parameter.
    It copies the parameters, and calls the original
    function using the copied parameters. 
    
    Emulates passing by value. '''
    
    def copy (*args):
        
        ''' Copies the parameters of the decorated function.
        Places them all in a new list, called *cargs (copied
        aruments), and calls decorated function using *cargs. '''
            
        cargs = [deepcopy (arg) for arg in args]
        return function (*cargs)
    
    return copy 

@pass_by_value
def pipe (data, *functions): 
    
    ''' Takes a variable/object and any amount of functions as
    arguments. Processes a value through a chain of functions, 
    passing the result of the previous one into the next one. '''
    
    def pipe_value (value, *functions):
    
        ''' Takes a single value and any amount of functions as
        arguments. Processes a value through a chain of functions, 
        passing the result of the previous one into the next one. '''
        
        for function in functions:
            value = function (value)
            
        return value

    if isinstance (data, list) or isinstance (data, set) or isinstance (data, tuple):
        return [pipe (value, *functions) for value in data]
    
    else: return pipe_value (data, *functions)
        

    
    
    
    

