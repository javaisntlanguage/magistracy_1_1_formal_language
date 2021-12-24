class Tree:
    def __init__(self):
        self.name = str()
        self.left = None
        self.right = None

    def init_tree(self, expression, _tree):
        pos_symbol = -1
        is_bracket = False

        if _tree is None:
            _tree = Tree()

        for i in range(len(expression)):
            if (expression[i] == '+' or expression[i] == '-') and not is_bracket:
                pos_symbol = i
            elif (expression[i] == '*' or expression[i] == ':') and pos_symbol == -1 and not is_bracket:
                pos_symbol = i
            elif expression[i] == '(':
                is_bracket = True
            elif expression[i] == ')':
                is_bracket = False

        if pos_symbol == -1:
            _tree.name = expression
        else:
            _tree.name = _tree.name + expression[pos_symbol]
            _tree.left = self.init_tree(self.del_brackets(expression[0:pos_symbol]), _tree.left)
            _tree.right = self.init_tree(
                self.del_brackets(expression[pos_symbol + 1:len(expression)]), _tree.right)
        return _tree

    @staticmethod
    def del_brackets(expression):
        checked_brackets = 0
        for i in range(len(expression)):
            if expression[i] == '(':
                checked_brackets += 1
            elif expression[i] == ')':
                checked_brackets -= 1
            elif checked_brackets != 0:
                continue
            else:
                return expression

        return expression[1: len(expression) - 1]

    def print_tree(self, _tree, level=0):
        if _tree is not None:
            self.print_tree(_tree.left, level + 1)
            for i in range(level):
                print("  ", end='')
            print(_tree.name)
            self.print_tree(_tree.right, level + 1)

    def calc(self, _tree, x, y, z, y1, w, x2, w3):
        if _tree is not None:
            if _tree.name == "+":
                return self.calc(_tree.left, x, y, z, y1, w, x2, w3) + self.calc(_tree.right, x, y, z, y1, w, x2, w3)
            elif _tree.name == "-":
                return self.calc(_tree.left, x, y, z, y1, w, x2, w3) - self.calc(_tree.right, x, y, z, y1, w, x2, w3)
            elif _tree.name == ":":
                return self.calc(_tree.left, x, y, z, y1, w, x2, w3) / self.calc(_tree.right, x, y, z, y1, w, x2, w3)
            elif _tree.name == "*":
                return self.calc(_tree.left, x, y, z, y1, w, x2, w3) * self.calc(_tree.right, x, y, z, y1, w, x2, w3)
            elif _tree.name == "x":
                return x
            elif _tree.name == "y":
                return y
            elif _tree.name == "z":
                return z
            elif _tree.name == "y1":
                return y1
            elif _tree.name == "w":
                return w
            elif _tree.name == "x2":
                return x2
            elif _tree.name == "w3":
                return w3
            else:
                return float(_tree.name)
        else:
            return 0


oneTree = Tree()
Expression = "x*(y+z-y1)+w*x2:w3"

oneTree = oneTree.init_tree(Expression, oneTree)
print("Дерево:\n")
oneTree.print_tree(oneTree)
x, y, z, y1, w, x2, w3 = 1, 1, 1, 1, 2, 2, 2
valueExpression = oneTree.calc(oneTree, x, y, z, y1, w, x2, w3)
print("Ответ: ", valueExpression)
