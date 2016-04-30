class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    for paren in symbol_string:
        if paren == '(':
            s.push(paren)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                s.pop()
    if balanced and s.is_empty():
        return True
    else:
        return False


def par_checker_gen(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while balanced and index < len(symbol_string):
        symbol = symbol_string[index]
        if symbol in '{[(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(top, symbol):
    open_parens = '{[('
    close_parens = '}])'
    return open_parens.index(top) == close_parens.index(symbol)


def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()
    while dec_number > 0:
        remainder = dec_number % base
        rem_stack.push(remainder)
        dec_number = dec_number // base
    new_str = ''
    while not rem_stack.is_empty():
        new_str += digits[rem_stack.pop()]
    return new_str


def infixToPostfix(infix):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    tokens = list(infix)
    op_stack = Stack()
    result = []
    for t in tokens:
        if t == '(':
            op_stack.push(t)
        elif t in alphabets:
            result.append(t)
        elif t == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                result.append(top_token)
                top_token = op_stack.pop()
        else:
            op_stack.push(t)
    while not op_stack.is_empty():
        result.append(op_stack.pop())
    return ''.join(result)

print(infixToPostfix("((a+t)*((b+(a+c))^(c+d)))"))

def postfix_eval(postfix_exp):
    operand_stack = Stack()
    tokens = postfix_exp.split()
    for token in tokens:
        if token.isdigit():
            operand_stack.push(int(token))
        else:
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            result = do_math(op1, op2, token)
            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op1, op2, operator):
    if operator  == '+':
        return op2 + op1
    elif operator == '-':
        return op2 - op1
    elif operator == '*':
        return op2 * op1
    else:
        return op2 / op1


class TextEditor:
    def __init__(self):
        self.letters = []

    def append(self, w):
        self.letters += list(w)
        return self.letters

    def erase(self, k):
        del self.letters[len(self.letters) - k:]
        return self.letters

    def get(self, index):
        return self.letters[index-1]


class ThreeStacks:
    def __init__(self, max_length):
        self.items = [None] * max_length * 3
        self.max_length = max_length
        self.pointer = [-1] * 3

    def pop(self, stack_num):
        pos = self.pointer[stack_num]
        if self.pointer[stack_num] != -1:
            data = self.items[self.position(pos, stack_num)]
            self.items[self.position(pos, stack_num)] = None
            self.pointer[stack_num] -= 1
            return data
        else:
            print("Stack is empty")

    def is_empty(self, stack_num):
        return self.pointer[stack_num]  == -1

    def push(self, stack_num, item):
        new_pos = self.pointer[stack_num] + 1
        if new_pos < self.max_length:
            self.items[self.position(new_pos, stack_num)] = item
            self.pointer[stack_num] += 1
        else:
            print("Stack out of space.")

    def position(self, pos, stack_num):
        return stack_num * self.max_length + pos


class StackWithMin:
    def __init__(self):
        self.items  = []
        self.min_stack = []

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            item = self.items.pop()
            if item == self.min():
                self.min_stack.pop()
            return item

    def push(self, item):
        if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
            self.min_stack.append(item)
        self.items.append(item)

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            return self.items[-1]

    def min(self):
        return None if len(self.min_stack) == 0 else self.min_stack[-1]


class SetOfStacks:

    def __init__(self,capacity):
        self.stacks = []
        self.capacity = capacity

    def empty(self):
        return len(self.stacks) == 0

    def pop(self):
        if self.empty():
            print("Set of stacks is empty. Nothing can be popped.")
            return None
        data = self.stacks[-1].pop()
        if self.stack_size(-1) == 0:
            self.stacks.pop()
        return data

    def pop_at(self, index):
        data = self.stacks[index].pop()
        if self.stack_size(index) == 0:
            self.stacks.pop(index)
        return data

    def push(self, item):
        if self.empty() or self.stack_size(-1) >= self.capacity:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def stack_size(self, stack_num):
        return len(self.stacks[stack_num])
