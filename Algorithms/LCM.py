# Uses python3
#Find the least common multiple of a and b
import sys

def gcd_naive(a, b):
    if b == 0:
        return a
    else:
        a1 = a % b
    return gcd_naive(b,a1)

def lcm_naive(a, b):
    return a*b//gcd_naive(a,b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

