Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=int(input("Введите количество игр "))
for i in range(x):
    n=int(input("Количество секторов "))
    k=int(input("Номер черной мишени "))
    a=[]
    max=-100
    if (k == -1):
       for i in range(n):
           a.append(int(input()))
       for i in range(n):
           sum = 0
           for j in range(n):
               d=i+j
               if d > n-1:
                   d=d-n
               sum = sum + a[d]
               if sum > max:
                    max=sum
       print(max)
    else:
        for i in range(n):
            a.append(int(input()))
        a[k]=min(a)
        if a[k]>0:
            a[k]=0
        for i in range(n):
            sum = 0
            for j in range(n):
                d = i + j
                if d > n - 1:
                    d = d - n
                sum = sum + a[d]
                if sum > max:
                    max = sum
        print(max)
