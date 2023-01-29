# create an empty array which has length 5
arr = [0] * 5

# iteration using for loop
for i in range(len(arr)):
    print(arr[i])

print("------- x -------")

# iteration using while loop
arr = [10, 20, 30, 40]
idx = 0

# while loop
while idx < len(arr):
    print(arr[idx])
    idx += 1