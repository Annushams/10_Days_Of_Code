import os
import sys



def equalStacks(h1, h2, h3):
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)
    while h1 and h2 and h3:
        if sum_h1 == sum_h2 == sum_h3:
            return sum_h1
        minimum_sum = min(sum_h1, sum_h2, sum_h3)
        while sum_h1 > minimum_sum:
            sum_h1 -= h1.pop(0)
        while sum_h2 > minimum_sum:
            sum_h2 -= h2.pop(0)
        while sum_h3 > minimum_sum:
            sum_h3 -= h3.pop(0)
    return 0


    
if __name__ == '__main__':
    n1N2N3 = input().split()
    n1 = int(n1N2N3[0])
    n2 = int(n1N2N3[1])
    n3 = int(n1N2N3[2])
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result = equalStacks(h1, h2, h3)
    print(result)
