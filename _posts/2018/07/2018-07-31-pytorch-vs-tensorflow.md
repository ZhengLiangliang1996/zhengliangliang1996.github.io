---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Pytorch VS Tensorflow"
date: "2018-07-31"
categories: 
  - "dl-ml-python"
---

Right now Pytorch and Tensorflow are the extremely popular AI frameworks , but AI researchers may find it a little bit tangled when it comes to the question that which framework to use. So rather than choose one of them to learn, why not use both of them since they will come in handy later on. So I'm going to introduce both of them from the perspective of  vanilla structure and API.

### **Pytorch** 

A PyTorch Tensor is conceptionally similar to a numpy array: it is an n-dimensional grid of numbers, and like numpy PyTorch provides many functions to efficiently operate on Tensors.

all of the packages we import in this blog for pytorch part:
```python
 1 import torch
 2 import torch.nn as nn
 3 import torch.optim as optim
 4 from torch.utils.data import DataLoader
 5 from torch.utils.data import sampler
 6 
 7 import torchvision.datasets as dset
 8 import torchvision.transforms as T
 9 
10 import numpy as np
```

Image data is typically stored in a Tensor shape x = N * C * H * W

- N is the number of datapoints
- C is the number of channels
- H is the height of the intermediate feature map in pixels
- W is the height of the intermediate feature map in pixels

When we process the fully connected layer, we need to flatten the C * H *W values into a single vector per image

 1 def flatten(x):
 2    N = x.shape[0] # read in N, C, H, W
 3    return x.view(N, -1)  # "flatten" the C * H * W values into a single vector per image

**Three-layer network ** Implement a vanilla structure of three-layer netwok, and the architecture will be as follows:

1. A convolutional layer (with bias) with `channel_1` filters, each with shape `KW1 x KH1`, and zero-padding of two
2. ReLU nonlinearity
3. A convolutional layer (with bias) with `channel_2` filters, each with shape `KW2 x KH2`, and zero-padding of one
4. ReLU nonlinearity
5. Fully-connected layer with bias, producing scores for C classes.

Nomally, the function contains 2 parameters, which are input x and params, and the params are specified based on how many layers and what type of architecture you're using.

Notice that this architecture includes 2 convolutional layer, we need the conv2d function from torch.nn.functional.conv2d<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/07/2018-07-31_123127.jpg" alt="screenshot" width="80%" height="auto">
</p>

And the core functions are conv2d,relu and mm
```python
 1 def three_layer_convnet(x, params):
 2    """
 3    Performs the forward pass of a three-layer convolutional network with the
 4    architecture defined above.
 5 
 6    Inputs:
 7    - x: A PyTorch Tensor of shape (N, 3, H, W) giving a minibatch of images
 8    - params: A list of PyTorch Tensors giving the weights and biases for the
 9      network; should contain the following:
10       - conv_w1: PyTorch Tensor of shape (channel_1, 3, KH1, KW1) giving weights
11         for the first convolutional layer
12       - conv_b1: PyTorch Tensor of shape (channel_1,) giving biases for the first
13         convolutional layer
14       - conv_w2: PyTorch Tensor of shape (channel_2, channel_1, KH2, KW2) giving
15         weights for the second convolutional layer
16       - conv_b2: PyTorch Tensor of shape (channel_2,) giving biases for the second
17         convolutional layer
18       - fc_w: PyTorch Tensor giving weights for the fully-connected layer. Can you
19         figure out what the shape should be?
20       - fc_b: PyTorch Tensor giving biases for the fully-connected layer. Can you
21         figure out what the shape should be?
22     
23     Returns:
24     - scores: PyTorch Tensor of shape (N, C) giving classification scores for x
25     """
26     conv_w1, conv_b1, conv_w2, conv_b2, fc_w, fc_b = params
27     scores = None
28     ################################################################################
29     # TODO: Implement the forward pass for the three-layer ConvNet.                #
30     ################################################################################
31     conv1 = F.conv2d(x, weight=conv_w1, bias=conv_b1, padding=2)
32     relu1 = F.relu(conv1)
33     conv2 = F.conv2d(relu1, weight=conv_w2, bias=conv_b2, padding=1)
34     relu2 = F.relu(conv2)
35     relu2_flat = flatten(relu2)
36     scores = relu2_flat.mm(fc_w) + fc_b
37     #pass
38     ################################################################################
39     #                                 END OF YOUR CODE                             #
40     ################################################################################
41     return scores
```
**Pytorch Initialization :**

