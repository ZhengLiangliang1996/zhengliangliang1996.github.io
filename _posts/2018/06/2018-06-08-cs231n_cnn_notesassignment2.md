---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "CS231N_CNN_Notes&amp;Assignment2"
date: "2018-06-08"
categories: 
  - "dl-ml-python"
tags: 
  - "cs231n"
---

The corresponding contents and materials of this blog are from Stanford Online Course CS231N and other Internet Resources.

* * *

**Training Neural Networks:<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_140234.png" alt="screenshot" width="80%" height="auto">
</p>**

This is a fundamental one layer network, and the following one is 2-layer Neural Network

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_140557.png" alt="screenshot" width="80%" height="auto">
</p>

Convolutional Neural Networks, I think the best way to imagine CNN is that: say the task is to let computer know if a picture with a mouse(The input) is mouse(mouse)

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_140933.png" alt="screenshot" width="80%" height="auto">
</p>

In the computer's vision, we need to use a small rectangle to scan the whole picture like this:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_141045.png" alt="screenshot" width="80%" height="auto">
</p>

Knowing that a picture is composed with hundreds of thousands of pixels, in every step where the small rectangle scanned, it can get the original pixel matrix, then we put the original matrix to a filter( which is get the pixel representation), after filtering, we can get a filtering matrix,then we apply the multiplication and summation operation:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_141523.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_141721.png" alt="screenshot" width="80%" height="auto">
</p>

After scanning, we can get a activation map, if we have 6 filters, then the image will be transferred into a "new image" of size 28 * 28 * 6

and how do we know the size of the new image?  It depends on the size of the filters and the size of the original images, you can find some of the calculation in cs231n slides(Lecture 05)

* * *

**Training Neural Networks:**

- Activation Function

Neural Science is a very complex field for humans nowadays , so it's still a mystery for neural scientist to know what's the detail functions and mechanisms of when one neural activates another, so in this maze, AI scientists use Activation function to simulate it.

some activation functions and there advantages and disadvantages:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_142942.png" alt="screenshot" width="80%" height="auto">
</p>

Problems with Sigmod : 1 . Saturated neurons "kill" the gradients 2 . Sigmoid outputs are not zero-centered(if the input to a neuron is always positive, then the hypothetical optimal w vector will be zig-zag path) 3 . exp() is a bit compute expensive

Problems with tanh(x) 1 . Saturated neurons "kill" the gradients But zero centered(nice!)

well, in ReLU, things are better :

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_144248.png" alt="screenshot" width="80%" height="auto">
</p>

* * *

**Preprocess the data**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_144430.png" alt="screenshot" width="80%" height="auto">
</p>

**Weight Initialization**

What would happen if the weight is constant, then all activations would become zero!

then we should use a resonable initialization, which is Xavier initialization:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_145004.png" alt="screenshot" width="80%" height="auto">
</p>

Remember: Nice distribution of activations at all layers will make the learning proceeds nicely.

* * *

**Batch Normalization**

We want zero-mean unit-variance activations

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-07_145709.png" alt="screenshot" width="80%" height="auto">
</p>

You may ask, why batch normalization: The introduction of Batch Normalization is to overcome the difficulty of training big and deep NNs, bn can also prevent the gradient dispersion,in this way the gradient can flow through the network.

**Babysitting the Learning Process:**

1. double check that the loss is reasonable  (Sanity Check)
2. Tricks(Make sure that your model can overfit very small protion of training data)

**Hyperparameter Optimization:**

Cross-Validation Strategy:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_092710.png" alt="screenshot" width="80%" height="auto">
</p>

It's best to optimize in log space

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_092838.png" alt="screenshot" width="80%" height="auto">
</p>

Monitoring and visualizing the loss curve will make it easy for programmers to debug.

Some normal problems occurs when visualizing the loss curve:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_093255.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_093333.png" alt="screenshot" width="80%" height="auto">
</p>

* * *

**Batch Normalization at Test time:**

