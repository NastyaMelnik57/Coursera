import sys

#we want to divide children in groups due to their ages in such way that the
#largest difference in age of any two children in one gorup will be at most 1#
#and we also want to minimize the number of groups
#The task is equal to cover points on the axe with segments of length 1
def MinGroupsNaive(C):
    R = set()
    i = 1
    n = len(C) - 1
    while i <= n:
        (l, r) = (C[i], C[i]+1)
        R.add((l,r))
        i += 1
        while i <= n and C[i] <= r:
                i += 1
    return len(R)

if __name__ == '__main__':
    input = sys.stdin.read()
    C = [float(i) for i in input.split()]
    print(MinGroupsNaive(C))
