import sys
import math

# Check if a file is passed as an argument
if len(sys.argv) != 2:
    print("Usage: factors fnumber")
    sys.exit(1)

# Open the file
try:
    f = open(sys.argv[1], 'r')
except IOError:
    print("File not found")
    sys.exit(1)

# Read the file line by line
for line in f:
    # Convert line to an integer
    n = int(line)

    # Initialize variables for factorization
    p = 2
    q = 1

    # Find the factors of n
    while p <= n:
        if n % p == 0:
            q = n // p
            break
        p += 1

    # Print the factorization
    print(str(n) + '=' + str(p) + '*' + str(q))

f.close()
sys.exit(0)

