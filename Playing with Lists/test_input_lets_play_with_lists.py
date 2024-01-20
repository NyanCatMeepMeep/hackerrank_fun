import lets_play_with_lists as lpwl

# Insert tests
my_array = []
print('*********Insert Tests')
my_array = lpwl.insert(my_array,8,0)
my_array = lpwl.insert(my_array,12,0)
my_array = lpwl.insert(my_array,8,0)
my_array = lpwl.insert(my_array,7,0)
my_array = lpwl.insert(my_array,6,0)
my_array = lpwl.insert(my_array,5,0)
my_array = lpwl.insert(my_array,4,0)
my_array = lpwl.insert(my_array,3,0)
my_array = lpwl.insert(my_array,2,0)
my_array = lpwl.insert(my_array,1,0)
# my_array = insert(my_array,4,9) Confirmed fail and exit
my_array = lpwl.insert(my_array,6,3)

# remove tests
print('*********Remove Tests')
my_array = lpwl.remove(my_array, 8)
my_array = lpwl.remove(my_array, 19)

# append tests
print('*********Append Tests')
my_array = lpwl.append(my_array,42)

# sort tests
# scramble a bit first
print('*********Sort Shortcut Tests')
print('Prep')
my_array = lpwl.insert(my_array,99,4)
my_array = lpwl.insert(my_array,69,7)
my_array = lpwl.insert(my_array,28,3)
print('sort')
my_array = lpwl.sort_shortcut(my_array)

print('*********Pop Tests')
my_array = lpwl.pop(my_array, 3)
my_array = lpwl.pop(my_array, 22)

print('*********Reverse Tests')
my_array = lpwl.reverse(my_array)