import os

path = 'C:\\'

def scan_dir(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            scan_dir(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)


scan_dir(path)