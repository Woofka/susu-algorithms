class bstNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class bst:
    def __init__(self):
        self.root = None

    def printPreOrder(self):
        """ Вызывает процедуру прямого обхода дерева """
        if self.root is None:
            print("Дерево пустое", end="")
        else:
            self.__preOrder(self.root)

    def __preOrder(self, node):
        """ Прямой обход дерева """
        if node is not None:
            print(node.value, end=" ")
            self.__preOrder(node.left)
            self.__preOrder(node.right)

    def printInOrder(self):
        """ Вызывает процедуру обратного обхода дерева """
        if self.root is None:
            print("Дерево пустое", end="")
        else:
            self.__inOrder(self.root)

    def __inOrder(self, node):
        """ Обратный обход дерева """
        if node is not None:
            self.__inOrder(node.left)
            print(node.value, end=" ")
            self.__inOrder(node.right)

    def printPostOrder(self):
        """ Вызывает процедуру концевого обхода дерева """
        if self.root is None:
            print("Дерево пустое", end="")
        else:
            self.__postOrder(self.root)

    def __postOrder(self, node):
        """ Концевой обход дерева """
        if node is not None:
            self.__postOrder(node.left)
            self.__postOrder(node.right)
            print(node.value, end=" ")

    def searchNode(self, value):
        """ Возвращает узел со значением <value>, если такого нет, то возразает потенциального предка,
            если такого нет (т.е. если дерево пустое), то возращает None """
        prevNode = None
        curNode = self.root
        result = None
        searchFinished = False
        while not searchFinished:
            if curNode is None:
                searchFinished = True
                result = prevNode
            else:
                if value == curNode.value:
                    searchFinished = True
                    result = curNode
                else:
                    if value > curNode.value:
                        prevNode = curNode
                        curNode = curNode.right
                    else:
                        prevNode = curNode
                        curNode = curNode.left
        return result

    def searchNodeValue(self, value):
        """ Возвращает True, если есть узел со значнием <value>, иначе возвращает False """
        node = self.searchNode(value)
        result = False
        if node is not None:
            if node.value == value:
                result = True
        return result

    @staticmethod
    def __searchNodeNext(node):
        """ Возвращает следующий по значению узел после <node> """
        nextNode = None
        if node.right is not None:
            nextNode = node.right
            searchFinished = False
            while not searchFinished:
                if nextNode.left is not None:
                    nextNode = nextNode.left
                else:
                    searchFinished = True
        return nextNode

    def addNode(self, value):
        """ Добавляет узел со значением <value> """
        if self.root is None:               # если дерево пустое
            self.root = bstNode(value)      # то присвоить корню узел со значением <value>
        else:
            done = False
            parent = self.root
            while not done:
                if value >= parent.value:
                    if parent.right is not None:
                        parent = parent.right
                    else:
                        parent.right = bstNode(value, parent)
                        done = True
                else:
                    if parent.left is not None:
                        parent = parent.left
                    else:
                        parent.left = bstNode(value, parent)
                        done = True

    def delNode(self, value):
        """ Удаляет из дерева узел со значением <value>, если таковой имеется """
        thisNode = self.searchNode(value)
        if thisNode is not None:
            if thisNode.value == value:
                parent = thisNode.parent
                if thisNode.left is None and thisNode.right is None:       # удаляемый элемент - лист
                    if parent is None:
                        self.root = None
                    else:
                        if parent.left is thisNode:
                            parent.left = None
                        else:
                            parent.right = None
                else:
                    if thisNode.left is None or thisNode.right is None:    # удаляемый элемент имеет 1 потомка
                        if thisNode.left is None:
                            if parent is None:
                                self.root = thisNode.right
                                self.root.parent = None
                            else:
                                if parent.left is thisNode:
                                    parent.left = thisNode.right
                                    parent.left.parent = parent
                                else:
                                    parent.right = thisNode.right
                                    parent.right.parent = parent
                        else:
                            if parent is None:
                                self.root = thisNode.left
                                self.root.parent = None
                            else:
                                if parent.left is thisNode:
                                    parent.left = thisNode.left
                                    parent.left.parent = parent
                                else:
                                    parent.right = thisNode.left
                                    parent.right.parent = parent
                    else:                                                  # удаляемый элемент имеет 2 потомков
                        nextNode = self.__searchNodeNext(thisNode)
                        self.delNode(nextNode.value)
                        if parent is None:
                            self.root = nextNode
                            self.root.parent = None
                            if thisNode.right is not None:
                                thisNode.right.parent = nextNode
                                nextNode.right = thisNode.right
                            else:
                                nextNode.right = thisNode.right
                            thisNode.left.parent = nextNode
                            nextNode.left = thisNode.left
                        else:
                            if parent.left is thisNode:
                                parent.left = nextNode
                                nextNode.parent = parent
                            else:
                                parent.right = nextNode
                                nextNode.parent = parent
                            if thisNode.right is not None:
                                thisNode.right.parent = nextNode
                                nextNode.right = thisNode.right
                            else:
                                nextNode.right = thisNode.right
                            thisNode.left.parent = nextNode
                            nextNode.left = thisNode.left


# ----- MAIN PROGRAM -----
if __name__ == "__main__":
    tree = bst()
    for i in [8, 5, 7, 6, 3, 4, 1, 2, 10, 9, 12, 11, 13]:
        tree.addNode(i)
    print("Прямой обход:    ", end='')
    tree.printPreOrder()
    print()
    print("Обратный обход:  ", end='')
    tree.printInOrder()
    print()
    print("Концевой обход:  ", end='')
    tree.printPostOrder()
    print()
