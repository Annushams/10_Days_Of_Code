def e_greatest_common_divisor(a, b):
    if b==0:
        return (a, 1, 0)
    else:
        d, x, y = e_greatest_common_divisor(b, a % b)
        return (d, y, x - (a // b) * y)
def modulo_inverse(a, x):
    d, y, k = e_greatest_common_divisor(a, x)
    return (x + y % x) % x
def solve(a, b, x):
    if b > 0:
        return(pow(a, b, x))
    else:
        return(pow(modulo_inverse(a, x), -b, x))


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        abx = input().split()
        a = int(abx[0])
        b = int(abx[1])
        x = int(abx[2])
        result = solve(a, b, x)
        print(result)