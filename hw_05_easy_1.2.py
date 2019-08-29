import os

for i in range(9):
    dir_path = os.path.join(os.getcwd(), f'dir_{i+1}')
    try:
        os.rmdir(dir_path)
    except OSError:
        print(f'В директории {dir_path} есть файл')
