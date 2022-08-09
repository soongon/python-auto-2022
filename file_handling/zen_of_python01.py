# 젠오브파이썬 파일을 한줄씩 출력..

zen_list = []

with open('zen_of_python.txt') as handler:
    zen_list = handler.readlines()

print(zen_list)

# 젠오브파이썬을 한줄씩 출력
for item in zen_list:
    print(item[:-1])

# should 가 포함된 라인만 출력
for item in zen_list:
    if item.find('should') >= 0:
        print(item[:-1])

# better 가 포함된 첫번째 라인만 출력
# hint) break 사용..
for item in zen_list:
    if item.find('better') >= 0:
        print(item[:-1])
        break
