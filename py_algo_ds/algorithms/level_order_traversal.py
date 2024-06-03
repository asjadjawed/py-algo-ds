"""
Level Order Traversal
"""

from __future__ import annotations

from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val: int, left: Node | None = None, right: Node | None = None):
        """
        Initialize a Node.

        Args:
            val (int): The value of the node.
            left (Optional[Node], optional): The left child of the node. Defaults to None.
            right (Optional[Node], optional): The right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: Optional[Node]) -> List[List[int]]:
    """
    Perform a level order traversal on a binary tree. This uses BFS.

    Args:
        root (Optional[Node]): The root of the binary tree.

    Returns:
        List[List[int]]: A list of lists where each inner list contains the values at each level of the tree.

    Examples:
        >>> root = Node(1, Node(2), Node(3, Node(4), Node(5)))
        >>> level_order_traversal(root)
        [[1], [2, 3], [4, 5]]
    """
    if root is None:
        return []

    lot = []
    node_queue = deque([root])
    while node_queue:
        sub_lot = []
        for _ in range(len(node_queue)):
            node = node_queue.popleft()
            sub_lot.append(node.val)
            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)
        lot.append(sub_lot)
    return lot
