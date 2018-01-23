#Uses python3

def calc_fib(n):
    last, first = 0, 1
    if n == 0:
    	return last
    for i in range(1, n):
        last, first = first, last + first
    return first

n = int(input())
print(calc_fib(n))

