def fac (num):
    p = num
    for i in range(1,num):
        p *= i
    print(p)

fac(int(input()))