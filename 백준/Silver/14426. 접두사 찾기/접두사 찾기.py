import sys
read = sys.stdin.readline

class Node(object):
    # trie 자료구조를 위한 node
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        # dictionary 자료구조 사용
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 해당 노드로 이동
            curr_node = curr_node.children[char]

        curr_node.data = string

    # 문자열이 존재하는지 search
    def search(self, string):
        current_node = self.head

        # 주어진 단어를 순회하며 각 글자들에 대해 판단한다.
        for char in string:
            # 만약 현재 글자가 현재 노드의 자식에 있다면,
            if char in current_node.children:
                # 현재 노드를 현재 글자를 key값으로 가지는 node로 이동
                current_node = current_node.children[char]
            # 만약 현재 글자가 현재 노드의 자식에 없다면
            else:
                # 접두사가 아니므로 false 반환
                return False
        # 만약 마지막 노드까지 왔을때, 현재 노드가 자식을 갖고있거나, data가 있어 존재하는 단어로 끝난다면, True를 반환
        if current_node.children or current_node.data:
            return True

        # if curr_node.data != None:
        #     return True

n, m = map(int, read().split())

word_trie = Trie()

# 주어진 문자열과 길이가 같은 문자열에 대해서만 탐색을 진행해
# 시간복잡도 줄이기 위함

for _ in range(n):
    word = read().strip()
    word_trie.insert(word)
cnt = 0
for _ in range(m):
    word = read().strip()
    if word_trie.search(word):
        cnt += 1

print(cnt)