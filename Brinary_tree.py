'''Given a binary tree, determine whether or not it is 
height-balanced. A height-balanced binary tree can be defined 
as one in which the heights of the two subtrees of any 
node never differ by more than one.'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# SOLUTION 1: Optimized O(n) approach
# --------------------------------------------------
def is_balanced(root):
    """
    Check if a binary tree is height-balanced.
    Returns True if balanced, False otherwise.
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(h) - recursive call stack, where h is height
    """
    def check_height(node):
        """
        Helper function that returns:
        - (-1, False) if the subtree is unbalanced
        - (height, True) if the subtree is balanced
        """
        if node is None:
            return (0, True)
        
        left_height, left_balanced = check_height(node.left)
        if not left_balanced:
            return (-1, False)
        
        right_height, right_balanced = check_height(node.right)
        if not right_balanced:
            return (-1, False)
        
        # Check if current node is balanced
        if abs(left_height - right_height) > 1:
            return (-1, False)
        
        # Current node is balanced, return height
        return (max(left_height, right_height) + 1, True)
    
    _, is_balanced_result = check_height(root)
    return is_balanced_result


# --------------------------------------------------
# SOLUTION 2: Simple recursive approach (less efficient)
# --------------------------------------------------
def is_balanced_simple(root):
    """
    Simple recursive approach to check if a tree is height-balanced.
    
    Time Complexity: O(n^2) - height() is called for each node
    Space Complexity: O(h) - recursive call stack
    """
    def height(node):
        if node is None:
            return 0
        return 1 + max(height(node.left), height(node.right))
    
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    # Check if current node is balanced and both subtrees are balanced
    return (abs(left_height - right_height) <= 1 and
            is_balanced_simple(root.left) and
            is_balanced_simple(root.right))


# --------------------------------------------------
# TEST CASES
# --------------------------------------------------
if __name__ == "__main__":
    # Test Case 1: Balanced tree
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = Node(3)
    root1.left = Node(9)
    root1.right = Node(20)
    root1.right.left = Node(15)
    root1.right.right = Node(7)
    
    print("Test 1 - Balanced tree:")
    print(f"  is_balanced: {is_balanced(root1)}")  # True
    print(f"  is_balanced_simple: {is_balanced_simple(root1)}")  # True
    
    # Test Case 2: Unbalanced tree
    #       1
    #      /
    #     2
    #    /
    #   3
    root2 = Node(1)
    root2.left = Node(2)
    root2.left.left = Node(3)
    
    print("\nTest 2 - Unbalanced tree:")
    print(f"  is_balanced: {is_balanced(root2)}")  # False
    print(f"  is_balanced_simple: {is_balanced_simple(root2)}")  # False
    
    # Test Case 3: Single node (balanced)
    root3 = Node(1)
    
    print("\nTest 3 - Single node:")
    print(f"  is_balanced: {is_balanced(root3)}")  # True
    print(f"  is_balanced_simple: {is_balanced_simple(root3)}")  # True
    
    # Test Case 4: Empty tree (balanced)
    root4 = None
    
    print("\nTest 4 - Empty tree:")
    print(f"  is_balanced: {is_balanced(root4)}")  # True
    print(f"  is_balanced_simple: {is_balanced_simple(root4)}")  # True
    
    # Test Case 5: Balanced but complex tree
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    #    /
    #   6
    root5 = Node(1)
    root5.left = Node(2)
    root5.right = Node(3)
    root5.left.left = Node(4)
    root5.left.right = Node(5)
    root5.left.left.left = Node(6)
    
    print("\nTest 5 - Balanced complex tree:")
    print(f"  is_balanced: {is_balanced(root5)}")  # False (node 2 is unbalanced)
    print(f"  is_balanced_simple: {is_balanced_simple(root5)}")  # False

