# 현재 디렉토리 밑에 documents/dir 디렉토리로 이동하여 해당 디렉토리의 모든 파일을 조회
import glob
import os

# current_path = os.getcwd()

os.chdir('/Users/soongonkim/Desktop/python-auto/file_handling/documents/dir')
dir_files = glob.glob('*')

for file in dir_files:
    print(file)