- `random_weight(shape)` initializes a weight tensor with the Kaiming normalization method.(normally do it with weights)
- `zero_weight(shape)` initializes a weight tensor with all zeros. Useful for instantiating bias parameters.(normally do it with biases)
```python
 1 def random_weight(shape):
 2    """
 3    Create random Tensors for weights; setting requires_grad=True means that we
 4    want to compute gradients for these Tensors during the backward pass.
 5    We use Kaiming normalization: sqrt(2 / fan_in)
 6    """
 7    if len(shape) == 2:  # FC weight
 8        fan_in = shape[0]
 9    else:
10         fan_in = np.prod(shape[1:]) # conv weight [out_channel, in_channel, kH, kW]
11     # randn is standard normal distribution generator. 
12     w = torch.randn(shape, device=device, dtype=dtype) * np.sqrt(2. / fan_in)
13     w.requires_grad = True
14     return w
15 
16 def zero_weight(shape):
17     return torch.zeros(shape, device=device, dtype=dtype, requires_grad=True)
18 
19 # create a weight of shape [3 x 5]
20 # you should see the type `torch.cuda.FloatTensor` if you use GPU. 
21 # Otherwise it should be `torch.FloatTensor`
22 random_weight((3, 5))
```
**PyTorch: Check Accuracy**

When checking accuracy we don't need to compute any gradients; as a result we don't need PyTorch to build a computational graph for us when we compute scores. To prevent a graph from being built we scope our computation under a `torch.no_grad()` context manager.
```python

 1 def check_accuracy_part2(loader, model_fn, params):
 2    """
 3    Check the accuracy of a classification model.
 4    
 5    Inputs:
 6    - loader: A DataLoader for the data split we want to check
 7    - model_fn: A function that performs the forward pass of the model,
 8      with the signature scores = model_fn(x, params)
 9    - params: List of PyTorch Tensors giving parameters of the model
10     
11     Returns: Nothing, but prints the accuracy of the model
12     """
13     split = 'val' if loader.dataset.train else 'test'
14     print('Checking accuracy on the %s set' % split)
15     num_correct, num_samples = 0, 0
16     with torch.no_grad():
17         for x, y in loader:
18             x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
19             y = y.to(device=device, dtype=torch.int64)
20             scores = model_fn(x, params)
21             _, preds = scores.max(1)
22             num_correct += (preds == y).sum()
23             num_samples += preds.size(0)
24         acc = float(num_correct) / num_samples
25         print('Got %d / %d correct (%.2f%%)' % (num_correct, num_samples, 100 * acc))
```
 **PyTorch: Training Loop**

The final step is to train the model , firstly move the data to proper device and then compute the loss , then using SGD to compute the gradients. then call the check accuracy function to print out the accuracy
```python
 1 def train_part2(model_fn, params, learning_rate):
 2    """
 3    Train a model on CIFAR-10.
 4    
 5    Inputs:
 6    - model_fn: A Python function that performs the forward pass of the model.
 7      It should have the signature scores = model_fn(x, params) where x is a
 8      PyTorch Tensor of image data, params is a list of PyTorch Tensors giving
 9      model weights, and scores is a PyTorch Tensor of shape (N, C) giving
10       scores for the elements in x.
11     - params: List of PyTorch Tensors giving weights for the model
12     - learning_rate: Python scalar giving the learning rate to use for SGD
13     
14     Returns: Nothing
15     """
16     for t, (x, y) in enumerate(loader_train):
17         # Move the data to the proper device (GPU or CPU)
18         x = x.to(device=device, dtype=dtype)
19         y = y.to(device=device, dtype=torch.long)
20 
21         # Forward pass: compute scores and loss
22         scores = model_fn(x, params)
23         loss = F.cross_entropy(scores, y)
24 
25         # Backward pass: PyTorch figures out which Tensors in the computational
26         # graph has requires_grad=True and uses backpropagation to compute the
27         # gradient of the loss with respect to these Tensors, and stores the
28         # gradients in the .grad attribute of each Tensor.
29         loss.backward()
30 
31         # Update parameters. We don't want to backpropagate through the
32         # parameter updates, so we scope the updates under a torch.no_grad()
33         # context manager to prevent a computational graph from being built.
34         with torch.no_grad():
35             for w in params:
36                 w -= learning_rate * w.grad
37 
38                 # Manually zero the gradients after running the backward pass
39                 w.grad.zero_()
40 
41         if t % print_every == 0:
42             print('Iteration %d, loss = %.4f' % (t, loss.item()))
43             check_accuracy_part2(loader_val, model_fn, params)
44             print()
```
To sum up, the whole process will be 1. Initialize hidden layer size and learning rate,weights 2. Passing data and params( in train function) to three_layer_convnet 3. After computing the scores,then calculate the cross entropy loss and start backward part and upgrating weights(SGD) 4. finally print out the accuracy

