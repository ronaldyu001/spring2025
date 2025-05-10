# HW5

## Q1

### a) Explain Algorithm

- In order to determine a safe sequence in which to apply patches to the servers, a topological sort using DFS can be used.
- A list of visited nodes and an empty stack to contain the resulting topological order will be needed.
- The DFS will start at a node, and do DFS from that node. Every time a node is visited, add it to the visited list. Once a node is reached that has no neighbors, add it to the stack and backtrack to the previous node, checking again for neighbors. If it has unvisited neighbors, do DFS on those with backtracking.
- After doing this for all the nodes, pop the stack and that is the list of nodes in topological order, which is safe to use to apply patches.


### b) Psuedocode

#### Initialize Variables

- Initialize an empty list for visited nodes and empty stack for the topological order.

#### Perform Topological Sort

- For each node in the graph (choose starting node),

  - If it is not visited,
    - Do DFS.

#### Perform DFS (called for each node for topological sort)

- For each neighbor of the node,

  - If it is not visited,
    - Recursively do DFS.
- Add node to the stack.

#### Return Topological Order

- Pop stack to get topological.


### c) Potential Problems and Solutions

#### Network Infrastructure Size

- If there are too many servers (nodes), Stack Overflow may occur due to too many recursive calls being made.
- To solve this, an iterative method could be applied.

#### Topological Sort Limitations

- In order to use Topological Sort, the target must be a Directed Acyclic Graph.
- To solve this, check for back edges during DFS and return an error to address the cycle.
- Check if graph is directed before attempting topological sort. If it is not directed, topological sort is not possible.


### d) Halt Algorithm

- The overall algorithm will be the same.
- However, add these when doing DFS:
  - If node is pre-specified and has already been patched,
    - Return error addressing this.

#### Challenges

- If the topological sort halts when a pre-specified target server is reached, the patch will be left incomplete.


### e) Load-Based Patching Psuedocode

#### Initialize Variables

- Initialize an empty list for visited nodes and empty stack for the topological order.
- Initialize a float for threshold activity and list for skipped nodes.

#### Perform Topological Sort

- For each node in the graph (choose starting node),

  - If it is not visited,
    - Do DFS.

#### Perform DFS (called for each node for topological sort)

- For each neighbor of the node,

  - If it is not visited,
    - Recursively do DFS.
  - if the the node load is more than the threshold,
    - Skip the node by returning and add it to skipped list.
- Add node to the stack.

#### Return Topological Order

- Pop the stack.

#### Attempt Patching Later

- After patching the nodes returned in topological order,
  - Go back through the list of skipped nodes,
    - If it is under the threshold,
      - Patch and remove from skipped.
    - Else,
      - Do nothing.

#### Keep Attempting Patching

- While skipped list not empty,
  - Keep coming back to the list of skipped nodes periodically.
  - For each node in the list of skipped nodes,
    - If load is under the threshold,
      - Patch and removed from skipped.
    - Else,
      - Do nothing.


## Q2)

### 2-1) California vs Carolina

#### 1) LCS

No arrows means diagonal to the top left, except for 0s.

|             |   | C   | A         | L         | I         | F         | O         | R         | N         | I         | A         |
| ----------- | - | --- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
|             | 0 | 0   | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| **C** | 0 | 1   | 1<br /><- | 1<br /><- | 1<br /><- | 1<br /><- | 1<br /><- | 1<br /><- | 1<br /><- | 1<br /><- | 1<br /><- |
| **A** | 0 | 1 ^ | 2         | 2<br /><- | 2<br /><- | 2<br /><- | 2<br /><- | 2<br /><- | 2<br /><- | 2<br /><- | 2         |
| **R** | 0 | 1 ^ | 2 ^       | 2 ^       | 2 ^       | 2 ^       | 2 ^       | 3         | 3<br /><- | 3<br /><- | 3<br /><- |
| **O** | 0 | 1 ^ | 2 ^       | 2 ^       | 2 ^       | 2 ^       | 3         | 3<br /><- | 3<br /><- | 3<br /><- | 3<br /><- |
| **L** | 0 | 1 ^ | 2 ^       | 3         | 3<br /><- | 3<br /><- | 3 ^       | 3 ^       | 3 ^       | 3 ^       | 3 ^       |
| **I** | 0 | 1 ^ | 2 ^       | 3 ^       | 4         | 4<br /><- | 4<br /><- | 4<br /><- | 4<br /><- | 4         | 4<br /><- |
| **N** | 0 | 1 ^ | 2 ^       | 3 ^       | 4 ^       | 4<br /><- | 4<br /><- | 4<br /><- | 5         | 5<br /><- | 5<br /><- |
| **A** | 0 | 1 ^ | 2         | 3 ^       | 4 ^       | 4 ^       | 4 ^       | 4 ^       | 5 ^       | 5 ^       | 6         |

Answer: CALINA

#### 2) Minimum Edit Distance

