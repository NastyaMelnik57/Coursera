import sys

#search in sorted list

def BinarySearch(A, low, high, key):
    while low <= high:
        mid = low + (high-low)//2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return (low - 1) #in case if there is no key in list


if __name__ == '__main__':
    input = sys.stdin.read()
    tokens = input.split()
    A = [int(i) for i in tokens[:-1]]
    key = int(tokens[-1])
    print(BinarySearch(A, 0, len(A)-1, key))