### **Module API: 2-layer network:**

Barebone PyTorch requires that we track all the parameter tensors by hand. This is fine for small networks with a few tensors, but it would be extremely inconvenient and error-prone to track tens or hundreds of tensors in larger networks.

To use the Module API, follow the steps below:

1. Subclass `nn.Module`. Give your network class an intuitive name like `TwoLayerFC`.
2. In the constructor `__init__()`, define all the layers you need as class attributes. Layer objects like `nn.Linear` and `nn.Conv2d` are themselves `nn.Module` subclasses and contain learnable parameters, so that you don't have to instantiate the raw tensors yourself. `nn.Module` will track these internal parameters for you. Refer to the [doc](http://pytorch.org/docs/master/nn.html) to learn more about the dozens of builtin layers. **Warning**: don't forget to call the `super().__init__()` first!
3. In the `forward()` method, define the _connectivity_ of your network. You should use the attributes defined in `__init__` as function calls that take tensor as input and output the "transformed" tensor. Do _not_ create any new layers with learnable parameters in `forward()`! All of them must be declared upfront in `__init__`.

Example for following architecture:

1. Convolutional layer with `channel_1` 5x5 filters with zero-padding of 2
2. ReLU
3. Convolutional layer with `channel_2` 3x3 filters with zero-padding of 1
4. ReLU
5. Fully-connected layer to `num_classes` classes

and all of the functions are from nn.Module, in the init funcution , we setup the layers information, and there are kaiming_normal and constant initilization function in the nn.Module
```python
 1 class ThreeLayerConvNet(nn.Module):
 2    def __init__(self, in_channel, channel_1, channel_2, num_classes):
 3        super().__init__()
 4        ########################################################################
 5        # TODO: Set up the layers you need for a three-layer ConvNet with the  #
 6        # architecture defined above.                                          #
 7        ########################################################################
 8        self.conv1 = nn.Conv2d(in_channel,channel_1,kernel_size = 5,padding =2,bias=True)
 9        nn.init.kaiming_normal_(self.conv1.weight)
10         nn.init.constant_(self.conv1.bias,0)
11         
12         self.conv2 = nn.Conv2d(channel_1,channel_2,kernel_size = 3,padding = 1,bias = True)
13         nn.init.kaiming_normal_(self.conv1.weight)
14         nn.init.constant_(self.conv1.bias,0)
15         
16         self.fc = nn.Linear(channel_2*32*32,num_classes)
17         nn.init.kaiming_normal_(self.fc.weight)
18         nn.init.constant_(self.fc.bias, 0)
19         
20         #pass
21         ########################################################################
22         #                          END OF YOUR CODE                            # 
23         ########################################################################
24 
25     def forward(self, x):
26         scores = None
27         ########################################################################
28         # TODO: Implement the forward function for a 3-layer ConvNet. you      #
29         # should use the layers you defined in __init__ and specify the        #
30         # connectivity of those layers in forward()                            #
31         ########################################################################
32         relu1 = F.relu(self.conv1(x))
33         relu2 = F.relu(self.conv2(relu1))
34         scores = self.fc(flatten(relu2))
35         #pass
36         ########################################################################
37         #                             END OF YOUR CODE                         #
38         ########################################################################
39         return scores
```
**Module API: Check Accuracy** This version is slightly different from the one in part II. You don't manually pass in the parameters anymore.
```python
 1 def check_accuracy_part34(loader, model):
 2    if loader.dataset.train:
 3        print('Checking accuracy on validation set')
 4    else:
 5        print('Checking accuracy on test set')   
 6    num_correct = 0
 7    num_samples = 0
 8    model.eval()  # set model to evaluation mode
 9    with torch.no_grad():
10         for x, y in loader:
11             x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
12             y = y.to(device=device, dtype=torch.long)
13             scores = model(x)
14             _, preds = scores.max(1)
15             num_correct += (preds == y).sum()
16             num_samples += preds.size(0)
17         acc = float(num_correct) / num_samples
18         print('Got %d / %d correct (%.2f)' % (num_correct, num_samples, 100 * acc))
```
**Module API : Training Loop**

