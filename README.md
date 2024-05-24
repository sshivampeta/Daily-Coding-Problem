# Daily Coding Problem Solutions

A collection of daily coding problem solutions in Python, covering various algorithmic challenges and data structure problems.

## 📚 Contents

### 1. **Binary Tree Traversal** (`Binary_tree_traversal.py`)
**Problem:** Serialize and deserialize a binary tree  
**Description:** Convert a binary tree to/from a string representation while preserving structure.

**Key Functions:**
- `serialize(root)` - Converts tree to comma-separated string using depth-first search
- `deserialize(s)` - Reconstructs tree from serialized string

**Includes:**
- Node class for binary tree representation
- Comprehensive test cases covering edge cases
- Logging for debugging

**Time Complexity:** O(n) for both operations  
**Space Complexity:** O(n) for the result string

---

### 2. **Height-Balanced Binary Tree** (`Brinary_tree.py`)
**Problem:** Determine if a binary tree is height-balanced  
**Definition:** A tree is height-balanced if heights of subtrees of any node never differ by more than 1.

**Two Solutions Provided:**

#### Solution 1: Optimized O(n) Approach ⭐ (Recommended)
- `is_balanced(root)` - Single-pass check with early termination
- **Time Complexity:** O(n)
- **Space Complexity:** O(h) where h is height

#### Solution 2: Simple Recursive Approach
- `is_balanced_simple(root)` - More intuitive but less efficient
- **Time Complexity:** O(n²) - recalculates heights
- **Space Complexity:** O(h)

**Test Cases Included:**
- Balanced multi-level tree
- Unbalanced linear chain
- Single node tree
- Empty tree
- Complex scenarios

---

### 3. **Two-Number Sum** (`Problem01.py`)
**Problem:** Given a list of numbers and a number k, return whether any two numbers add up to k.

**Example:** `[10, 15, 3, 7]` with k=17 returns `True` (10 + 7 = 17)

**Four Solutions Provided:**

#### 1. One-Pass Hash Set ⭐ (Optimal - Bonus Solution)
- `has_pair_one_pass(nums, k)`
- **Time:** O(n), **Space:** O(n)
- Single pass through the list
- Early return when pair found

#### 2. Two-Pass Hash Map
- `has_pair_two_pass(nums, k)`
- Explicitly handles duplicate numbers
- Checks counts before confirming pairs

#### 3. Two Pointers (Sorting)
- `has_pair_two_pointers(nums, k)`
- **Time:** O(n log n), **Space:** O(1)
- Requires pre-sorted array

#### 4. Brute Force
- `has_pair_bruteforce(nums, k)`
- **Time:** O(n²), **Space:** O(1)
- All possible pairs comparison

**Features:**
- Logging throughout for debugging
- Edge case handling
- Detailed commenting

---

### 4. **Product Array** (`Problem02.py`)
**Problem:** For each element in an array, return the product of all other elements (without using division).

**Three Solutions Provided:**

#### 1. Using Division (with zero handling)
- `product_with_division(nums)`
- Handles edge cases with zero values
- Uses division when possible

#### 2. Prefix + Suffix Arrays (No Division)
- `product_prefix_suffix(nums)`
- Builds prefix and suffix arrays
- **Time:** O(n), **Space:** O(n)

#### 3. Optimized (No Division, O(1) Extra Space)
- `product_optimized(nums)`
- Space-efficient approach
- Single result array with two passes
- **Time:** O(n), **Space:** O(1)

**Features:**
- Detailed logging for each step
- Prefix/suffix visualization
- Handles edge cases (empty arrays, zeros)

---

### 5. **Partition Array** (`array_of_number.py`)
**Problem:** Split an array into k partitions such that the maximum sum of any partition is minimized.

**Example:** `[5, 1, 2, 7, 3, 4]` with k=3 returns `8`, with partitions `[5, 1, 2]`, `[7]`, `[3, 4]`

**Three Solutions Provided:**

