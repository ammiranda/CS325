import time

def fib_recur(n):
   if n == 0:
      return 0
   elif n == 1:
      return 1
   else:
      return fib_recur(n - 1) + fib_recur(n - 2)

def fib_iter(n):
   cur_term = 0
   next_term = 1
   total = 0

   for k in range(0, n):
      total = cur_term + next_term
      next_term = cur_term
      cur_term = total

   return total


