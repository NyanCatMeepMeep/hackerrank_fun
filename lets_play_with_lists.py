# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

def insert(array, num, pos):
    #  check is the list is empty, if it is empty and the position is greater than zero, return an error
    #  if the array is not empty but the position is beyond what can be reached, return an error
    #  if the array is good, insert it into the position

    temp_arr = array

    if len(array) == 0 and pos > 1:
        print("Oops- looks like this array doesn't have enough values to insert into your desired location! Skipping this request.")
        pass
    elif len(array) == 0 and pos == 0:
        temp_arr.append(num)
    elif len(array) != 0 and pos > len(array):
        print("Oops- looks like this array doesn't have enough values to insert into your desired location! Skipping this request.")
        pass
    elif len(array) != 0 and pos == len(array):
        temp_arr.append(num)
    elif len(array) != 0 and pos < len(array):
        temp_arr.insert(pos,num)

    # print('Your array now looks like: ')
    # print(temp_arr)
    return temp_arr

def remove(array, num):
    temp_arr = array
    value_count = 0
    for value in array:
        if value == num:
            value_count = value_count + 1

    if value_count == 0:
        print("Oops, it doesn't look like that value is in this list.  Skipping this request.")
        pass
    elif value_count != 0:
        temp_arr.remove(num)

    # print('Your array now looks like: ')
    # print(temp_arr)
    return temp_arr

def append(array, num):
    temp_arr = array

    temp_arr.append(num)

    # print('Your array now looks like: ')
    # print(temp_arr)
    return temp_arr

def sort_shortcut(array):
    temp_arr = array

    temp_arr.sort()

    print('Your array now looks like: ')
    print(temp_arr)
    return temp_arr

def pop(array, pos):
    temp_arr = array

    if len(temp_arr) < pos:
        print("Oops- looks like this array doesn't have enough values to complete this pop request! Skipping this request.")
        pass
    else:
        temp_arr.pop(pos)

    print('Your array now looks like: ')
    print(temp_arr)
    return temp_arr

def reverse(array):
    temp_arr = array

    temp_arr.reverse()

    print('Your array now looks like: ')
    print(temp_arr)
    return temp_arr
