#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def hourglassSum(arr):
    next_arr = []  # Holds 3-member subset of main array.
    temp_arr = []  # This will hold the values for summing.
    sum_arr = []  # Hold running sum of sub arrays.

    # These change what rows of the subset are to be used.
    # They move the sets vertically down the 6x6 grid.
    y = 0
    z = 3
    for y in range(4):  # There are 4 moves down.
        next_arr = arr[y:z]  # This will hold 3 rows at a time.
        # These move across the 6x6 grid one column at a time
        # with each grouping holding 3 numbers. They are reset
        # after each hourglass (3x3) grid is processed.
        s = 0
        e = 3
        for _ in range(4):  # There are 4 moves across
            for i, row in enumerate(next_arr, start=1):
                if i in (1, 3):
                    temp_arr.extend(row[s:e])  # Holds 3 numbers across
                else:
                    # Gets middle number of second row.
                    temp_arr.extend(row[s+1:e-1])

                if i == 3:
                    # Sum the numbers in temp_array and append it to sum_arr.
                    sum_arr.append(sum(temp_arr))
                    temp_arr.clear()  # Clear temp_arr for next 3x3 grid.
            s += 1
            e += 1
        y += 1
        z += 1
    return max(sum_arr)


def main():

    # hg_array = [[1, 1, 1, 0, 0, 0],
    #             [0, 1, 0, 0, 0, 0],
    #             [1, 1, 1, 0, 0, 0],
    #             [0, 0, 2, 4, 4, 0],
    #             [0, 0, 0, 2, 0, 0],
    #             [0, 0, 1, 2, 4, 0]]
    # hg_array = [[1, 1, 1, 0, 0, 0],
    #             [0, 1, 0, 0, 0, 0],
    #             [1, 1, 1, 0, 0, 0],
    #             [0, 9, 2, -4, -4, 0],
    #             [0, 0, 0, -2, 0, 0],
    #             [0, 0, -1, -2, -4, 0]]
    # 13 is correct

    hg_array = [[0, -4, -6, 0, -7, -6],
                [-1, -2, -6, -8, -3, -1],
                [-8, -4, -2, -8, -8, -6],
                [-3, -1, -2, -5, -7, -4],
                [-3, -5, -3, -6, -6, -6],
                [-3, -6, 0, -8, -6, -7]]
    # Correct answer -19

    # hg_array = [[-1, 1, -1, 0, 0, 0],
    #             [0, -1, 0, 0, 0, 0],
    #             [-1, -1, -1, 0, 0, 0],
    #             [0, -9, 2, -4, -4, 0],
    #             [-7, 0, 0, -2, 0, 0],
    #             [0, 0, -1, -2, -4, 0]]
    # Correct answer = 0
    print(hourglassSum(hg_array))


main()
