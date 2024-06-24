---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Cost Functions and its properties in Deep Learning"
date: "2022-01-08"
categories: 
  - "dl-ml-python"
---

**Loss Function and Cost Function**

In supervised learning, concretely we're learning from given training set $$\left(x_i, y_i\right)$$ and formulate our hypotheses $$h_\theta(x)$$. Here, the $$\theta_i$$ 's are the parameters (also called weights) parameterizing the space of linear functions mapping from $$\mathcal{X}$$ to $$\mathcal{Y}$$. When there is no risk of confusion, we will drop the $$\theta$$ subscript in $$h_\theta(x)$$, and write it more simply as $$h(x)$$.

The goal of our learning is to minimize the distance between hypotheses and the real y, and Loss function is a function to measure such distance.


**The difference between Loss Function and Cost Function**

- Loss function always appear when we are talking about 1 single training sample, given a prediction and calculate the loss between the prediction and real value.
- Cost function refers to the whole loss when we are talking about set of training sets (e.g. in mini-batch gradient descent)
- Hypothesis (objective function) is the function that needs to be optimized.

**Mean Squared Error (MSE) L2 Loss**

Mean Squared Error is the most common cost function used in regression problems, also called L2 loss, the formula is as followed:

$$
\left.J(\theta)=\frac{1}{n} \sum_{i=1}^n\left(y^{(i)}-\hat{y}^{(i)}\right)\right)^2
$$

We could see from the graph below, the square error is increased in a quadratic way, the lowest loss is 0 and and highest loss could be infinite.

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2022/01/screenshot-2022-01-08-at-18.45.40.png" alt="screenshot" width="80%" height="auto">
</p>


The MSE is very useful in regression problem, from the perspective of bias and variance perspective, we could do a bias and variance decomposition from MSE function.

- **Bias** indicates the distance between the expectation of predicted value and real value. Geometrically speaking, if bias is big, then predicted deviates further from the real value. It is the relationship between predicted value and real value, denotes as $$=\mathbb{E}(\hat{\theta})-\theta$$
- **Variance** describes the variation range of the predicted value, the degree of dispersion, that is, the distance from its own expectation. The larger the variance, the more spread out the distribution of the data. It is the relationship within the predicted values, denote as $$\operatorname{Var}=\mathbb{E}\left[(\hat{\theta}-\mathbb{E}(\hat{\theta}))^2\right]$$

By using the decomposition trick in MSE equation shown in [2](#eqdecompositionmse). We could get that MSE is actually the addition of variance and the square of bias.

$$
\begin{aligned} M S E(\hat{\theta}) & =\mathbb{E}\left[(\hat{\theta}-\mathbb{E}(\hat{\theta})+\mathbb{E}(\hat{\theta})-\theta)^2\right] \\ & =\mathbb{E}\left[(\hat{\theta}-\mathbb{E}(\hat{\theta}))^2+2((\hat{\theta}-\mathbb{E}(\hat{\theta}))(\mathbb{E}(\hat{\theta})-\theta))+(\mathbb{E}(\hat{\theta})-\theta)^2\right] \\ & =\mathbb{E}\left[(\hat{\theta}-\mathbb{E}(\hat{\theta}))^2\right]+2 \mathbb{E}[(\hat{\theta}-\mathbb{E}(\hat{\theta}))(\mathbb{E}(\hat{\theta})-\theta)]+\mathbb{E}\left[(\mathbb{E}(\hat{\theta})-\theta)^2\right] \\ & =\mathbb{E}\left[(\hat{\theta}-\mathbb{E}(\hat{\theta}))^2\right]+2(\mathbb{E}(\hat{\theta})-\theta) \mathbb{E}(\hat{\theta}-\mathbb{E}(\hat{\theta}))^2+\mathbb{E}\left[(\mathbb{E}(\hat{\theta})-\theta)^2\right] \\ & =\mathbb{E}\left[(\hat{\theta}-\mathbb{E}(\hat{\theta}))^2\right]+\mathbb{E}\left[(\mathbb{E}(\hat{\theta})-\theta)^2\right] \\ & =\operatorname{Var}(\hat{\theta})+\operatorname{Bias}(\hat{\theta}, \theta)^2\end{aligned}
$$

**Probabilistic interpretation of MSE**

A better explanation for using the MSE could be derived from a probabilistic interpretation. The relationship of the target hypothesis and real value y could be formed as

$$
y^{(i)}=\theta^T x^{(i)}+\epsilon^{(i)}
$$

where $$\epsilon^{(i)}$$ is an error term that captures either unmodeled effects, or random noise. Let us further assume that the $$\epsilon^{(i)}$$ are distributed IID (independently and identically distributed) according to a Gaussian distribution (also called a Normal distribution) with mean zero and some variance $$\sigma^2$$. We can write this assumption as ' $$\epsilon{ }^{(i)} \sim \mathcal{N}\left(0, \sigma^2\right)$$.' l.e., the density of $$\epsilon^{(i)}$$ is given by

$$
p\left(\epsilon^{(i)}\right)=\frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(\epsilon^{(i)}\right)^2}{2 \sigma^2}\right)
$$

This implies that

$$
p\left(y^{(i)} \mid x^{(i)} ; \theta\right)=\frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(y^{(i)}-\theta^T x^{(i)}\right)^2}{2 \sigma^2}\right)
$$

When we wish to explicitly view this as a function of $$\theta$$, we will instead call it the likelihood function:

$$
L(\theta)=L(\theta ; X, \vec{y})=p(\vec{y} \mid X ; \theta)
$$

The MLE (Maximization of Likelihood Estimation) is a method we used to do the parameter estimation, here we have the parameter theta to be estimated, in order to maximize the likelihood, normally we took the log of this likelihood function (because likelihood function involves tons of probability products, using log form to transform it to summation form), so we have:

