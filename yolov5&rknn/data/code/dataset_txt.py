import os
filePath = '../traffic-data/images/'

with open('../../rknn/dataset.txt', 'w') as f:
    for file_name in os.listdir(filePath):
        f.write(os.path.join('../data/traffic-data/images', file_name))
        f.write("\n")
f.close()
