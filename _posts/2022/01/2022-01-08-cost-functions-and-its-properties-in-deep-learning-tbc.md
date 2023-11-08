---
title: "Cost Functions and its properties in Deep Learning (TBC)"
date: "2022-01-08"
categories: 
  - "dl-ml-python"
---

**Loss Function and Cost Function**

In supervised learning, concretely we're learning from given training set $latex {(x\_i, y\_i)}&fg=000000$ and formulate our hypotheses $latex {h\_\\theta(x)}&fg=000000$. Here, the $latex {\\theta\_{i}}&fg=000000$ 's are the parameters (also called weights) parameterizing the space of linear functions mapping from $latex {\\mathcal{X}}&fg=000000$ to $latex {\\mathcal{Y}}&fg=000000$. When there is no risk of confusion, we will drop the $latex {\\theta}&fg=000000$ subscript in $latex {h\_{\\theta}(x)}&fg=000000$, and write it more simply as $latex {h(x)}&fg=000000$.

The goal of our learning is to minimize the distance between hypotheses and the real y, and Loss function is a function to measure such distance.

**The difference between Loss Function and Cost Function**

- Loss function always appear when we are talking about 1 single training sample, given a prediction and calculate the loss between the prediction and real value.
- Cost function refers to the whole loss when we are talking about set of training sets (e.g. in mini-batch gradient descent)
- Hypothesis (objective function) is the function that needs to be optimized.

**Mean Squared Error (MSE) L2 Loss**

Mean Squared Error is the most common cost function used in regression problems, also called L2 loss, the formula is as followed:

$latex \\displaystyle J(\\theta)=\\frac{1}{n} \\sum\_{i=1}^{n}\\left(y^{(i)}-\\hat{y}^{(i)})\\right)^{2} \\ \\ \\ \\ \\ (1)&fg=000000$

We could see from the graph below, the square error is increased in a quadratic way, the lowest loss is 0 and and highest loss could be infinite.

![](images/2022/01/screenshot-2022-01-08-at-18.45.40.png)

The MSE is very useful in regression problem, from the perspective of bias and variance perspective, we could do a bias and variance decomposition from MSE function.

- **Bias** indicates the distance between the expectation of predicted value and real value. Geometrically speaking, if bias is big, then predicted deviates further from the real value. It is the relationship between predicted value and real value, denotes as $latex {Bias =\\mathbb{E}(\\hat{\\theta})-\\theta}&fg=000000$
- **Variance** describes the variation range of the predicted value, the degree of dispersion, that is, the distance from its own expectation. The larger the variance, the more spread out the distribution of the data. It is the relationship within the predicted values, denote as $latex {Var=\\mathbb{E}\\left\[(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))^{2}\\right\]}&fg=000000$

By using the decomposition trick in MSE equation shown in [2](#eqdecompositionmse). We could get that MSE is actually the addition of variance and the square of bias.

$latex \\displaystyle \\begin{aligned} MSE(\\hat{\\theta}) &= \\mathbb{E}\\left\[(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta})+\\mathbb{E}(\\hat{\\theta})-\\theta)^{2}\\right\] \\\\ &=\\mathbb{E}\\left\[(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))^{2}+2((\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))(\\mathbb{E}(\\hat{\\theta})-\\theta))+(\\mathbb{E}(\\hat{\\theta})-\\theta)^{2}\\right\] \\\\ &=\\mathbb{E}\\left\[(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))^{2}\\right\]+2 \\mathbb{E}\[(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))(\\mathbb{E}(\\hat{\\theta})-\\theta)\]+\\mathbb{E}\\left\[(\\mathbb{E}(\\hat{\\theta})-\\theta)^{2}\\right\] \\\\ &=\\mathbb{E}\\left\[(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))^{2}\\right\]+2(\\mathbb{E}(\\hat{\\theta})-\\theta) \\mathbb{E}(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))^{2}+\\mathbb{E}\\left\[(\\mathbb{E}(\\hat{\\theta})-\\theta)^{2}\\right\] \\\\ &=\\mathbb{E}\\left\[(\\hat{\\theta}-\\mathbb{E}(\\hat{\\theta}))^{2}\\right\]+\\mathbb{E}\\left\[(\\mathbb{E}(\\hat{\\theta})-\\theta)^{2}\\right\] \\\\ &=Var(\\hat{\\theta})+Bias(\\hat{\\theta}, \\theta)^{2} \\end{aligned} \\ \\ \\ \\ \\ (2)&fg=000000$

**Probabilistic interpretation of MSE**

