class BSTnode(object):
    """
    Representation of a node in a binary search tree.
    Has a left child, right child, and key value.
    """
    def __init__(self, t):
        self.key = t
        self.disconnect()

    def disconnect(self):
        self.parent = None
        self.left = None
        self.right = None


class BST(object):
    """
    Simple binary search tree implementation.
    This BST supports insert, find, and delete-min operations.
    Each tree contains some (possibly 0) BSTnode objects, representing nodes,
    and a pointer to the root.
    """

    def __init__(self):
        self.root = None

    def insert(self, t):
        """Insert key into this BST, modifying it in-place."""
        new = BSTnode(t)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if t < node.key:
                    # Go left
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    # Go right
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return new

    def insert_2(self, t):
        new = BSTnode(t)
        p = None
        node = self.root
        while node is not None:
            p = node
            if t < node.key:
                node = node.left
            else:
                node = node.right
        if p is None:
            self.root = new
        else:
            if t < p.key:
                p.left = new
            else:
                p.right = new
            new.parent = p
        return new

    def find(self, t):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = self.root
        while node is not None:
            if node.key == t:
                return node
            elif t < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def delete_min(self):
        """Delete the minimum element and return the old node containing it."""
        if self.root is None:
            return None, None
        else:
            # Walk to the leftmost node.
            node = self.root
            while node.left is not None:
                node = node.left
            # Remove that node and promote its right subtree
            if node.parent is not None:
                node.parent.left = node.right
            else: # The root was smallest.
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent

    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

    def inorder(self):
        if self.root is None: print('<empty tree>')
        def traverse(node):
            if node is None: return
            traverse(node.left)
            print(node.key)
            traverse(node.right)
        traverse(self.root)

def tree_min(tree):
    node = tree
    if node is None: return None
    else:
        while node.left is not None:
            node = node.left
        return node.key


def successor(tree):
    if tree.right is not None:
        return tree_min(tree.right)
    while tree.parent is not None and tree.right is tree.parent.right is tree:
        tree = tree.parent
    return tree.key

b = BST()
b.insert(5)
b.insert(10)
b.insert(4)
b.insert_2(7)
b.insert(6)
print(tree_min(b.root))
print(successor(b.root))
print(b)