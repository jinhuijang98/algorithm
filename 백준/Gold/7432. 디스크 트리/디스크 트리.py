def print_directory_structure(paths):
    # 디렉토리 구조를 저장할 딕셔너리
    directory_structure = {}

    # 각 경로를 딕셔너리에 추가
    for path in paths:
        current_dict = directory_structure
        components = path.split('\\')
        for component in components:
            if component not in current_dict:
                current_dict[component] = {}
            current_dict = current_dict[component]

    # 딕셔너리를 기반으로 디렉토리 구조 출력
    def print_structure(current_dict, depth=0):
        for key in sorted(current_dict.keys()):
            print(" " * depth + key)
            print_structure(current_dict[key], depth + 1)

    print_structure(directory_structure)

# 입력 받기
n = int(input())
paths = [input() for _ in range(n)]

# 디렉토리 구조 출력
print_directory_structure(paths)