#### 1. Binary Search + Greedy ⭐ (Optimal)
- `partition_array_binary_search(N, k)` 
- **Time:** O(n × log(sum(N)))
- **Space:** O(1)
- Search for minimum possible maximum sum
- Greedy validation for each candidate

#### 2. Dynamic Programming
- `partition_array_dp(N, k)`
- **Time:** O(n² × k)
- **Space:** O(n × k)
- `dp[i][j]` = min max sum for first i elements in j partitions
- Considers all possible partition boundaries

#### 3. Greedy with Backtracking
- `partition_array_greedy(N, k)`
- **Time:** O(n × log(sum(N)))
- **Space:** O(k)
- Similar to binary search but with detailed partition tracking
- Visualizes final partition result

**Key Insights:**
- Answer is bounded: [max(N), sum(N)]
- Binary search reduces problem to validation
- Greedy validation: process left-to-right, fill partitions greedily
- Edge cases: k=1, k>=n

**Test Cases Include:**
- Given example and variations
- Single element array
- Single partition (k=1)
- Each element in own partition (k>=n)
- Duplicate values

---

### 6. **Full Binary Tree Conversion** (`rebalance_tree.py`)
**Problem:** Convert a binary tree to a full binary tree by removing nodes with only one child.

**Definition:** A full binary tree is one where each node is either a leaf or has two children.

**Example:**
```
Original:           Converted:
     0                  0
   /   \              /   \
  1     2            5     4
 /       \                /  \
3         4              6    7
 \       / \
  5     6   7
```

**Three Solutions Provided:**

#### 1. Recursive Post-Order Traversal ⭐ (Optimal)
- `prune_tree(root)`
- **Time:** O(n)
- **Space:** O(h) where h is height
- Process children before parent (post-order)
- Return child if node has only one child, return node if leaf or both children exist

#### 2. Iterative Post-Order Traversal
- `prune_tree_iterative(root)`
- **Time:** O(n)
- **Space:** O(h)
- Uses two stacks for post-order traversal
- Alternative to recursion for avoiding stack overflow

#### 3. Recursive with Verbose Tracking
- `prune_tree_verbose(root)`
- **Time:** O(n)
- **Space:** O(h)
- Tracks removed node count
- Enhanced logging for understanding pruning process

**Key Insights:**
- Post-order traversal essential (process children first)
- Nodes are "removed" by returning child references
- Leaf nodes are always preserved (0 children = full)
- Parent-child references updated during traversal

**Test Cases Include:**
- Given example from problem
- Single node tree
- Already full binary tree
- Chain tree (all single children)
- Complex mixed structure

**Utility Functions:**
- `tree_to_list_bfs(root)` - Level-order representation
- `print_tree(root)` - Pretty-print tree structure
- `create_example_tree()` - Build problem example

---

### 7. **Find Cousins in Binary Tree** (`binary_tree_find_cousins.py`)
**Problem:** Find all cousins of a given node in a binary tree.

**Definition:** Two nodes are cousins if they are on the same level of the tree but have different parents.

**Example:**
```
    1          In this tree, 4 and 6 are cousins
   / \         (same level, different parents)
  2   3        5 and 6 are also cousins
 / \   \
4   5   6
```

**Four Solutions Provided:**

#### 1. BFS Level-Order Traversal ⭐ (Optimal)
- `find_cousins_bfs(root, target)`
- **Time:** O(n)
- **Space:** O(w) - where w is maximum width of tree
- Track parent of each node during BFS
- Find target's level and parent, return nodes at same level with different parent

#### 2. DFS with Parent Tracking
- `find_cousins_dfs(root, target)`
- **Time:** O(n)
- **Space:** O(h) - recursive call stack
- Two passes: find target depth/parent, then collect cousins
- Clean separation of concerns

#### 3. Single Pass DFS (Optimized)
- `find_cousins_single_pass(root, target)`
- **Time:** O(n)
- **Space:** O(h)
- Single DFS traversal with depth tracking
- Maps depth to list of (node, parent) tuples

