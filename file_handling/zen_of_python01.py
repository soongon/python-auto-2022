
def main():
    # 파일 읽기
    zen_file_to_lines = []

    with open('zen_of_python.txt') as file:
        zen_file_to_lines = file.readlines()

    print(type(zen_file_to_lines))

    # 전체 라인 출력
    for line in zen_file_to_lines:
        print(line[:-1])

    print('============================================')
    # Should 가 포함된 라인만 출력하고 나머지는 pass 라고 표시
    for line in zen_file_to_lines:
        # if line.find('should') >= 0:
        if 'should' in line:
            print(line[:-1])
        else:
            print('pass')

    print('=============================================')
    # better 가 포함된 첫번째 라인만 출력
    for line in zen_file_to_lines:
        if 'better' in line:
            print(line[:-1])
            break


if __name__ == '__main__':
    main()
