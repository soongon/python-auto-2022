print('단어를 입력하면 첫글자를 마지막으로 옮기고 뒤에 ay를 추가하는 코드')

a_word = input('단어를 입력하세요: ')

if len(a_word) > 0 and a_word.isalpha():
    print(a_word[1:] + a_word[0] + 'ay')
else:
    print('올바른 단어를 입력하세요')
