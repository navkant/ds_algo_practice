import sys
sys.setrecursionlimit(10**6)

def printNRec(n):
    if n == 0:
        return
    print(n, end = ' ')
    printNRec(n-1)

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    printNRec(N)
    return

if __name__ == '__main__':
    main()