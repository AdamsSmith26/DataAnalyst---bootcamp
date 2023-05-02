def dfactorial(n:int): 
    s = 1
    while n>=0:
        if n==0:
            s=1
            n-=2
        if n==1:
            s=1
            n-=2
        if n>=2:
            s*=n
            n-=2

    return s
    


res = dfactorial(0)
res1 = dfactorial(1)
res2 = dfactorial(2)
res3 = dfactorial(3)
res4 = dfactorial(4)

print(res, res1, res2, res3, res4)
