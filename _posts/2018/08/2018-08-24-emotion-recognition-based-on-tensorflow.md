---
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

![fear.jpg](https://zhengliangliang.files.wordpress.com/2018/08/fear.jpg)          ![2018-08-24_085215.jpg](https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_085215.jpg)

- **Dataset, input shape and label shape**

From kaggle , click this [link](https://www.kaggle.com/c/facial-keypoints-detector/data)

**Training Input shape**: 3761 grayscale images of 48 \* 48 pixels (3761, 48, 48, 1) **Training Label shape**: 3761 class images, seven elements label(mentioned above). **Test Set**:(1312, 48, 48, 1) **Single Image shape**:(48, 48, 1) (The following test img will be resize to 48\*48) **label set** = \[0. 0. 1. 0. 0. 0. 0.\]  (FEAR)

![Figure_1.png](https://zhengliangliang.files.wordpress.com/2018/08/figure_1.png)

- **CNN architecture**

 **conv layer**![2018-08-24_090035.jpg](https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_090035.jpg)

Original x\_image size (48,48,1), through a CNN layer with filter (5, 5, 32) stride = 1, padding = same, then h\_conv1 will be (48, 48, 32), then passed to max pooling 2\*2, stride = 2 and the shape will be shrunk to(24, 24, 32), then another cnn with filter (3, 3, 64), then again, the max poling, the resulting images are downsampled to 12 \* 12 pixels

**fully connected layer**

![2018-08-24_090833.jpg](https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_090833.jpg)

The (12, 12, 64) will be flatten and passed through 2 fc layers, the final label will be 7 labels.

* * *

- **Coding part**

We set the paths for storing the dataset on the computer, and the network parameters with the following code:(you can simply ignore it if you don't need it)

 1 FLAGS \= tf.flags.FLAGS
 2 tf.flags.DEFINE\_string("data\_dir", "EmotionDetector/", "Path to data files")
 3 tf.flags.DEFINE\_string("logs\_dir", "logs/EmotionDetector\_logs/", "Path to where log files are to be saved")
 4 tf.flags.DEFINE\_string("mode", "train", "mode: train (Default)/ test")

Some constants:

 1 BATCH\_SIZE \= 128
 2 LEARNING\_RATE \= 1e-3
 3 MAX\_ITERATIONS \= 1001
 4 REGULARIZATION \= 1e-2
 5 IMAGE\_SIZE \= 48
 6 NUM\_LABELS \= 7
 7 VALIDATION\_PERCENT \= 0.1

First of al, define weights and biases' shape using dict. Pay attention to the shape of weights and biases.

 1 weights \= {
 2    'wc1': weight\_variable(\[5, 5, 1, 32\], name\="We\_conv1"),
 3    'wc2': weight\_variable(\[3, 3, 32, 64\],name\="We\_conv2"),
 4    'wf1': weight\_variable(\[(IMAGE\_SIZE // 4) \* (IMAGE\_SIZE // 4) \* 64, 256\],name\="W\_fc1"),
 5    'wf2': weight\_variable(\[256, NUM\_LABELS\], name\="W\_fc2")
 6 }
 7 
 8 biases \= {
 9    'bc1': bias\_variable(\[32\], name\="b\_conv1"),
10     'bc2': bias\_variable(\[64\], name\="b\_conv2"),
11     'bf1': bias\_variable(\[256\], name\="b\_fc1"),
12     'bf2': bias\_variable(\[NUM\_LABELS\], name\="b\_fc2")
13 }

And the **weight\_variable** above is a function for randomly initialization.

 1 def weight\_variable(shape, stddev\=0.02, name\=None):
 2    initial \= tf.truncated\_normal(shape, stddev\=stddev)
 3    if name is None:
 4        return tf.Variable(initial)
 5    else:
 6        return tf.get\_variable(name, initializer\=initial)

in tensorflow, we have a truncated\_normal, and all you have to do is pass the shape and standard deviation, in this case, we set stddev to 0.02.

Then the rest we need to think about is the calculation of loss, normally in tensorflow we use softmax cross entropy with logits for every loss and tf.reduce\_mean for all of the losses, in this project, we also add the regularization part to prevent overfitting.

 1 def loss(pred, label):
 2    cross\_entropy\_loss \= tf.reduce\_mean(tf.nn.softmax\_cross\_entropy\_with\_logits(logits\=pred, labels\=label))
 3    tf.summary.scalar('Entropy', cross\_entropy\_loss)
 4    reg\_losses \= tf.add\_n(tf.get\_collection("losses"))
 5    tf.summary.scalar('Reg\_loss', reg\_losses)
 6    return cross\_entropy\_loss + REGULARIZATION \* reg\_losses

In this loss function, we add tf.summary.scalar for tensorboard, you can simply ignore it if you don't want to see the graph part, we get the reg\_losses from add\_n and get\_collection, then times the REGULARIZATION constant for the final summation.

AFTER defining the loss function, we need a optimizer, in this case, we use AdamOptimizer which you can find on tensorflow documentation.

 1 def train(loss, step):
 2    return tf.train.AdamOptimizer(LEARNING\_RATE).minimize(loss, global\_step\=step)

Then comes the most important part, cnn emotion, implemented the architecture we've seen above:

 1 def emotion\_cnn(dataset):
 2    with tf.name\_scope("conv1") as scope:
 3        #W\_conv1 = weight\_variable(\[5, 5, 1, 32\])
 4        #b\_conv1 = bias\_variable(\[32\])
 5        tf.summary.histogram("We\_conv1", weights\['wc1'\])
 6        tf.summary.histogram("b\_conv1", biases\['bc1'\])
 7        conv\_1 \= tf.nn.conv2d(dataset, weights\['wc1'\],\\
 8                              strides\=\[1, 1, 1, 1\], padding\="SAME")
 9        h\_conv1 \= tf.nn.bias\_add(conv\_1, biases\['bc1'\])
10         #h\_conv1 = conv2d\_basic(dataset, W\_conv1, b\_conv1)
11         h\_1 \= tf.nn.relu(h\_conv1)
12         h\_pool1 \= max\_pool\_2x2(h\_1)
13         add\_to\_regularization\_loss(weights\['wc1'\], biases\['bc1'\])
14 
15     with tf.name\_scope("conv2") as scope:
16         #W\_conv2 = weight\_variable(\[3, 3, 32, 64\])
17         #b\_conv2 = bias\_variable(\[64\])
18         tf.summary.histogram("We\_conv2", weights\['wc2'\])
19         tf.summary.histogram("b\_conv2", biases\['bc2'\])
20         conv\_2 \= tf.nn.conv2d(h\_pool1, weights\['wc2'\], strides\=\[1, 1, 1, 1\], padding\="SAME")
21         h\_conv2 \= tf.nn.bias\_add(conv\_2, biases\['bc2'\])
22         #h\_conv2 = conv2d\_basic(h\_pool1, weights\['wc2'\], biases\['bc2'\])
23         h\_2 \= tf.nn.relu(h\_conv2)
24         h\_pool2 \= max\_pool\_2x2(h\_2)
25         add\_to\_regularization\_loss(weights\['wc2'\], biases\['bc2'\])
26 
27     with tf.name\_scope("fc\_1") as scope:
28         prob \= 0.5
29         image\_size \= IMAGE\_SIZE // 4
30         h\_flat \= tf.reshape(h\_pool2, \[-1, image\_size \* image\_size \* 64\])
31         #W\_fc1 = weight\_variable(\[image\_size \* image\_size \* 64, 256\])
32         #b\_fc1 = bias\_variable(\[256\])
33         tf.summary.histogram("W\_fc1", weights\['wf1'\])
34         tf.summary.histogram("b\_fc1", biases\['bf1'\])
35         h\_fc1 \= tf.nn.relu(tf.matmul(h\_flat, weights\['wf1'\]) + biases\['bf1'\])
36         h\_fc1\_dropout \= tf.nn.dropout(h\_fc1, prob)
37         
38     with tf.name\_scope("fc\_2") as scope:
39         #W\_fc2 = weight\_variable(\[256, NUM\_LABELS\])
40         #b\_fc2 = bias\_variable(\[NUM\_LABELS\])
41         tf.summary.histogram("W\_fc2", weights\['wf2'\])
42         tf.summary.histogram("b\_fc2", biases\['bf2'\])
43         #pred = tf.matmul(h\_fc1, weights\['wf2'\]) + biases\['bf2'\]
44         pred \= tf.matmul(h\_fc1\_dropout, weights\['wf2'\]) + biases\['bf2'\]
45 
46     return pred

tf.summary\_histogram is for tensorboard, functions like tf.nn.conv2d, tf.nn.relu, tf.nn.dropout can be found on [documentation](https://tensorflow.google.cn/api_docs/). and some details you might notice is that every part is on there own scope, and bias and weights should be added to regularization loss function for L2 loss.

 1 def add\_to\_regularization\_loss(W, b):
 2    tf.add\_to\_collection("losses", tf.nn.l2\_loss(W))
 3    tf.add\_to\_collection("losses", tf.nn.l2\_loss(b))

* * *

- **Main function for data feeding and sess.run**

In the main function, not only should we load data (**read\_data** function in the EmotionDetectorUtils, you can find this file in the end of this blog), but we also need to make placeholder for variables like **input\_dataset** and **input\_labels**(since they are assigned by batch data when training),  and **global\_step**, which is a vairable we need to mark in every 10 step or 100 step during training.

 1    global\_step \= tf.Variable(0, trainable\=False)
 2    dropout\_prob \= tf.placeholder(tf.float32)
 3    input\_dataset \= tf.placeholder(tf.float32, \[None, IMAGE\_SIZE, IMAGE\_SIZE, 1\],name\="input")
 4    input\_labels \= tf.placeholder(tf.float32, \[None, NUM\_LABELS\])

**outside the sess.run**, we should call the emotion\_cnn, loss, train function because once we use sess.run and pass the value returned by these function, these function will be automatically called during training time. so remember always put them outside of the **tf.Session() as sess** part.

 1    pred \= emotion\_cnn(input\_dataset)
 2    output\_pred \= tf.nn.softmax(pred,name\="output")
 3    loss\_val \= loss(pred, input\_labels)
 4    train\_op \= train(loss\_val, global\_step)

**inside the sess.run**, we start the training part, first and foremost, global vairable initializer(), remember we have already initialized lots of varaibles, and this function will initialize them all. In the for loop of training, we call **sess.run(train\_op, feed\_dict = feed\_dict)** and feed batch data for every step training, in every 10 steps, we calculate the **Training loss** and print it out, and in every 100 steps, we print out the **validation loss. And other code is about tensorboard and model saver, I will discuss it later on in other blogs.**

 1   with tf.Session() as sess:
 2        sess.run(tf.global\_variables\_initializer())
 3        summary\_writer \= tf.summary.FileWriter(FLAGS.logs\_dir, sess.graph\_def)
 4        saver \= tf.train.Saver()
 5        ckpt \= tf.train.get\_checkpoint\_state(FLAGS.logs\_dir)
 6        if ckpt and ckpt.model\_checkpoint\_path:
 7            saver.restore(sess, ckpt.model\_checkpoint\_path)
 8            print("Model Restored!")
 9 
10         for step in range(MAX\_ITERATIONS):
11             batch\_image, batch\_label \= get\_next\_batch(train\_images, train\_labels, step)
12             feed\_dict \= {input\_dataset: batch\_image, input\_labels: batch\_label}
13 
14             sess.run(train\_op, feed\_dict\=feed\_dict)
15             if step % 10 \== 0:
16                 train\_loss, summary\_str \= sess.run(\[loss\_val, summary\_op\], feed\_dict\=feed\_dict)
17                 summary\_writer.add\_summary(summary\_str, global\_step\=step)
18                 print("Training Loss: %f" % train\_loss)
19 
20             if step % 100 \== 0:
21                 valid\_loss \= sess.run(loss\_val, feed\_dict\={input\_dataset: valid\_images, input\_labels: valid\_labels})
22                 print("%s Validation Loss: %f" % (datetime.now(), valid\_loss))
23                 saver.save(sess, FLAGS.logs\_dir + 'model.ckpt', global\_step\=step)

* * *

- Result:

![fear.jpg](https://zhengliangliang.files.wordpress.com/2018/08/fear.jpg)               ![2018-08-24_085215.jpg](https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_085215.jpg)

 

![gavin_fakesmile.jpg](https://zhengliangliang.files.wordpress.com/2018/08/gavin_fakesmile1.jpg)                              ![2018-08-24_100845.jpg](https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_1008451.jpg)

 

![smile.jpg](https://zhengliangliang.files.wordpress.com/2018/08/smile.jpg)                           ![2018-08-24_100832.jpg](https://zhengliangliang.files.wordpress.com/2018/08/2018-08-24_100832.jpg)

* * *

Reference :   DeepLearning With Tensorflow

Source code : [Github](https://github.com/ZhengLiangliang1996/EmotionRecognition).

Thanks for reading, if there is a mistake on typing or on code, please let me now by leaving a commend below or sending email to zhengliangliang1996@gmail.com.
