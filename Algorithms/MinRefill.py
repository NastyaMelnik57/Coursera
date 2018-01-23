import sys

def MinRefills(x,n,L):
    numRefills = 0
    currentRefill = 0
    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and x[currentRefill + 1] - x[lastRefill] <= L):
            currentRefill = currentRefill + 1
        if currentRefill == lastRefill:
            return 'IMPOSSIBLE'
        if currentRefill <= n:
            numRefills = numRefills + 1
    return numRefills

if __name__ == '__main__':
    input = sys.stdin.read()
    tokens = input.split()
    x = [int(i) for i in tokens[:-2]]
    n = int(tokens[-2])
    L = int(tokens[-1])
    print(MinRefills(x,n,L))
