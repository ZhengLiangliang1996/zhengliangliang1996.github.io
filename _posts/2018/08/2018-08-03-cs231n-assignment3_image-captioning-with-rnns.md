---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "CS231n Assignment3_Image Captioning with RNNs"
date: "2018-08-03"
categories: 
  - "dl-ml-python"
---

Yesterday I finished a vanilla recurrent neural networks and used them to train a model that could generate novel captions for images. It's really excited that as the the domain of NLP, word embedding can be combining with Computer Vision CNN for image captioning,which is sort of like Lego construction.(All the images drawn in draft are from [link](https://www.cnblogs.com/hellcat/p/7191967.html) )

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_112358.jpg" alt="screenshot" width="80%" height="auto">
</p>

The whole process will be pretty much as following:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_112636.jpg" alt="screenshot" width="80%" height="auto">
</p>

* * *

Vanilla RNN single step forward:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_100635.jpg" alt="screenshot" width="80%" height="auto">
</p>
```python
 1 def rnn_step_forward(x, prev_h, Wx, Wh, b):
 2  """
 3  Run the forward pass for a single timestep of a vanilla RNN that uses a tanh
 4  activation function.
 5 
 6  The input data has dimension D, the hidden state has dimension H, and we use
 7  a minibatch size of N.
 8 
 9  Inputs:
10   - x: Input data for this timestep, of shape (N, D).
11   - prev_h: Hidden state from previous timestep, of shape (N, H)
12   - Wx: Weight matrix for input-to-hidden connections, of shape (D, H)
13   - Wh: Weight matrix for hidden-to-hidden connections, of shape (H, H)
14   - b: Biases of shape (H,)
15  
16   Returns a tuple of:
17   - next_h: Next hidden state, of shape (N, H)
18   - cache: Tuple of values needed for the backward pass.
19   """
20   next_h, cache = None, None
21   ##############################################################################
22   # TODO: Implement a single forward step for the vanilla RNN. Store the next  #
23   # hidden state and any values you need for the backward pass in the next_h   #
24   # and cache variables respectively.                                          #
25   ##############################################################################
26   next_h = np.tanh(prev_h.dot(Wh) + x.dot(Wx) + b)
27   cache = (x,Wx,Wh,prev_h,next_h)
28   #pass
29     ##############################################################################
30     #                               END OF YOUR CODE                             #
31     ##############################################################################
32   return next_h, cache
```

Notice these two parameters: - Wx: Weight matrix for input-to-hidden connections, of shape (D, H) - Wh: Weight matrix for hidden-to-hidden connections, of shape (H, H)

RNN one step backward, according to their size and pay attention to the transpose.<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_101459.jpg" alt="screenshot" width="80%" height="auto">
</p>
```python
 1 def rnn_step_backward(dnext_h, cache):
 2    """
 3    Backward pass for a single timestep of a vanilla RNN.
 4    Inputs:
 5    - dnext_h: Gradient of loss with respect to next hidden state, of shape (N, H)
 6    - cache: Cache object from the forward pass
 7    Returns a tuple of:
 8    - dx: Gradients of input data, of shape (N, D)
 9    - dprev_h: Gradients of previous hidden state, of shape (N, H)
10     - dWx: Gradients of input-to-hidden weights, of shape (D, H)
11     - dWh: Gradients of hidden-to-hidden weights, of shape (H, H)
12     - db: Gradients of bias vector, of shape (H,)
13     """
14     dx, dprev_h, dWx, dWh, db = None, None, None, None, None
15     ##############################################################################
16     # TODO: Implement the backward pass for a single step of a vanilla RNN.      #
17     #                                                                            #
18     # HINT: For the tanh function, you can compute the local derivative in terms #
19     # of the output value from tanh.                                             #
20     ##############################################################################
21     x, Wx, Wh, prev_h, next_h = cache
22     d_tanh = 1 - next_h**2
23     dx = (dnext_h*dtanh).dot(Wx.T)
24     dWx = x.T.dot(dnext_h*dtanh)
25     dprev_h = (dnext_h*dtanh).dot(Wh.T)
26     dWh = prev_h.T.dot(dnext_h*dtanh)
27     db = np.sum(dnext_h*dtanh,axis=0)# 按列相加
28     #pass
29     ##############################################################################
30     #                               END OF YOUR CODE                             #
31     ##############################################################################
32     return dx, dprev_h, dWx, dWh, db
```
After single step, we need to finish the reccurent loop part

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/1161096-20170716200928128-376197048.jpg" alt="screenshot" width="80%" height="auto">
</p><p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_102633.jpg" alt="screenshot" width="80%" height="auto">
</p>

