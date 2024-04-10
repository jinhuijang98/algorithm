"""
모든 노드들의 길이를 구한다음에
오른쪽만 이동한 거리를 빼준다.


 루트 노드는 항상 1번 노드이다.
"""
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS1(Node):
    global count
    visit[Node]=True

    if not visit[Tree[Node][0]] and Tree[Node][0]!=-1:
        DFS1(Tree[Node][0])
        count += 1
    if not visit[Tree[Node][1]] and Tree[Node][1]!=-1:
        DFS1(Tree[Node][1])
        count += 1

def DFS2(Node):
    global count2
    visit[Node]=True

    if not visit[Tree[Node][1]] and Tree[Node][1]!=-1:
        DFS2(Tree[Node][1])
        count2 += 1
N=int(input())
Tree={}

for i in range(N):
    a,b,c=map(int,input().split())
    Tree[a]=[b,c]

visit=[False]*(N+1)
count=0
DFS1(1)
count2=0
visit=[False]*(N+1)
DFS2(1)

print(2*count-count2)