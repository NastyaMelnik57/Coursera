# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    last, first = 0, 1
    if n == 0:
        return last
    for i in range(1, n):
        last, first = first % 10, (first + last) % 10
    return first

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
