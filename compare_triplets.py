def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(0, len(a)):
        if a[i] == b[i]:
            continue
        if a[i] > b[i]:
            alice += 1
        else:
            bob += 1
    return [alice, bob]


def main():
    print(compareTriplets([17, 28, 30], [99, 16, 8]))


main()
