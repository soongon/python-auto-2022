# handler = open('new-file.txt', 'w')
# handler.write('hello world\n')
# handler.write('좋습니다. 아마존..\n')
# handler.close()
# print('작성 완료')


with open('new-file.txt', 'w') as handler:
    handler.write('hello world\n')
    handler.write('좋습니다. 아마존..\n')

print('작성 완료')
