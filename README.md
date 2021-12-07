# randomtools
randomtools

Just to specify, these aren't RNG tools. They're tools that are random 

So far, it includes: 

- Pipe function, similar to F#'s pipe operator
- Existential quantifiers for first order logic
- A numerical integration tools

Documentation/Instructions:

---PIPE FUNCTION---

What does it do? It takes a variable or object, and 'pipes' it through a bunch of functions. 
It calls the first function on the data, then feeds the result to the next, and keeps doing that
until it's been fed through the last function. Then it returns the result. 

Syntax: 
- pipe (data, *functions)
- Example: pipe ([6, 8], lambda x: x / 3, lambda x: x + 1) -> Output: [4, 5]

Params:
- data: Can be any variable. Not fully tested yet.
- functions: A bunch of functions. Include as many as you want, just make sure they're after 'data'

Notes:
- Uses a decorator to mimic the behaviour of passing by value. So it doesn't change the params it's called with
- Data is 'piped' through the functions in the order they're listed.

---QUANTIFIERS---

What does it do? It checks if a condition is true for any or for all items in a set. 'existential' returns
true if at least one item in a collection returns true for the condition, and 'universal' returns true if all 
items in a collection return true for the condition.

Syntax:
- universal (condition, collection)
- existential (condition, collection)
- Example: existential (lambda x: x == 5, {6, 3, 5, 7, 8}) -> Output: True

Params:
- condition: Any function that returns either true or false
- collection: A set, list, tuple or dictionary

---INTEGRATION---

Syntax:
- integrate (lower, upper, func, accuracy = 500)
- Example: print (integrate (2, 8, func = lambda n : (n ** 2) + (5 * n) + 6)) -> Output: 352.68165513598973

Params: 
- lower: The lower bound of the integral
- upper: The upper bound of the integral
- func: The function to integrate
- accuracy: The amount of 'slices' to split the area to find into 

Notes:
- The higher the accuracy, the better the approximation will be 
- Using a multi-variable function will break the program, I haven't added error handling yet lol









