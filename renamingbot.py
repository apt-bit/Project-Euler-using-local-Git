import os

files = os.listdir()

for file in files:
    for i in range(10):
        if file == ('problem' + str(i) + '.py'):
            os.rename(file, ('problem0' + str(i) + '.py'))
