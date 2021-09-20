def my_median(sample):
    n = len(sample)
    #print(n)
    if n%2:
        sarr=(sorted(sample, reverse=True))
        print(sarr)
        m = (n+1)/2
        #print(int(m))
        print(f"median = {sarr[int(m)-1]} ")
    else:
        sarr=(sorted(sample, reverse=True))
        print(sarr)
        m1 = n/2
        m2 = m1 -1
        #print(f"{int(m1)}-{int(m2)}")
        m = (sarr[int(m2)] + sarr[int(m1)])/2
        print(f"median = {m}")


def my_average(sample):
    n = len(sample)
    a = sum(sample)/n
    print(f"average = {round(a, 2)}")


def my_max(sample):
    n = len(sample)
    sarr=(sorted(sample, reverse=True))
    print(f"max = {sarr[0]}")


def my_min(sample):
    n = len(sample)
    sarr=(sorted(sample, reverse=True))
    print(f"min = {sarr[n-1]}")


sample=[6, 2, 3, 4, 5, 1, 9]

my_median(sample)
my_average(sample)
my_min(sample)
my_max(sample)
