#!/usr/bin/python3
import sys

def factorize(n):
    factors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            factors.append((i, n//i))
            break
        else:
            factors.append((n, 1))
            return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors fnumber")
        sys.exit(1)

    fnumber = sys.argv[1]
    with open(fnumber) as f:
        for line in f:
            n = int(line.strip())
            factors = factorize(n)
            print("{} = {} * {}".format(n, factors[0][0], factors[0][1]))

if __name__ == "__main__":
    main()

