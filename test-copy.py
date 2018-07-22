import shutil
import os
import csv

current = os.getcwd()
os.chdir('copy_test')
print(os.listdir())
os.chdir('folder1')
# print(os.getcwd())

file_list = os.listdir()
print(file_list)

for x in file_list:
    shutil.copyfile(x, current + '/cookie.txt')
# for path, dirs, files in os.walk('.'):
#     print(path)

# White Boarding Time