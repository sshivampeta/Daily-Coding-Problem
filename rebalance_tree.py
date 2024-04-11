'''Recall that a full binary tree is one in which each node is either a leaf node, or has two children.
 Given a binary tree, convert it to a full one by removing nodes
   with only one child.
   
   Example:
         0
      /     \
    1         2
  /            \
3                 4
  \             /   \
    5          6     7
    
   Converts to:
     0
  /     \
5         4
        /   \
       6     7
'''

import logging
from collections import deque

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# SOLUTION 1: Recursive Post-Order Traversal ⭐ (Optimal)
# --------------------------------------------------
def prune_tree(root):
    """
    Remove nodes with only one child from binary tree.
    
    Approach:
    - Post-order traversal (process children before parent)
    - For each node:
      - If both children exist: keep node
      - If only left child: return left child (remove current node)
      - If only right child: return right child (remove current node)
      - If no children (leaf): keep node
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(h) - recursive call stack height
    """
    if root is None:
        return None
    
    logging.info(f"Processing node {root.val}")
    
    # Recursively process left and right subtrees
    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    
    # Check current node
    left_exists = root.left is not None
    right_exists = root.right is not None
    
    # Case 1: Both children exist - keep the node
    if left_exists and right_exists:
        logging.info(f"  Node {root.val}: has both children - KEEP")
        return root
    
    # Case 2: Only left child exists
    if left_exists:
        logging.info(f"  Node {root.val}: only left child - REMOVE (replace with left subtree)")
        return root.left
    
    # Case 3: Only right child exists
    if right_exists:
        logging.info(f"  Node {root.val}: only right child - REMOVE (replace with right subtree)")
        return root.right
    
    # Case 4: No children (leaf node) - keep the node
    logging.info(f"  Node {root.val}: leaf node - KEEP")
    return root


# --------------------------------------------------
# SOLUTION 2: Iterative using Post-Order Traversal
# --------------------------------------------------
def prune_tree_iterative(root):
    """
    Iterative approach using two stacks for post-order traversal.
    
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    if root is None:
        return None
    
    stack1 = [root]
    stack2 = []
    parent_map = {}  # Track parents for updating references
    
    # First pass: build post-order traversal in stack2
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack2.append(None)  # Marker for post-order
            if node.left:
                stack1.append(node.left)
        if node.right:
            if node.right:
                stack1.append(node.right)
    
    # Process nodes in reverse post-order (bottom-up)
    processed = set()
    while stack2:
        node = stack2.pop()
        
        if node is None:
            continue
        
        if id(node) in processed:
            continue
        
        processed.add(id(node))
        
        left_exists = node.left is not None
        right_exists = node.right is not None
        
        if left_exists and right_exists:
            continue  # Keep node
        elif left_exists:
            temp = node.left
            node.val = temp.val
            node.left = temp.left
            node.right = temp.right
        elif right_exists:
            temp = node.right
            node.val = temp.val
            node.left = temp.left
            node.right = temp.right
    
    return root


# --------------------------------------------------
# SOLUTION 3: Recursive with Explicit Node Removal Tracking
# --------------------------------------------------
def prune_tree_verbose(root):
    """
    Recursive solution with detailed logging of which nodes are removed.
    
    Time Complexity: O(n)
    Space Complexity: O(h)
    """
    removed_count = [0]  # Use list to track in nested function
    
    def helper(node):
        if node is None:
            return None
        
        # Process left and right subtrees
        node.left = helper(node.left)
        node.right = helper(node.right)
        
        left_exists = node.left is not None
        right_exists = node.right is not None
        
        # Apply pruning rules
        if left_exists and right_exists:
            # Keep node with two children
            return node
        elif left_exists:
            # Remove node with only left child
            removed_count[0] += 1
            logging.info(f"Removing node {node.val} (only left child exists)")
            return node.left
        elif right_exists:
            # Remove node with only right child
            removed_count[0] += 1
            logging.info(f"Removing node {node.val} (only right child exists)")
            return node.right
        else:
            # Keep leaf node
            return node
    
    result = helper(root)
    logging.info(f"Total nodes removed: {removed_count[0]}")
    return result


# --------------------------------------------------
# UTILITY FUNCTIONS
# --------------------------------------------------
def tree_to_list_bfs(root):
    """Convert tree to level-order list representation"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    
    return result


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
    #         0
    #      /     \
    #    1         2
    #  /            \
    # 3               4
    #   \            /  \
    #    5           6    7
    
    node3 = TreeNode(3)
    node3.right = TreeNode(5)
    
    node1 = TreeNode(1)
    node1.left = node3
    
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node4.left = node6
    node4.right = node7
    
    node2 = TreeNode(2)
    node2.right = node4
    
    root = TreeNode(0)
    root.left = node1
    root.right = node2
    
    return root


def run_tests():
    print("=" * 70)
    print("TESTING FULL BINARY TREE CONVERSION")
    print("=" * 70)
    
    # Test 1: Example from problem
    print("\n--- Test 1: Example from Problem ---")
    print("\nOriginal Tree:")
    root1 = create_example_tree()
    print_tree(root1)
    print("\nLevel-order: ", tree_to_list_bfs(root1))
    
    root1_pruned = prune_tree(root1)
    print("\nPruned Tree:")
    print_tree(root1_pruned)
    print("Level-order: ", tree_to_list_bfs(root1_pruned))
    
    # Test 2: Single node
    print("\n--- Test 2: Single Node ---")
    root2 = TreeNode(1)
    print("Original:")
    print_tree(root2)
    root2_pruned = prune_tree(root2)
    print("Pruned:")
    print_tree(root2_pruned)
    
    # Test 3: Already full tree
    print("\n--- Test 3: Already Full Binary Tree ---")
    #     1
    #    / \
    #   2   3
    #  / \ / \
    # 4  5 6  7
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    root3.right.left = TreeNode(6)
    root3.right.right = TreeNode(7)
    
    print("Original:")
    print_tree(root3)
    root3_pruned = prune_tree(root3)
    print("Pruned:")
    print_tree(root3_pruned)
    
    # Test 4: Chain tree (all nodes have only one child)
    print("\n--- Test 4: Chain Tree (All Single Children) ---")
    # 1 - 2 - 3 - 4 - 5
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    root4.right.right.right = TreeNode(4)
    root4.right.right.right.right = TreeNode(5)
    
    print("Original:")
    print_tree(root4)
    root4_pruned = prune_tree(root4)
    print("Pruned:")
    print_tree(root4_pruned)
    
    # Test 5: Complex tree
    print("\n--- Test 5: Complex Tree ---")
    #       10
    #      /
    #     5
    #    / \
    #   3   7
    #   /     \
    #  1       9
    root5 = TreeNode(10)
    root5.left = TreeNode(5)
    root5.left.left = TreeNode(3)
    root5.left.right = TreeNode(7)
    root5.left.left.left = TreeNode(1)
    root5.left.right.right = TreeNode(9)
    
    print("Original:")
    print_tree(root5)
    root5_pruned = prune_tree(root5)
    print("Pruned:")
    print_tree(root5_pruned)


if __name__ == "__main__":
    run_tests()