#### 4. BFS with Early Termination
- `find_cousins_bfs_optimized(root, target)`
- **Time:** O(n) worst case
- **Space:** O(w)
- Attempt to optimize by stopping after target level

**Key Insights:**
- Cousins must be on same level (depth/height)
- Different parent is the defining characteristic
- Level-order traversal naturally groups nodes by level
- Parent tracking is crucial for differentiation
- Handle edge cases: root node, non-existent node, single node tree

**Test Cases Include:**
- Given example with multiple cousin pairs
- Deep tree with asymmetric structure
- Single node tree (no cousins)
- Linear tree (right-only chain)
- Node not found in tree

**Utility Functions:**
- `print_tree(root)` - Pretty-print tree structure
- `create_example_tree()` - Build problem example

---

### 8. **Maximum XOR** (`find_max_xor.py`)
**Problem:** Find the maximum XOR of any two elements in an array.

**Example:** Array `[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]`  
Maximum XOR: 83 ^ 36 = 123

**Four Solutions Provided:**

#### 1. Bit Manipulation with Trie ⭐ (Optimal)
- `max_xor_trie(nums)`
- **Time:** O(n × 32) = O(n)
- **Space:** O(n × 32) = O(n)
- Build trie of binary representations (32-bit integers)
- For each number, traverse trie greedily picking opposite bits
- Opposite bits maximize XOR value

#### 2. Bit Manipulation with Set (No Trie)
- `max_xor_set(nums)`
- **Time:** O(n × 32) = O(n)
- **Space:** O(n)
- Build answer bit by bit from MSB to LSB
- For each bit, try to set it to 1 and check if achievable
- Use set for O(1) prefix lookup

#### 3. Brute Force
- `max_xor_bruteforce(nums)`
- **Time:** O(n²)
- **Space:** O(1)
- Try all pairs and compute XOR
- Straightforward but slow for large arrays

#### 4. Greedy Bit Building
- `max_xor_greedy(nums)`
- **Time:** O(n × 32) = O(n)
- **Space:** O(n)
- Similar to set approach but more explicit
- Build result bit by bit with prefix masking

**Key Insights:**
- XOR is maximized when bits differ as much as possible
- Working from MSB (most significant bit) ensures maximum value
- For each bit position, try to set it; verify with prefixes
- Trie approach elegantly matches opposite bits for each number
- Set approach uses mathematical property: `a ^ b = c` ⟹ `a ^ c = b`

**Important Property:**
- If we want `a ^ b = result`, and we know `result ^ a = b`
- So for each bit, we try `temp = current_result | (1 << i)`
- Then check if `temp ^ prefix_a = prefix_b` for some prefixes

**Test Cases Include:**
- Given example with various numbers
- Simple arrays (powers of 2, sequential numbers)
- Edge cases (single element, two elements)
- Arrays with zeros
- Binary representation tracing

**Utility Functions:**
- `print_binary(num)` - 32-bit binary representation
- `trace_xor_pair(nums, target_xor)` - Find which pair gives max XOR

---

## 🚀 Usage

### Running Individual Solutions

```bash
# Run serialization/deserialization tests
python Binary_tree_traversal.py

# Run height-balanced tree tests
python Brinary_tree.py

# Run two-number sum examples
python Problem01.py

# Run product array examples
python Problem02.py

# Run partition array examples
python array_of_number.py

# Run full binary tree conversion tests
python rebalance_tree.py

# Run find cousins in tree tests
python binary_tree_find_cousins.py

# Run maximum XOR tests
python find_max_xor.py
```

### Example Usage in Code

```python
from Brinary_tree import is_balanced, Node

# Create a balanced tree
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(is_balanced(root))  # True
```

```python
from Problem01 import has_pair_one_pass

nums = [10, 15, 3, 7]
k = 17

print(has_pair_one_pass(nums, k))  # True
```

---

## 📊 Complexity Comparison

