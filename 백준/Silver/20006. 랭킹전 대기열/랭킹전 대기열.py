p, m = map(int, input().split())
room_list = list()

for _ in range(p) :
  l, n = input().split()
  l = int(l)
  flg = False
  for _room_list in room_list :
    if len(_room_list) < m and abs(l - _room_list[0][0]) <= 10 :
      _room_list.append((l, n))
      flg = True
      break
  if not flg :
    room_list.append([(l, n)])

for _room_list in room_list :
  print('Started!' if len(_room_list) == m else 'Waiting!')
  _room_list.sort(key = lambda x : x[-1])
  for l, n in _room_list :
    print(l, n)