$$
\begin{aligned} L(\theta) & =\prod_{i=1}^n p\left(y^{(i)} \mid x^{(i)} ; \theta\right) \\ & =\prod_{i=1}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(y^{(i)}-\theta^T x^{(i)}\right)^2}{2 \sigma^2}\right)\end{aligned}
$$

$$
\begin{aligned} \ell(\theta) & =\log L(\theta) \\ & =\log \prod_{i=1}^n \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(y^{(i)}-\theta^T x^{(i)}\right)^2}{2 \sigma^2}\right) \\ & =\sum_{i=1}^n \log \frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{\left(y^{(i)}-\theta^T x^{(i)}\right)^2}{2 \sigma^2}\right) \\ & =n \log \frac{1}{\sqrt{2 \pi} \sigma}-\frac{1}{\sigma^2} \cdot \frac{1}{2} \sum_{i=1}^n\left(y^{(i)}-\theta^T x^{(i)}\right)^2 .\end{aligned}
$$

Hence, maximizing $$\ell\left(\theta\right)$$ gives the same answer as minimizing

$$
\frac{1}{2} \sum_{i=1}^n\left(y^{(i)}-\theta^T x^{(i)}\right)^2
$$
The equation [9](#eqols) is also known as ordinary least square. When linear regression model is built, you would usually use the least square error (LSE) method that is minimizing the total euclidean distance between a line and the data points.

Once the model is built, in order to evaluate its performances. A metric is introduced to evaluate 'how far' is your model to the actual real data points in average. The MSE is a good estimate function.

Therefore, LSE is a method that builds a model and MSE is a metric that evaluate your model's performances, but this 2 have a lot in common in the probabilistic perspective, that is the reason I used hypothesis in the derivation, so you could see the same but in 2 different context.

**Mean Absolute Error (MAE) L1 Loss**

Mean Absolute Error (MAE) is another class of loss function used in regression problem, also known as L1 loss, the cost function is shown in equation [10](#eqmae).


$$
J_{\theta}={\frac{1}{n}}\sum_{i=1}^{n}|y_{i}-{\hat{y}}_{i}|
$$


The loss of mae when assumed y real is 0 could be plotted below. We could tell from the graph that the biggest loss could be infinite and the lowest is 0, and the loss increased linearly.

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2022/01/screenshot-2022-01-10-at-21.47.47.png" alt="screenshot" width="80%" height="auto">
</p>

**Probabilistic interpretation of MAE**

Same as the derivation of MSE, when we're considering the loss of MAE, we assumed that the error is distributed as Laplace distribution $$(\mu=0, b=1)$$, the error $$\epsilon$$ distribution of could be written as [11](#eqlaplace)

$$
p\left(y_{i}\mid x_{i}\right)=\frac{1}{2}\exp\left(-\left|y_{i}-\hat{y}_{i}\right|\right) 
$$


Using the Maximum Likelihood Estimation (MLE) as in mean square error example, we could have the following derivation 

$$
L(x,y)=\prod_{i=1}^{n}\frac{1}{2}\exp\left(-\left|y_{i}-\hat{y}_{i}\right|\right) 
$$

$$
L L(x,y)=-n\log2-\sum_{i=1}^{n}|y_{i}-\hat{y_{i}}| 
$$

$$
N L L(x,y)=\sum_{i=1}^{n}|y_{i}-\hat{y}_{i}| 
$$

As we can see after that we could get the form of MAE, by maximize the LL is the same as minimize NLL.

**Difference between MSE and MAE**

The MSE loss (L2) generally converges faster than the MAE loss (L1), but the MAE loss is more robust to outliers.

MSE generally converges faster than MAE. When using the gradient descent algorithm, and the gradient of MAE loss is $$-\hat{y_{i}}$$, that is, the scale of the gradient of MSE will change with the size of the error, while the scale of the gradient of MAE will always remain 1 , Even when the absolute error is very small, the gradient scale of MAE is also 1, which is actually very unfavorable for model training. This is also the reason why MSE is more popular.

MAE is more robust to outliers. We can understand this from the 2 perspectives:

Firstly, the following figure shows the MAE and MSE losses drawn into the same picture. Since the MAE loss and the absolute error are linear, the MSE loss and the error have a quadratic relationship. When the error is very large, The MSE loss will be much larger than the MAE loss. Therefore, when there is an outlier with a very large error in the data, MSE will generate a very large loss, which will have a greater impact on the training of the model.

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2022/01/screenshot-2022-01-10-at-21.21.18.png" alt="screenshot" width="80%" height="auto">
</p>

Secondly, when we look at the assumption of the two loss functions. MSE assumes that the error is distributed as a Gaussian distribution, and MAE assumes that the error is distributed as a Laplace distribution. The Laplace distribution by itself is more robust to outliers. when outliers appear on the right side of the right figure, the Laplace distribution is much less affected than the Gaussian distribution. Graph is from [Machine Learning A Probabilistic Perspective](https://doc.lagout.org/science/Artificial%20Intelligence/Machine%20learning/Machine%20Learning_%20A%20Probabilistic%20Perspective%20%5BMurphy%202012-08-24%5D.pdf)

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2022/01/screenshot-2022-01-10-at-21.30.28.png" alt="screenshot" width="80%" height="auto">
</p>

**Code**

Graph could be found in my [github](https://github.com/ZhengLiangliang1996/Loss-Function/blob/main/Cost%20Function.ipynb)

**Reference**

- [Machine Learning A Probabilistic Perspective](https://doc.lagout.org/science/Artificial%20Intelligence/Machine%20learning/Machine%20Learning_%20A%20Probabilistic%20Perspective%20%5BMurphy%202012-08-24%5D.pdf)