| Problem | Solution | Time | Space | Notes |
|---------|----------|------|-------|-------|
| Tree Serialization | DFS | O(n) | O(n) | Best approach |
| Height-Balanced | Optimized | O(n) | O(h) | ⭐ Recommended |
| Height-Balanced | Simple | O(n²) | O(h) | More intuitive |
| Two-Sum | Hash Set | O(n) | O(n) | ⭐ Best (one-pass) |
| Two-Sum | Two Pointers | O(n log n) | O(1) | If sorting allowed |
| Two-Sum | Brute Force | O(n²) | O(1) | Baseline |
| Product Array | Optimized | O(n) | O(1) | ⭐ Best |
| Product Array | Prefix+Suffix | O(n) | O(n) | Extra clarity |
| Partition Array | Binary Search | O(n log S) | O(1) | ⭐ Optimal |
| Partition Array | Dynamic Programming | O(n²k) | O(nk) | All boundaries |
| Partition Array | Greedy | O(n log S) | O(k) | Visualizes result |
| Full Binary Tree | Post-Order Recursive | O(n) | O(h) | ⭐ Optimal |
| Full Binary Tree | Iterative | O(n) | O(h) | Stack-based alternative |
| Full Binary Tree | Verbose | O(n) | O(h) | Enhanced logging |
| Find Cousins | BFS Level-Order | O(n) | O(w) | ⭐ Optimal approach |
| Find Cousins | DFS Parent Tracking | O(n) | O(h) | Two-pass clean |
| Find Cousins | Single Pass DFS | O(n) | O(h) | Depth-mapped |
| Find Cousins | BFS Optimized | O(n) | O(w) | Early termination |
| Max XOR | Trie Approach | O(n) | O(n) | ⭐ Optimal |
| Max XOR | Set Approach | O(n) | O(n) | Bit-by-bit building |
| Max XOR | Brute Force | O(n²) | O(1) | All pairs |
| Max XOR | Greedy Bits | O(n) | O(n) | Explicit approach |

---

## 🔍 Key Concepts Covered

- **Binary Trees:** Serialization, balance checking, tree traversal, tree pruning, tree conversion, cousin finding, level-based queries
- **Hash Tables:** One-pass algorithms, complement lookups
- **Two Pointers:** Sorted array manipulation
- **Prefix/Suffix Arrays:** Space-efficient computation
- **Binary Search:** Answer space search, optimization problems
- **Dynamic Programming:** Multi-dimensional DP, boundary optimization
- **Greedy Algorithms:** Partition filling, early termination
- **Tree Traversal:** Pre-order, in-order, post-order, level-order (BFS), depth tracking
- **Parent Tracking:** Finding relationships in tree structures
- **Bit Manipulation:** Trie structures, bit-by-bit construction, XOR optimization
- **Trie Data Structure:** Binary trie, prefix matching, bit representation
- **Logging:** Debugging and algorithm visualization
- **Edge Cases:** Empty inputs, duplicates, zeros, k constraints, single nodes, non-existent nodes

---

## 💡 Learning Path

1. Start with **Problem01** - Understanding hash-based optimizations
2. Move to **Binary_tree_traversal** - Graph/tree concepts
3. Then **Brinary_tree** - Optimization techniques
4. Continue with **Problem02** - Advanced array manipulation
5. Study **array_of_number** - Binary search and optimization
6. Progress to **rebalance_tree** - Tree transformation and pruning
7. Next **binary_tree_find_cousins** - Level-based tree queries
8. Finish with **find_max_xor** - Bit manipulation and Trie structures

---

## 📝 Notes

- All solutions include comprehensive test cases
- Logging is enabled to trace algorithm execution
- Multiple approaches shown for comparison and learning
- Edge cases are explicitly tested

---

## 📌 Problem Source

These are daily coding problems, typically from sites like:
- Daily Coding Problem
- LeetCode
- Interview preparation platforms

Each problem includes the original problem statement as docstrings.

---

## 🛠️ Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## 📄 License

Educational purposes - Solutions and explanations for learning

---

**Last Updated:** April 10, 2026  
**Status:** Active development  
**Total Problems:** 8
