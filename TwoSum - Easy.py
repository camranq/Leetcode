def bruteForceTwoSum(nums, target):
    # Iterate through the array using two nested loops.
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            # Check if the sum of the pair equals the target.
            if nums[i] + nums[j] == target:
                # If a solution is found, return the indices of the two numbers.
                return [i, j]

def TwoSum(nums, target):
    # Create an empty hash map to store numbers and their indices.
    num_to_index = {}  # This will be used to store (number, index) pairs.

    # Iterate through the array to find a pair of numbers that add up to the target.
    for i, num in enumerate(nums):
        # Calculate the complement that we need to find in the hash map.
        complement = target - num
        # Check if the complement exists in the hash map.
        if complement in num_to_index:
        # If the complement is found, return the indices of the two numbers.
            return [num_to_index[complement], i]
        # Otherwise, add the current number to the hash map.
        else:
            num_to_index[num] = i
    # Handle cases where no solution is found.

#Example
nums = [2, 7, 11, 15]
target = 9
result = TwoSum(nums, target)
print(result)  # This should print the indices of the two numbers that add up to the target.