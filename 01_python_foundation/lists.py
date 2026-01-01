# Todo: Necessary imports
import copy
import numpy as np

# Todo: Creating lists
speeds = [10, 20, 30]  # same data type
data = [10, "car", True, 3.5]  # mixed data type

# Todo: Indexing
print(speeds[0])
print(speeds[2])
print(speeds[-1])  # last element
print(speeds[1:3])  # outer limit excluded
print(speeds[-3:])  # full list

# Todo: Modifying lists
speeds[1] = 25
speeds.append(40)  # add one element at end
speeds.insert(3, 35)  # add an element at an index position
speeds.extend([50, 60])  # add elements as iterable
print(speeds)

# Todo: Removing items
speeds.remove(60)  # removes a value
print(speeds)
del speeds[0]  # removes using index position
print(speeds)
speeds.pop(0)  # removes using index position
print(speeds)
speeds.pop()  # removes last element
print(speeds)

# Todo: Looping over lists
for item in speeds:  # iterates over each element in the iterable
    print(item)

for item in enumerate(speeds):  # provides index position along with value
    print(item)

for index, value in enumerate(speeds):
    print(index, value)

# Todo: List slicing
window = speeds[1:3]
print(window)
last_3 = speeds[-3:]
print(last_3)
except_1 = speeds[1:]
print(except_1)
except_last = speeds[:-1]
print(except_last)

# Todo: List Comprehension
speeds_over_30 = [item for item in speeds if item > 30]  # to print speeds over 30
print(speeds_over_30)

# Todo: Sorting lists
unsorted_list = [1, 3, 5, 2, 4]
unsorted_list.sort()
print(unsorted_list)
sorted_list = sorted(unsorted_list)
print(sorted_list)
bounding_boxes = [(0, 0, 40, 40), (0, 0, 20, 20)]  # bounding box in format (x_min, y_min, width, height)
bounding_boxes.sort(key=lambda b: b[2])  # sorting based on index position - 2. b is an item in list.
print(bounding_boxes)

# Todo: Copying lists
# wrong shallow copy
a = [1, 2, 3]
c = a
print(c)  # c does not get a new list. both points to the same list in memory
c[0] = 100
print(c, a)  # the change made to list c affects list 'a' as well. this is called a shallow reference, not a copy.

# shallow copy - only copies the top level. inner lists (a = [[1,2], [3,4]]) will not be copied.
d = [1, 2, 3]
e = d.copy()
e[0] = 100
print(d, e)  # now both d and e are independent lists. e is copied from d and made changes.

# deep copy - copies both outer and all inner lists.
f = [[1, 2], [3, 4]]  # list with inner lists.
g = copy.deepcopy(f)
g[0][0] = 5
print(f)
print(g)

# Todo: List of lists
trajectories = [[1, 2], [3, 4], [5, 6]]
print(trajectories[0][0])

# Todo: Checking Membership
print(40 in speeds)  # used for label filtering

# Todo: Length of list
print(len(speeds))

# Todo: Concatenation
list_a = [1, 2, 3]
list_b = [1, 2, 3]
concatenated_list = list_a + list_b
print(concatenated_list)

# Todo: Clearing list
list_b.clear()
print(list_b)

# Todo: Converting to numpy array
speeds_array = np.array(speeds)
print(speeds)
print(speeds_array)