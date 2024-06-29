---
giscus_comments: true
layout: post
title: "What is Mathematics: Solution Chapter 2"
date: "2024-06-26"
categories: 
  - "math"
toc:
  sidebar: true
---

## Before the solutions :) 
The solution presented on the blog is my personal solutions for the exercises in the book 'What is Mathematics: An Elementary Approach To Ideas And Methods' by Herbert Robbins and Richard Courant,  please leave a comment if you spot any mistakes or you have questions on the solution. Thanks in advance! 


## Incommensurable segments, irrational numbers, and the concept of limit

1. Prove that $$ \sqrt[3]{2}, \sqrt{3}, \sqrt{5}, \sqrt[3]{3} $$ are not rational. (Hint: Use the lemma of p. 47).

    
    (1). $$ \sqrt[3]{2}$$
    
    Assume $$\sqrt[3]{2}$$ is rational:

    $$
    \sqrt[3]{2} = \frac{p}{q} \quad \text{gcd}(p, q) = 1
    $$

    $$
    \begin{aligned}
    2 = \frac{p^3}{q^3} \Rightarrow 2q^3 = p^3
    \end{aligned}
    $$

    Based on the lemma, p divdes ab, therefore p divides a or b. since $$\text{gcd}(p, q) = 1$$, Therefore

    $$ 
    2 \left| p^3 \Rightarrow 2\right|p
    $$

    therefore p is some even number, and can be denoted as 2k

    $$
    2q^3 = (2k)^3
    $$


    $$
    q^3 = 4k^3 \quad \text{and q} \quad \text{is even}, \quad \text{contradicting gcd}(p, q) = 1.
    $$

    Therefore $$\sqrt[3]{2}$$ is irrational number.


    (2). $$ \sqrt{3}$$

    Assume $$\sqrt{3}$$ is rational:

    $$
    \sqrt{3} = \frac{p}{q} \quad \text{gcd}(p, q) = 1
    $$

    $$
    \begin{aligned}
    3 = \frac{p^2}{q^2} \Rightarrow 3q^2 = p^2
    \end{aligned}
    $$

    Based on the lemma, p divdes ab, therefore p divides a or b. since $$\text{gcd}(p, q) = 1$$, Therefore

    $$ 
    3 \left| p^2 \Rightarrow 3\right|p
    $$

    therefore can be denoted as 3k

    $$
    3q^2 = (3k)^2
    $$


    $$
    q^2 = 3k^2 \quad \Rightarrow 3\left|q^2 \Rightarrow 3\right|q, \quad \text{which contradicting gcd}(p, q) = 1.
    $$

    Therefore $$\sqrt{3}$$ is irrational number.

    (3). $$\sqrt{5}$$

    Assume $$\sqrt{5}$$ is rational:

    $$
    \sqrt{5} = \frac{p}{q} \quad \text{gcd}(p, q) = 1
    $$

    $$
    \begin{aligned}
    5 = \frac{p^2}{q^2} \Rightarrow 5q^2 = p^2
    \end{aligned}
    $$

    Based on the lemma, p divdes ab, therefore p divides a or b. since $$\text{gcd}(p, q) = 1$$, Therefore

    $$ 
    5 \left| p^2 \Rightarrow 3\right|p
    $$

    therefore can be denoted as 3k

    $$
    5q^2 = (5k)^2
    $$

    $$
    q^2 = 5k^2 \quad \Rightarrow 5\left|q^2 \Rightarrow 5\right|q, \quad \text{which contradicting gcd}(p, q) = 1.
    $$

    Therefore $$\sqrt{5}$$ is irrational number.

    (4). $$\sqrt[3]{3}$$

    Assume $$\sqrt[3]{3}$$ is rational:

    $$
    \sqrt[3]{3} = \frac{p}{q} \quad \text{gcd}(p, q) = 1
    $$

    $$
    \begin{aligned}
    3 = \frac{p^3}{q^3} \Rightarrow 3q^3 = p^3
    \end{aligned}
    $$

    Based on the lemma, p divdes ab, therefore p divides a or b. since $$\text{gcd}(p, q) = 1$$, Therefore

    $$ 
    3 \left| p^3 \Rightarrow 2\right|p
    $$

    therefore p can be denoted as 3k

    $$
    3q^3 = (3k)^3
    $$


    $$
    q^3 = 9k^3 \quad \Rightarrow 9\left|q^2 \Rightarrow 9\right|q
    $$
  
    if a number can divides 9, it can also divdes 3, which contradicting with $$\text{gcd}(p,d)=1$$.

    Therefore $$\sqrt[3]{3}$$ is irrational number.

