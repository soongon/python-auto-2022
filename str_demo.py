# 문자열 (str) 다루기
favorite_color = 'romantic red'

print(favorite_color)
print(type(favorite_color))

# indexing .. 글자 한글자 추출
extracted = favorite_color[10]
print(extracted)

# slicing .. 여러 글자 추출
print(favorite_color[2:-4])  # mantic
print(favorite_color[-3:])  # red

# 문자열 (str)은 객체이기 때문에 여러 함수(메소드)를 사용할 수 있다.
print(favorite_color.capitalize())
splitted = favorite_color.split(' ')
print(splitted)