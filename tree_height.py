# python3

import sys
import threading

def compute_height(a, parents):
    root = None
    position = [[] for _ in range(a)]
    for i in range(a):
        if parents[i] == -1:
            root = i
        else:
            position[parents[i]].append(i)



    def max_height(b):
        height = 1
        if not position[b]:
            return height
        else:

            for child in position[b]:
                height = max(height, max_height(child))
            return height + 1
    return max_height(root)




def main():
    text = input("Enter F - I: ")
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))

    elif "F" in text:

        filename = input()
        file_path = './test/' + filename

        if "a" not in filename:
            try:
                with open(file_path) as f:

                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
            except Exception as e:
                print("Error:", str(e))
                return
        else:

            print("invalid filename")
            return
    print(compute_height(n, parents))


if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10 ** 7)  # max depth of recursion
    threading.stack_size(2 ** 27)  # new thread will get stack of such size
    threading.Thread(target=main).start()