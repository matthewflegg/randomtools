# randomtools
randomtools

Just to specify, these aren't RNG tools. They're tools that are random 

So far, it includes: 

- Pipe function, similar to F#'s pipe operator
- Existential quantifiers for first order logic
- A numerical integration function
- A graph class using adjacency lists

Documentation/Instructions:

---PIPE FUNCTION---

What does it do? It takes a variable or object, and 'pipes' it through a bunch of functions. 
It calls the first function on the data, then feeds the result to the next, and keeps doing that
until it's been fed through the last function. Then it returns the result. 

Syntax: 
- pipe (data, *functions)
- Example: pipe (8, lambda x: x / 3, lambda x: x + 1) -> Output: [4, 5]

Params:
- data: Can be any non-iterable variable. See notes for info about how to chain over an iterable. 
- functions: A bunch of functions. Include as many as you want, just make sure they're after 'data'

Notes:
- Data is 'piped' through the functions in the order they're listed.
- As of 14.12.21, you cannot chain an iterable without allowing for the functions passed into it to handle iterables.
- Instead, you can use pipe_iterable (data, *functions). It's the same syntax, except data is an iterable object.
- pipe pipes a single var, and returns the result. pipe_iterable basically just does that for each item in an iterable. It DOESN'T pass the iterable 
  into any of the functions.
 
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

--GRAPH CLASS METHODS--

> Constructor

Syntax:
- G = Graph (AdjDict)
- Example: 

adjDict = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['E'], 'E': ['D']}
G = Graph (adjDict)

Params:
- AdjDict: A dictionary containing the vertices as keys, and the values as a list of vertices that vertex is adjacent to 

> GetVertices ()

An instance method that returns a list of vertices. 
Literally just list (self.adj.keys ()) lol ;)

Syntax:
- object.GetVertices ()
- Example: print (G.GetVertices ()) -> Output: ['A', 'B', 'C', 'D', 'E']

Params: 
- None 

> GetEdges ()

An instance method that returns a list of edges, which are represented as sets. 
A set contains two vertices that have an edge between them.

Syntax:
- object.GetEdges ()
- Example: print (G.GetEdges ()) -> Output: [{'B', 'A'}, {'C', 'A'}, {'B', 'D'}, {'D', 'C'}. {'E', 'D'}]

Params:
- None

> AddVertex ()

Instance method that adds a vertex to the adjacency list.

Syntax:
- object.AddVertex (vertex)
- Example: 

G.AddVertex ('F')
print (g.GetVertices ()) -> Output: ['A', 'B', 'C', 'D', 'E', 'F']

Params:
= vertex: the name of the vertex.

> AddEdge ()

Instance method that adds an edge to the adjacency dict.

Syntax:
- object.AddEdge (edge)
- Example:

G.AddEdge ({'E', 'F'})
G.AddEdge ({'D', 'F'})
print (G.GetEdges ()) -> Output: [{'B', 'A'}, {'C', 'A'}, {'B', 'D'}, {'D', 'C'}, {'E', 'D'}, {'E', 'F'}, {'F', 'D'}]

Params:
- edge (set): a set containing the two vertices the edge connects.
