a, b = map(int, input().split())

def dfs(x, b):
    stack = []
    visited = {}
    stack.append(b)
    # t = 1
    while stack:
        b = stack.pop(0)

        for i in range(1, 3):
            if i % 2:
                if b % 2 == 0:
                    t = b //2
                    stack.append(t)
                    visited.setdefault(b, 1)
                    visited[t] = visited[b] + 1
                    if t == x:
                        return visited[t]

            else:
                # b = str(b)
                if str(b)[-1] == '1':
                    bb = str(b)
                    if len(bb) > 1:
                        bb = bb[:-1]
                        t = int(bb)
                        # visited += 1
                        visited.setdefault(b, 1)
                        visited[t] = visited[b] + 1
                        stack.append(t)
                        if t == x:
                            return visited[t]
    return -1


print(dfs(a, b))