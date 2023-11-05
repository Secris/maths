sum_all = 0

num_1 = 1
num_2 = 2
temp = 0

sum_all += num_2 # pre-seed with two because it is even

while temp < 4000000:
    temp = num_1 + num_2
    print(str(num_1) + " + " + str(num_2) + " = " + str(temp))
    if temp % 2 == 0:
        sum_all += temp

    num_1 = num_2
    num_2 = temp

print("Sum of all even: " + str(sum_all))