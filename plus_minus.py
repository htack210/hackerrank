def plusMinus(arr):
    pos_num = 0
    zero_num = 0
    neg_num = 0
    denom = len(arr)

    for i in range(0, denom):
        if arr[i] > 0:
            pos_num += 1
        elif arr[i] < 0:
            neg_num += 1
        else:
            zero_num += 1
    print(f'{pos_num/denom:.6f}')
    print(f'{neg_num/denom:.6f}')
    print(f'{zero_num/denom:.6f}')


def main():
    plusMinus([1, 1, 0, -1, -1])


main()