```python
 1 def rnn_forward(x, h0, Wx, Wh, b):
 2    """
 3    Run a vanilla RNN forward on an entire sequence of data. We assume an input
 4    sequence composed of T vectors, each of dimension D. The RNN uses a hidden
 5    size of H, and we work over a minibatch containing N sequences. After running
 6    the RNN forward, we return the hidden states for all timesteps.
 7    Inputs:
 8    - x: Input data for the entire timeseries, of shape (N, T, D).
 9    - h0: Initial hidden state, of shape (N, H)
10     - Wx: Weight matrix for input-to-hidden connections, of shape (D, H)
11     - Wh: Weight matrix for hidden-to-hidden connections, of shape (H, H)
12     - b: Biases of shape (H,)
13     Returns a tuple of:
14     - h: Hidden states for the entire timeseries, of shape (N, T, H).
15     - cache: Values needed in the backward pass
16     """
17     h, cache = None, None
18     ##############################################################################
19     # TODO: Implement forward pass for a vanilla RNN running on a sequence of    #
20     # input data. You should use the rnn_step_forward function that you defined  #
21     # above. You can use a for loop to help compute the forward pass.            #
22     ##############################################################################
23     # get the size of x 
24 	N,T,D = x.shape
25 	_,H = h0.shape
26 	# initialize the hidden h
27 	h = np.zeors((N,T,H))
28 	cache = []
29 	h_next = h0
30 	for i in range(T):
31 		h[:,i,:],cache_next = rnn_step_forward(x[:,i,:], h_next, Wx, Wh, b)
32 		h_next = h[:,i,:]
33 		cache.append(cache_next)
34     #pass
35     ##############################################################################
36     #                               END OF YOUR CODE                             #
37     ##############################################################################
38     return h, cache
```

For the Backward RNN: <p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_104145.jpg" alt="screenshot" width="80%" height="auto">
</p>

```python
 1 def rnn_backward(dh, cache):
 2    """
 3    Compute the backward pass for a vanilla RNN over an entire sequence of data.
 4    Inputs:
 5- dh: Upstream gradients of all hidden states, of shape (N, T, H). 
 6    
 7NOTE: 'dh' contains the upstream gradients produced by the 
 8    individual loss functions at each timestep, *not* the gradients
 9    being passed between timesteps (which you'll have to compute yourself
10     by calling rnn_step_backward in a loop).
11     Returns a tuple of:
12     - dx: Gradient of inputs, of shape (N, T, D)
13     - dh0: Gradient of initial hidden state, of shape (N, H)
14     - dWx: Gradient of input-to-hidden weights, of shape (D, H)
15     - dWh: Gradient of hidden-to-hidden weights, of shape (H, H)
16     - db: Gradient of biases, of shape (H,)
17     """
18     dx, dh0, dWx, dWh, db = None, None, None, None, None
19     ##############################################################################
20     # TODO: Implement the backward pass for a vanilla RNN running an entire      #
21     # sequence of data. You should use the rnn_step_backward function that you   #
22     # defined above. You can use a for loop to help compute the backward pass.   #
23     ##############################################################################
24     x,Wx,Wh,prev_h,nexth = cache[-1] # start from the final one 
25     x, Wx, Wh, prev_h, next_h = cache[-1] # start from the final one
26     _,D = x.shape
27     N,T,H = dh.shape
28     dx = np.zeros((N,T,D)) # initialization
29     dh0 = np.zeros((N,H))
30     dWx = np.zeros((D,H))
31     dWh = np.zeros((H,H))
32     db = np.zeros(H)
33     dprev_h_ = np.zeros((N,H))
34     for i in range(T-1,-1,-1): # start from the final one
35         dx_, dprev_h_, dWx_, dWh_, db_ = rnn_step_backward(dh[:,i,:] + dprev_h_,cache.pop())
36         dx[:,i,:] = dx_
37         dh0 = dprev_h_
38         dWx += dWx_
39         dWh += dWh_
40         db += db_	
41     #pass
42     ##############################################################################
43     #                               END OF YOUR CODE                             #
44     ##############################################################################
45     return dx, dh0, dWx, dWh, db
```

