ar = [1,2,3,5,6,7,8,9,10,11]
mis = 0
for i in range(len(ar)):
    if ar[i] - i != 1:
        mis = ar[i] -1
        break
    mis += 1
# for item in ar:
#     if ((item - mis) != 1):
#         mis = item - 1
#         break
#     mis += 1

# Other option:
# 1. Make a full length array and compare
# 2. Get a sum of the array and the length of the array the subtract the full sum to the checking array

#####################################
#
# Best option:
# Keep halfening to find where the error is
#
#####################################
print(mis)
