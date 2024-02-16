import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random
from shutil import copyfile

# 根据自己的数据标签修改
classes=['red', 'yellow', 'green', 'turn_left', 'turn_right', 'stop']

def clear_hidden_files(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abspath = os.path.join(os.path.abspath(path), i)
        if os.path.isfile(abspath):
            if i.startswith("._"):
                os.remove(abspath)
        else:
            clear_hidden_files(abspath)

def convert(size, box, image_id):
    if size[0]==0 or size[1] == 0:
        os.remove("/home/bill/Projects/jsjsj2/data/xml/" + image_id + ".xml")
        os.remove("/home/bill/Projects/jsjsj2/data/images/" + image_id + ".jpg")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" + image_id)

    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    in_file = open('/home/bill/Projects/jsjsj2/data/xml/%s.xml' %image_id)
    out_file = open('/home/bill/Projects/jsjsj2/data/YOLOLabels/%s.txt' %image_id, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    if str(root.find('size')) == "None":
        os.remove("/home/bill/Projects/jsjsj2/data/xml/"+image_id+".xml")
        os.remove("/home/bill/Projects/jsjsj2/data/images/" + image_id + ".jpg")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"+image_id)
        return 1
    else:
        size = root.find('size')
        print(root.find('size'))
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        # print(w,h)

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            # print(difficult, cls)
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            bb = convert((w, h), b, image_id)
            if str(cls_id) + " " + " ".join([str(a) for a in bb]) == "":
                print(image_id)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

        out_file.close()
        filename = os.path.basename(out_file.name)
        print(filename, ':', os.path.getsize("/home/bill/Projects/jsjsj2/data/YOLOLabels/" + filename))
        # with open('data/VOC2012HLD/YOLOLabels/%s.txt' %image_id, 'r') as f:  # 打开文件
        #     data = f.read()  # 读取文件
        #     print(data)
        in_file.close()
        return 0



wd = os.getcwd()
wd = os.getcwd()
data_base_dir = os.path.join(wd, "/home/bill/Projects/jsjsj2/")
if not os.path.isdir(data_base_dir):
    os.mkdir(data_base_dir)
work_sapce_dir = os.path.join(data_base_dir, "data/")
if not os.path.isdir(work_sapce_dir):
    os.mkdir(work_sapce_dir)
annotation_dir = os.path.join(work_sapce_dir, "xml/")
if not os.path.isdir(annotation_dir):
        os.mkdir(annotation_dir)
clear_hidden_files(annotation_dir)
image_dir = os.path.join(work_sapce_dir, "images/")
if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
clear_hidden_files(image_dir)
yolo_labels_dir = os.path.join(work_sapce_dir, "YOLOLabels/")
if not os.path.isdir(yolo_labels_dir):
        os.mkdir(yolo_labels_dir)
clear_hidden_files(yolo_labels_dir)
yolov5_images_dir = os.path.join(data_base_dir, "use/images/")
if not os.path.isdir(yolov5_images_dir):
        os.mkdir(yolov5_images_dir)
clear_hidden_files(yolov5_images_dir)
yolov5_labels_dir = os.path.join(data_base_dir, "use/labels/")
if not os.path.isdir(yolov5_labels_dir):
        os.mkdir(yolov5_labels_dir)
clear_hidden_files(yolov5_labels_dir)
yolov5_images_train_dir = os.path.join(yolov5_images_dir, "train/")
if not os.path.isdir(yolov5_images_train_dir):
        os.mkdir(yolov5_images_train_dir)
clear_hidden_files(yolov5_images_train_dir)
yolov5_images_test_dir = os.path.join(yolov5_images_dir, "val/")
if not os.path.isdir(yolov5_images_test_dir):
        os.mkdir(yolov5_images_test_dir)
clear_hidden_files(yolov5_images_test_dir)
yolov5_labels_train_dir = os.path.join(yolov5_labels_dir, "train/")
if not os.path.isdir(yolov5_labels_train_dir):
        os.mkdir(yolov5_labels_train_dir)
clear_hidden_files(yolov5_labels_train_dir)
yolov5_labels_test_dir = os.path.join(yolov5_labels_dir, "val/")
if not os.path.isdir(yolov5_labels_test_dir):
        os.mkdir(yolov5_labels_test_dir)
clear_hidden_files(yolov5_labels_test_dir)

train_file = open(os.path.join(wd, "yolov5_train.txt"), 'w')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'w')
train_file.close()
test_file.close()
train_file = open(os.path.join(wd, "yolov5_train.txt"), 'a')
test_file = open(os.path.join(wd, "yolov5_val.txt"), 'a')
list_imgs = os.listdir(image_dir) # list image files
probo = random.randint(1, 100)
print("Probobility: %d" % probo)
for i in range(0,len(list_imgs)):
    path = os.path.join(image_dir,list_imgs[i])
    if os.path.isfile(path):
        image_path = image_dir + list_imgs[i]
        voc_path = list_imgs[i]
        (nameWithoutExtention, extention) = os.path.splitext(os.path.basename(image_path))
        (voc_nameWithoutExtention, voc_extention) = os.path.splitext(os.path.basename(voc_path))
        annotation_name = nameWithoutExtention + '.xml'
        annotation_path = os.path.join(annotation_dir, annotation_name)
        label_name = nameWithoutExtention + '.txt'
        label_path = os.path.join(yolo_labels_dir, label_name)
    probo = random.randint(1, 100)
    # print("Probobility: %d" % probo)
    if(probo < 80): # train dataset
        if os.path.exists(annotation_path):
            train_file.write(image_path + '\n')
            print(image_path)
            if convert_annotation(nameWithoutExtention)==0:# convert label
                copyfile(image_path, yolov5_images_train_dir + voc_path)
                copyfile(label_path, yolov5_labels_train_dir + label_name)
            else:
                continue


    else: # test dataset
        if os.path.exists(annotation_path):
            print(image_path)
            test_file.write(image_path + '\n')
            if convert_annotation(nameWithoutExtention)==0:# convert label
                copyfile(image_path, yolov5_images_test_dir + voc_path)
                copyfile(label_path, yolov5_labels_test_dir + label_name)
            else:
                continue

train_file.close()
test_file.close()
