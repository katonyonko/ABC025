import io
import sys

_INPUT = """\
6
0 15 0
0 0 25
20 10
0 0
25 0
18 22 15
11 16 17
4 25
22 15
10 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(1000000)
  B=[list(map(int,input().split())) for _ in range(2)]
  C=[list(map(int,input().split())) for _ in range(3)]
  memo=[(-1,-1)]*(3**9)

  def score(banmen):
    m,f=0,0
    for i in range(2):
      for j in range(3):
        if banmen[i*3+j]==banmen[(i+1)*3+j]: m+=B[i][j]
        else: f+=B[i][j]
    for i in range(3):
      for j in range(2):
        if banmen[i*3+j]==banmen[i*3+j+1]: m+=C[i][j]
        else: f+=C[i][j]
    return m,f

  def rec(k):
    if memo[k][0]!=-1 and memo[k][1]!=-1: return memo[k]
    banmen=[]
    tmp=k
    for i in range(9):
      banmen.append(tmp%3)
      tmp//=3
    if 2 not in set(banmen): return score(banmen)
    turn=banmen.count(2)
    if turn%2==0:
      s=max([rec(k-3**i)[1] for i in range(9) if banmen[i]==2])
      for  i in range(9):
        if banmen[i]==2 and rec(k-3**i)[1]==s:
          t=rec(k-3**i)[0]
    else:
      t=max([rec(k-2*3**i)[0] for i in range(9) if banmen[i]==2])
      for  i in range(9):
        if banmen[i]==2 and rec(k-2*3**i)[0]==t:
          s=rec(k-2*3**i)[1]
    memo[k]=(t,s)
    return t,s

  print(*rec(3**9-1),sep='\n')