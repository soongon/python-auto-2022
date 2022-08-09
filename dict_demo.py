# dictionay .. dict .. mutable.. sequence(x)

favorite_movies = {
    '박훈정': '신세계',
    '봉준호': '기생충',
    '곽경택': '친구',
}

# indexing / slicing(x)
print(favorite_movies['봉준호'])
print(favorite_movies.get('봉준호호'))

# 아이템 추가 / 변경
favorite_movies['곽경택'] = '똥개'
print(favorite_movies)
favorite_movies['최동훈'] = '타짜'  # upsert
print(favorite_movies)

# 삭제
del favorite_movies['곽경택']
print(favorite_movies)