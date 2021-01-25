# python3

import sys
import threading

def fillDepth(parents, i , depth):
    if parents[i] == -1:
        depth[i] = 1
        return
    elif depth[i] != 0:
        return

    else:
        if depth[parents[i]] == 0:
            fillDepth(parents, parents[i], depth)
        if depth[i] == 0:
            depth[i] = 1 + depth[parents[i]]

def compute_height(n, parents):
    # Replace this code with a faster implementation
    depth = [0 for i in range(n)]

    for i in range(n):
        fillDepth(parents, i, depth)
    return max(depth)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
