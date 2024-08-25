n = [10,21,30,40,51,60]
print("n = ",n)
# Reverse
print("n[::-1] = ",n[::-1]) 
# First two elements
print("n[0:2] = ",n[0:2])
# Every alternate element starting from 0 index
print("n[::2] = ",n[::2])
# Every alternate element starting from 1 index
print("n[1::2] = ",n[1::2])
# Reverse starting from last index-1
print("n[4::-1] = ",n[4::-1])
# Reverse until last index
print("n[:4:-1] = ",n[:4:-1])
# Second and third last elements
print("n[4:2:-1] = ",n[4:2:-1])
# Print 30,21,10 
print("n[2::-1] = ",n[2::-1])

## Output
# n =  [10, 21, 30, 40, 51, 60]
# n[::-1] =  [60, 51, 40, 30, 21, 10]
# n[0:2] =  [10, 21]
# n[::2] =  [10, 30, 51]
# n[1::2] =  [21, 40, 60]
# n[4::-1] =  [51, 40, 30, 21, 10]
# n[:4:-1] =  [60]
# n[4:2:-1] =  [51, 40]
# n[2::-1] =  [30, 21, 10]
