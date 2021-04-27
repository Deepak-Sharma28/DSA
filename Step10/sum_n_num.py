

def sum_of_n(n):
    if n>0:
        return n+ sum_of_n(n-1)
    else:
        return 0
       
print(sum_of_n(int(input())))