We also use a slightly different training loop. Rather than updating the values of the weights ourselves, we use an Optimizer object from the `torch.optim` package, which abstract the notion of an optimization algorithm and provides implementations of most of the algorithms commonly used to optimize neural networks.
```python
 1 def train_part34(model, optimizer, epochs=1):
 2    """
 3    Train a model on CIFAR-10 using the PyTorch Module API.
 4    
 5    Inputs:
 6    - model: A PyTorch Module giving the model to train.
 7    - optimizer: An Optimizer object we will use to train the model
 8    - epochs: (Optional) A Python integer giving the number of epochs to train for
 9    
10     Returns: Nothing, but prints model accuracies during training.
11     """
12     model = model.to(device=device)  # move the model parameters to CPU/GPU
13     for e in range(epochs):
14         for t, (x, y) in enumerate(loader_train):
15             model.train()  # put model to training mode
16             x = x.to(device=device, dtype=dtype)  # move to device, e.g. GPU
17             y = y.to(device=device, dtype=torch.long)
18 
19             scores = model(x)
20             loss = F.cross_entropy(scores, y)
21 
22             # Zero out all of the gradients for the variables which the optimizer
23             # will update.
24             optimizer.zero_grad()
25 
26             # This is the backwards pass: compute the gradient of the loss with
27             # respect to each  parameter of the model.
28             loss.backward()
29 
30             # Actually update the parameters of the model using the gradients
31             # computed by the backwards pass.
32             optimizer.step()
33 
34             if t % print_every == 0:
35                 print('Iteration %d, loss = %.4f' % (t, loss.item()))
36                 check_accuracy_part34(loader_val, model)
37                 print()
```
Sum up the Module API: 1.initialize learning rate and chennel_1,passing then through model and initilize weights and declare the architecture 2. passing values to optim.SGD, 3. training them

### **Pytorch Sequential API**

Part III introduced the PyTorch Module API, which allows you to define arbitrary learnable layers and their connectivity.

For simple models like a stack of feed forward layers, you still need to go through 3 steps: subclass `nn.Module`, assign layers to class attributes in `__init__`, and call each layer one by one in `forward()`. Is there a more convenient way?

Fortunately, PyTorch provides a container Module called `nn.Sequential`, which merges the above steps into one. It is not as flexible as `nn.Module`, because you cannot specify more complex topology than a feed-forward stack, but it's good enough for many use cases.

Three Layers: Using Sequential API

1. Convolutional layer (with bias) with 32 5x5 filters, with zero-padding of 2
2. ReLU
3. Convolutional layer (with bias) with 16 3x3 filters, with zero-padding of 1
4. ReLU
5. Fully-connected layer (with bias) to compute scores for 10 classes

```python
 1 channel_1 = 32
 2 channel_2 = 16
 3 learning_rate = 1e-2
 4 
 5 model = None
 6 optimizer = None
 7 
 8 ################################################################################
 9 # TODO: Rewrite the 2-layer ConvNet with bias from Part III with the           #
10 # Sequential API.                                                              #
11 ################################################################################
12 #pass
13 model = nn.Sequential(
14     nn.Conv2d(3,channel_1,kernel_size=5,padding=2),
15     nn.ReLU(),
16     nn.Conv2d(channel_1,channel_2,kernel_size=3,padding=1),
17     nn.ReLU(),
18     Flatten(),
19     nn.Linear(channel_2*32*32,10)
20 )
21 
22 optimizer = optim.SGD(model.parameters(),lr=learning_rate,
23                      momentum=0.9,nesterov=True)
24 ################################################################################
25 #                                 END OF YOUR CODE 
26 ################################################################################
27 
28 train_part34(model, optimizer)
```
Using training_part34 and Sequential API, it's super easy to set to the layers and transported the data to be trained: Finally the accuracy result will be:

```
 1 Iteration 0, loss = 2.2939
 2 Checking accuracy on validation set
 3 Got 140 / 1000 correct (14.00)
 4 
 5 Iteration 100, loss = 1.4576
 6 Checking accuracy on validation set
 7 Got 471 / 1000 correct (47.10)
 8 
 9 Iteration 200, loss = 1.3825
10 Checking accuracy on validation set
11 Got 466 / 1000 correct (46.60)
12 
13 Iteration 300, loss = 1.5948
14 Checking accuracy on validation set
15 Got 524 / 1000 correct (52.40)
16 
17 Iteration 400, loss = 1.2816
18 Checking accuracy on validation set
19 Got 513 / 1000 correct (51.30)
20 
21 Iteration 500, loss = 1.3663
22 Checking accuracy on validation set
23 Got 530 / 1000 correct (53.00)
24 
25 Iteration 600, loss = 1.1300
26 Checking accuracy on validation set
27 Got 545 / 1000 correct (54.50)
28 
29 Iteration 700, loss = 1.2276
30 Checking accuracy on validation set
31 Got 542 / 1000 correct (54.20)

* * *
```
### **Tensorflow**

