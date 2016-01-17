from math import sqrt


def main():
    print(problem_007())
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


if __name__ == "__main__":
    main()
