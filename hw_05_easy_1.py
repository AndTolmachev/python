import os

for i in range(9):
    dir_path = os.path.join(os.getcwd(), f'dir_{i+1}')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