In this Tensorflow introduction, we gonna do the same structure as we do in the introduction of Pytorch

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/07/2018-07-31_135946.jpg" alt="screenshot" width="80%" height="auto">
</p>

All of the packages we imported:
```python
 1 import os
 2 import tensorflow as tf
 3 import numpy as np
 4 import math
 5 import timeit
 6 import matplotlib.pyplot as plt
 7 
 8 %matplotlib inline
```
**Barebone Tensorflow:**

We can see this in action by defining a simple `flatten` function that will reshape image data for use in a fully-connected network.

In TensorFlow, data for convolutional feature maps is typically stored in a Tensor of shape N x H x W x C where:

- N is the number of datapoints (minibatch size)
- H is the height of the feature map
- W is the width of the feature map
- C is the number of channels in the feature map

Notice that this is a little different from pytorch.

**Three_layer_convnet**
```python
 1 def three_layer_convnet(x, params):
 2    """
 3    A three-layer convolutional network with the architecture described above.
 4    
 5    Inputs:
 6    - x: A TensorFlow Tensor of shape (N, H, W, 3) giving a minibatch of images
 7    - params: A list of TensorFlow Tensors giving the weights and biases for the
 8      network; should contain the following:
 9      - conv_w1: TensorFlow Tensor of shape (KH1, KW1, 3, channel_1) giving
10         weights for the first convolutional layer.
11       - conv_b1: TensorFlow Tensor of shape (channel_1,) giving biases for the
12         first convolutional layer.
13       - conv_w2: TensorFlow Tensor of shape (KH2, KW2, channel_1, channel_2)
14         giving weights for the second convolutional layer
15       - conv_b2: TensorFlow Tensor of shape (channel_2,) giving biases for the
16         second convolutional layer.
17       - fc_w: TensorFlow Tensor giving weights for the fully-connected layer.
18         Can you figure out what the shape should be?
19       - fc_b: TensorFlow Tensor giving biases for the fully-connected layer.
20         Can you figure out what the shape should be?
21     """
22     conv_w1, conv_b1, conv_w2, conv_b2, fc_w, fc_b = params
23     scores = None
24     ############################################################################
25     # TODO: Implement the forward pass for the three-layer ConvNet.            #
26     ############################################################################
27     x_padded = tf.pad(x,[[0,0],[2,2],[2,2],[0,0]],'CONSTANT')
28     conv1 = tf.nn.conv2d(x_padded,conv_w1,[1,1,1,1],padding='VALID')+conv_b1
29     relu1 = tf.nn.relu(conv1)
30     x_padded_1 = tf.pad(relu1,[[0,0],[1,1],[1,1],[0,0]],'CONSTANT')
31     conv2 = tf.nn.conv2d(x_padded_1,conv_w2,[1,1,1,1],padding='VALID')+conv_b2
32     relu2 = tf.nn.relu(conv2)
33     fc_x = flatten(relu2)
34     h = tf.matmul(fc_x, fc_w) + fc_b
35     scores = h
36     #pass
37     ############################################################################
38     #                              END OF YOUR CODE                            #
39     ############################################################################
40     return scores
```
All of the functions are from tf.nn . From the above code you may find it very similar to pytorch, but we need to declear the padded form in tf.pad then pass them in tf.nn.conv2d function, and the stride parameter would be like [1,1,1,1]

Training step:

1. Compute the loss
2. Compute the gradient of the loss with respect to all network weights
3. Make a weight update step using (stochastic) gradient descent.