|             |   | C | A | L | I | F | O | R | N | I | A  |
| ----------- | - | - | - | - | - | - | - | - | - | - | -- |
|             | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| **C** | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  |
| **A** | 2 | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8  |
| **R** | 3 | 2 | 1 | 1 | 2 | 3 | 4 | 4 | 5 | 6 | 7  |
| **O** | 4 | 3 | 2 | 2 | 2 | 3 | 3 | 4 | 5 | 6 | 7  |
| **L** | 5 | 4 | 3 | 2 | 3 | 3 | 4 | 4 | 5 | 6 | 7  |
| **I** | 6 | 5 | 4 | 3 | 2 | 3 | 4 | 5 | 5 | 5 | 6  |
| **N** | 7 | 6 | 5 | 4 | 3 | 3 | 4 | 5 | 5 | 6 | 6  |
| **A** | 8 | 7 | 6 | 5 | 4 | 4 | 4 | 5 | 6 | 6 | 6  |

Answer: 6


### 2-2)

#### Question

Why is Dynamic Programming (DP) generally considered impractical for solving the Bin Packing Problem in real-world scenarios? Support your reasoning by discussing how the problem conflicts with the two main characteristics of dynamic programming approaches discussed in the class.

#### Answer

The Bin Packing Problem has two issues for DP:

- Item placement can be metaphorically compared to a timeline. When you change one event early on, it can lead to completely different events occuring after that. For instance, let's say the first item A is placed into Bin 1 and the rest are filled. Compared to if the first item A is placed into Bin 2, the resulting contents of Bin 1 and Bin 2 can be drasticaly different depending on where the first item A was placed. This means the subproblems may not sufficiently overlap, making it less useful to store past scenarios.
  - This violates the property of Overlapping Subproblems.
- Additionally, by choosing the most optimal solution for each subproblem, this doesn't necessariy lead to the global best. For instance, just by choosing the optimal item to place at each step, doesn't mean that the overall result is optimal. In this case, the goal is to fill the bins as close to their capacity as possible. But selecting an optimal item early on may lead to bad pairings for the other items later on.
  - This violates the property of Optimal Substructure


## 3)

### Output

Suggestions for "hey":
No suggestions available.

Suggestions for "we":
No suggestions available.

Suggestions for "are":
No suggestions available.

Suggestions for "all":
No suggestions available.

Suggestions for "homan":
Word: woman, Edit Distance: 1, Frequency: 325
Word: human, Edit Distance: 1, Frequency: 170
Word: coman, Edit Distance: 1, Frequency: 17
Word: roman, Edit Distance: 1, Frequency: 8
Word: man, Edit Distance: 2, Frequency: 1652
Word: women, Edit Distance: 2, Frequency: 390
Word: home, Edit Distance: 2, Frequency: 295

Suggestions for "and":
No suggestions available.

Suggestions for "in":
No suggestions available.

Suggestions for "spote":
Word: spoke, Edit Distance: 1, Frequency: 218
Word: spite, Edit Distance: 1, Frequency: 117
Word: spot, Edit Distance: 1, Frequency: 76
Word: spots, Edit Distance: 1, Frequency: 12
Word: smote, Edit Distance: 1, Frequency: 4
Word: spore, Edit Distance: 1, Frequency: 3
Word: some, Edit Distance: 2, Frequency: 1536

Suggestions for "of":
No suggestions available.

Suggestions for "our":
No suggestions available.

Suggestions for "belst":
Word: best, Edit Distance: 1, Frequency: 268
Word: beast, Edit Distance: 1, Frequency: 26
Word: belt, Edit Distance: 1, Frequency: 12
Word: felt, Edit Distance: 2, Frequency: 697
Word: west, Edit Distance: 2, Frequency: 286
Word: rest, Edit Distance: 2, Frequency: 209
Word: else, Edit Distance: 2, Frequency: 201

Suggestions for "effrts":
Word: efforts, Edit Distance: 1, Frequency: 103
Word: effort, Edit Distance: 2, Frequency: 130
Word: effects, Edit Distance: 2, Frequency: 82
Word: forts, Edit Distance: 2, Frequency: 8
Word: exerts, Edit Distance: 2, Frequency: 3
Word: effete, Edit Distance: 2, Frequency: 1
Word: parts, Edit Distance: 3, Frequency: 296

Suggestions for "sometimes":
No suggestions available.

Suggestions for "speling":
Word: spelling, Edit Distance: 1, Frequency: 4
Word: feeling, Edit Distance: 2, Frequency: 362
Word: seeing, Edit Distance: 2, Frequency: 207
Word: speaking, Edit Distance: 2, Frequency: 185
Word: swelling, Edit Distance: 2, Frequency: 167
Word: smiling, Edit Distance: 2, Frequency: 161
Word: opening, Edit Distance: 2, Frequency: 146

Suggestions for "mistakes":
No suggestions available.

Suggestions for "happen":
No suggestions available.

Suggestions for "nobody":
No suggestions available.

Suggestions for "is":
No suggestions available.

Suggestions for "perrfect":
Word: perfect, Edit Distance: 1, Frequency: 39
Word: prefect, Edit Distance: 2, Frequency: 2
Word: project, Edit Distance: 3, Frequency: 288
Word: effect, Edit Distance: 3, Frequency: 187
Word: perfectly, Edit Distance: 3, Frequency: 45
Word: protect, Edit Distance: 3, Frequency: 41
Word: correct, Edit Distance: 3, Frequency: 38

