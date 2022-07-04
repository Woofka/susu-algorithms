n = 5
tree = [0 for i in range(4*n+1)]


def build(seq, v, tl, tr):
    if tl == tr:
        tree[v] = seq[tl]
    else:
        tm = (tr + tl) // 2
        build(seq, v*2, tl, tm)
        build(seq, v*2+1, tm+1, tr)
        tree[v] = tree[v*2] + tree[v*2+1]


def smth():
    pass


# ----- MAIN PROGRAM -----
if __name__ == "__main__":
    b = [1, 2, 3, 4, 5]
    build(b, 1, 0, n-1)
    print(tree)
