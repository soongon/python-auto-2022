import glob
import os.path
# base_path = 'c:\\mydocument\\jobs\\'

base_path = os.path.join('/', 'mydocuemnt', 'jobs')

files = glob.glob('*')

for file in files:
    print(os.path.join(base_path, file))
