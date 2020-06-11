'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here

    # sorting array here
    arr.sort()

    # start the index
    index = 0

    # Iterating over intergers and incrementing by 2
    while (index < len(arr)):
        # If interger and current index are not equal to the following interger thats the solution
        if arr[index] != arr[index + 1]:
            return arr[index]
        index += 2

    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
