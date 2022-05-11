class Node:
    def __init__(self, value):
        self.value = value
        self.children = set()
        self.parent = None

    def addChild(self, node):
        self.children.add(node)
        node.parent = self
        return node

    def detachFromParent(self):
        if (self.parent != None):
            self.parent.children.remove(self)
            self.parent = None

    def makeRoot(self):
        parent = self.parent
        if (parent != None):
            parent.makeRoot()
            self.detachFromParent()
            self.addChild(parent)

    def printNode(self, indent=""):
        print(indent + str(self.value))
        indent += "    "
        num = 1
        for child in self.children:
            child.printNode(indent)


eight = Node(8)
ten = Node(10)
four = Node(4)
two = Node(2)
one = Node(1)
three = Node(3)
eight.addChild(four)
eight.addChild(ten)
four.addChild(two)
two.addChild(one)
two.addChild(three)

print("input:")
eight.printNode()

print("Changing root to 2")
two.makeRoot()
two.printNode()