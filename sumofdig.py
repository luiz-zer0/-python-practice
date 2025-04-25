def sum_dig(i):
    total=0
    while i>0:
        total+=i%10
        i=i//10
    return total
print(sum_dig(1234))
