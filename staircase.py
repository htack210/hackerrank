
def staircase(n):
    base = n

    for i in range(0, base):
        padding = base - (i + 1)
        print((" " * padding), end='')
        print('#' * (i + 1))


def main():
    staircase(6)


main()
