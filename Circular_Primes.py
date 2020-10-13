class Permutable_Primes():
    """Finds Circular primes upto 10001"""

    @staticmethod
    def sieve_eresthonsis():
        sieve = list(range(10001))
        sieve[0] = sieve[1] = 0
        for i in range(2, 10001):
            if sieve[i]:
                for j in range(i*i, 10001, i):
                    sieve[j]=0
        return sieve

    @staticmethod
    def expo(N, P): # Uses Russian Peasant Exponentiation a.k.a. Binary Exponentiation (I think)
        res = 1
        while P:
            if P&1:
                res *= N
            N*=N
            P//=2
        return res

    @classmethod
    def permutable_primes(cls):
        primes = []
        sieve = cls.sieve_eresthonsis()
        for i in range(2, 10001):
            if sieve[i]:
                if i<=11:
                    primes+=[i]
                else:
                    # Creates permutaion of numbers
                    temp = i; cnt = 0
                    while temp:
                        cnt+=1
                        temp//=10
                    num = i
                    flag = 0
                    dum = []
                    while True:
                        rem = num%10
                        div = num//10
                        num = (cls.expo(10, cnt-1) * rem) + div
                        if sieve[num]:
                            # If the permutaion is a prime then it tis added
                            dum+=[num]
                            flag+=1 # Counts the number of permuted numbers
                        if num==i:
                            break
                    if flag==cnt:   # If number of permutations are not equal to that of digit number, then it is not a circular or absolute prime
                        primes.extend(dum)
        return sorted(set(primes))
    # In my opinion don't fully trust th wikipedia page for permutable primes, do the Project Euler's one

#print(Permutable_Primes.permutable_primes())