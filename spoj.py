import math


def primes(n):
    marks = [True] * (n+1)
    p = 2
    k = int(math.sqrt(n)) + 1
    while (p <= k):
        if marks[p] is True:
            i = p**2
            while i <= n:
                marks[i] = False
                i += p
        p += 1
    primes_list = []
    for i in range(2, n+1):
        if marks[i] is True:
            primes_list.append(i)
    return primes_list

def seg_primes(lower, upper):
    marks = [True] * ((upper - lower) + 1)
    prime_numbers = primes(int(math.sqrt(upper)) + 1)
    if lower == 1:
        marks[0] = False
    for p in prime_numbers:
        i = lower
        while i % p != 0:
            i += 1
        while i <= upper:
            if i != p:
                marks[i-lower] = False
            i += p
    for i, mark in enumerate(marks):
        if mark:
            print(i+lower)


"""
if __name__ == '__main__':
    t = int(input())
    bounds_list = [input().split() for i in range(t)]
    for bounds in bounds_list:
        lower, upper = int(bounds[0]), int(bounds[1])
        seg_primes(lower, upper)
        print('')"""

def multiply_ints(array):
    before = [1]
    after = [1]
    prods = []
    for num in array:
        before.append(before[-1] * num)
    for num in reversed(array):
        after.append(after[-1] * num)
    for i in range(len(array)):
        prods.append(before[i] * after[-i-2])
    return prods

print(multiply_ints([2,7,3,4]))

def solve(a):
   temp = []
   b = []
   for i in xrange(len(a)-1, -1,-1):
      if a[i] == ' ':
         b.extend(temp[::-1])
         a.append(' ')
         temp = []
      else:
         temp.append(a[i])
   b.extend(temp)
   return b

print(solve([ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't' ]))