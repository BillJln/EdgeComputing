import os
import sys
import numpy as np
from rknn.api import RKNN

rknn = RKNN()
ret = rknn.config(reorder_channel='0 1 2',
                  mean_values=[[0, 0, 0]],
                  std_values=[[255, 255, 255]],
                  optimization_level=3,
                  target_platform='rk3399pro',
                  output_optimize=1,
                  quantize_input_node=True)

print(ret)

# ret = rknn.load_onnx(model="../runs/train/exp4/weights/best.onnx",
#                      outputs=['378', '439', '500'])

# ret = rknn.load_onnx(model="../runs/train/exp6/weights/best.onnx",
#                      outputs=['388', '449', '327'])

ret = rknn.load_onnx(model="../runs/train/exp6/weights/best.onnx",
                     outputs=['327', '388', '449'])

ret = rknn.build(do_quantization=True, dataset='./dataset.txt', pre_compile=False, rknn_batch_size=1)

ret = rknn.export_rknn('./rknnWeights/yolov5n.rknn')

print(ret)

rknn.release()