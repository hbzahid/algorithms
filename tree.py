from stack import Stack


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left = None
        self.right = None
        self.parent = None

    def insert_left(self, node):
        t = BinaryTree(node)
        if self.left is None:
            self.left = t
        else:
            t.left = self.left
            self.left = t
            self.left.parent = t
        t.parent = self

    def insert_right(self, node):
        t = BinaryTree(node)
        if self.right is None:
            self.right = t
        else:
            t.right = self.right
            self.right = t
            self.right.parent = t
        t.parent = self

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def get_parent(self):
        return self.parent

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


def build_parse_tree(exp):
    tokens = exp.split()
    e_tree = BinaryTree('')
    current_tree = e_tree
    for t in tokens:
        if t == '(':
            current_tree.insert_left('')
            current_tree = current_tree.get_left_child()
        elif t == ')':
            current_tree = current_tree.get_parent()
        elif t not in ['*', '+', '-', '/']:
            current_tree.set_root_val(int(t))
            current_tree = current_tree.get_parent()
        elif t in ['*', '+', '-', '/']:
            current_tree.set_root_val(t)
            current_tree.insert_right('')
            current_tree = current_tree.get_right_child()
        else:
            raise ValueError
    return e_tree


def evaluate(parse_tree):
    import operator

    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/':operator.truediv}
    leftC = parse_tree.get_left_child()
    rightC = parse_tree.get_right_child()

    if leftC and rightC:
        return opers[parse_tree.get_root_val()](evaluate(leftC), evaluate(rightC))
    else:
        return parse_tree.get_root_val()

print(evaluate(build_parse_tree("( ( ( 10 + 5 ) * 3 ) / 5 )")))