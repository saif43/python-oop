# t1=0
# t2=1
# next = 0
# for i in range(int(input('Enter number: '))):
#     print(t1)
#     next = t1+t2
#     t1 = t2
#     t2 = next


def fibo(n,t1,t2):
    print(t1)
    n-=1
    if n==0:
        return
    fibo(n,t2,t1+t2)

fibo(int(input('Enter number: ')),0,1)