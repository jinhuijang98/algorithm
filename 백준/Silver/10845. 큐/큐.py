import sys
input = sys.stdin.readline

# enQ
def enq(data):
    global rear
    rear += 1
    Q[rear] = data
    return Q

# deQ
def deq():
    global front
    front += 1
    return Q[front-1]



N = int(input())
front = 0
rear = -1
Q = [0]*(N+1)
for i in range(N):
    order = input().strip()
    if order.split(' ')[0] == 'push':
        enq(int(order.split(' ')[1]))
    elif order == 'pop':
        if rear < front:
            print(-1)
        else:
            print(deq())
    elif order == 'size':
        if rear == -1 or rear < front:
            print(0)
        else:
            print(rear - front+1)
    elif order == 'empty':
        if rear == -1 or rear < front:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if rear < front:
            print(-1)
        else:
            print(Q[front])
    else:       # order == 'back'
        if rear < front:
            print(-1)
        else:
            print(Q[rear])