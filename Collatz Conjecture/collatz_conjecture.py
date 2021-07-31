'''
Each number is obtained from the previous iteration.
Start with x
If x is odd 3x+1
If x is even x/2
Repeat

So far all numbers tested end with a 4,2,1 loop.

Will all positive integers eventually reach 1?
Do all result in the same 4,2,1 loop
'''

import sys, math

def collatz(x):
    # Do collatz stuff
    x = int(x)
    result = []

    print("collatz: " + str(x))
    while(x >= 1):
        result.append(math.trunc(x))
        # Abort if 1 has been reached
        if x == 1:
            break

        if x % 2 == 0:
            x = x / 2
        else:
            x = (x * 3) + 1

    return result


def main(args):
    results = "ERROR: No result"
    if len(args) >= 1:
        if args[0].isdigit():
            results = collatz(args[0])
        else:
            print("Please supply a number like this: \n" + sys.argv[0] + " 12")
    else:
        startNum = input("Please enter a starting number: ")
        if startNum.isdigit():
            results = collatz(startNum)
    
    print(results)


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])