---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Emotion Recognition Based on Tensorflow"
date: "2018-08-24"
categories: 
  - "dl-ml-python"
coverImage: "fear.jpg"
---

I chose a very simple project to be implemented to finish the whole classs inasmuch as in CS231n course, students were left a project to be done themselves. Well, this could be very simple and basic because I haven't learnt very detail and implemented all assignments by myself. And this tiny project will be my every first tensorflow & Computer vision project, later on I hope that I can make something creative like advanced style transfer. : )

* * *

- **Task: Emotion Recognition Based on CNNs**

Input a facial image, ouput the emotion( 0 = anger , 1 = disgust , 2 = fear , 3 = happy , 4 = sad , 5 = surprise , 6 = neutral) percentage.

**For example:** 

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_085215.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **Dataset, input shape and label shape**

From kaggle , click this [link](https://www.kaggle.com/c/facial-keypoints-detector/data)

**Training Input shape**: 3761 grayscale images of 48 * 48 pixels (3761, 48, 48, 1) **Training Label shape**: 3761 class images, seven elements label(mentioned above). **Test Set**:(1312, 48, 48, 1) **Single Image shape**:(48, 48, 1) (The following test img will be resize to 48*48) **label set** = [0. 0. 1. 0. 0. 0. 0.]  (FEAR)

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/figure_1.png" alt="screenshot" width="80%" height="auto">
</p>

- **CNN architecture**

 **conv layer**<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_090035.jpg" alt="screenshot" width="80%" height="auto">
</p>

Original x_image size (48,48,1), through a CNN layer with filter (5, 5, 32) stride = 1, padding = same, then h_conv1 will be (48, 48, 32), then passed to max pooling 2*2, stride = 2 and the shape will be shrunk to(24, 24, 32), then another cnn with filter (3, 3, 64), then again, the max poling, the resulting images are downsampled to 12 * 12 pixels

**fully connected layer**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_090833.jpg" alt="screenshot" width="80%" height="auto">
</p>

The (12, 12, 64) will be flatten and passed through 2 fc layers, the final label will be 7 labels.

* * *

- **Coding part**

We set the paths for storing the dataset on the computer, and the network parameters with the following code:(you can simply ignore it if you don't need it)

 1 FLAGS = tf.flags.FLAGS
 2 tf.flags.DEFINE_string("data_dir", "EmotionDetector/", "Path to data files")
 3 tf.flags.DEFINE_string("logs_dir", "logs/EmotionDetector_logs/", "Path to where log files are to be saved")
 4 tf.flags.DEFINE_string("mode", "train", "mode: train (Default)/ test")

Some constants:
```
 1 BATCH_SIZE = 128
 2 LEARNING_RATE = 1e-3
 3 MAX_ITERATIONS = 1001
 4 REGULARIZATION = 1e-2
 5 IMAGE_SIZE = 48
 6 NUM_LABELS = 7
 7 VALIDATION_PERCENT = 0.1
 ```

First of al, define weights and biases' shape using dict. Pay attention to the shape of weights and biases.

``` 
 1 weights = {
 2    'wc1': weight_variable([5, 5, 1, 32], name="We_conv1"),
 3    'wc2': weight_variable([3, 3, 32, 64],name="We_conv2"),
 4    'wf1': weight_variable([(IMAGE_SIZE // 4) * (IMAGE_SIZE // 4) * 64, 256],name="W_fc1"),
 5    'wf2': weight_variable([256, NUM_LABELS], name="W_fc2")
 6 }
 7 
 8 biases = {
 9    'bc1': bias_variable([32], name="b_conv1"),
10     'bc2': bias_variable([64], name="b_conv2"),
11     'bf1': bias_variable([256], name="b_fc1"),
12     'bf2': bias_variable([NUM_LABELS], name="b_fc2")
13 }
```

And the **weight_variable** above is a function for randomly initialization.
```
 1 def weight_variable(shape, stddev=0.02, name=None):
 2    initial = tf.truncated_normal(shape, stddev=stddev)
 3    if name is None:
 4        return tf.Variable(initial)
 5    else:
 6        return tf.get_variable(name, initializer=initial)
```
in tensorflow, we have a truncated_normal, and all you have to do is pass the shape and standard deviation, in this case, we set stddev to 0.02.

Then the rest we need to think about is the calculation of loss, normally in tensorflow we use softmax cross entropy with logits for every loss and tf.reduce_mean for all of the losses, in this project, we also add the regularization part to prevent overfitting.

 1 def loss(pred, label):
 2    cross_entropy_loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=label))
 3    tf.summary.scalar('Entropy', cross_entropy_loss)
 4    reg_losses = tf.add_n(tf.get_collection("losses"))
 5    tf.summary.scalar('Reg_loss', reg_losses)
 6    return cross_entropy_loss + REGULARIZATION * reg_losses