Note that the step of updating the weights is itself an operation in the computational graph - the calls to `tf.assign_sub` in `training_step` return TensorFlow operations that mutate the weights when they are executed. There is an important bit of subtlety here - when we call `sess.run`, TensorFlow does not execute all operations in the computational graph; it only executes the minimal subset of the graph necessary to compute the outputs that we ask TensorFlow to produce. As a result, naively computing the loss would not cause the weight update operations to execute, **since the operations needed to compute the loss do not depend on the output of the weight update**. To fix this problem, we insert a **control dependency** into the graph, adding a duplicate `loss` node to the graph that does depend on the outputs of the weight update operations; this is the object that we actually return from the `training_step` function. As a result, asking TensorFlow to evaluate the value of the `loss`returned from `training_step` will also implicitly update the weights of the network using that minibatch of data.
```python
 1 def training_step(scores, y, params, learning_rate):
 2    """
 3    Set up the part of the computational graph which makes a training step.
 4 
 5    Inputs:
 6    - scores: TensorFlow Tensor of shape (N, C) giving classification scores for
 7      the model.
 8    - y: TensorFlow Tensor of shape (N,) giving ground-truth labels for scores;
 9      y[i] == c means that c is the correct class for scores[i].
10     - params: List of TensorFlow Tensors giving the weights of the model
11     - learning_rate: Python scalar giving the learning rate to use for gradient
12       descent step.
13       
14     Returns:
15     - loss: A TensorFlow Tensor of shape () (scalar) giving the loss for this
16       batch of data; evaluating the loss also performs a gradient descent step
17       on params (see above).
18     """
19     # First compute the loss; the first line gives losses for each example in
20     # the minibatch, and the second averages the losses acros the batch
21     losses = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=scores)
22     loss = tf.reduce_mean(losses)
23 
24     # Compute the gradient of the loss with respect to each parameter of the the
25     # network. This is a very magical function call: TensorFlow internally
26     # traverses the computational graph starting at loss backward to each element
27     # of params, and uses backpropagation to figure out how to compute gradients;
28     # it then adds new operations to the computational graph which compute the
29     # requested gradients, and returns a list of TensorFlow Tensors that will
30     # contain the requested gradients when evaluated.
31     grad_params = tf.gradients(loss, params)
32     
33     # Make a gradient descent step on all of the model parameters.
34     new_weights = []   
35     for w, grad_w in zip(params, grad_params):
36         new_w = tf.assign_sub(w, learning_rate * grad_w)
37         new_weights.append(new_w)
38 
39     # Insert a control dependency so that evaluting the loss causes a weight
40     # update to happen; see the discussion above.
41     with tf.control_dependencies(new_weights):
42         return tf.identity(loss)
```
you need to be familiar with the function tf.nn.sparse_softmax_cross_entropy_with_logits **Tensorflow : Trainning Loop**
```python
 1 def train_part2(model_fn, init_fn, learning_rate):
 2    """
 3    Train a model on CIFAR-10.
 4    
 5    Inputs:
 6    - model_fn: A Python function that performs the forward pass of the model
 7      using TensorFlow; it should have the following signature:
 8      scores = model_fn(x, params) where x is a TensorFlow Tensor giving a
 9      minibatch of image data, params is a list of TensorFlow Tensors holding
10       the model weights, and scores is a TensorFlow Tensor of shape (N, C)
11       giving scores for all elements of x.
12     - init_fn: A Python function that initializes the parameters of the model.
13       It should have the signature params = init_fn() where params is a list
14       of TensorFlow Tensors holding the (randomly initialized) weights of the
15       model.
16     - learning_rate: Python float giving the learning rate to use for SGD.
17     """
18     # First clear the default graph
19     tf.reset_default_graph()
20     is_training = tf.placeholder(tf.bool, name='is_training')
21     # Set up the computational graph for performing forward and backward passes,
22     # and weight updates.
23     with tf.device(device):
24         # Set up placeholders for the data and labels
25         x = tf.placeholder(tf.float32, [None, 32, 32, 3])
26         y = tf.placeholder(tf.int32, [None])
27         params = init_fn()           # Initialize the model parameters
28         scores = model_fn(x, params) # Forward pass of the model
29         loss = training_step(scores, y, params, learning_rate)
30 
31     # Now we actually run the graph many times using the training data
32     with tf.Session() as sess:
33         # Initialize variables that will live in the graph
34         sess.run(tf.global_variables_initializer())
35         for t, (x_np, y_np) in enumerate(train_dset):
36             # Run the graph on a batch of training data; recall that asking
37             # TensorFlow to evaluate loss will cause an SGD step to happen.
38             feed_dict = {x: x_np, y: y_np}
39             loss_np = sess.run(loss, feed_dict=feed_dict)
40             
41             # Periodically print the loss and check accuracy on the val set
42             if t % print_every == 0:
43                 print('Iteration %d, loss = %.4f' % (t, loss_np))
44                 check_accuracy(sess, val_dset, x, scores, is_training)
```
**Barebones TensorFlow: Check Accuracy**
```python
 1 def check_accuracy(sess, dset, x, scores, is_training=None):
 2    """
 3    Check accuracy on a classification model.
 4    
 5    Inputs:
 6    - sess: A TensorFlow Session that will be used to run the graph
 7    - dset: A Dataset object on which to check accuracy
 8    - x: A TensorFlow placeholder Tensor where input images should be fed
 9    - scores: A TensorFlow Tensor representing the scores output from the
10       model; this is the Tensor we will ask TensorFlow to evaluate.
11       
12     Returns: Nothing, but prints the accuracy of the model
13     """
14     num_correct, num_samples = 0, 0
15     for x_batch, y_batch in dset:
16         feed_dict = {x: x_batch, is_training: 0}
17         scores_np = sess.run(scores, feed_dict=feed_dict)
18         y_pred = scores_np.argmax(axis=1)
19         num_samples += x_batch.shape[0]
20         num_correct += (y_pred == y_batch).sum()
21     acc = float(num_correct) / num_samples
22     print('Got %d / %d correct (%.2f%%)' % (num_correct, num_samples, 100 * acc))
```
I will omit the initilization part because it's similar to the pytorch part. To sum up, the process of training the passing values are the same as they do in the pytorch, but in the tensorflow we need to use placeholder and sess.run to make it work,and tbh, tensorflow it's a little bit difficult to get started at the very begining comparing to pytorch.

