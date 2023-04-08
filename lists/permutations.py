# Python function t0 find all the permutations of the members of a list.

def permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        m = nums[i]
        rem_list = nums[:i] + nums[i+1:]
        for p in permutations(rem_list):
            result.append([m] + p)
    return result

nums = [1,2,3,4]
print("Original list:")
print(nums)
print("Permutations of the members of the said list:")
print(permutations(nums))
nums = [-100,-300,0]
print("\nOriginal list:")
print(nums)
print("Permutations of the members of the said list:")
print(permutations(nums))

