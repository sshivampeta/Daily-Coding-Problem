# Largest Number Arrangement Problem

## Problem Statement

Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.

### Example
```
Input: [10, 7, 76, 415]
Output: "77641510"

Explanation:
- Possible arrangements: 10776415, 10774165, 7761410, 77641510, etc.
- 77641510 is the largest
```

### Additional Examples
```
Input: [3, 30, 34, 5, 9]
Output: "9534330"

Input: [0, 0, 0]
Output: "0"

Input: [12, 121]
Output: "12112"
(because "12112" > "12112" when comparing "12" + "121" vs "121" + "12")
```

---

## Key Insight

The problem is NOT about sorting numbers numerically. Instead, we need a **custom comparator** that determines the optimal order.

### The Comparator Logic

For two numbers `a` and `b` (as strings):
- If concatenating as `a + b` produces a larger number than `b + a`, then `a` should come first
- Otherwise, `b` should come first

**Example:**
```
Compare 10 and 7:
  "10" + "7" = "107"
  "7" + "10" = "710"
  
"710" > "107" lexicographically
So 7 should come first
```

```
Compare 76 and 415:
  "76" + "415" = "76415"
  "415" + "76" = "41576"
  
"76415" > "41576" lexicographically
So 76 should come first
```

---

## Solutions Overview

### Solution 1: Custom Comparator with Sorting ⭐ (Optimal)

**Implementation:**
```python
from functools import cmp_to_key

def largest_number_comparator(nums):
    nums_str = [str(num) for num in nums]
    
    def compare(a, b):
        if a + b > b + a:
            return -1  # a comes first
        elif a + b < b + a:
            return 1   # b comes first
        else:
            return 0   # equal
    
    nums_str.sort(key=cmp_to_key(compare))
    
    result = ''.join(nums_str)
    
    # Handle edge case of all zeros
    if all(c == '0' for c in result):
        return "0"
    
    return result
```

**Complexity:**
- **Time:** O(n log n × k) where n = count of numbers, k = average string length
- **Space:** O(n × k) for string conversion

**Why it works:**
- Custom comparator defines a total ordering on the strings
- Sorting gives optimal arrangement that maximizes the final number
- Python's sort is stable and efficient (Timsort)

---

### Solution 2: Custom Comparator with Key Function

**Implementation:**
```python
def largest_number_key(nums):
    nums_str = [str(num) for num in nums]
    nums_str.sort(key=lambda x: x * 10, reverse=True)
    
    result = ''.join(nums_str)
    
    if all(c == '0' for c in result):
        return "0"
    
    return result
```

**Complexity:**
- **Time:** O(n log n × k)
- **Space:** O(n × k)

**Notes:**
- Uses multiplication trick to simulate comparison
- More Pythonic but less explicit than compare function
- Works because `"999" * 10 > "998" * 10` simulates the comparison

---

### Solution 3: Manual Bubble Sort

**Implementation:**
```python
def largest_number_bubble(nums):
    nums_str = [str(num) for num in nums]
    n = len(nums_str)
    
    for i in range(n):
        for j in range(n - 1 - i):
            if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]:
                nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
    
    result = ''.join(nums_str)
    
    if all(c == '0' for c in result):
        return "0"
    
    return result
```

**Complexity:**
- **Time:** O(n²)
- **Space:** O(n)

**Use Case:** Educational purposes - clearly shows the comparison logic

---

### Solution 4: Counting Sort

Not practical for this problem. Comparison-based sorting is more general and flexible.

---

## Edge Cases

### 1. All Zeros
```python
Input: [0, 0, 0]
Output: "0"  # NOT "000"
```
**Why:** Need to return single "0" for all-zero case

### 2. Single Element
```python
Input: [5]
Output: "5"
```

### 3. Empty List
```python
Input: []
Output: ""
```

### 4. Numbers with Common Prefixes
```python
Input: [12, 121]
Output: "12112"

Compare:
  "12" + "121" = "12121"
  "121" + "12" = "12112"
  
"12121" > "12112", so 12 comes first
```

### 5. Large Numbers
No overflow issues since we work with strings

