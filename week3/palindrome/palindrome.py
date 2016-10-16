#!/usr/bin/python3

def panlindrome(seq):
  n = len(seq)

  L = [[0 for x in range(n)] for x in range(n)]

  for i in range(n):
    L[i][i] = 1

  for cl in range(2, n + 1):
    for i in range(n - cl + 1):
      j = i + cl - 1
      if seq[i] == seq[j] and cl == 2:
        L[i][j] = 2
      elif seq[i] == seq[j]:
        L[i][j] = L[i + 1][j - 1] + 2
      else:
        L[i][j] = max(L[i][j - 1], L[i + 1][j])

  return L[0][n - 1]

print(panlindrome("GEEKS FOR GEEKS"))
print(panlindrome("MOOM akzmd"))
