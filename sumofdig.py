def sum_dig(i):
    total=0
    for i in str(i):
        total+=int(i)
    return total
print(sum_dig(1234))