# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

two_max = [min(a[0], a[1]), max(a[0], a[1])]

for i in range(2, n):
    two_max = sorted([two_max[0], two_max[1], a[i]])[1:]

print(two_max[0] * two_max[1])
