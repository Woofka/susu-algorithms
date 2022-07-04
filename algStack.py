"""
Функции для работы со стеками. Стек представляется в виде листа,
где 0-ой элемент обозначает число элементов стека
"""


# ----------------------------------------- #
# ------------ BASIC PROCEDURES ----------- #
# ----------------------------------------- #
def st_isempty(st):
    """
    Function
    Return True if stack <st> is empty
    Return False if stack <st> isn't empty
    """
    if st[0] == 0:
        return True
    else:
        return False


def st_push(st, elem):
    """
    Procedure
    Add <elem> into a stack <st>
    """
    if len(st) > st[0]+1:
        st[st[0]:st[0]+2] = st[st[0]], elem
        st[0] += 1
    else:
        st[st[0]:st[0] + 1] = st[st[0]], elem
        st[0] += 1


def st_pop(st):
    """
    Procedure
    If possible pop the top element of stack <st>
    """
    if st[0] > 0:
        st[0] -= 1


def st_top(st):
    """
    Function
    Return the top element of stack <st>
    """
    if st[0] > 0:
        return st[st[0]]
    else:
        print('There\'re no elements in the stack')
        return 0


# -------------------------------------------- #
# ------------ ADVANCED PROCEDURES ----------- #
# -------------------------------------------- #
def st_poptop(st):
    """
    Function
    If possible return the top element of stack <st> and pop it
    """
    if st[0] > 0:
        st[0] -= 1
        return st[st[0]+1]
    else:
        print('There\'re no elements in the stack')
        return 0


def st_amount(st):
    """
    Function
    Return an amount of elements of stack <st>
    """
    return st[0]


def st_elems(st):
    """
    Function
    Return a list of elements of stack <st>
    """
    return st[1:st[0]+1]


# ------ MAIN PROGRAM ------
