''' Defines the set P = {1 ... 25} and the set  Q = {5, 7, 9 ... 19}. '''
P, Q = { i for i in range (1, 26) }, { (2 * j) + 1 for j in range (2, 10) }           

''' Checks if a predicate is true for any x, given a set and a predicate as parameters. 
The predicate must be a function that returns either true or false based on a condition. '''
existential = lambda predicate, set : True if any (map (predicate, set)) == True else False

''' Checks if a predicate is true for all x, given a set and a predicate as parameters. 
The predicate must be a function that returns either true or false based on a condition. '''
universal = lambda predicate, set : True if all (map (predicate, set)) == True else False

''' Checks if ∃x ∈ ϕ, H(x), where H(x) ≔ (2 < x < 19) and ϕ = P ∩ Q & outputs result. '''
print (f'∃x ∈ ϕ, H(x): {existential (lambda x : True if 2 < x < 19 else False, P.intersection (Q))}')

''' Checks if ∀x ∈ ϕ, H(x), where H(x) ≔ (2 < x < 19) and ϕ = P ∩ Q & outputs result. '''
print (f'∀x ∈ ϕ, H(x): {universal (lambda x : True if 2 < x < 19 else False, P.intersection (Q))}')