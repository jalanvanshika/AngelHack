import cv2
import math
import os
import tensorflow as tf
import tensorflow.python.platform
from tensorflow.python.platform import gfile
import numpy as np
from bottlenect import features
def frameCap():
    path = input('enter path')
    frameList=[]
    vidcap = cv2.VideoCapture(path)
    success,image = vidcap.read()
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    est_video_length_minutes = 3         # Round up if not sure.
    est_tot_frames = est_video_length_minutes * 30 * fps  # Sets an upper bound # of frames in video clip

    n = 30                             # Desired interval of frames to include
    desired_frames = n * np.arange(est_tot_frames) 
    for i in desired_frames:
        vidcap.set(1,i-1)                      
        success,image = vidcap.read(1)
        image = np.array([cv2.cvtColor(image, cv2.COLOR_BGR2RGB)])
        image = features(image)
        frameList.append(image)
        print('DONE SOME FRAMES\n')
    vidcap.release()    
    frameList = np.array(frameList)
    b = os.path.basename(a)
    np.save(b[:b.find('.mp4')]+'.npz')
frameCap()