import math
from itertools import permutations
def is_prime(n):
    if n == 1:
        return False
    sq = int(math.sqrt(n)) + 1
    for i in range(2, sq):
        if n % i == 0:
            return False
        i += 1
    return True

def is_triangle_num(n):
    sq=int(math.sqrt(2*n))
    if sq*(sq+1)==2*n:
        return True
    return False

def is_pentagonal_num(n):
    sq=math.sqrt(1+24*n)
    if sq*sq==1+24*n and (1+sq)%6==0:
        #print(n,(1+sq)//6)
        return True
    return False

def problem41():
    def test(lst):
        for digits in permutations(lst):
            n=int("".join([str(x) for x in digits]))
            if is_prime(n):
                return n

    lst=[9, 8, 7, 6, 5, 4, 3, 2,1]
    for i in range(8):
        lst=lst[1:]
        print(test(lst))
    print(test(lst))
# problem41()

def problem42():
    f = open('p042_words.txt')
    s = f.read().replace('"', '')
    # print(s)
    ar = sorted(s.split(","))
    ans = 0
    for i in range(len(ar)):
        a = 0
        name = ar[i]
        # print(name)
        for c in name:
            a += ord(c) - ord('A') + 1
        if is_triangle_num(a):
            ans+=1
    print(ans)
#problem42()



def problem43():
    lst=[9, 8, 7, 6, 5, 4, 3, 2,1,0]
    ans=[]
    for digits in permutations(lst):
        n=int("".join([str(x) for x in digits]))
        if int("".join([str(x) for x in digits[1:4]]))%2==0\
            and int("".join([str(x) for x in digits[2:5]]))%3==0 \
            and int("".join([str(x) for x in digits[3:6]])) % 5 == 0 \
            and int("".join([str(x) for x in digits[4:7]])) % 7 == 0 \
            and int("".join([str(x) for x in digits[5:8]])) % 11 == 0 \
            and int("".join([str(x) for x in digits[6:9]])) % 13 == 0 \
            and int("".join([str(x) for x in digits[7:10]])) % 17 == 0:
                ans.append(n)
    print(sum(ans))
#problem43()


def problem44():
    f=lambda x:x*(3*x-1)//2
    ans=[0]
    mind=9999999999999
    for i in range(1,10000):
        for j in range(i-1,0,-1):
            pi=f(i)
            pj=f(j)
            d = pi-pj
            if d>=mind:
                break
            if is_pentagonal_num(d) and is_pentagonal_num(pi+pj):
                mind=d
                print(i,pi,j,pj,mind)
    print(mind)
#problem44()

def problem45():
    for n in range(143,50000):
        h=n*(2*n-1)
        if is_pentagonal_num(h) and is_triangle_num(h):
            print(h)
#problem45()

def problem46():
    prime = []
    n = 2
    while len(prime) <= 10000:
        flag = True
        for i in prime:
            if n % i == 0:
                flag = False
                break
        if flag:
            prime.append(n)
        n += 1

    for n in range(3,1000000,2):
        if is_prime(n):
            continue
        sq=int(math.sqrt(n/2))+1
        flag=False
        for i in range(1,sq):
            if n-2*i*i in prime:
                flag=True
        if not flag:
            print(n)
            break
# problem46()

def problem47():
    def find_prime_factors(n):
        i=2
        factors={}
        while i*i<=n:
            while n%i==0:
                factors[i]=1
                n//=i
            i+=1
        if n>0:
            factors[n]=1
        return list(factors.keys())

    for n in range(1,1000000000):
        if len(find_prime_factors(n))==4 and len(find_prime_factors(n+1))==4 and len(find_prime_factors(n+2))==4 and len(find_prime_factors(n+3))==4:
            print(n)
            print(find_prime_factors(n))
            break
# problem47()

def problem48():
    digits=[0]+[1 for i in range(1000)]
    for i in range(1,1001):
        for pos in range(i,1001):
            digits[pos]*=pos
            digits[pos]%=100000000000000

    print(str(sum(digits))[-10:])
# problem48()


def problem49():
    for i in range(1000,9999):
        if not is_prime(i):
            continue
        for s in range(1,(9999-i)//2+1):
            if i+2*s>=10000:
                break
            if is_prime(i+s) and is_prime(i+s+s):
                hash1=[0 for i in range(10)]
                for c in str(i):
                    hash1[int(c)]+=1
                hash2 = [0 for i in range(10)]
                for c in str(i+s):
                    hash2[int(c)] += 1
                hash3 = [0 for i in range(10)]
                for c in str(i+s+s):
                    hash3[int(c)] += 1
                if hash1==hash2 and hash2==hash3:
                    print(i,i+s,i+s+s)

#problem49()


def problem50(): #线性筛法
    prime=[]
    is_pri=[1 for i in range(1000000)]

    for i in range(2,1000000):
        if is_pri[i]:
            prime.append(i)
            for j in range(i*i,1000000,i):
                is_pri[j]=0

    maxlen=0
    ans=0
    for i in range(1,len(prime)):
        s=0
        for j in range(i,len(prime)):
            s+=prime[j]
            if s>=1000000:
                break
            if is_pri[s] and j-i+1>maxlen:
                maxlen=j-i+1
                ans=s
    print(ans)


problem50()
