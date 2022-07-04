"""
Класс стека. Стек представляется в виде листа,
где 0-ой элемент обозначает число элементов стека
"""


class Stack:
    def __init__(self):
        self.stack = [0]

    # ----------------------------------------- #
    # ------------ BASIC PROCEDURES ----------- #
    # ----------------------------------------- #
    def isempty(self):
        """
        Function
        Return True if stack <st> is empty
        Return False if stack <st> isn't empty
        """
        if self.stack[0] == 0:
            return True
        else:
            return False

    def push(self, elem):
        """
        Procedure
        Add <elem> into a stack <st>
        """
        if len(self.stack) > self.stack[0]+1:
            self.stack[self.stack[0]:self.stack[0]+2] = self.stack[self.stack[0]], elem
            self.stack[0] += 1
        else:
            self.stack[self.stack[0]:self.stack[0] + 1] = self.stack[self.stack[0]], elem
            self.stack[0] += 1

    def pop(self):
        """
        Procedure
        If possible pop the top element of stack <st>
        """
        if self.stack[0] > 0:
            self.stack[0] -= 1

    def top(self):
        """
        Function
        Return the top element of stack <st> or '0' if there're no elements
        """
        if self.stack[0] > 0:
            return self.stack[self.stack[0]]
        else:
            return 0

    # -------------------------------------------- #
    # ------------ ADVANCED PROCEDURES ----------- #
    # -------------------------------------------- #
    def poptop(self):
        """
        Function
        If possible return the top element of stack <st> and pop it or '0' if there're no elements
        """
        if self.stack[0] > 0:
            self.stack[0] -= 1
            return self.stack[self.stack[0]+1]
        else:
            return 0

    def amount(self):
        """
        Function
        Return an amount of elements of stack <st>
        """
        return self.stack[0]

    def elems(self):
        """
        Function
        Return a list of elements of stack <st>
        """
        return self.stack[1:self.stack[0]+1]
