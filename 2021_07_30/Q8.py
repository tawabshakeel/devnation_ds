
def twoSum(self, nums: list[int], target: int) -> list[int]:

    # declaring a dictionary to keep track of all the values seen so far
    # in the value to index (key value pair)
    visited_numbers = dict()

    # iterating over the entire array
    for index, num in enumerate(nums):

        # subtracting the num from the target to search for its pair
        number_to_be_search = target - num

        # if the pair is found, return the index of the both numbers
        if number_to_be_search in visited_numbers:
            return [index, visited_numbers[number_to_be_search]]
            # otherwise we simply add it to out dictionary for future lookup
        else:
            return  visited_numbers[num] = index