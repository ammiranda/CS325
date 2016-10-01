#include<stdio.h>

unsigned long long fib_iter(int n);
unsigned long long fib_recur(int n);

int main()
{
  int arr[] = {5, 10, 20, 30, 50};
  
  for (int i = 0; i < 10; i++) {
    //printf("%d ", arr[i]);
    printf("%llu ", fib_iter(arr[i]));
   // printf("%llu ", fib_recur(arr[i]));
  }
  
  return 0;
}

unsigned long long fib_iter(int n) {
  int cur_term = 0;
  int next_term = 1;
  int total = 0;

  for (int i = 0; i <= n; i++) {
    total = cur_term + next_term;
    next_term = cur_term;
    cur_term = total;
  }

  return total;
}

unsigned long long fib_recur(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fib_recur(n - 1) + fib_recur(n - 2);
  }
}