A better explanation for using the MSE could be derived from a probabilistic interpretation. The relationship of the target hypothesis and real value y could be formed as

$latex \\displaystyle y^{(i)}=\\theta^{T} x^{(i)}+\\epsilon^{(i)} \\ \\ \\ \\ \\ (3)&fg=000000$

where $latex {\\epsilon^{(i)}}&fg=000000$ is an error term that captures either unmodeled effects, or random noise. Let us further assume that the $latex {\\epsilon^{(i)}}&fg=000000$ are distributed IID (independently and identically distributed) according to a Gaussian distribution (also called a Normal distribution) with mean zero and some variance $latex {\\sigma^{2}}&fg=000000$. We can write this assumption as '$latex {\\epsilon^{(i)} \\sim}&fg=000000$ $latex {\\mathcal{N}\\left(0, \\sigma^{2}\\right) . '}&fg=000000$ I.e., the density of $latex {\\epsilon^{(i)}}&fg=000000$ is given by

$latex \\displaystyle p\\left(\\epsilon^{(i)}\\right)=\\frac{1}{\\sqrt{2 \\pi} \\sigma} \\exp \\left(-\\frac{\\left(\\epsilon^{(i)}\\right)^{2}}{2 \\sigma^{2}}\\right) \\ \\ \\ \\ \\ (4)&fg=000000$

This implies that

$latex \\displaystyle p\\left(y^{(i)} \\mid x^{(i)} ; \\theta\\right)=\\frac{1}{\\sqrt{2 \\pi} \\sigma} \\exp \\left(-\\frac{\\left(y^{(i)}-\\theta^{T} x^{(i)}\\right)^{2}}{2 \\sigma^{2}}\\right) \\ \\ \\ \\ \\ (5)&fg=000000$

When we wish to explicitly view this as a function of $latex {\\theta}&fg=000000$, we will instead call it the likelihood function:

$latex \\displaystyle L(\\theta)=L(\\theta ; X, \\vec{y})=p(\\vec{y} \\mid X ; \\theta) \\ \\ \\ \\ \\ (6)&fg=000000$

The MLE (Maximization of Likelihood Estimation) is a method we used to do the parameter estimation, here we have the parameter theta to be estimated, in order to maximize the likelihood, normally we took the log of this likelihood function (because likelihood function involves tons of probability products, using log form to transform it to summation form), so we have:

$latex \\displaystyle \\begin{aligned} L(\\theta) &=\\prod\_{i=1}^{n} p\\left(y^{(i)} \\mid x^{(i)} ; \\theta\\right) \\\\ &=\\prod\_{i=1}^{n} \\frac{1}{\\sqrt{2 \\pi} \\sigma} \\exp \\left(-\\frac{\\left(y^{(i)}-\\theta^{T} x^{(i)}\\right)^{2}}{2 \\sigma^{2}}\\right) \\end{aligned} \\ \\ \\ \\ \\ (7)&fg=000000$

$latex \\displaystyle \\begin{aligned} \\ell(\\theta) &=\\log L(\\theta) \\\\ &=\\log \\prod\_{i=1}^{n} \\frac{1}{\\sqrt{2 \\pi} \\sigma} \\exp \\left(-\\frac{\\left(y^{(i)}-\\theta^{T} x^{(i)}\\right)^{2}}{2 \\sigma^{2}}\\right) \\\\ &=\\sum\_{i=1}^{n} \\log \\frac{1}{\\sqrt{2 \\pi} \\sigma} \\exp \\left(-\\frac{\\left(y^{(i)}-\\theta^{T} x^{(i)}\\right)^{2}}{2 \\sigma^{2}}\\right) \\\\ &=n \\log \\frac{1}{\\sqrt{2 \\pi} \\sigma}-\\frac{1}{\\sigma^{2}} \\cdot \\frac{1}{2} \\sum\_{i=1}^{n}\\left(y^{(i)}-\\theta^{T} x^{(i)}\\right)^{2} . \\end{aligned} \\ \\ \\ \\ \\ (8)&fg=000000$

Hence, maximizing $latex {\\ell(\\theta)}&fg=000000$ gives the same answer as minimizing

$latex \\displaystyle \\frac{1}{2} \\sum\_{i=1}^{n}\\left(y^{(i)}-\\theta^{T} x^{(i)}\\right)^{2} \\ \\ \\ \\ \\ (9)&fg=000000$

