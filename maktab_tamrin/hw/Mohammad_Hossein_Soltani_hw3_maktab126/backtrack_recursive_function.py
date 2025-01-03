def find_subsets(nums):
    # Here we defined a backtrack in the find_subsets function
    # just for simplicity for user.
    def backtrack(start, path):
        subsets.append(path)
        for i in range(start, len(nums)):
            subsets.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
    
    subsets = []
    backtrack(0, [])
    return subsets

# Example usage:
nums = [1, 2, 3]
all_subsets = find_subsets(nums)
print(all_subsets)
