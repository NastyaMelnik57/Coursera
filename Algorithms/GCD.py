#Define greatest common divisor using Euclidian algorithm

def GCD(a, b):
    if b == 0:
        return a
    else:
        a1 = max(b, a) % min(b, a)
    return GCD(b, a1)

def main():
    a, b = map(int, input().split())
    print(GCD(a, b))

if __name__ == "__main__":
    main()

