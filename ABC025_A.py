import io
import sys

_INPUT = """\
6
abcde
8
aeiou
22
vwxyz
25
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  N=int(input())
  ans=[]
  for i in range(5):
    for j in range(5):
      ans.append(S[i]+S[j])
  ans.sort()
  print(ans[N-1])