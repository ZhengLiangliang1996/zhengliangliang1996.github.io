---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "NLP: Word2Vec Skip-Gram(CS224n) implemented in raw way and in Tensorflow"
date: "2018-08-17"
categories: 
  - "dl-ml-python"
---

The following contents and images are from cs224n and [hankcs](http://www.hankcs.com/nlp/cs224n-assignment-1.html/2).

----------------------------------------------------------------------------------------------------------------------------

Before getting into the word2vec part, let's talk about how do you understand a sentence or say when you're reading, how do you figure out the meaning of the whole bunch of words, the meaning and the specific image of the words right? So, when it comes to Computer Science, how do you teach computer to know what's the "meaning" of a word, or a sentence? In the last couple of decades, scientists were using classifying dictionary like wordnet, but it takes massive amount of time for people to put words in order, and it cannot tackle the problem of word similarity.

Then a linguist called J. R. Firth came up with an idea that a word can be understood through its context, it's the basic idea of NLP statistics. it is also called distributed representations.

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/006Fmjmcly1fgcgiwa1j4j317w08mtaj.jpg "hankcs.com 2017-06-07 上午11.04.07.png"" alt="screenshot" width="80%" height="auto">
</p>

So the word2vec means we're using "center words" and its context to predict each other. In cs224n there are 2 algorithms:

- Skip-grams: using center words to predict its context
- CBOW(Continuous Bag of Words): using context to predict center words

Anther algorithm will be more efficient called **Negative Sampling**.

**Skip-gram:** 

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/006Fmjmcly1fgcmzglo19j31ay0n41kx.jpg "hankcs.com 2017-06-07 下午2.47.31.png"" alt="screenshot" width="80%" height="auto">
</p>

We are using conditional probability to describe how precise we can predict its context, our task is to maximize all of the conditional probabilities, when doing so, we can get its context well. then we can write down its (Likelihood function)

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-17_205348.jpg" alt="screenshot" width="80%" height="auto">
</p>

Then the objective function will be :

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-17_205501.jpg" alt="screenshot" width="80%" height="auto">
</p>

We take the negative log likelihood of the likelihood function, then we need to minimize the objective function.

So, how to calculate all the conditional probabilities?  we use softmax(the reason we use softmax is that it can map arbitrary values Xi to a probability ditribution Pi)

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-17_205806.jpg" alt="screenshot" width="80%" height="auto">
</p>

Uo is one context word(outside word) and Vc is the vector of center words, and Uw is the whoe contexts words.

some fundamental math:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-17_210256.jpg" alt="screenshot" width="80%" height="auto">
</p>

And a ppt from manning can show all the stages of Skipgram:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/006Fmjmcly1fgco3v2ca7j30pq0j7drt.jpg "2017-06-07_15-24-56.png"" alt="screenshot" width="80%" height="auto">
</p>

First we look up the center word from word embedding using one hot vector * word embedding matrix, the dot product result can be the representation of center word Vc, and then it times the output representation to calculate the similarity of every words with respect to Vc. then we doing the softmax to get the right probability.

First we should know how to normalizeRows: Implement a function that normalizes each row of a matrix to have unit length.

 1 def normalizeRows(x):
 2    """ Row normalization function
 3 
 4    Implement a function that normalizes each row of a matrix to have
 5    unit length.
 6    """
 7 
 8    ### YOUR CODE HERE
 9    denominator = np.apply_along_axis(lambda x:np.sqrt(x.T.dot(x)),1,x)#跨列
10     x /= denominator[:,None] #将整个
11     #raise NotImplementedError
12     ### END YOUR CODE
13     
14     return x

Then comes the softmaxCostAndGradient: First we calculate the dot product of the v_hat(predicted word or say center word) , then through softmax and cross entropy to calculate its loss, then doing the Gradient,in the function, we should return cost(loss) gradPred (gradients)for center word. and gradients for other word(outside word).

- take the derivative wrt vc

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-21_143055.jpg" alt="screenshot" width="80%" height="auto">
</p>

U = [u1,u2,....uw] means the matrix made of all word vectors, y_hat - y means the probability vector.

- tkae the derivative wrt U

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-21_143328.jpg" alt="screenshot" width="80%" height="auto">
</p>
```python
 1 def softmaxCostAndGradient(predicted, target, outputVectors, dataset):
 2    """ Softmax cost function for word2vec models
 3 
 4    Implement the cost and gradients for one predicted word vector
 5    and one target word vector as a building block for word2vec
 6    models, assuming the softmax prediction function and cross
 7    entropy loss.
 8 
 9    Arguments:
10     predicted -- numpy ndarray, predicted word vector (hat{v} in
11                  the written component)
12     target -- integer, the index of the target word
13     outputVectors -- "output" vectors (as rows) for all tokens
14     dataset -- needed for negative sampling, unused here.
15 
16     Return:
17     cost -- cross entropy cost for the softmax word prediction
18     gradPred -- the gradient with respect to the predicted word
19            vector
20     grad -- the gradient with respect to all the other word
21            vectors
22 
23     We will not provide starter code for this function, but feel
24     free to reference the code you previously wrote for this
25     assignment!
26     """
27 
28     ### YOUR CODE HERE
29     #softmax
30     vhat = predicted 
31     z = np.dot(outputVectors,vhat)
32     preds = softmax(z)
33     # cross entropy
34     cost = -np.log(preds[target])
35     
36     # Gradient
37     z = preds.copy()
38     z[target] -= 1.0
39     grad = np.outer(z,vhat) # wrt outside words
40     gradPred = np.dot(outputVectors.T,z) # wrt center word
41     ### END YOUR CODE
42 
43     return cost, gradPred, grad
```

Then we implemented the skipgram part, all we have to do is also compute all the cost(loss) and gradients, and we got bunch of parameter in this function

1. **currentWord** -- a string of the current **center** word
2. **C** -- integer, context size
3. **contextWords** -- list of no more than 2*C strings, the context words
4. **tokens** -- a dictionary that maps words to their indices in the word vector list(impotant in implementation)
5. **inputVectors** -- "input" word vectors (as rows) for all tokens
6. **outputVectors** -- "output" word vectors (as rows) for all tokens
7. **word2vecCostAndGradient** -- the cost and gradient function for a prediction vector given the target word vectors, could be one of the two cost functions you implemented above.

Recalled that the objective function is a neg log of the likelihood function:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-17_205501.jpg" alt="screenshot" width="80%" height="auto">
</p>

in the for loop, we just scan all the contextWords and calculate the gradient<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-21_144422.jpg" alt="screenshot" width="80%" height="auto">
</p>

and all of the cost and gradient will be summation:
```python
 1 def skipgram(currentWord, C, contextWords, tokens, inputVectors, outputVectors,
 2             dataset, word2vecCostAndGradient=softmaxCostAndGradient):
 3    """ Skip-gram model in word2vec
 4 
 5    Implement the skip-gram model in this function.
 6 
 7    Arguments:
 8    currentWord -- a string of the current center word
 9    C -- integer, context size
10     contextWords -- list of no more than 2*C strings, the context words
11     tokens -- a dictionary that maps words to their indices in
12               the word vector list
13     inputVectors -- "input" word vectors (as rows) for all tokens
14     outputVectors -- "output" word vectors (as rows) for all tokens
15     word2vecCostAndGradient -- the cost and gradient function for
16                                a prediction vector given the target
17                                word vectors, could be one of the two
18                                cost functions you implemented above.
19 
20     Return:
21     cost -- the cost function value for the skip-gram model
22     grad -- the gradient with respect to the word vectors
23     """
24 
25     cost = 0.0
26     gradIn = np.zeros(inputVectors.shape)
27     gradOut = np.zeros(outputVectors.shape)
28 
29     ### YOUR CODE HERE
30     #tokens是词到idx的映射 得到idx再回输入中去找到词向量
31     centerword_idx = tokens[currentWord]
32     vhat = inputVectors[centerword_idx]
33     
34     # 对每一个上个文的单词进行word2vec训练 计算累计cost与gradients
35     for j in contextWords:
36         u_idx = tokens[j]
37         c_cost, c_grad_in,c_grad_out = 
38             word2vecCostAndGradient(vhat, u_idx, outputVectors, dataset)
39         cost += c_cost
40         gradIn[centerword_idx] += c_grad_in
41         gradOut += c_grad_out
42     #raise NotImplementedError
43     ### END YOUR CODE
44 
45     return cost, gradIn, gradOut
```
* * *

Implement skipgram in tensorflow:

some packages needed to be imported:
```python
 1 import os
 2 os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
 3 
 4 import numpy as np
 5 from tensorflow.contrib.tensorboard.plugins import projector
 6 import tensorflow as tf
 7 
 8 import utils
 9 import word2vec_utils
```
First we need to know our model hyperparameters:
```python
 1 # Model hyperparameters
 2 VOCAB_SIZE = 50000
 3 BATCH_SIZE = 128
 4 EMBED_SIZE = 128            # dimension of the word embedding vectors
 5 SKIP_WINDOW = 1             # the context window
 6 NUM_SAMPLED = 64            # number of negative examples to sample
 7 LEARNING_RATE = 1.0
 8 NUM_TRAIN_STEPS = 100000
 9 VISUAL_FLD = 'visualization'
10 SKIP_STEP = 5000
```
In tensorflow, normally we will build a graph for model , in every def, we have a name_scope for valuable sharing:

in the SkipGramModel, or in any model, first we should do is to create an iterator to get dataset:
```
 1 # Step 1: get input, output from the dataset
 2    iterator = dataset.make_initializable_iterator()
 3    center_words, target_words = iterator.get_next()
 ```

After this, we neen to define weights, and the weights are for embed matrix, and in this step we initialize it.
```
 1 # Step 2: define weights. 
 2    # In word2vec, it's the weights that we care about
 3    embed_matrix = tf.get_variable('embed_matrix', 
 4                                    shape=[VOCAB_SIZE, EMBED_SIZE],
 5                                    initializer=tf.random_uniform_initializer())
 ```

notice that the shape is [VOCAB_SIZE, EMBED_SIZE], in the following step, we define the inference. This is a function in tf.nn , embedding——lookup means that we return the index(actually in this case ceter_words is just position,indices) in the embed_matrix.
```
 1 # Step 3: define the inference
 2 embed = tf.nn.embedding_lookup(embed_matrix, center_words, name='embed')
```
Next step is to define loss function, recall that in skip_gram model, we use softmax for probability, and in this tf version, we use nce,which is another loss function.
```python
 1    # Step 4: define loss function
 2    # construct variables for NCE loss
 3    nce_weight = tf.get_variable('nce_weight', 
 4                                 shape=[VOCAB_SIZE, EMBED_SIZE],
 5                                 initializer=tf.truncated_normal_initializer(stddev=1.0 / (EMBED_SIZE ** 0.5)))
 6    nce_bias = tf.get_variable('nce_bias', initializer=tf.zeros([VOCAB_SIZE]))
```
for the whole loss, we need to summation, and in tensorflow, simply we just convey nce loss in the tf.reduce_mean, when the model was trained, it will sum all of the loss automatically.
```python
 1    # define loss function to be NCE loss function
 2    loss = tf.reduce_mean(tf.nn.nce_loss(weights=nce_weight, 
 3                                        biases=nce_bias, 
 4                                        labels=target_words, 
 5                                        inputs=embed, 
 6                                        num_sampled=NUM_SAMPLED, 
 7                                        num_classes=VOCAB_SIZE), name='loss')
```
Then comes the optimizer, the reduce_mean and train_GradientDescentOptimizer function should be remembered since they are frequently used function.
```
 1    # Step 5: define optimizer that follows gradient descent update rule
 2    # to minimize loss
 3    optimizer = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(loss)
```
And for the training part: 1 . initiliaze ierator and variables,  and in each epoch, we sess.run the loss and optimizer, then print out loss in each 5000 step,  and the loss will be total_loss / 5000, in the code below you can find it : 
```python
 1    with tf.Session() as sess:
 2 
 3        # Step 6: initialize iterator and variables
 4        sess.run(iterator.initializer)
 5        sess.run(tf.global_variables_initializer())
 6 
 7        total_loss = 0.0 
 8        writer = tf.summary.FileWriter('graphs/word2vec_simple', sess.graph)
 9 
10         for index in range(NUM_TRAIN_STEPS):
11             try:
12                 # Step 7: execute optimizer and fetch loss
13                 loss_batch, _ = sess.run([loss, optimizer])
14 
15                 total_loss += loss_batch
16 
17                 if (index + 1) % SKIP_STEP == 0:
18                     print('Average loss at step {}: {:5.1f}'.format(index, total_loss / SKIP_STEP))
19                     total_loss = 0.0
20             except tf.errors.OutOfRangeError:
21                 sess.run(iterator.initializer)
22         writer.close()
```
After training on spyder, the result:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-21_163627.jpg" alt="screenshot" width="80%" height="auto">
</p>
