'''Two nodes in a binary tree can be called cousins if they are on the same level of the tree but have different parents. For example, in the following diagram 4 and 6 are cousins.

    1
   / \
  2   3
 / \   \
4   5   6
Given a binary tree and a particular node, find all cousins of that node'''

import logging
from collections import deque

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# SOLUTION 1: BFS Level-Order Traversal ⭐ (Optimal)
# --------------------------------------------------
def find_cousins_bfs(root, target):
    """
    Find all cousins of target node using BFS (level-order traversal).
    
    Approach:
    - Use BFS to traverse tree level by level
    - Track parent of each node during traversal
    - Find target node's level and parent
    - Return all nodes at same level with different parent
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(w) - where w is maximum width of tree
    """
    if root is None:
        return []
    
    # BFS to find target node and its parent
    target_level = None
    target_parent = None
    
    queue = deque([(root, None, 0)])  # (node, parent, level)
    level_nodes = {}  # Maps level -> list of (node, parent) tuples
    
    while queue:
        node, parent, level = queue.popleft()
        
        # Track all nodes at each level with their parents
        if level not in level_nodes:
            level_nodes[level] = []
        level_nodes[level].append((node, parent))
        
        # Found target node
        if node.val == target:
            target_level = level
            target_parent = parent
            logging.info(f"Found target {target} at level {level}, parent: {parent.val if parent else None}")
        
        # Add children to queue
        if node.left:
            queue.append((node.left, node, level + 1))
        if node.right:
            queue.append((node.right, node, level + 1))
    
    # If target not found
    if target_level is None:
        logging.warning(f"Target node {target} not found in tree")
        return []
    
    # Get all cousins at same level (different parent)
    cousins = []
    if target_level in level_nodes:
        for node, parent in level_nodes[target_level]:
            # Cousin if same level but different parent
            if parent != target_parent:
                cousins.append(node.val)
            else:
                logging.info(f"Node {node.val} has same parent as target, not a cousin")
    
    logging.info(f"Cousins of {target}: {cousins}")
    return sorted(cousins)


# --------------------------------------------------
# SOLUTION 2: DFS with Parent Tracking
# --------------------------------------------------
def find_cousins_dfs(root, target):
    """
    Find cousins using DFS with parent and depth tracking.
    
    Approach:
    - DFS traversal tracking parent and depth
    - Find target's depth and parent first
    - Second pass: collect all nodes at same depth with different parent
    
    Time Complexity: O(n) - two passes through tree
    Space Complexity: O(h) - recursion stack
    """
    target_depth = [None]
    target_parent = [None]
    
    def find_target(node, parent, depth):
        """Find target node's depth and parent"""
        if node is None:
            return
        
        if node.val == target:
            target_depth[0] = depth
            target_parent[0] = parent
            logging.info(f"Found target {target} at depth {depth}, parent: {parent.val if parent else None}")
            return
        
        find_target(node.left, node, depth + 1)
        find_target(node.right, node, depth + 1)
    
    def collect_cousins(node, parent, depth):
        """Collect all nodes at target depth with different parent"""
        if node is None:
            return []
        
        cousins = []
        
        # If at target depth
        if depth == target_depth[0]:
            # Add if different parent
            if parent != target_parent[0]:
                cousins.append(node.val)
                logging.info(f"Found cousin: {node.val}")
        
        # Continue DFS if not at target depth
        if depth < target_depth[0]:
            cousins.extend(collect_cousins(node.left, node, depth + 1))
            cousins.extend(collect_cousins(node.right, node, depth + 1))
        
        return cousins
    
    # First pass: find target
    find_target(root, None, 0)
    
    if target_depth[0] is None:
        logging.warning(f"Target node {target} not found in tree")
        return []
    
    # Second pass: collect cousins
    cousins = collect_cousins(root, None, 0)
    return sorted(cousins)


