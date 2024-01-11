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

---

## 🔍 Key Concepts Covered

- **Binary Trees:** Serialization, balance checking, tree traversal
- **Hash Tables:** One-pass algorithms, complement lookups
- **Two Pointers:** Sorted array manipulation
- **Prefix/Suffix Arrays:** Space-efficient computation
- **Logging:** Debugging and algorithm visualization
- **Edge Cases:** Empty inputs, duplicates, zeros

---

## 💡 Learning Path

1. Start with **Problem01** - Understanding hash-based optimizations
2. Move to **Binary_tree_traversal** - Graph/tree concepts
3. Then **Brinary_tree** - Optimization techniques
4. Finally **Problem02** - Advanced array manipulation

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

**Last Updated:** April 2026  
**Status:** Active development
