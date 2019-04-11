def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    array_count = len(arr)
    result = 0
    for x in range(array_count):
        right_to_left = right_to_left + arr[x][x]
    print(right_to_left)
    for x in range(array_count):
            left_to_right = left_to_right + arr[x][array_count - 1 - x]
    print(left_to_right)

    if left_to_right >= right_to_left:
        result = left_to_right - right_to_left
    else:
        result = right_to_left - left_to_right
    return result

""" 
[11, 2,  4], 
[ 4, 5,  6], 
[10, 8,-12]
"""
def main():
    diagonale_array = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonalDifference(diagonale_array))

if __name__ == '__main__':
    main()