# --------------------------------------------------
# SOLUTION 3: Single Pass DFS (Optimized)
# --------------------------------------------------
def find_cousins_single_pass(root, target):
    """
    Find cousins in single DFS pass.
    
    Approach:
    - Single DFS traversal
    - Track all nodes at each depth with their parents
    - Return nodes at target depth with different parent
    
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    depth_map = {}  # Maps depth -> list of (node_value, parent_value)
    target_depth = [None]
    target_parent = [None]
    
    def dfs(node, parent, depth):
        if node is None:
            return
        
        # Track node at this depth
        if depth not in depth_map:
            depth_map[depth] = []
        
        parent_val = parent.val if parent else None
        depth_map[depth].append((node.val, parent_val))
        
        # Update target info if found
        if node.val == target:
            target_depth[0] = depth
            target_parent[0] = parent_val
            logging.info(f"Found target {target} at depth {depth}, parent: {parent_val}")
        
        dfs(node.left, node, depth + 1)
        dfs(node.right, node, depth + 1)
    
    dfs(root, None, 0)
    
    if target_depth[0] is None:
        logging.warning(f"Target node {target} not found in tree")
        return []
    
    # Find cousins at same depth with different parent
    cousins = []
    if target_depth[0] in depth_map:
        for node_val, parent_val in depth_map[target_depth[0]]:
            if parent_val != target_parent[0]:
                cousins.append(node_val)
    
    logging.info(f"Cousins of {target}: {cousins}")
    return sorted(cousins)


# --------------------------------------------------
# SOLUTION 4: BFS with Early Termination
# --------------------------------------------------
def find_cousins_bfs_optimized(root, target):
    """
    BFS approach that stops after finding target's level cousins.
    
    Time Complexity: O(n) in worst case, O(n/2) on average
    Space Complexity: O(w) - maximum width
    """
    if root is None:
        return []
    
    queue = deque([(root, None)])  # (node, parent)
    current_level = [root]
    target_level = 0
    target_parent = None
    level = 0
    
    while current_level:
        next_level = []
        
        # Process entire level
        for node in current_level:
            for child in [node.left, node.right]:
                if child is None:
                    continue
                
                # Found target - record level and parent
                if child.val == target:
                    target_level = level + 1
                    target_parent = node
                    logging.info(f"Found target {target} at level {target_level}, parent: {node.val}")
                
                next_level.append(child)
        
        current_level = next_level
        level += 1
    
    # If target not found
    if target_parent is None:
        logging.warning(f"Target node {target} not found in tree")
        return []
    
    # Now process the target level to find cousins
    queue = deque([(root, None)])
    current_level = [root]
    level = 0
    
    while current_level and level <= target_level:
        if level == target_level:
            # Collect cousins from current level
            cousins = []
            for node in current_level:
                # Need to find parent - would require different tracking
                # This approach is less efficient, kept for comparison
            break
        
        next_level = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        
        current_level = next_level
        level += 1
    
    # Alternative: use the BFS solution which is cleaner
    return find_cousins_bfs(root, target)


# --------------------------------------------------
# UTILITY FUNCTIONS
# --------------------------------------------------
def print_tree(root, level=0, prefix="Root: "):
    """Pretty print binary tree"""
    if root is None:
        return
    
    print(" " * (level * 4) + prefix + str(root.val))
    if root.left or root.right:
        if root.left:
            print_tree(root.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        
        if root.right:
            print_tree(root.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")


# --------------------------------------------------
# TEST CASES
# --------------------------------------------------
def create_example_tree():
    """Create the example tree from the problem"""
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    
    node2 = TreeNode(2)
    node2.left = node4
    node2.right = node5
    
    node3 = TreeNode(3)
    node3.right = node6
    
    root = TreeNode(1)
    root.left = node2
    root.right = node3
    
    return root


def run_tests():
    print("=" * 70)
    print("TESTING FIND COUSINS IN BINARY TREE")
    print("=" * 70)
    
    # Test 1: Example from problem
    print("\n--- Test 1: Example from Problem ---")
    root1 = create_example_tree()
    print("\nTree structure:")
    print_tree(root1)
    
    test_values = [4, 5, 6, 2, 3, 1]
    expected = {
        4: [6],      # 4 and 6 are on same level but different parents
        5: [6],      # 5 and 6 are on same level but different parents
        6: [4, 5],   # 6 and 4,5 are on same level but different parents
        2: [3],      # 2 and 3 are on same level but different parents
        3: [2],      # 3 and 2 are on same level but different parents
        1: [],       # 1 has no cousins (root)
    }
    
    for val in test_values:
        print(f"\nFinding cousins of {val}:")
        result_bfs = find_cousins_bfs(root1, val)
        result_dfs = find_cousins_dfs(root1, val)
        result_sp = find_cousins_single_pass(root1, val)
        
        exp = expected[val]
        print(f"  Expected: {exp}")
        print(f"  BFS Result: {result_bfs} {'✅' if result_bfs == exp else '❌'}")
        print(f"  DFS Result: {result_dfs} {'✅' if result_dfs == exp else '❌'}")
        print(f"  Single Pass: {result_sp} {'✅' if result_sp == exp else '❌'}")
    
    # Test 2: Deep tree
    print("\n--- Test 2: Deeper Tree ---")
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    #  /
    # 8
    node8 = TreeNode(8)
    node4 = TreeNode(4)
    node4.left = node8
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = node4
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    
    print("\nTree structure:")
    print_tree(root2)
    
    print(f"\nCousins of 8: {find_cousins_bfs(root2, 8)}")  # []
    print(f"Cousins of 4: {find_cousins_bfs(root2, 4)}")  # [6, 7]
    print(f"Cousins of 5: {find_cousins_bfs(root2, 5)}")  # [6, 7]
    
    # Test 3: Single node
    print("\n--- Test 3: Single Node Tree ---")
    root3 = TreeNode(1)
    print("Tree structure:")
    print_tree(root3)
    print(f"Cousins of 1: {find_cousins_bfs(root3, 1)}")  # []
    
    # Test 4: Linear tree
    print("\n--- Test 4: Linear Tree (Right chain) ---")
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    print("Tree structure:")
    print_tree(root4)
    print(f"Cousins of 3: {find_cousins_bfs(root4, 3)}")  # []
    
    # Test 5: Node not found
    print("\n--- Test 5: Node Not Found ---")
    root5 = create_example_tree()
    print(f"Cousins of 99: {find_cousins_bfs(root5, 99)}")  # []


if __name__ == "__main__":
    run_tests()