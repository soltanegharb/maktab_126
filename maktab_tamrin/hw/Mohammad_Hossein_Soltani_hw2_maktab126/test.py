# old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# new_list = old_list
# print(new_list is old_list)
# new_list[2][2] = 9

# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))

# print('New List:', new_list)
# print('ID of New List:', id(new_list))
# old_list[2][2]= 'b'
# print('New List:', new_list)
# print('ID of New List:', id(new_list))

# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))

# new_list = [1, 2, 3]

# print('New List:', new_list)
# print('ID of New List:', id(new_list))

# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))

# import copy
# new_list = copy.deepcopy(old_list)
# print('New List:', new_list)
# print('ID of New List:', id(new_list))
# print('Old List:', old_list)
# print('ID of Old List:', id(old_list))
# print(new_list is old_list)

o_list = [1, 2, [3, 4]]
n_list = o_list.copy()

print('Old List:', o_list)
print('id of Old List:', id(o_list))
print('New List:', n_list)
print('id of New List:', id(n_list))
