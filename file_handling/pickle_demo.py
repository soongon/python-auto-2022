# 픽클 할 데이터
import pickle

favorite_colors = ['red', 'white', 'blue', 'orange']

# 픽클로 만들기
with open('favorite_colors.pickle', 'wb') as file:
    pickle.dump(favorite_colors, file)

print('픽클 생성 완료')

# 픽클 파일 원복하기
with open('favorite_colors.pickle', 'rb') as file:
    original_colors = pickle.load(file)
    print(original_colors)