Word_embedding : FORWARD , In deep learning systems, we commonly represent words using vectors. Each word of the vocabulary will be associated with a vector, and these vectors will be learned jointly with the rest of the system. The whole process will be like this one , from caption_in to the X is the word_embedding process: <p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_110902.jpg" alt="screenshot" width="80%" height="auto">
</p>

```python
 1 def word_embedding_forward(x, W):
 2  """
 3  Forward pass for word embeddings. We operate on minibatches of size N where
 4  each sequence has length T. We assume a vocabulary of V words, assigning each
 5  to a vector of dimension D.
 6   
 7  Inputs:
 8  - x: Integer array of shape (N, T) giving indices of words. Each element idx
 9    of x muxt be in the range 0 <= idx < V.
10   - W: Weight matrix of shape (V, D) giving word vectors for all words.
11    
12   Returns a tuple of:
13   - out: Array of shape (N, T, D) giving word vectors for all input words.
14   - cache: Values needed for the backward pass
15   """
16  
17   out = W[x, :]
18   cache = (W, x)
19    
20   return out, cache
```

This process just choose the giving indices of words from the vectors of all words And the backward will be like : 

```python
 1 def word_embedding_backward(dout, cache):
 2    """
 3    Backward pass for word embeddings. We cannot back-propagate into the words
 4    since they are integers, so we only return gradient for the word embedding
 5    matrix.
 6    HINT: Look up the function np.add.at
 7    Inputs:
 8    - dout: Upstream gradients of shape (N, T, D)
 9    - cache: Values from the forward pass
10     Returns:
11     - dW: Gradient of word embedding matrix, of shape (V, D).
12     """
13     dW = None
14     ##############################################################################
15     # TODO: Implement the backward pass for word embeddings.                     #
16     #                                                                            #
17     # Note that words can appear more than once in a sequence.                   #
18     # HINT: Look up the function np.add.at                                       #
19     ##############################################################################
20     W, x = cache
21     dW = np.zeros_like(W)
22 	# add dout at the indices x TO dW
23     np.add.at(dW, x, dout)
24     #pass
25     ##############################################################################
26     #                               END OF YOUR CODE                             #
27     ##############################################################################
28     return dW
```

