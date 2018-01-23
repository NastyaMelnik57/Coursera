import sys

#search in list step by step

def LinearSearch(A, low, high, key):
    for i in range(low, high):
        if A[i] == key:
            return i
    return 'NOT_FOUND'

if __name__ == '__main__':
    input = sys.stdin.read()
    tokens = input.split()
    A = [int(i) for i in tokens[:-1]]
    key = int(tokens[-1])
    print(LinearSearch(A, 0, len(A)-1, key))
