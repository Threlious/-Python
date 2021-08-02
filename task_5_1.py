def odd_nums(n):
    for n in range(1, n + 1, 2):
        yield n


odd_to_15 = odd_nums(15)
print(type(odd_to_15))
for i in odd_to_15:
    print(i)