Notice that in evert timestop we should use an afine function to transform the RNN hidden vector at vector into scores for each word，we omit this because I have implemented it in assignment2, if you want to see the code , you can go to my github,and in this [file](https://github.com/ZhengLiangliang1996/CS231n/blob/master/assignment3/cs231n/rnn_layers.py#L209). in function temporal_affine_forward/backward

At every timestep we produce a score for each word in vocabulary, then use the ground truth word to compute the softmax loss function:[file](https://github.com/ZhengLiangliang1996/CS231n/blob/master/assignment3/cs231n/rnn_layers.py#L209)

```python
 1    def loss(self, features, captions):
 2        """
 3        Compute training-time loss for the RNN. We input image features and
 4        ground-truth captions for those images, and use an RNN (or LSTM) to compute
 5        loss and gradients on all parameters.
 6        Inputs:
 7        - features: Input image features, of shape (N, D)
 8        - captions: Ground-truth captions; an integer array of shape (N, T) where
 9          each element is in the range 0 <= y[i, t] < V
10         Returns a tuple of:
11         - loss: Scalar loss
12         - grads: Dictionary of gradients parallel to self.params
13         """
14         # Cut captions into two pieces: captions_in has everything but the last word
15         # and will be input to the RNN; captions_out has everything but the first
16         # word and this is what we will expect the RNN to generate. These are offset
17         # by one relative to each other because the RNN should produce word (t+1)
18         # after receiving word t. The first element of captions_in will be the START
19         # token, and the first element of captions_out will be the first word.
20         captions_in = captions[:, :-1]
21         captions_out = captions[:, 1:]
22 
23         # You'll need this
24         mask = (captions_out != self._null)
25 
26         # Weight and bias for the affine transform from image features to initial
27         # hidden state
28         W_proj, b_proj = self.params['W_proj'], self.params['b_proj']
29 
30         # Word embedding matrix
31         W_embed = self.params['W_embed']
32 
33         # Input-to-hidden, hidden-to-hidden, and biases for the RNN
34         Wx, Wh, b = self.params['Wx'], self.params['Wh'], self.params['b']
35 
36         # Weight and bias for the hidden-to-vocab transformation.
37         W_vocab, b_vocab = self.params['W_vocab'], self.params['b_vocab']
38 
39         loss, grads = 0.0, {}
40         ############################################################################
41         # TODO: Implement the forward and backward passes for the CaptioningRNN.   #
42         # In the forward pass you will need to do the following:                   #
43         # (1) Use an affine transformation to compute the initial hidden state     #
44         #     from the image features. This should produce an array of shape (N, H)#
45         # (2) Use a word embedding layer to transform the words in captions_in     #
46         #     from indices to vectors, giving an array of shape (N, T, W).         #
47         # (3) Use either a vanilla RNN or LSTM (depending on self.cell_type) to    #
48         #     process the sequence of input word vectors and produce hidden state  #
49         #     vectors for all timesteps, producing an array of shape (N, T, H).    #
50         # (4) Use a (temporal) affine transformation to compute scores over the    #
51         #     vocabulary at every timestep using the hidden states, giving an      #
52         #     array of shape (N, T, V).                                            #
53         # (5) Use (temporal) softmax to compute loss using captions_out, ignoring  #
54         #     the points where the output word is <NULL> using the mask above.     #
55         #                                                                          #
56         # In the backward pass you will need to compute the gradient of the loss   #
57         # with respect to all model parameters. Use the loss and grads variables   #
58         # defined above to store loss and gradients; grads[k] should give the      #
59         # gradients for self.params[k].                                            #
60         #                                                                          #
61         # Note also that you are allowed to make use of functions from layers.py   #
62         # in your implementation, if needed.                                       #
63         ############################################################################
64         # Word Embedding
65         captions_in_emb,emb_cache = word_embedding_forward(captions_in,W_embed)
66         # Affine Forward 
67         h_0,feature_cache = affine_forward(features,W_proj,b_proj)
68         #RNN part
69         h,rnn_cache = rnn_forward(captions_in_emb, h_0, Wx, Wh, b)
70         
71         # Temporal Afine 
72         temporal_out, temporal_cache = temporal_affine_forward(h, W_vocab, b_vocab)
73         
74         # Softloss 
75         loss, dout = temporal_softmax_loss(temporal_out, captions_out, mask)
76         
77         # Gradient 倒序
78         dtemp, grads['W_vocab'], grads['b_vocab'] = temporal_affine_backward(dout, temporal_cache)
79         drnn, dh0, grads['Wx'], grads['Wh'], grads['b'] = rnn_backward(dtemp, rnn_cache)
80         dfeatures, grads['W_proj'], grads['b_proj'] = affine_backward(dh0, feature_cache)
81      
82         grads['W_embed'] = word_embedding_backward(drnn, emb_cache)
83         #pass
84         ############################################################################
85         #                             END OF YOUR CODE                             #
86         ############################################################################
87 
88         return loss, grads
```

This function basically implement the process shown in the image that we saw in the very begining.

AFTER finishing this function, in the cs231n assignment3 file, they also present a function that is used for overfitting small data, only in this way can we know that this model can be used. So don't forget to overfit small data first right after finishing your model!

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_120908.jpg" alt="screenshot" width="80%" height="auto">
</p>

If you see this image showing then you should have a big smile on your face : )

And the description of the image will be start with the <start> tp=token and end with <END> token, the result will be like : <p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_1213181.jpg" alt="screenshot" width="80%" height="auto">
</p>

 

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-03_1213411.jpg" alt="screenshot" width="80%" height="auto">
</p>

 

TBH, it could be really hard to write the code from the very begining and build all the functions and connect them based on logical basis, but if you can imagine the whole process or how the data will be transported and calculated, after imaging so,recalling the one specific process image in your mind, then the functions can be easier to be implemented. Tips: Every time you need to do dot product, make sure you know the size of the elements!!!

3rd Aug 2018
