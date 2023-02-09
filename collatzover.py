import sys

if not __name__ == "__main__":
    sys.exit()

def is_even(n: int):
    return n % 2 == 0

numbers_found = []

def test(n):
    global numbers_found
    
    if n == 1:
        print("Not a counterexample...")
        numbers_found = []
        return False

    if n in numbers_found:
        print("Found a counterexample!")
        print("The Collatz Conjecture is now disproven!")
        numbers_found = []
        return True

    numbers_found.append(n)

    if is_even(n):
        test(n / 2)
    else:
        test(n * 3 + 1)

n = 1

while True:
    print("Testing number " + str(n) + "...")
    
    if test(n):
        break
    
    n += 1

