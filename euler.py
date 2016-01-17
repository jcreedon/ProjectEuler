

def main():
    print(problem_004())
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


if __name__ == "__main__":
    main()
