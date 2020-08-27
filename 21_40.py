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
    def is_prime(n):
        if n==1:
            return False
        sq=int(math.sqrt(n))+1
        for i in range(2,sq):
            if n%i==0:
                return False
            i+=1
        return True
    maxcnt=0
    maxa,maxb=0,0
    for b in range(2,1001):
        if not is_prime(b):
            continue
        for a in range(-b,1000):
            n=0
            while True:
                num = (n + a) * n + b
                if num<=1 or not is_prime(num):
                    break
                n+=1
            print(a,b,n)
            if n>maxcnt:
                maxa,maxb=a,b
                maxcnt=n
    print(maxcnt,maxa,maxb)
    print(maxa*maxb)
# problem27()

def problem28():
    res=1
    number=1
    for i in range(500):
        gap=(i+1)*2
        start=number+gap
        end=number+4*gap
        number+=4*gap
        #print(i,start,end)
        res+=(start+end)*2
    print(res)
# problem28()

def problem29():
    sequence=[]
    for a in range(2,101):
        for b in range(2,101):
            p=pow(a,b)
            if p not in sequence:
                sequence.append(p)
    print(len(sequence))
#problem29()

def problem30():
    ans=[]
    for n in range(1,2000000):
        s=str(n)
        if n==sum([math.pow(int(c),5) for c in s]):
            ans.append(n)
            print(n)
    print(ans,sum(ans))
#problem30()

def problem31():
    p=[1,2,5,10,20,50,100,200]
    w=[0,0,0,0,0,0,0,0]
    methods=[]
    def dfs(res,pos):
        if res<0:
            return
        if pos==0:
            ans=w.copy()
            ans[0]=res
            methods.append(ans)
            w[0]=0
            return
        while res>=0:
            dfs(res,pos-1)
            w[pos] += 1
            res -= p[pos]
        w[pos]=0
    dfs(200,7)
    print(methods)
    print(len(methods))
#problem31()

def problem32():
    res=[]
    for a in range(1,100000):
        for b in range(a,100000):
            c = str(a*b)
            c=str(a)+str(b)+c
            if len(c)==9:
                cnt=0
                for ch in range(1,10):
                    ch=str(ch)
                    if ch not in c:
                        cnt=1
                        break
                if cnt==0 and int(a*b) not in res:
                    print(a,b,c)
                    res.append(a*b)
            if len(c)>9:
                break
    print(sum(res))
#problem32()

def problem33():
    curious_fractions=[]
    for ii in range(10,100):
        for jj in range(ii+1,100):
            frac=ii/jj
            for first in [0,1]:
                for second in [0,1]:
                    if str(ii)[first]==str(jj)[second] and str(jj)[1-second]!='0' and str(jj)[second]!='0':
                        frac2=int(str(ii)[1-first])/int(str(jj)[1-second])
                        if frac==frac2:
                            curious_fractions.append((ii,jj))
    print(curious_fractions)

#problem33()

def problem34():
    fac=[1,1,2,6]
    for i in range(4,10):
        fac.append(fac[i-1]*i)
    print(fac)
    res=[]
    for n in range(1,10000000):
        if n==sum([fac[int(i)] for i in str(n)]):
            res.append(n)
            print(n)
    print(res)

# problem34()

def problem35():
    def is_prime(n):
        sq=int(math.sqrt(n))+1
        for i in range(2,sq):
            if n%i==0:
                return False
            i+=1
        return True
    res=[]
    for n in range(2,1000001):
        s=str(n)
        flag=True
        for i in range(len(s)):
            if is_prime(int(s)):
                s=s[-1]+s[:-1]
            else:
                flag=False
                break
        if flag:
            res.append(n)
            #print(n)
    print(len(res))
#problem35()

def problem36():
    ans=[]
    for n in range(1,1000000):
        b = "{:b}".format(n)
        if str(n)==str(n)[::-1] and str(b)==str(b)[::-1]:
            print(n,b)
            ans.append(n)
    print(sum(ans))

#problem36()

def problem37():
    def is_prime(n):
        if n==1:
            return False
        sq=int(math.sqrt(n))+1
        for i in range(2,sq):
            if n%i==0:
                return False
            i+=1
        return True
    ans=[]
    for n in range(10,10000000):
        flag=True
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[:i+1])) or not is_prime(int(str(n)[i:])):
                flag=False
                break
        if flag:
            ans.append(n)
            print(n)
            if len(ans)==11:
                break
    print(sum(ans))
# problem37()

def problem38():
    res=[]
    for i in range(100000):
        a=int(str(9)+str(i))
        s=str(a)
        p=a
        while len(s)<9:
            p += a
            s += str(p)
        if len(s) == 9:# 包含1-9
            cnt = 0
            for ch in range(1, 10):
                ch = str(ch)
                if ch not in s:
                    cnt = 1
                    break
            if cnt == 0 and int(s) not in res:
                print(a,s)
                res.append(int(s))
    print(res)
# problem38()

def problem39():
    maxp=0
    max_solution_num=0
    for p in range(1,1001):
        cnt=0
        for a in range(1, p//3+2):
            for b in range(a, p//2+2):
                c=p-a-b
                if c>b>=a>0 and c*c==a*a+b*b:
                     cnt+=1
                     print(a,b,c,p)
        if cnt>max_solution_num:
            max_solution_num=cnt
            maxp=p
    print(maxp)
# problem39()

def problem40():
    pos=1
    ans=1
    b=[1,10,100,1000,10000,100000,1000000]
    j=0
    for i in range(1,1000000):
        s=str(i)
        if pos<=b[j]<pos+len(s):
            ans*=int(s[b[j]-pos])
            print(s[b[j]-pos])
            j+=1
            if j>=len(b):
                break
        pos+=len(s)
    print(ans)
#problem40()