# Todo: Basic For loop
import numpy

speeds = [10, 20, 30]
for speed in speeds:
    print(speed)

# Todo: Basic While loop
count = 1
while count <= 3:
    print(count)
    count += 1

# Todo: Loop with index - enumerate()
for index, speed in enumerate(speeds):
    print(index, speed)

# Todo: Looping over multiple lists - zip()
times = [1.0, 1.5, 2.0]
for time, speed in zip(times, speeds):
    print(time, speed)

# Todo: Looping in reverse
for i in reversed(range(5)):  # 5 elements
    print(i)

# Todo: Looping over dictionaries
sensor = {"camera": "front.png", "speed": 30, "steer": 5}
for key, value in sensor.items():
    print(key, value)

# Todo: Loop with conditions
for speed in speeds:
    if speed >= 20:
        print(speed)

# Todo: Loop control - break and continue
# break: stop the loop early
for speed in speeds:
    if speed >= 20:
        break
    print(speed)

# continue: skip to next iteration
for speed in speeds:
    if speed == 20:
        continue  # iteration gets skipped here and next iteration is done.
    print(speed)

# Todo: Nested loops
for i in range(3):
    for j in range(3):
        print(i, j)

# Todo: List comprehension - advanced looping
squared_speeds = [speed ** 2 for speed in speeds]  # syntax: [expression for item in iterable condition(optional)]
print(squared_speeds)

# Todo: Performance tip - Numpy arrays are faster than loops
arr1 = [1, 2, 3]
print(arr1 * 3)  # * in normal list, repeats the list instead of multiplying each element

# difference between using normal list and array for element wise multiplication
out = []
for x in arr1:
    out.append(x * 2)
print(out)

arr = numpy.array([1, 2, 3])  # performs element-wise multiplication instead of repeating lists.
print(arr * 2)  # vectorized(operate on entire array at once than looping) preferred over loops.