We can't use the formal batch normalization for calculating mean and variance in the test time, so instead of using it, we replace it as the following:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094121.png" alt="screenshot" width="80%" height="auto">
</p>

There are different kinds of normalization in training partG:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094301.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094313.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094332.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094341.png" alt="screenshot" width="80%" height="auto">
</p>

**Optimization:**

Previous classes we've learnt the SGD optimization, but there are problems with SGD:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094542.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094636.png" alt="screenshot" width="80%" height="auto">
</p>

So scientist come up with SGD + Momontum Optimization"

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_094751.png" alt="screenshot" width="80%" height="auto">
</p>

Let's get into the most important 2 optimization ways:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_095001.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_095117.png" alt="screenshot" width="80%" height="auto">
</p>

**Regularization : Dropout**

randomly set some neurons to zero Probability of dropping is a hyperparameter, and 0.5 is common

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_095505.png" alt="screenshot" width="80%" height="auto">
</p>

More common is the "Inverted Dropout"

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_095740.png" alt="screenshot" width="80%" height="auto">
</p>

* * *

Transfer Learning:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/06/2018-06-08_120359.png" alt="screenshot" width="80%" height="auto">
</p>

and I will write some introductions about this in later blogs ,stay tuned.

* * *

**Assignment:**

First of all, we need to implement a FullyConnectedNets

Affine Layer in forward pass:
```python
 1 def affine_forward(x, w, b):
 2  """
 3  Computes the forward pass for an affine (fully-connected) layer.
 4 
 5  The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
 6  examples, where each example x[i] has shape (d_1, ..., d_k). We will
 7  reshape each input into a vector of dimension D = d_1 * ... * d_k, and
 8  then transform it to an output vector of dimension M.
 9 
10   Inputs:
11   - x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
12   - w: A numpy array of weights, of shape (D, M)
13   - b: A numpy array of biases, of shape (M,)
14   
15   Returns a tuple of:
16   - out: output, of shape (N, M)
17   - cache: (x, w, b)
18   """
19   out = None
20   #############################################################################
21   # TODO: Implement the affine forward pass. Store the result in out. You     #
22   # will need to reshape the input into rows.                                 #
23   #############################################################################
24   N = x.shape[0]
25   x_rsp = x.reshape(N, -1)
26   out = x_rsp.dot(w) + b
27   #pass
28   #############################################################################
29   #                             END OF YOUR CODE                              #
30   #############################################################################
31   cache = (x, w, b)
32   return out, cache

Turn the x to a vector and multiply w.

 1 def affine_backward(dout, cache):
 2  """
 3  Computes the backward pass for an affine layer.
 4 
 5  Inputs:
 6  - dout: Upstream derivative, of shape (N, M)
 7  - cache: Tuple of:
 8    - x: Input data, of shape (N, d_1, ... d_k)
 9    - w: Weights, of shape (D, M)
10 
11   Returns a tuple of:
12   - dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
13   - dw: Gradient with respect to w, of shape (D, M)
14   - db: Gradient with respect to b, of shape (M,)
15   """
16   x, w, b = cache
17   dx, dw, db = None, None, None
18   #############################################################################
19   # TODO: Implement the affine backward pass.                                 #
20   #############################################################################
21   N = x.shape[0]  
22   x_rsp = x.reshape(N , -1)  
23   dx = dout.dot(w.T)
24   dx = dx.reshape(*x.shape)
25   dw = x_rsp.T.dot(dout)
26   db = np.sum(dout, axis = 0)
27   #pass
28   #############################################################################
29   #                             END OF YOUR CODE                              #
30   #############################################################################
31   return dx, dw, db
```
And the affine_backward function will be the simple gradient process above.

