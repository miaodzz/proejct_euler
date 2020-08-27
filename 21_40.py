import math
def problem21():
    def properdivesors(n):
        ret = [1]
        sq = int(math.sqrt(n))
        for i in range(2, sq + 1):
            if n % i == 0:
                ret += [i, int(n / i)]
        if len(ret) > 1 and ret[-1] == ret[-2]:
            ret.pop()
        return sum(ret)
    ans=[]
    #print(properdivesors(284))
    for i in range(1,10000):
        k=properdivesors(i)
        if k!=i and properdivesors(k)==i:
            ans.append(k)
            #print(k)
    print(sum(ans))

#problem21()


def problem22():
    f = open('p022_names.txt')
    s=f.read().replace('"','')
    #print(s)
    ar=sorted(s.split(","))
    ans=0
    for i in range(len(ar)):
        a=0
        name = ar[i]
        #print(name)
        for c in name:
            a+=ord(c)-ord('A')+1
        ans+=i*a
    print(ans)
#problem22()

def problem23():
    def properdivesors(n):
        ret = [1]
        sq=int(math.sqrt(n))
        for i in range(2,sq+1):
            if n % i == 0:
                ret += [i, int(n/i)]
        if len(ret)>1 and ret[-1]==ret[-2]:
            ret.pop()
        return sum(ret)
    appd=[]
    for i in range(1,28124):
        #print(i)
        if properdivesors(i)>i:
            appd+=[i]
    print(appd)
    summ=0
    for i in range(1,28124):
        flag = False
        for a in appd:
            if 2*a>i:
                break
            if i-a in appd:
                flag=True
                break
        if not flag:
            #print(i)
            summ+=i
    print(summ)
# problem23()

def problem24():
    fac=[0,1]
    for i in range(2,10):
        fac.append(i*fac[i-1])
    fac=list(reversed(fac[1:]))
    print(fac)
    ans=999999
    s="0123456789"
    for i in range(0,9,1):
        pos=ans//fac[i]
        ans%=fac[i]
        s=s[:i] +s[i+pos] +s[i:i+pos]+s[i+pos+1:]
        print(s)

# problem24()

def problem25():
    fib1=1
    fib2=1
    i=3
    while True:
        tmp=fib1+fib2
        if len(str(tmp))>=1000:
            print(i,tmp)
            break
        i+=1
        fib1,fib2=fib2,tmp

#problem25( )

def problem26():
    def get_recurring_cycle(n):
        i=1
        res=[]
        while i not in res:
            res.append(i)
            i*=10
            i%=n
        start=res.index(i)
        end=len(res)
        return end-start

    maxloop=0
    d=0
    for i in range(2,1001):
        c=get_recurring_cycle(i)
        print(i,c)
        if c>maxloop:
            maxloop=c
            d=i
    print(d,maxloop)

#problem26()

def problem27():
    def isPrime():
        