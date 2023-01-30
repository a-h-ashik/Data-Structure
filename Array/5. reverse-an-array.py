# out of palce
arr = [1, 2, 3, 4]
new_arr = [0] * len(arr)
j = 0
for i in range(len(arr)-1, -1, -1):
    new_arr[j] = arr[i]
    j += 1

print(new_arr)

# in place
arr2 = [10, 20, 30, 40]
l_idx = len(arr2) - 1
s_idx = 0
while s_idx < l_idx:
    temp = arr2[s_idx]
    arr2[s_idx] = arr2[l_idx]
    arr2[l_idx] = temp
    s_idx += 1
    l_idx -= 1

print(arr2)