arr = [1, 2, 3, 4]

# declare an empty array
new_arr = [0] * len(arr)

for i in range(len(arr)):
    # reading value from arr and inserting it in new_arr
    new_arr[i] = arr[i]

print(new_arr)