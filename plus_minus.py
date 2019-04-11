
#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    positive = 0
    negotive = 0
    zero = 0
    for item in arr:
        if item != 0:
            if item < 0:
                negotive += 1
            if item > 0:
                positive += 1
        else:
            zero += 1

    print('{:f}'.format(positive / len(arr)))
    print('{:f}'.format(negotive / len(arr)))
    print('{:f}'.format(zero / len(arr)))


if __name__ == '__main__':

    arr = [-4, 3, -9, 0, 4, 1]

    plusMinus(arr)