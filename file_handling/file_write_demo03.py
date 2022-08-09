# writelines() 함수 사용

strings_to_write = [
    'hello world\n',
    '좋아요 파이썬..\n',
]

handler = open('new-file2.txt', 'a', encoding='utf-8')
handler.writelines(strings_to_write)
handler.close()
