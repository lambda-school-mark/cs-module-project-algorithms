'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # initialize a left and right pointer
    # left is 033
    left = 0
    # right is last in arr
    right = len(arr) - 1
    new_array = [0 for each in range(len(arr))]

    for i in arr:
        if i == 0:
            new_array[right] = i
            right -= 1
        else:
            new_array[left] = i
            left += 1
    return new_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
