# bubble soft
# сортировка пузырек
import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print("not sorted:")
print(arr)
print("------")

###############################################

is_soeted = True
for i in range(n):
    for j in range (n - 1):
        left = arr[j]
        right = arr[j + 1]
        is_sorted = False
        if left > right:
            arr[j] = right
            arr[j + 1] = left    
    if is_sorted is True:
        break
    else:
        is_sorted = True
    

###########################################

print("sorted:")
print(arr)