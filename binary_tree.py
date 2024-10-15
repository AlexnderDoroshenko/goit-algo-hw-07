class TreeNode:
    def __init__(self, key: int):
        """
        Initializes a tree node.

        :param key: The value of the node.
        """
        self.left: TreeNode = None
        self.right: TreeNode = None
        self.val: int = key


class BinarySearchTree:
    def __init__(self):
        """Initializes an empty binary search tree."""
        self.root: TreeNode = None

    def insert(self, key: int) -> None:
        """
        Inserts a new value into the tree.

        :param key: The value to be inserted.
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node: TreeNode, key: int) -> None:
        """Recursively inserts a value into the tree."""
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def find_max(self) -> int:
        """
        Finds the maximum value in the tree.

        :return: The maximum value.
        """
        return self._find_max_rec(self.root)

    def _find_max_rec(self, node: TreeNode) -> TreeNode:
        """Recursively finds the maximum value."""
        current = node
        while current.right is not None:
            current = current.right
        return current.val

    def find_min(self) -> int:
        """
        Finds the minimum value in the tree.

        :return: The minimum value.
        """
        return self._find_min_rec(self.root)

    def _find_min_rec(self, node: TreeNode) -> TreeNode:
        """Recursively finds the minimum value."""
        current = node
        while current.left is not None:
            current = current.left
        return current.val

    def sum_values(self) -> int:
        """
        Calculates the sum of all values in the tree.

        :return: The sum of values.
        """
        return self._sum_values_rec(self.root)

    def _sum_values_rec(self, node: TreeNode) -> int:
        """Recursively calculates the sum of values."""
        if node is None:
            return 0
        return node.val + self._sum_values_rec(node.left) + self._sum_values_rec(node.right)


# Tests
def test_find_max():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(7)
    bst.insert(10)
    assert bst.find_max() == 10, "Test failed: expected 10."
    print("Max test passed")


def test_sum_values():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    assert bst.sum_values() == 16, "Test failed: expected 16."
    print("Sum test passed")


def test_find_min():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(1)
    assert bst.find_min() == 1, "Test failed: expected 1."
    print("Min test passed")


test_find_max()
test_sum_values()
test_find_min()
