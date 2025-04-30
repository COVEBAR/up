nums = [1,2,1,3,4]
unique_nums = []
for i in nums:
    if i not in unique_nums:
        print(i)
        unique_nums.append(i)
    else:
        print("true")
        break
else:
    print("false")