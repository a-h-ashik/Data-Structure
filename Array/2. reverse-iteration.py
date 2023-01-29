arr = [10, 20, 30, 40]

# reverse iteration using for loop
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])

print("------- x -------")

# reverse iteration using while loop
last_idx = len(arr) - 1
while last_idx >= 0:
    print(arr[last_idx])
    last_idx -= 1