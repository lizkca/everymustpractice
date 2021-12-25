s = '1.23, 2.4, 3.123'
num_list = s.split(',')
result = 0
for num in num_list:
    result = result + float(num)
print(result)
