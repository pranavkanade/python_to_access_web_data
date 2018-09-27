import re
# from functools import reduce
count = 0

# def sum1(a, b=0):
#     return a+b

with open('actual.txt', 'r') as read_file:
    for line in read_file:
        res = list(map(int, re.findall('\d+', line)))
        count += sum(res)
        # if len(res): count += reduce(sum1, res)
        # elif len(res) == 1:
        #     count += res[0]

print(count)

# One liner
# print(sum(list(map(int, re.findall('\d+', open('actual.txt').read())))))