2. Prove that $$ \sqrt{2} + \sqrt{3} $$ and $$ \sqrt{2} + \sqrt[3]{2} $$ are not rational. (Hint: If e.g. the first of these numbers were equal to a rational number \( r \), then, writing $$ \sqrt{3} = r - \sqrt{2} $$ and squaring, $$ \sqrt{2} $$ would be rational.)

    (1). $$\sqrt{2} + \sqrt{3}$$
    If $$ r = \sqrt{2} + \sqrt{3} $$ is rational:

    $$ 
      \sqrt{3} = r - \sqrt{2}, \quad \sqrt{3} \quad \text{is irrational}.
    $$

    squaring both side, we have

    $$
    \begin{aligned}
    3 &= (r - \sqrt{2})^2 \\
    3 &= r^2 - 2r\sqrt{2} + 2 \\
    1 &= r^2 - r\sqrt{2} \\
    1 &= r(r - 2\sqrt{2})
    \end{aligned}
    $$

    1 is rational number, and we assume r is rational number, by subtracting an irrational number, it is impossible to gain 1. Therefore it contradicts the assumption, r should be irrational.

    (2). $$ \sqrt{2} + \sqrt[3]{2} $$

    If $$ \sqrt{2} + \sqrt[3]{2} $$ is rational:

3. Prove that $$ \sqrt{2} + \sqrt{3} + \sqrt{5} $$ is irrational. Try to make up similar and more general examples.
  
    If $$\sqrt{2} + \sqrt{3} + \sqrt{5}$$ is rational,


    $$
    \begin{aligned}
    r = \sqrt{2} + \sqrt{3} + \sqrt{5}
    (r - \sqrt{5}) &= \sqrt{2} + \sqrt{3} \\
    (r - \sqrt{5})^2 &= (\sqrt{2} + \sqrt{3})^2 \\
    r^2 - 2r\sqrt{5} + 5 &= 2 + 2\sqrt{6} + 3 \\
    r^2 &= 2\sqrt{6} + 2\sqrt{5}r \\
    2\sqrt{6} &= r^2 - 2\sqrt{5}r \\
    24 &= r^4 - 6\sqrt{5}r^3 + 20r^2 \\
    \end{aligned}
    $$

    24 is rational, but it contains $$6(\sqrt{5})$$ on the right side, this is absurdly impossible.

    Therefore, $$\sqrt{2} + \sqrt{3} + \sqrt{5}$$ is irrational.

4. Calculate $$\sqrt[3]{2}$$ and $$\sqrt[3]{5}$$ with an accuracy of at least $$10^{-2}$$

    By appling Newton's Method

    $$
    \begin{aligned}
    x &= \sqrt[3]{2} \\
    x^3 &= 2 \\
    \end{aligned}
    $$

    $$
    f(x) = x^3 - 2
    $$

    $$
    x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}= 1 - \frac{1^3 - 2}{3\cdot 1^2} = 1.33
    $$

    $$
    x_2 = x_1 - \frac{f(x_1)}{f'(x_1)}= 1.33 - \frac{1.33 - 2}{3\cdot (1.33)^2} \approx 1.26
    $$

    By using Interval (binary search). 

    $$
    a < \sqrt[3]{5} < b, \quad a = 1, \quad b = 2
    $$

    $$
    c = \frac{a+b}{2} = 1.5
    $$

    $$
    (1.5)^3 < 5
    $$

    Therefore it should be inside interval $$1.5 \sim 2$$

    $$
    \frac{1.5 + 2}{2} = 1.75
    $$

    $$
    (1.75)^3 = 5.3579 > 5
    $$

    Therefore it should be inside interval $$1.5 \sim 1.75$$

    $$
    1.75 + 1.5 = 1.625 
    $$


    $$
    (1.625)^3 \approx 4.29 < 5
    $$

    Therefore it should be inside interval $$1.625 \sim 1.75$$

    $$
    (\frac{1.625 + 1.75}{2})^3 \approx 4.80 < 5
    $$  

    $$
    \therefore \text{between } 1.625 \text{ and } 1.75
    $$



