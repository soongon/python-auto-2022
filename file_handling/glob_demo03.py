# documents/dir/file1.txt 파일을 file_handling 디렉토리로 복사
import os
import shutil


def copy_file():
    os.chdir('/file_handling/documents/dir')
    shutil.copy('file1.txt', '/file_handling')


# document/dir/subdir 디렉토리를 file_handling 디렉토리에 백업
def copy_directory():
    os.chdir('/Users/soongonkim/Desktop/python-auto/file_handling/documents/dir')
    shutil.copytree('./subdir', '/Users/soongonkim/Desktop/python-auto/file_handling/backup')


# docuemtn/dir/subdir 디렉토리를 zip으로 압축하여 file_handling/backup 디렉토리에 백업
# 파일이름은 오늘 날짜 예) 2022-08-10-01.zip 으로 한다.


def main():
    copy_file()
    copy_directory()


if __name__ == '__main__':
    main()
