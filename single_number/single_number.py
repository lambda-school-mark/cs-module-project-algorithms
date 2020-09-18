'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # # go through the array
    # for num in arr:
    #     # figure out how many of each integer
    #     count = arr.count(num)
    #     # if there is only one instance of given number
    #     if count == 1:
    #         #return it
    #         return num

    nums = set()

    for item in arr:
        if item in nums:
            nums.remove(item)

        else:
            nums.add(item)

    return nums.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
