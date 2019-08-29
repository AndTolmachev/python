import os


for i in os.listdir(os.getcwd()):
    if '.' not in i:
        print(i)