"Sandwich" layers:  There are some common patterns of layers that are frequently used in neural nets. For example, affine layers are frequently followed by a ReLU nonlinearity.
```python
 1 def affine_relu_forward(x, w, b):
 2    """
 3    Convenience layer that perorms an affine transform followed by a ReLU
 4 
 5    Inputs:
 6    - x: Input to the affine layer
 7    - w, b: Weights for the affine layer
 8 
 9    Returns a tuple of:
10     - out: Output from the ReLU
11     - cache: Object to give to the backward pass
12     """
13     a, fc_cache = affine_forward(x, w, b)
14     out, relu_cache = relu_forward(a)
15     cache = (fc_cache, relu_cache)
16     return out, cache
```
and the backward is as easy as the forward:
```python
 1 def affine_relu_backward(dout, cache):
 2    """
 3    Backward pass for the affine-relu convenience layer
 4    """
 5    fc_cache, relu_cache = cache
 6    da = relu_backward(dout, relu_cache)
 7    dx, dw, db = affine_backward(da, fc_cache)
 8    return dx, dw, db
```
And the loss Layers (Loss Function)to compute the  loss, i will omit the detailed algorithm here but you can find more information and algorithms in this [link](https://blog.csdn.net/u012767526/article/details/51396196)

**Two- Layer network: A two-layer fully-connected neural network with ReLU nonlinearity and softmax loss that uses a modular layer design. We assume an input dimension of D, a hidden dimension of H, and perform classification over C classes.**

and the architecture should be affine - relu - affine - softmax
```python
 1        ############################################################################
 2        # TODO: Initialize the weights and biases of the two-layer net. Weights    #
 3        # should be initialized from a Gaussian centered at 0.0 with               #
 4        # standard deviation equal to weight_scale, and biases should be           #
 5        # initialized to zero. All weights and biases should be stored in the      #
 6        # dictionary self.params, with first layer weights                         #
 7        # and biases using the keys 'W1' and 'b1' and second layer                 #
 8        # weights and biases using the keys 'W2' and 'b2'.                         #
 9        ############################################################################
10         # initialization 
11         self.params['W1'] = weight_scale * np.random.randn(input_dim,hidden_dim)
12         self.params['b1'] = np.zeros(hidden_dim)
13         self.params['W2'] = weight_scale * np.random.randn(hidden_dim,num_classes)
14         self.params['b2'] = np.zeros(num_classes)
```
Then is the loss function,we use the softmax,after forward passing , we use softmax to calculate the loss and backward passing to count the grad. and in the following code, notice that if y is none, then it is in the test, otherwise it is in the training stage.
```python
 1   def loss(self, X, y=None):
 2        """
 3        Compute loss and gradient for a minibatch of data.
 4 
 5        Inputs:
 6        - X: Array of input data of shape (N, d_1, ..., d_k)
 7        - y: Array of labels, of shape (N,). y[i] gives the label for X[i].
 8 
 9        Returns:
10         If y is None, then run a test-time forward pass of the model and return:
11         - scores: Array of shape (N, C) giving classification scores, where
12           scores[i, c] is the classification score for X[i] and class c.
13 
14         If y is not None, then run a training-time forward and backward pass and
15         return a tuple of:
16         - loss: Scalar value giving the loss
17         - grads: Dictionary with the same keys as self.params, mapping parameter
18           names to gradients of the loss with respect to those parameters.
19         """
20         scores = None
21         ############################################################################
22         # TODO: Implement the forward pass for the two-layer net, computing the    #
23         # class scores for X and storing them in the scores variable.              #
24         ############################################################################
25         ar1_out, ar1_cache = affine_relu_forward(X,self.params['W1'],self.params['b1'])
26         a2_out, a2_cache= affine_forward(ar1_out,self.params['W2'],self.params['b2'])
27         scores = a2_out
28         #pass
29         ############################################################################
30         #                             END OF YOUR CODE                             #
31         ############################################################################
32 
33         # If y is None then we are in test mode so just return scores
34         if y is None:
35             return scores
36 
37         loss, grads = 0, {}
38         ############################################################################
39         # TODO: Implement the backward pass for the two-layer net. Store the loss  #
40         # in the loss variable and gradients in the grads dictionary. Compute data #
41         # loss using softmax, and make sure that grads[k] holds the gradients for  #
42         # self.params[k]. Don't forget to add L2 regularization!                   #
43         #                                                                          #
44         # NOTE: To ensure that your implementation matches ours and you pass the   #
45         # automated tests, make sure that your L2 regularization includes a factor #
46         # of 0.5 to simplify the expression for the gradient.                      #
47         ############################################################################
48         loss,dscores = softmax_loss(scores,y)
49         loss = loss + 0.5 * self.reg * np.sum(self.params['W1'] * self.params['W1']) + 0.5 * self.reg * np.sum(self.params['W2'] * self.params['W2'])
50         dx2, dw2, db2 = affine_backward(dscores, a2_cache)
51         grads['W2'] = dw2 + self.reg * self.params['W2']
52         grads['b2'] = db2
53         #dx2_relu = relu_backward(dx2, r1_cache)
54         #dx1, dw1, db1 = affine_backward(dx2_relu, a1_cache)
55         dx1 , dw1, db1 = affine_relu_backward(dx2, ar1_cache)
56         grads['W1'] = dw1 + self.reg * self.params['W1']
57         grads['b1'] = db1
58         #pass
59         ############################################################################
60         #                             END OF YOUR CODE                             #
61         ############################################################################
62 
63         return loss, grads
```
Solver part: pre-define all the parameters such as update_rule or optimization configuration (Learning rate),lr decay ,number of epochs and so on, and usually the usage of the solve will be like:
```python
 1 Example usage might look something like this:
 2 
 3    data = {
 4      'X_train': # training data
 5      'y_train': # training labels
 6      'X_val': # validation data
 7      'y_val': # validation labels
 8    }
 9    model = MyAwesomeModel(hidden_size=100, reg=10)
10     solver = Solver(model, data,
11                     update_rule='sgd',
12                     optim_config={
13                       'learning_rate': 1e-3,
14                     },
15                     lr_decay=0.95,
16                     num_epochs=10, batch_size=100,
17                     print_every=100)
18     solver.train()

-----------------------------------------------------------------------------------------------------------------------------
```
**Multilayer Network: Inplement a fully-connected network with an arbitrary number of hidden layers**

And the architecture will be :

{affine - [batch/layer norm] - relu - [dropout]} x (L - 1) - affine - softmax

Initialize a new FullyConnectedNet.
```python
 1 class FullyConnectedNet(object):
 2    """
 3    A fully-connected neural network with an arbitrary number of hidden layers,
 4    ReLU nonlinearities, and a softmax loss function. This will also implement
 5    dropout and batch/layer normalization as options. For a network with L layers,
 6    the architecture will be
 7 
 8    {affine - [batch/layer norm] - relu - [dropout]} x (L - 1) - affine - softmax
 9 
10     where batch/layer normalization and dropout are optional, and the {...} block is
11     repeated L - 1 times.
12 
13     Similar to the TwoLayerNet above, learnable parameters are stored in the
14     self.params dictionary and will be learned using the Solver class.
15     """
16 
17     def __init__(self, hidden_dims, input_dim=3*32*32, num_classes=10,
18                  dropout=1, normalization=None, reg=0.0,
19                  weight_scale=1e-2, dtype=np.float32, seed=None):
20         """
21         Initialize a new FullyConnectedNet.
22 
23         Inputs:
24         - hidden_dims: A list of integers giving the size of each hidden layer.
25         - input_dim: An integer giving the size of the input.
26         - num_classes: An integer giving the number of classes to classify.
27         - dropout: Scalar between 0 and 1 giving dropout strength. If dropout=1 then
28           the network should not use dropout at all.
29         - normalization: What type of normalization the network should use. Valid values
30           are "batchnorm", "layernorm", or None for no normalization (the default).
31         - reg: Scalar giving L2 regularization strength.
32         - weight_scale: Scalar giving the standard deviation for random
33           initialization of the weights.
34         - dtype: A numpy datatype object; all computations will be performed using
35           this datatype. float32 is faster but less accurate, so you should use
36           float64 for numeric gradient checking.
37         - seed: If not None, then pass this random seed to the dropout layers. This
38           will make the dropout layers deteriminstic so we can gradient check the
39           model.
40         """
41         self.normalization = normalization
42         self.use_dropout = dropout != 1
43         self.reg = reg
44         self.num_layers = 1 + len(hidden_dims)
45         self.dtype = dtype
46         self.params = {}
47 
48         ############################################################################
49         # TODO: Initialize the parameters of the network, storing all values in    #
50         # the self.params dictionary. Store weights and biases for the first layer #
51         # in W1 and b1; for the second layer use W2 and b2, etc. Weights should be #
52         # initialized from a normal distribution centered at 0 with standard       #
53         # deviation equal to weight_scale. Biases should be initialized to zero.   #
54         #                                                                          #
55         # When using batch normalization, store scale and shift parameters for the #
56         # first layer in gamma1 and beta1; for the second layer use gamma2 and     #
57         # beta2, etc. Scale parameters should be initialized to ones and shift     #
58         # parameters should be initialized to zeros.                               #
59         ############################################################################
60         # initialization
61         layer_input_dim = input_dim
62         for i,hd in enumerate(hidden_dims):
63             self.params['W%d'%(i+1)] = weight_scale * np.random.randn(layer_input_dim,hd)
64             self.params['b%d'%(i+1)] = weight_scale * np.zeros(hd)
65             #batch normalization
66             if self.normalization:
67                 self.params['gamma%d'%(i+1)] = np.ones(hd)
68                 self.params['beta%d'%(i+1)] = np.zeros(hd)
69             layer_input_dim = hd
70         #final output layer
71         self.params['W%d'%(self.num_layers)] = weight_scale * np.random.randn(layer_input_dim,num_classes)
72         self.params['b%d'%(self.num_layers)] = weight_scale * np.zeros(num_classes)        
73         #pass
74         ############################################################################
75         #                             END OF YOUR CODE                             #
76         ############################################################################
77 
78         # When using dropout we need to pass a dropout_param dictionary to each
79         # dropout layer so that the layer knows the dropout probability and the mode
80         # (train / test). You can pass the same dropout_param to each dropout layer.
81         self.dropout_param = {}
82         if self.use_dropout:
83             self.dropout_param = {'mode': 'train', 'p': dropout}
84             if seed is not None:
85                 self.dropout_param['seed'] = seed
86 
87         # With batch normalization we need to keep track of running means and
88         # variances, so we need to pass a special bn_param object to each batch
89         # normalization layer. You should pass self.bn_params[0] to the forward pass
90         # of the first batch normalization layer, self.bn_params[1] to the forward
91         # pass of the second batch normalization layer, etc.
92         self.bn_params = []
93         if self.normalization=='batchnorm':
94             self.bn_params = [{'mode': 'train'} for i in range(self.num_layers - 1)]
95         if self.normalization=='layernorm':
96             self.bn_params = [{} for i in range(self.num_layers - 1)]
97 
98         # Cast all parameters to the correct datatype
99         for k, v in self.params.items():
100             self.params[k] = v.astype(dtype)
```
Same as the two-layers net, the loss function :
```python
 1    def loss(self, X, y=None):
 2        """
 3        Compute loss and gradient for the fully-connected net.
 4 
 5        Input / output: Same as TwoLayerNet above.
 6        """
 7        X = X.astype(self.dtype)
 8        mode = 'test' if y is None else 'train'
 9 
10         # Set train/test mode for batchnorm params and dropout param since they
11         # behave differently during training and testing.
12         if self.use_dropout:
13             self.dropout_param['mode'] = mode
14         if self.normalization=='batchnorm':
15             for bn_param in self.bn_params:
16                 bn_param['mode'] = mode
17         scores = None
18         ############################################################################
19         # TODO: Implement the forward pass for the fully-connected net, computing  #
20         # the class scores for X and storing them in the scores variable.          #
21         #                                                                          #
22         # When using dropout, you'll need to pass self.dropout_param to each       #
23         # dropout forward pass.                                                     #
24         #                                                                          #
25         # When using batch normalization, you'll need to pass self.bn_params[0] to #
26         # the forward pass for the first batch normalization layer, pass           #
27         # self.bn_params[1] to the forward pass for the second batch normalization #
28         # layer, etc.                                                           #
29         ############################################################################
30         layer_input = X
31         ar_cache = {} # Affine ReLU Cache
32         dp_cache = {} # DropOut Cache
33         
34         for lay in range(self.num_layers-1):
35             #if using the batch normalization
36             if self.normalization:
37                 layer_input, ar_cache[lay] = affine_bn_relu_forward(layer_input,
38                                   self.params['W%d'%(lay+1)],self.params['b%d'%(lay+1)],
39                                   self.params['gamma%d'%(lay+1)],self.params['beta%d'%(lay+1)],
40                                   self.bn_params[lay])
41             else:
42                 layer_input, ar_cache[lay] = affine_relu_forward(layer_input,self.params['W%d'%(lay+1)],self.params['b%d'%(lay+1)])
43             if self.use_dropout:
44                 lay_input,dp_cache[lay] = dropout_forward(layer_input,self.dropout_param)
45                 
46         #The Last layer 
47         ar_out,ar_cache[self.num_layers] = affine_forward(layer_input,self.params['W%d'%(self.num_layers)],self.params['b%d'%(self.num_layers)])
48         scores = ar_out
49         #pass
50         ############################################################################
51         #                             END OF YOUR CODE                             #
52         ############################################################################
53 
54         # If test mode return early
55         if mode == 'test':
56             return scores
57 
58         loss, grads = 0.0, {}
59         ############################################################################
60         # TODO: Implement the backward pass for the fully-connected net. Store the #
61         # loss in the loss variable and gradients in the grads dictionary. Compute #
62         # data loss using softmax, and make sure that grads[k] holds the gradients #
63         # for self.params[k]. Don't forget to add L2 regularization!               #
64         #                                                                          #
65         # When using batch/layer normalization, you don't need to regularize the scale   #
66         # and shift parameters.                                                    #
67         #                                                                          #
68         # NOTE: To ensure that your implementation matches ours and you pass the   #
69         # automated tests, make sure that your L2 regularization includes a factor #
70         # of 0.5 to simplify the expression for the gradient.                      #
71         ############################################################################
72         #first calculate the loss using softmax_loss
73         loss,dscores = softmax_loss(scores,y)
74         dhout = dscores # upstream derivatives
75         loss = loss + 0.5 * self.reg * np.sum(self.params['W%d'%(self.num_layers)] * self.params['W%d'%(self.num_layers)])
76         # From the last layer to the input layer
77         dx,dw,db = affine_backward(dhout,ar_cache[self.num_layers])
78         grads['W%d'%(self.num_layers)] = dw + self.reg * self.params['W%d'%(self.num_layers)]
79         grads['b%d'%(self.num_layers)] = db
80         dhout = dx #upstream gradient
81         for idx in range(self.num_layers - 1):
82             lay = self.num_layers - 1 - idx - 1
83             loss = loss + 0.5 *  self.reg * np.sum(self.params['W%d'%(lay+1)] * self.params['W%d'%(lay+1)])
84             if self.use_dropout:
85                 dhout = dropout_backward(dhout,dp_cache[lay])
86             if self.normalization:
87                 dx, dw, db, dgamma, dbeta = affine_bn_relu_backward(dhout,ar_cache[lay])
88             else:
89                 dx, dw, db = affine_relu_backward(dhout,ar_cache[lay])
90             grads['W%d'%(lay+1)] = dw + self.reg * self.params['W%d'%(lay+1)]
91             grads['b%d'%(lay+1)] = db
92             if self.normalization:
93                grads['gamma%d'%(lay+1)] = dgamma
94                grads['beta%d'%(lay+1)] = dbeta
95             dhout = dx
96         #pass
97         ############################################################################
98         #                             END OF YOUR CODE                             #
99         ############################################################################
100 
101         return loss, grads
```