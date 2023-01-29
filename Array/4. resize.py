arr = [1, 2, 3, 4]
add = int(input("How much length do you want to add: "))

# declare an array using given size
resized_arr = [0] * ( len(arr) + add )

# copying all values in resized array
for i in range(len(arr)):
    resized_arr[i] = arr[i]

print(resized_arr)
