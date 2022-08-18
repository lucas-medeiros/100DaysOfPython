# @author   Lucas Cardoso de Medeiros
# @since    06/06/2022
# @version  1.0

# SYMMETRIC TREE

# Rules:
# Given a binary tree root, check if it is symmetric around its center (mirror)

# root1 and root2 is None -> True
# only 1 root is None -> False
# root1 != root2 -> False


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


# Solution 1: recursion
# O(logn) complexity
def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None and root2 is not None:
        return False
    elif root1 is not None and root2 is None:
        return False
    elif root1.data != root2.data:
        return False
    else:
        return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)


def is_symmetric(root):
    if root is None:
        return True
    return are_symmetric(root.left, root.right)


if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)
    root.print_tree()
    print(is_symmetric(root))
