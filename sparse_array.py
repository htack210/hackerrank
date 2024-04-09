def matchingStrings(stringList, queries):
    counts = []
    for i in queries:
        counts.append(stringList.count(i))
    return counts


def main():
    queries = ['aba', 'xzxb', 'ab']
    stringList = ['aba', 'baba', 'aba', 'xzxb']
    print(matchingStrings(stringList, queries))


main()
