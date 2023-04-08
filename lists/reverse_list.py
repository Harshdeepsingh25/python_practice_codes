#Python function to reverse a list at a specific location.

def reverse_list_in_location(lst, start_pos, end_pos):
    while start_pos < end_pos:
        lst[start_pos], lst[end_pos] = lst[end_pos], lst[start_pos]
        start_pos += 1
        end_pos -= 1
    return lst

nums = [10,20,30,40,50,60,70,80]
start_pos = 2
end_pos = 4
print("Original list:")
print(nums)
print("Reverse elements of the said list between index position "+str(start_pos)+ " and "+str(end_pos))
print(reverse_list_in_location(nums,start_pos,end_pos))
start_pos = 6
end_pos = 7
print("\nOriginal list:")
print(nums)
print("Reverse elements of the said list between index position "+str(start_pos)+ " and "+str(end_pos))
print(reverse_list_in_location(nums,start_pos,end_pos))
start_pos = 0
end_pos = 7
print("\nOriginal list:")
print(nums)
print("Reverse elements of the said list between index position "+str(start_pos)+ " and "+str(end_pos))
print(reverse_list_in_location(nums,start_pos,end_pos))