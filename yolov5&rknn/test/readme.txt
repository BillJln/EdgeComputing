解压yolov5.tar.gz

在当前文件夹（解压完的yolov5文件夹的父文件夹，示例：开发板：root@debian10:/home/nle/notebook；PC:(py36-rknn) bill@bill-desktop:~/Projects/jsjsj）下运行命令：

示例： 运行指令+需要检测的图片/视频（自行替换绝对路径图片和绝对路径视频路径）
图片检测：sudo python3 yolov5/test/rknn_detect_image.py yolov5/test/image/000015.jpg（开发板），python yolov5/test/rknn_detect_image.py yolov5/test/image/000015.jpg （conda）
视频检测：sudo python3 yolov5/test/rknn_detect_video.py yolov5/test/video/video.mp4（开发板），python yolov5/test/rknn_detect_video.py /home/bill/Projects/jsjsj/yolov5/test/video/video.mp4 （conda）

运行结果：
图片检测：结果存放在yolov5/test/result文件夹内
视频检测：结果存放于yolov5/test/result.txt
