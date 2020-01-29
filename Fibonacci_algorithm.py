#
# 1 1 2 3 5 8 13 21 ....... F(n-1) + F(n-2)
#
# F_n = case 1 :
# 	F_(n-1) + F_(n-2) if n>= 3
# Case 2 :
# 	1 					if n = 1 or 2
#

# def fib(n):
#     if n>=3:
#         return fib(n-1)+ fib(n-2)
#     else:
#         return 1


#O(2^n) time | O(n) space
# def fib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return fib(n-1) + fib(n-2)



# O(n) times | O(n) space
# def fib(n, memoize = {1: 0, 2: 1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = fib(n-1, memoize) + fib(n-2, memoize)
#         return memoize[n]


#O(n) time | O(1) space
def fib(n):
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]