In this loss function, we add tf.summary.scalar for tensorboard, you can simply ignore it if you don't want to see the graph part, we get the reg_losses from add_n and get_collection, then times the REGULARIZATION constant for the final summation.

AFTER defining the loss function, we need a optimizer, in this case, we use AdamOptimizer which you can find on tensorflow documentation.

 1 def train(loss, step):
 2    return tf.train.AdamOptimizer(LEARNING_RATE).minimize(loss, global_step=step)

Then comes the most important part, cnn emotion, implemented the architecture we've seen above:
```python
 1 def emotion_cnn(dataset):
 2    with tf.name_scope("conv1") as scope:
 3        #W_conv1 = weight_variable([5, 5, 1, 32])
 4        #b_conv1 = bias_variable([32])
 5        tf.summary.histogram("We_conv1", weights['wc1'])
 6        tf.summary.histogram("b_conv1", biases['bc1'])
 7        conv_1 = tf.nn.conv2d(dataset, weights['wc1'],
 8                              strides=[1, 1, 1, 1], padding="SAME")
 9        h_conv1 = tf.nn.bias_add(conv_1, biases['bc1'])
10         #h_conv1 = conv2d_basic(dataset, W_conv1, b_conv1)
11         h_1 = tf.nn.relu(h_conv1)
12         h_pool1 = max_pool_2x2(h_1)
13         add_to_regularization_loss(weights['wc1'], biases['bc1'])
14 
15     with tf.name_scope("conv2") as scope:
16         #W_conv2 = weight_variable([3, 3, 32, 64])
17         #b_conv2 = bias_variable([64])
18         tf.summary.histogram("We_conv2", weights['wc2'])
19         tf.summary.histogram("b_conv2", biases['bc2'])
20         conv_2 = tf.nn.conv2d(h_pool1, weights['wc2'], strides=[1, 1, 1, 1], padding="SAME")
21         h_conv2 = tf.nn.bias_add(conv_2, biases['bc2'])
22         #h_conv2 = conv2d_basic(h_pool1, weights['wc2'], biases['bc2'])
23         h_2 = tf.nn.relu(h_conv2)
24         h_pool2 = max_pool_2x2(h_2)
25         add_to_regularization_loss(weights['wc2'], biases['bc2'])
26 
27     with tf.name_scope("fc_1") as scope:
28         prob = 0.5
29         image_size = IMAGE_SIZE // 4
30         h_flat = tf.reshape(h_pool2, [-1, image_size * image_size * 64])
31         #W_fc1 = weight_variable([image_size * image_size * 64, 256])
32         #b_fc1 = bias_variable([256])
33         tf.summary.histogram("W_fc1", weights['wf1'])
34         tf.summary.histogram("b_fc1", biases['bf1'])
35         h_fc1 = tf.nn.relu(tf.matmul(h_flat, weights['wf1']) + biases['bf1'])
36         h_fc1_dropout = tf.nn.dropout(h_fc1, prob)
37         
38     with tf.name_scope("fc_2") as scope:
39         #W_fc2 = weight_variable([256, NUM_LABELS])
40         #b_fc2 = bias_variable([NUM_LABELS])
41         tf.summary.histogram("W_fc2", weights['wf2'])
42         tf.summary.histogram("b_fc2", biases['bf2'])
43         #pred = tf.matmul(h_fc1, weights['wf2']) + biases['bf2']
44         pred = tf.matmul(h_fc1_dropout, weights['wf2']) + biases['bf2']
45 
46     return pred
```
tf.summary_histogram is for tensorboard, functions like tf.nn.conv2d, tf.nn.relu, tf.nn.dropout can be found on [documentation](https://tensorflow.google.cn/api_docs/). and some details you might notice is that every part is on there own scope, and bias and weights should be added to regularization loss function for L2 loss.

 1 def add_to_regularization_loss(W, b):
 2    tf.add_to_collection("losses", tf.nn.l2_loss(W))
 3    tf.add_to_collection("losses", tf.nn.l2_loss(b))

* * *

- **Main function for data feeding and sess.run**

In the main function, not only should we load data (**read_data** function in the EmotionDetectorUtils, you can find this file in the end of this blog), but we also need to make placeholder for variables like **input_dataset** and **input_labels**(since they are assigned by batch data when training),  and **global_step**, which is a vairable we need to mark in every 10 step or 100 step during training.

 1    global_step = tf.Variable(0, trainable=False)
 2    dropout_prob = tf.placeholder(tf.float32)
 3    input_dataset = tf.placeholder(tf.float32, [None, IMAGE_SIZE, IMAGE_SIZE, 1],name="input")
 4    input_labels = tf.placeholder(tf.float32, [None, NUM_LABELS])

**outside the sess.run**, we should call the emotion_cnn, loss, train function because once we use sess.run and pass the value returned by these function, these function will be automatically called during training time. so remember always put them outside of the **tf.Session() as sess** part.

 1    pred = emotion_cnn(input_dataset)
 2    output_pred = tf.nn.softmax(pred,name="output")
 3    loss_val = loss(pred, input_labels)
 4    train_op = train(loss_val, global_step)

**inside the sess.run**, we start the training part, first and foremost, global vairable initializer(), remember we have already initialized lots of varaibles, and this function will initialize them all. In the for loop of training, we call **sess.run(train_op, feed_dict = feed_dict)** and feed batch data for every step training, in every 10 steps, we calculate the **Training loss** and print it out, and in every 100 steps, we print out the **validation loss. And other code is about tensorboard and model saver, I will discuss it later on in other blogs.**

 1   with tf.Session() as sess:
 2        sess.run(tf.global_variables_initializer())
 3        summary_writer = tf.summary.FileWriter(FLAGS.logs_dir, sess.graph_def)
 4        saver = tf.train.Saver()
 5        ckpt = tf.train.get_checkpoint_state(FLAGS.logs_dir)
 6        if ckpt and ckpt.model_checkpoint_path:
 7            saver.restore(sess, ckpt.model_checkpoint_path)
 8            print("Model Restored!")
 9 
10         for step in range(MAX_ITERATIONS):
11             batch_image, batch_label = get_next_batch(train_images, train_labels, step)
12             feed_dict = {input_dataset: batch_image, input_labels: batch_label}
13 
14             sess.run(train_op, feed_dict=feed_dict)
15             if step % 10 == 0:
16                 train_loss, summary_str = sess.run([loss_val, summary_op], feed_dict=feed_dict)
17                 summary_writer.add_summary(summary_str, global_step=step)
18                 print("Training Loss: %f" % train_loss)
19 
20             if step % 100 == 0:
21                 valid_loss = sess.run(loss_val, feed_dict={input_dataset: valid_images, input_labels: valid_labels})
22                 print("%s Validation Loss: %f" % (datetime.now(), valid_loss))
23                 saver.save(sess, FLAGS.logs_dir + 'model.ckpt', global_step=step)

* * *

- Result:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_085215.jpg" alt="screenshot" width="80%" height="auto">
</p>

 

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_1008451.jpg" alt="screenshot" width="80%" height="auto">
</p>

 

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_100832.jpg" alt="screenshot" width="80%" height="auto">
</p>

* * *

Reference :   DeepLearning With Tensorflow

Source code : [Github](https://github.com/ZhengLiangliang1996/EmotionRecognition).

Thanks for reading, if there is a mistake on typing or on code, please let me now by leaving a commend below or sending email to zhengliangliang1996@gmail.com.
