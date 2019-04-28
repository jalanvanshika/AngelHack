import cv2
import math
import os
import tensorflow as tf
import tensorflow.python.platform
from tensorflow.python.platform import gfile
import numpy as np
from extract_video_feat import frameCap
import glob
dir=os.path.join('Videos','Assault')
files = glob.glob(os.path.join(dir,'*.mp4'))
for file in files:
	print('processing-',file,'\n')
	frameCap(file)