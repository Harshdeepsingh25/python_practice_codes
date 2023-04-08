# Python function to remove duplicates from a list while preserving the order.

from collections import OrderedDict
def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))

nums = [1,2,4,3,5,4,6,9,2,1]
print("Original lists:")
print(nums)
result = remove_duplicates(nums)
print("Remove duplicates from the said list while preserving the order:")
print(result)
chars = ['a','a','b','a', 'a', 'c', 'c', 'c','d','e','a', 'b', 'b', 'b']
print("\nOriginal lists:")
print(chars)
result = remove_duplicates(chars)
print("Remove duplicates from the said list while preserving the order:")
print(result)