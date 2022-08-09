# list 는 mutable 한 collection

favorite_colors = ['red', 'blue', 'brown', 'pink', 'tan', 'olive']

# 참고.. immutable 한 list를 제공 .. tuple
tuple_favorite_colors = 'red', 'blue', 'brown'

# indexing / slicing
print(favorite_colors[2])
print(favorite_colors[1:4])  # slicing / sub listing

# 아이템 추가 .. append item
favorite_colors.append('white')
print(favorite_colors)

# 아이템 수정 .. modify item
favorite_colors[1] = '파랑'
print(favorite_colors)

# 아이템 삭제 .. delete(remove) item
del favorite_colors[2]
print(favorite_colors)
favorite_colors.remove('tan')
print(favorite_colors)