Suggestions for "most":
No suggestions available.

Suggestions for "of":
No suggestions available.

Suggestions for "the":
No suggestions available.

Suggestions for "time":
No suggestions available.

Suggestions for "your":
No suggestions available.

Suggestions for "avorage":
Word: average, Edit Distance: 1, Frequency: 18
Word: voyage, Edit Distance: 2, Frequency: 12
Word: forage, Edit Distance: 2, Frequency: 7
Word: storage, Edit Distance: 2, Frequency: 3
Word: averages, Edit Distance: 2, Frequency: 1
Word: averaged, Edit Distance: 2, Frequency: 1
Word: george, Edit Distance: 3, Frequency: 150

Suggestions for "typo":
Word: type, Edit Distance: 1, Frequency: 87
Word: to, Edit Distance: 2, Frequency: 28766
Word: two, Edit Distance: 2, Frequency: 1138
Word: too, Edit Distance: 2, Frequency: 548
Word: top, Edit Distance: 2, Frequency: 42
Word: types, Edit Distance: 2, Frequency: 33
Word: tips, Edit Distance: 2, Frequency: 16

Suggestions for "or":
No suggestions available.

Suggestions for "misspeling":
Word: missing, Edit Distance: 3, Frequency: 28
Word: misspelled, Edit Distance: 3, Frequency: 1
Word: listening, Edit Distance: 4, Frequency: 89
Word: kissing, Edit Distance: 4, Frequency: 38
Word: whispering, Edit Distance: 4, Frequency: 19
Word: disputing, Edit Distance: 4, Frequency: 12
Word: mingling, Edit Distance: 4, Frequency: 11

Suggestions for "does":
No suggestions available.

Suggestions for "not":
No suggestions available.

Suggestions for "really":
No suggestions available.

Suggestions for "amount":
No suggestions available.

Suggestions for "to":
No suggestions available.

Suggestions for "mlch":
Word: much, Edit Distance: 1, Frequency: 671
Word: such, Edit Distance: 2, Frequency: 1436
Word: each, Edit Distance: 2, Frequency: 411
Word: march, Edit Distance: 2, Frequency: 135
Word: rich, Edit Distance: 2, Frequency: 92
Word: match, Edit Distance: 2, Frequency: 41
Word: mack, Edit Distance: 2, Frequency: 22

Suggestions for "but":
No suggestions available.

Suggestions for "sometimes":
No suggestions available.

Suggestions for "when":
No suggestions available.

Suggestions for "you":
No suggestions available.

Suggestions for "use":
No suggestions available.

Suggestions for "twitter":
No suggestions available.

Suggestions for "those":
No suggestions available.

Suggestions for "mistkes":
Word: mistakes, Edit Distance: 1, Frequency: 15
Word: mistaken, Edit Distance: 2, Frequency: 59
Word: mistake, Edit Distance: 2, Frequency: 39
Word: mistress, Edit Distance: 2, Frequency: 24
Word: mister, Edit Distance: 2, Frequency: 2
Word: misses, Edit Distance: 2, Frequency: 2
Word: mists, Edit Distance: 2, Frequency: 1

Suggestions for "can":
No suggestions available.

Suggestions for "come":
No suggestions available.

Suggestions for "back":
No suggestions available.

Suggestions for "to":
No suggestions available.

Suggestions for "hauunt":
Word: haunt, Edit Distance: 1, Frequency: 2
Word: aunt, Edit Distance: 2, Frequency: 52
Word: hunt, Edit Distance: 2, Frequency: 31
Word: gaunt, Edit Distance: 2, Frequency: 5
Word: taunt, Edit Distance: 2, Frequency: 1
Word: hand, Edit Distance: 3, Frequency: 834
Word: count, Edit Distance: 3, Frequency: 748

Suggestions for "you":
No suggestions available.

Suggestions for "like":
No suggestions available.

Suggestions for "the":
No suggestions available.

Suggestions for "lingering":
No suggestions available.

Suggestions for "odoor":
Word: door, Edit Distance: 1, Frequency: 498
Word: odour, Edit Distance: 1, Frequency: 20
Word: odor, Edit Distance: 1, Frequency: 6
Word: poor, Edit Distance: 2, Frequency: 129
Word: floor, Edit Distance: 2, Frequency: 106
Word: doors, Edit Distance: 2, Frequency: 47
Word: doom, Edit Distance: 2, Frequency: 6

Suggestions for "of":
No suggestions available.

Suggestions for "man":
No suggestions available.

Suggestions for "colone":
Word: colonel, Edit Distance: 1, Frequency: 143
Word: colony, Edit Distance: 1, Frequency: 57
Word: colon, Edit Distance: 1, Frequency: 9
Word: cologne, Edit Distance: 1, Frequency: 3
Word: alone, Edit Distance: 2, Frequency: 337
Word: close, Edit Distance: 2, Frequency: 219
Word: colonies, Edit Distance: 2, Frequency: 207
