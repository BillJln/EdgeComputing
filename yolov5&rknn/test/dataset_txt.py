import os
filePath = '/home/bill/Projects/jsjsj2/data/images'

with open('./dataset.txt', 'w') as f:
    for file_name in os.listdir(filePath):
        f.write(os.path.join(filePath, file_name))
        f.write("\n")
f.close()
