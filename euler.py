from math import sqrt
import numpy


def main():
    print(problem_010())
    return


def problem_001():
    s = 0
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s


def problem_002():
    f1 = 1
    f2 = 1
    s = 0

    while f1 < 4000000:
        if f1 % 2 == 0:
            s += f1
        new_f1 = f2
        new_f2 = f1 + f2
        f1 = new_f1
        f2 = new_f2

    return s


def problem_003():
    return max(factor(600851475143))


def factor(n):
    i = 2
    limit = n // 2 + 1
    while i <= limit:
        if n % i == 0:
            n /= i
            limit = n // 2 + 1
            yield i
        else:
            i += 1
    if i > 1:
        yield n


def problem_004(n=999):
    i = n
    a1 = n
    a2 = n

    while i > 0:
        while a1 >= a2:
            if str(a1 * a2) == str(a1 * a2)[::-1]:
                return a1 * a2
            a1 -= 1
            a2 += 1
        i -= 1
        a1 = n
        a2 = i

    return 0


def problem_005(n=20):
    factors = dict()
    for i in range(2, n+1):
        temp = dict()
        for j in factor(i):
            if j in temp:
                temp[j] += 1
            else:
                temp[j] = 1
        for k, v in temp.items():
            if k not in factors or factors[k] < v:
                factors[k] = v

    p = 1

    for k, v in factors.items():
        p *= k ** v

    return p


def problem_006(n=100):
    sum_squares = 0
    square_sum = 0

    for i in range(1, n+1):
        sum_squares += i ** 2
        square_sum += i

    square_sum **= 2

    return square_sum - sum_squares


def problem_007(n=10001):
    c = 1
    i = 1
    while c < n:
        i += 2
        if is_prime(i):
            c += 1
    return i


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(sqrt(n) + 1)
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


def problem_008(s="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450",w=13):
    p = 0
    c = len(s) - w + 1
    for i in range(0, c):
        t = 1
        for j in list(s[i:i+w]):
            t *= int(j)
        if t > p:
            p = t
    return p


def problem_009():
    for c in range(334, 999):
        b = c - 1
        a = 1000 - b - c
        s1 = a ** 2 + b ** 2
        s2 = c ** 2
        while b >= a and s1 > s2:
            b -= 1
            a += 1
            s1 = a ** 2 + b ** 2
            s2 = c ** 2
        if s1 == s2:
            return a * b * c
    return 0


def problem_010(n=2000000):
    s = 0
    for i in primes_from_2_to(n):
        s += i
    return s


def primes_from_2_to(n):
    sieve = numpy.ones(n/3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k*k/3::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2, 3, ((3*numpy.nonzero(sieve)[0][1:]+1) | 1)]


if __name__ == "__main__":
    main()
