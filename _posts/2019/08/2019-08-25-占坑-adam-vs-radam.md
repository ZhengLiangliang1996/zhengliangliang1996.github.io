---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Adam vs. RAdam"
date: "2019-08-25"
categories: 
  - "未分类"
---

- **Optimizer**

During the training process, we will adjust the parameters in our model to minimize loss function, optimizer is the trick(or say way) to do the job. A vanilla optimizer is to take the gradient of your loss function wrt corresponding weight and multiply by negative learning rate, this is simple gradient descent, SGD is more or less the same. While some other optimizers are momentum based: momentum update, Nesterov Momentum. Inspired by Newton's method (approximate root of an equation by calculating Hessian matrix), there are second order method. Last but not the least, Per-parameter adaptive learning rate methods are also frequently used optimizers, for example Adagrad and RMSprop. (More detailed could be found in [CS231n](http://cs231n.github.io/neural-networks-3/) or optimizers comparison code in [pytorch](https://github.com/ZhengLiangliang1996/PytorchLearning/blob/master/Pytorch06_optimizer.ipynb)).

- **Adam**

Adam is a bit like RMSProp with momentum, the update rule works as below: (Sorry I wrote it by hand)

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2019/08/253495255.jpg" alt="screenshot" width="80%" height="auto">
</p>

m and v are estimates of first and second moments, if this is an unbiased estimator, the expected values of the estimators should be equal to the dx we're trying to estimate. We made the following calculation to get the expectation of m_t, which will contain dx inside and could be used to repremsent dx later.

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2019/08/1276645224.jpg" alt="screenshot" width="80%" height="auto">
</p>

Using induction to get the normal expression of mt, which sums up previous beta_1 and times our parameter dx_i. (There is a mistake in the accumulation term, i should starts from 1)

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2019/08/224847056.jpg" alt="screenshot" width="80%" height="auto">
</p>

We could take dx_i out of the sum because it does not depend on i, beta_i is always constant so it could stay outside of the expectation notion. The estimation of m_t here is E[dx_i], if we move 1 - beta_1 to the left we could get the exact same equation in the third line.

Finally the update rule will become as follows,

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2019/08/1891530343.jpg" alt="screenshot" width="80%" height="auto">
</p>

Intuitively we made changes of the learning rate by scaling it, m_t could be seen as mean and v_t could be seen as variance.

- RAdam

RAdam is the rectifier version of Adam proposed by [Liu, Jian, He et al](https://arxiv.org/pdf/1908.03265.pdf) that provides an dynamic adjustment to the adaptive learning rate based on their detailed study into the effects of variance and momentum during training.

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2019/08/903133253.jpg" alt="screenshot" width="80%" height="auto">
</p>

In LIU's paper there is a warm up, which serves as a variance reducer, but the degree of warm up required is unknown and varies dataset to dataset.  They thus built a rectifier term, that would allow the adaptive momentum to slowly but steadily be allowed to work up to full expression as a function of the underlying variance.

 

The followings are some detail about p and r, from [liu](https://arxiv.org/pdf/1908.03265.pdf)<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2019/08/screenshot-from-2019-08-27-19-38-54.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2019/08/screenshot-from-2019-08-27-19-39-13.png" alt="screenshot" width="80%" height="auto">
</p>

 

written by LiangLiang ZHENG