---

## Algorithm Walkthrough

### Step-by-Step Example: [10, 7, 76, 415]

**Initial:** [10, 7, 76, 415]

**Comparisons during sort:**

1. **Compare 10 vs 7:**
   - "10" + "7" = "107"
   - "7" + "10" = "710"
   - "710" > "107" → 7 comes first

2. **Compare 7 vs 76:**
   - "7" + "76" = "776"
   - "76" + "7" = "767"
   - "776" > "767" → 7 comes first

3. **Compare 7 vs 415:**
   - "7" + "415" = "7415"
   - "415" + "7" = "4157"
   - "7415" > "4157" → 7 comes first

4. **Compare 76 vs 415:**
   - "76" + "415" = "76415"
   - "415" + "76" = "41576"
   - "76415" > "41576" → 76 comes first

5. **Compare 76 vs 10:**
   - "76" + "10" = "7610"
   - "10" + "76" = "1076"
   - "7610" > "1076" → 76 comes first

**Final Order:** [7, 76, 415, 10]  
**Result:** "77641510"

---

## Test Cases

| Input | Expected Output | Notes |
|-------|-----------------|-------|
| [10, 7, 76, 415] | "77641510" | Main example |
| [3, 30, 34, 5, 9] | "9534330" | Common prefix: 3, 30, 34 |
| [0, 0, 0] | "0" | All zeros edge case |
| [12, 121] | "12112" | Prefix comparison |
| [1] | "1" | Single element |
| [] | "" | Empty input |
| [100, 1, 10] | "11010100" | Mixed lengths |
| [9, 8, 7, 6, 5] | "98765" | Already sorted descending |
| [1, 2, 3, 4, 5] | "54321" | Reverse numeric order |

---

## Complexity Analysis

| Aspect | Details |
|--------|---------|
| **Time** | O(n log n × k) where n = number count, k = avg string length |
| **Space** | O(n × k) for string storage |
| **Comparisons per sort** | O(n log n) |
| **String concatenation per compare** | O(k) |

---

## Why Custom Comparator Works

The key property is **transitivity**: if the comparator defines a consistent ordering, sorting will find the global optimum.

**Proof sketch:**
- If arrangement A > arrangement B when swapping any two adjacent elements, then A is optimal
- Our comparator ensures this property for any pairs
- By extension, the globally sorted arrangement is optimal

---

## Real-World Applications

1. **Ticket Pricing:** Arrange price digits to maximize revenue
2. **Phone Numbers:** Create largest possible phone number from digits
3. **Numbers Game:** Largest number arrangement puzzle
4. **Competitive Programming:** Common interview question

---

## Implementation Tips

1. **Convert to strings:** Easier comparison and concatenation
2. **Handle zeros:** Check if result is all zeros, return "0"
3. **Use built-in sort:** More efficient than manual implementation
4. **Verify results:** Check against smaller permutations for correctness

---

## Common Mistakes

❌ **Wrong:** Sorting numerically
```python
nums.sort(reverse=True)  # [415, 76, 10, 7] → "415767102" ✗
```

❌ **Wrong:** Sorting lexicographically
```python
nums_str.sort(reverse=True)  # ["76", "7", "415", "10"] → "7674151010" ✗
```

✅ **Correct:** Custom comparator
```python
nums_str.sort(key=cmp_to_key(lambda a, b: -1 if a+b > b+a else 1))
# ["7", "76", "415", "10"] → "77641510" ✓
```

---

## Performance Considerations

- **For small lists (n < 100):** Any solution works
- **For medium lists (n < 10,000):** Comparator sorting is ideal
- **For large lists (n > 100,000):** Still O(n log n), but watch concatenation overhead
- **For extremely large lists:** Consider specialized algorithms

---

## Related Problems

- **LeetCode 179:** Largest Number (exact same problem)
- **LeetCode 1323:** Maximum 69 Number (similar digit manipulation)
- **String Concatenation Problems:** Other string ordering challenges

---

**Created:** April 11, 2026  
**Source File:** `Dictionay_Sort_.py`
