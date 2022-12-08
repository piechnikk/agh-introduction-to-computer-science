sum = 754
temp_sum = 0
a = b = 1
while temp_sum < sum:
    temp_sum += a
    a, b = b, a + b
a = b = 1
while temp_sum > sum:
    temp_sum -= a
    a, b = b, a + b
print(temp_sum == sum)
