# test_file = open('test.txt')
# lines = test_file.readlines()
# print(lines)
# test_file.close()


with open('test.txt') as test_file:
    lines = test_file.readlines()
    print(lines)
