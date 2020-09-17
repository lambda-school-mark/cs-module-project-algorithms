'''
Input: a List of integers
Returns: a List of integers
'''
import math
arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]


def product_of_all_other_numbers(arr):
    # copy the list
    copy = arr.copy()
    current_index = 0
    # loop through each index
    for num in arr:
        # take out current index
        product = [num for i, num in enumerate(
            arr) if i != current_index]
        # replace value at index with product of other indexes
        copy[current_index] = math.prod(product)
        # make index iterate with for loop
        current_index += 1
    # return arr
    print(copy)
    return copy


product_of_all_other_numbers(arr)

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
#            9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(
#         f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
