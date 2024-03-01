import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# --------------------------------------------------
# SERIALIZE
# --------------------------------------------------
def serialize(root):
    result = []

    def dfs(node):
        if node is None:
            result.append("null")
            return

        logging.info(f"Serialize node: {node.val}")
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(result)


# --------------------------------------------------
# DESERIALIZE
# --------------------------------------------------
def deserialize(s):
    values = iter(s.split(","))

    def dfs():
        val = next(values)

        if val == "null":
            return None

        logging.info(f"Deserialize node: {val}")
        node = Node(val)
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


# --------------------------------------------------
# TESTS
# --------------------------------------------------
def run_tests():
    # Example from problem
    node = Node('root',
                Node('left',
                     Node('left.left')),
                Node('right'))

    serialized = serialize(node)
    print("Serialized:", serialized)

    deserialized = deserialize(serialized)

    assert deserialized.left.left.val == 'left.left'
    print("Test 1 passed ✅")

    # Edge cases
    cases = [
        None,  # empty tree
        Node(1),  # single node
        Node(1, Node(2), None),  # left skewed
        Node(1, None, Node(3)),  # right skewed
        Node(1, Node(2), Node(3)),  # full tree
    ]

    for i, case in enumerate(cases, 2):
        s = serialize(case)
        restored = deserialize(s)

        def compare(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (
                a.val == b.val and
                compare(a.left, b.left) and
                compare(a.right, b.right)
            )

        assert compare(case, restored)
        print(f"Test {i} passed ✅")


# --------------------------------------------------
# MAIN
# --------------------------------------------------
def main():
    run_tests()


if __name__ == "__main__":
    main()