The equation [9](#eqols) is also known as ordinary least square. When linear regression model is built, you would usually use the least square error (LSE) method that is minimizing the total euclidean distance between a line and the data points.

Once the model is built, in order to evaluate its performances. A metric is introduced to evaluate 'how far' is your model to the actual real data points in average. The MSE is a good estimate function.

Therefore, LSE is a method that builds a model and MSE is a metric that evaluate your model's performances, but this 2 have a lot in common in the probabilistic perspective, that is the reason I used hypothesis in the derivation, so you could see the same but in 2 different context.

**Mean Absolute Error (MAE) L1 Loss**

Mean Absolute Error (MAE) is another class of loss function used in regression problem, also known as L1 loss, the cost function is shown in equation [10](#eqmae).

$latex \\displaystyle J\_{\\theta}=\\frac{1}{n} \\sum\_{i=1}^{n}\\left|y\_{i}-\\hat{y}\_{i}\\right| \\ \\ \\ \\ \\ (10)&fg=000000$

The loss of mae when assumed y real is 0 could be plotted below. We could tell from the graph that the biggest loss could be infinite and the lowest is 0, and the loss increased linearly.

![](images/2022/01/screenshot-2022-01-10-at-21.47.47.png)

**Probabilistic interpretation of MAE**

Same as the derivation of MSE, when we're considering the loss of MAE, we assumed that the error is distributed as Laplace distribution $latex {(\\mu=0, b=1)}&fg=000000$, the error $latex {\\epsilon}&fg=000000$ distribution of could be written as [11](#eqlaplace)

$latex \\displaystyle p\\left(y\_{i} \\mid x\_{i}\\right)=\\frac{1}{2} \\exp \\left(-\\left|y\_{i}-\\hat{y}\_{i}\\right|\\right) \\ \\ \\ \\ \\ (11)&fg=000000$

Using the Maximum Likelihood Estimation (MLE) as in mean square error example, we could have the following derivation \\

$latex \\displaystyle \\begin{aligned} &L(x, y)=\\prod\_{i=1}^{n} \\frac{1}{2} \\exp \\left(-\\left|y\_{i}-\\hat{y}\_{i}\\right|\\right) \\\\ &L L(x, y)=-n \\log 2-\\sum\_{i=1}^{n}\\left|y\_{i}-\\hat{y}\_{i}\\right| \\\\ &N L L(x, y)=\\sum\_{i=1}^{n}\\left|y\_{i}-\\hat{y}\_{i}\\right| \\end{aligned} \\ \\ \\ \\ \\ (12)&fg=000000$

As we can see after that we could get the form of MAE, by maximize the LL is the same as minimize NLL.

**Difference between MSE and MAE**

The MSE loss (L2) generally converges faster than the MAE loss (L1), but the MAE loss is more robust to outliers.

MSE generally converges faster than MAE. When using the gradient descent algorithm, and the gradient of MAE loss is $latex {-\\hat{y}\_{i}}&fg=000000$, that is, the scale of the gradient of MSE will change with the size of the error, while the scale of the gradient of MAE will always remain 1 , Even when the absolute error is very small, the gradient scale of MAE is also 1, which is actually very unfavorable for model training. This is also the reason why MSE is more popular.

MAE is more robust to outliers. We can understand this from the 2 perspectives:

Firstly, the following figure shows the MAE and MSE losses drawn into the same picture. Since the MAE loss and the absolute error are linear, the MSE loss and the error have a quadratic relationship. When the error is very large, The MSE loss will be much larger than the MAE loss. Therefore, when there is an outlier with a very large error in the data, MSE will generate a very large loss, which will have a greater impact on the training of the model.

![](images/2022/01/screenshot-2022-01-10-at-21.21.18.png)

Secondly, when we look at the assumption of the two loss functions. MSE assumes that the error is distributed as a Gaussian distribution, and MAE assumes that the error is distributed as a Laplace distribution. The Laplace distribution by itself is more robust to outliers. when outliers appear on the right side of the right figure, the Laplace distribution is much less affected than the Gaussian distribution. Graph is from [Machine Learning A Probabilistic Perspective](https://doc.lagout.org/science/Artificial%20Intelligence/Machine%20learning/Machine%20Learning_%20A%20Probabilistic%20Perspective%20%5BMurphy%202012-08-24%5D.pdf)

![](images/2022/01/screenshot-2022-01-10-at-21.30.28.png)

**Code**

Graph could be found in my [github](https://github.com/ZhengLiangliang1996/Loss-Function/blob/main/Cost%20Function.ipynb)

**Reference**

- [Machine Learning A Probabilistic Perspective](https://doc.lagout.org/science/Artificial%20Intelligence/Machine%20learning/Machine%20Learning_%20A%20Probabilistic%20Perspective%20%5BMurphy%202012-08-24%5D.pdf)
