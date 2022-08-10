# 젠파일 전체 읽어서 한줄씩 출력
def read_zen_to_line():
    lines = []
    with open('zen_of_python.txt') as file:
        lines = file.readlines()

    for line in lines:
        print(line[:-1])


def main():
    read_zen_to_line()


if __name__ == '__main__':
    main()
