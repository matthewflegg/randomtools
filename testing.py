from tools import *

def testing ():
    
    # Some random functions 
    square = lambda a: a ** 2
    half = lambda a: a / 2
    
    # TESTING PIPE ON A SINGLE VALUE   
    print (pipe (5, square, half)) # Should return 12.5
    
    # TESTING PIPE ON LISTS, SETS & TUPLES
    print (pipe_iterable ([5, 7, 9], square, half)) # Should return 12.5, 24.5, 40.5 in an ordered list
    print (pipe_iterable ({5, 7, 9}, square, half)) # Should return 12.5, 24.5, 40.5 in an unordered list
    print (pipe_iterable ((5, 7, 9), square, half)) # Should return 12.5, 24.5, 40.5 in an ordered list
    
    # TESTING LOGICAL QUANTIFIERS
    print (existential (lambda x: True if x == 50 else False, [34, 56, 32, 76])) # Should return false
    print (universal (lambda x: True if x == 50 else False, [50, 50, 50, 50, 50])) # Should return true
    
    # Defines the set P = {1, 2, 3 ... 25} and the set  Q = {5, 7, 9 ... 19}
    P, Q = { i for i in range (1, 26) }, { (2 * j) + 1 for j in range (2, 10) }   
    print (existential (lambda x : True if 2 < x < 19 else False, P.intersection (Q))) # Should return true
    print (universal (lambda x : True if 2 < x < 19 else False, P.intersection (Q))) # Should return false
    
    # TESTING QUANTIFIERS + PIPE
    dataset = [10, 58, 23, 15, 92]    
    print (existential (lambda x: True if x == 50 else False, pipe_iterable (dataset, square, half))) # Should return true
    print (universal (lambda x: True if x == 50 else False, pipe_iterable (dataset, square, half))) # Should return false
    
    # TESTING INTEGRAL TOOLS
    print (integrate (3, 9, lambda a : (a ** 2) + (5 * a) + 6, accuracy = 1500))
    print (integrate (2, 8, lambda n : (n ** 2) + (5 * n) + 6))
    
    # TESTING GRAPH CLASS
    adj = {
        'A' : ['B', 'C'],
        'B' : ['A', 'D'],
        'C' : ['A', 'D'],
        'D' : ['E'],
        'E' : ['D']
    }
    
    # Test __init__
    g = Graph (adj)

    # Test edges & vertices
    print (g.GetVertices ())
    print (g.GetEdges ())

    # Test add vertex
    g.AddVertex ('F')
    print (g.GetVertices ())

    # Test add edge 
    g.AddEdge ({'E', 'F'})
    g.AddEdge ({'D', 'F'})
    print (g.GetEdges ())