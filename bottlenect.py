import os
import tensorflow as tf
import tensorflow.python.platform
from tensorflow.python.platform import gfile
import numpy as np

def features(image):
	def create_graph():

	    with gfile.FastGFile('frozen_inference_graph.pb', 'rb') as f:
	        graph_def = tf.GraphDef()
	        graph_def.ParseFromString(f.read())
	    _ = tf.import_graph_def(graph_def, name='')
	create_graph()
	with tf.device('/gpu:0'):
		out = tf.get_default_graph().get_tensor_by_name('FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/BatchNorm/batchnorm/add_1:0')
		inn = tf.get_default_graph().get_tensor_by_name('image_tensor:0')
	with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
	    outtt = sess.run(out, feed_dict={inn:image})
	    return np.squeeze(outtt)