### Keras Model API

Implementing a neural network using the low-level TensorFlow API is a good way to understand how TensorFlow works, but it's a little inconvenient - we had to manually keep track of all Tensors holding learnable parameters, and we had to use a control dependency to implement the gradient descent update step. This was fine for a small network, but could quickly become unweildy for a large complex model.

Fortunately TensorFlow provides higher-level packages such as `tf.keras` and `tf.layers` which make it easy to build models out of modular, object-oriented layers; `tf.train` allows you to easily train these models using a variety of different optimization algorithms.

### Keras Model API: Three-Layer ConvNet
```python
1. Convolutional layer with 5 x 5 kernels, with zero-padding of 2
2. ReLU nonlinearity
3. Convolutional layer with 3 x 3 kernels, with zero-padding of 1
4. ReLU nonlinearity
5. Fully-connected layer to give class scores

 1 class ThreeLayerConvNet(tf.keras.Model):
 2    def __init__(self, channel_1, channel_2, num_classes):
 3        super().__init__()
 4        ########################################################################
 5        # TODO: Implement the __init__ method for a three-layer ConvNet. You   #
 6        # should instantiate layer objects to be used in the forward pass.     #
 7        ########################################################################
 8        initializer = tf.variance_scaling_initializer(scale=2.0)
 9        self.conv1 = tf.layers.Conv2D(channel_1,[5,5],strides=1, 
10                                 padding="valid", activation=tf.nn.relu,
11                                 kernel_initializer = initializer)
12         self.conv2 = tf.layers.Conv2D(channel_2,[3,3],strides=1, 
13                                 padding="valid", activation=tf.nn.relu,
14                                 kernel_initializer = initializer)
15         self.fc1 = tf.layers.Dense(num_classes,kernel_initializer=initializer)
16         #pass
17         ########################################################################
18         #                           END OF YOUR CODE                           #
19         ########################################################################
```
Training Loop:

We need to implement a slightly different training loop when using the `tf.keras.Model` API. Instead of computing gradients and updating the weights of the model manually, we use an `Optimizer` object from the `tf.train` package which takes care of these details for us. You can read more about
```python
 1 def train_part34(model_init_fn, optimizer_init_fn, num_epochs=1):
 2    """
 3    Simple training loop for use with models defined using tf.keras. It trains
 4    a model for one epoch on the CIFAR-10 training set and periodically checks
 5    accuracy on the CIFAR-10 validation set.
 6    
 7    Inputs:
 8    - model_init_fn: A function that takes no parameters; when called it
 9      constructs the model we want to train: model = model_init_fn()
10     - optimizer_init_fn: A function which takes no parameters; when called it
11       constructs the Optimizer object we will use to optimize the model:
12       optimizer = optimizer_init_fn()
13     - num_epochs: The number of epochs to train for
14     
15     Returns: Nothing, but prints progress during trainingn
16     """
17     tf.reset_default_graph()    
18     with tf.device(device):
19         # Construct the computational graph we will use to train the model. We
20         # use the model_init_fn to construct the model, declare placeholders for
21         # the data and labels
22         x = tf.placeholder(tf.float32, [None, 32, 32, 3])
23         y = tf.placeholder(tf.int32, [None])
24         
25         # We need a place holder to explicitly specify if the model is in the training
26         # phase or not. This is because a number of layers behaves differently in
27         # training and in testing, e.g., dropout and batch normalization.
28         # We pass this variable to the computation graph through feed_dict as shown below.
29         is_training = tf.placeholder(tf.bool, name='is_training')
30         
31         # Use the model function to build the forward pass.
32         scores = model_init_fn(x, is_training)
33 
34         # Compute the loss like we did in Part II
35         loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=scores)
36         loss = tf.reduce_mean(loss)
37 
38         # Use the optimizer_fn to construct an Optimizer, then use the optimizer
39         # to set up the training step. Asking TensorFlow to evaluate the
40         # train_op returned by optimizer.minimize(loss) will cause us to make a
41         # single update step using the current minibatch of data.
42         
43         # Note that we use tf.control_dependencies to force the model to run
44         # the tf.GraphKeys.UPDATE_OPS at each training step. tf.GraphKeys.UPDATE_OPS
45         # holds the operators that update the states of the network.
46         # For example, the tf.layers.batch_normalization function adds the running mean
47         # and variance update operators to tf.GraphKeys.UPDATE_OPS.
48         optimizer = optimizer_init_fn()
49         update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
50         with tf.control_dependencies(update_ops):
51             train_op = optimizer.minimize(loss)
52 
53     # Now we can run the computational graph many times to train the model.
54     # When we call sess.run we ask it to evaluate train_op, which causes the
55     # model to update.
56     with tf.Session() as sess:
57         sess.run(tf.global_variables_initializer())
58         t = 0
59         for epoch in range(num_epochs):
60             print('Starting epoch %d' % epoch)
61             for x_np, y_np in train_dset:
62                 feed_dict = {x: x_np, y: y_np, is_training:1}
63                 loss_np, _ = sess.run([loss, train_op], feed_dict=feed_dict)
64                 if t % print_every == 0:
65                     print('Iteration %d, loss = %.4f' % (t, loss_np))
66                     check_accuracy(sess, val_dset, x, scores, is_training=is_training)
67                     print()
68                 t += 1
```
Finally :

