import io
import sys

_INPUT = """\
6
3 5 10
East 7
West 3
West 11
3 3 8
West 6
East 3
East 1
5 25 25
East 1
East 1
West 1
East 100
West 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,A,B=map(int,input().split())
  ans=0
  for i in range(N):
    s,d=input().split()
    if s=='East': ans+=min(max(A,int(d)),B)
    else: ans-=min(max(A,int(d)),B)
  if ans>0: print('East',ans)
  elif ans<0: print('West',-ans)
  else: print(0)