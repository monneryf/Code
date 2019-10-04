import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from sklearn.datasets import fetch_california_housing

import tensorflow as TF

#####################################################################################
##########     DATA                     #############################################
#####################################################################################

x = TF.Variable(3,name="x")
y = TF.Variable(4,name="y")

f = x*x*y + y + 2

sess = TF.Session()
sess.run(x.initializer)
sess.run(y.initializer)

result = sess.run(f)

print(result)

sess.close()

#####################################################################################

sess = tf.InteractiveSession()
init.run()
result = f.eval()
print(result)

sess.close()

#####################################################################################

graph = tf.Graph()

with graph.as_default():
    x2 = tf.Variable(2)

#####################################################################################

housing = fetch_california_housing()
m, n = housing.data.shape
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing.data]

X = tf.constant(housing_data_plus_bias, dtype=tf.float32, name="X")
y = tf.constant(housing.target.reshape(-1, 1), dtype=tf.float32, name="y")
XT = tf.transpose(X)
theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT, X)), XT), y)

with tf.Session() as sess:
    theta_value = theta.eval()

#####################################################################################

theta = tf.Variable(tf.random_uniform([n + 1, 1], -1.0, 1.0), name="theta")

init = tf.global_variables_initializer()
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)

    for epoch in range(n_epochs):
        if epoch % 100 == 0:  # checkpoint every 100 epochs
            save_path = saver.save(sess, "/tmp/my_model.ckpt")

        sess.run(training_op)

    best_theta = theta.eval()
    save_path = saver.save(sess, "/tmp/my_model_final.ckpt")

#####################################################################################

with tf.Session() as sess:
    saver.restore(sess, "/tmp/my_model_final.ckpt")

#####################################################################################

from datetime import datetime

now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
root_logdir = "tf_logs"
logdir = "{}/run-{}/".format(root_logdir, now)

mse_summary = tf.summary.scalar('MSE', mse)
file_writer = tf.summary.FileWriter(logdir, tf.get_default_graph())