### Keras Sequential API

Here you should use `tf.keras.Sequential` to reimplement the same three-layer ConvNet architecture used in Part II and Part III. As a reminder, your model should have the following architecture:

1. Convolutional layer with 16 5x5 kernels, using zero padding of 2
2. ReLU nonlinearity
3. Convolutional layer with 32 3x3 kernels, using zero padding of 1
4. ReLU nonlinearity
5. Fully-connected layer giving class scores

You should initialize the weights of the model using a `tf.variance_scaling_initializer` as above.
```python
 1 def model_init_fn(inputs, is_training):
 2    model = None
 3    ############################################################################
 4    # TODO: Construct a three-layer ConvNet using tf.keras.Sequential.         #
 5    ############################################################################
 6    input_shape = (32, 32, 3)
 7    channel_1, channel_2, num_classes = 32, 16, 10
 8    initializer = tf.variance_scaling_initializer(scale=2.0)
 9    layers = [
10         # 'Same' padding acts similar to zero padding of 2 for this input
11         tf.layers.Conv2D(channel_1,[5,5],strides=1, 
12                                 padding="same", activation=tf.nn.relu,
13                                 kernel_initializer = initializer,input_shape=(32, 32,3)),
14         tf.layers.Conv2D(channel_2,[3,3],strides=1, 
15                                 padding="same", activation=tf.nn.relu,
16                                 kernel_initializer = initializer),
17         tf.layers.Flatten(input_shape=input_shape),
18         tf.layers.Dense(num_classes, kernel_initializer=initializer),
19     ]
20     model = tf.keras.Sequential(layers)
21     #pass
22     ############################################################################
23     #                            END OF YOUR CODE                              #
24     ############################################################################
25     return model(inputs)
26 
27 learning_rate = 5e-4
28 def optimizer_init_fn():
29     optimizer = None
30     ############################################################################
31     # TODO: Complete the implementation of model_fn.                           #
32     ############################################################################
33     optimizer = tf.train.MomentumOptimizer(learning_rate, 0.9, use_nesterov=True)
34 
35     ############################################################################
36     #                           END OF YOUR CODE                               #
37     ############################################################################
38     return optimizer
39 
40 train_part34(model_init_fn, optimizer_init_fn)
```
 

* * *

To be honest, I personally prefer pytorch because it is more succinct and simple in syntax. In contrast, tensorflow is very grammatically complex and needs to be written repeatedly to write such as sess.run and placeholder to run the whole code. **In tensorflow's Sequential API, dropout and batchnorm are not available,** but those API is very simple and available in pytorch.

Objectively speaking, the advantage of tensorflow is that TF has the perfect community and documentation which are supported by GOOGLE, which is a great benefit for industrial developers. So in the future, although tensorflow has some shortcomings, I will still use it anyway.

(The following content and introduction are based on the assignment of CS231n)

liangliangzheng

July,31,2018
