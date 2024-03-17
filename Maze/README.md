Problems like solving a maze can be solved through search algorithms such as depth-first search and breadth-first search algorithms.

Search problems have a set of initial set of:
* Initial State
* Actions
* Transition Model
* Goal Test
* Path Cost Function

## Approach
General approach taken to solve search problems is given below. Here frontier is going to represent all the available options (path to goal test) that have not been explored or visited yet.
1. Start with a frontier that contains the initial state
2. Repeat
   1. If frontier is empty, then no solution
   2. Remove a node from the frontier
   3. If node contains goal state, return solution
   4. Expand the node, add resulting nodes to the frontier
      To expand a node means to look at all of the neighbouring nodes of that nodes.

## Algorithms
Algorithms can be of two types:
1. **Uninformed Search**:
   A search strategy that uses no problem-specific knowledge.
   For example, depth-first search and breadth-first search
2. **Informed Search**:
   A search strategy that uses problem-specific knowledge to find solutions more efficiently.
   For example, greedy best-first search

### Depth-First Search
The search traversal in depth-first search is implemented through stack.
It starts at the root node and explores as far as possible along each branch before backtracking. The search begins from the first node and goes deeper and deeper exploring down until the goal test is found. If the goal test is not found, the search path is changed to the path that was stopped exploring during the initial search, same procedure is repeated for that branch.

### Breadth-First Search
Queue is used for implementing breadth-first search. 
It navigates in a breadth motion and utilizes based on queue to jump from one node to another, after encountering an end in the path. All the nodes present in the same level are traversed completely before exploring the next level.

### Greedy Best-First Search
It is a search algorithm that expands the node that is closest to the gaol, as estimated by a heuristic function h(n).

### A* Search
It is an advanced model of greedy best-first search that expands node with the lowest value of g(n)+h(n),
where g(n)=cost to reach node
      h(n)=estimated cost to the goal

## Files
- maze.py contains general code for traversing through the maze, using both depth-first and breadth-first algorithms.
- maze1.txt contains an example of an unsolved maze where A is the initial point, B is the goal and # represents walls.
- usingBFS.py is specifically programmed to solve the problem using breadth-first algorithm.
- Similarly, usingDFS.py is specifically programmed to solve the problem using depth-first algorithm.
