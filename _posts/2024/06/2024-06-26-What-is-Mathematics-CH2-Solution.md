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

    By applying Newton's Method

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


5. Prove that 
$$
1 - q + q^2 - q^3 + q^4 - \cdots = \frac{1}{1 + q}, \quad \text{if} \quad |q| < 1.
$$

    $$
        \begin{align*}
        S_n &= 1 - q + q^2 - q^3 + q^4 - \cdots \\
        qS_n &= q - q^2 + q^3 - q^4 + \cdots \\
        S_n + qS_n &= 1 + (-1)^{n}q^n \to \infty \\
        \end{align*}
    $$

    $$q^n$$ will be 0 if n goes to infinity.

    $$
    \begin{align*}
      S_n(1+q) &= 1 \\
      S_n &= \frac{1}{1+q}
      \end{align*}
    $$

6. What is the limit of the sequence $$a_1, a_2, a_3, \cdots$$, where $$a_n = n/(n + 1)$$? (Hint: Write the expression in the form 
$$
\frac{n}{n + 1} = 1 - \frac{1}{n + 1}
$$ 
and observe that the second term tends to zero.)


    $$
    \begin{align*}
    a_n &= \left(\frac{1}{n+1}\right) = 1 - \frac{n+1}{n} \text{, the second term tends to 0} \\
    & = 0
    \end{align*}
    $$


7. What is the limit of 
$$
\frac{n^2 + n + 1}{n^2 - n + 1} \quad \text{for} \quad n \to \infty \quad ?
$$ 
(Hint: Write the expression in the form 
$$
\frac{1 + \frac{1}{n} + \frac{1}{n^2}}{1 - \frac{1}{n} + \frac{1}{n^2}}
$$ 
.)

    $$
      \begin{align*}
      \text{Divide by } n^2 \text{ for all terms,} \\
      \frac{1 + \frac{1}{n} + \frac{1}{n^2}}{1 - \frac{1}{n} + \frac{1}{n^2}} & \to 1
      \end{align*}
    $$

8. Prove, for \( |q| < 1 \), that 
$$
1 + 2q + 3q^2 + 4q^3 + \cdots = \frac{1}{(1 - q)^2}.
$$ 
(Hint: Use the result of exercise 3 on p. 18.)

  
    $$
      \begin{align}
      S&=1+2q+3q^2+\qquad\cdots\qquad  \qquad+nq^{n-1}\\
      qS&=\qquad q+2q^2+3q^3+\cdots +\quad(n-1)q^{n-1}+nq^n \\
      \text{Subtracting,}&\\
      (1-q)S&=1+\;\ q \ +\ q^2 +\ q^3+\cdots \qquad \qquad +q^{n-1}-nq^n\\
      &=\frac {\;\ 1-q^n}{1-q}-nq^n\\
      S&=\frac{1-q^n-nq^n(1-q)}{(1-q)^2}\\
      &=\frac{1-(n+1)q^n+nq^{n+1}}{(1-q)^2}\qquad
      \end{align}
    $$

    By analyzing the sum, $$\frac{(n+1)q^n}{(1-q)^2}$$ and $$\frac{nq^{n+1}}{(1-q)^2}$$ tend to 0,
    and $$\frac{1}{(1-q)^2}$$ is the term left. 

    Q.E.D

9. What is the limit of the infinite series 
$$
1 - 2q + 3q^2 - 4q^3 + \cdots \quad ?
$$

    $$
      \begin{aligned}
      S_n &= 1 - 2q + 3q^2 - 4q^3 + \cdots \\
      qS_n &= q - 2q^2 + 3q^3 - 4q^4 + \cdots \\
      (1+q)S_n &= 1 - q + q^2 - q^3 + q^4 - \cdots \\
      (1+q)S_n &= 1 + (-1)^{n+1}q^{n+1} \\
      (-1)^{n+1}q^{n+1} &\to 0 \quad \quad \text{Therefore,} \\
      S_n &= \frac{1}{(1+q)^2}
      \end{aligned}
    $$

10. What is the limit of 
$$
\frac{1 + 2 + 3 + \cdots + n}{n^2}, \quad \text{of} \quad \frac{1^2 + 2^2 + \cdots + n^2}{n^2} \quad ?
$$ 
(Hint: Use the results of pp. 12, 14, 15.)
    $$
    \begin{aligned}
    S_1 &= \frac{1 + 2 + 3 + \cdots + n}{n^2} = \frac{n(n+1)}{2n^2} = \frac{n+1}{2n} = \frac{1}{2} + \frac{1}{2n} \to \frac{1}{2} \\
    S_2 &= \frac{1^2 + 2^2 + \cdots + n^2}{n^3} = \frac{n(n+1)(2n+1)}{6n^3} = \frac{(n+1)(2n+1)}{6n^2} \\ &= \frac{2n^2+3n+1}{6n^2} = \frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2} \to \frac{1}{3}\\
    S_3 &= \frac{1^3 + 2^3 + \cdots + n^3}{n^4} = \left( \frac{n(n+1)}{2n} \right)^2 = \frac{(n+1)^2}{4n^2} = \frac{1}{4} + \frac{1}{2n} + \frac{1}{4n^2} \to \frac{1}{4}
    \end{aligned}
    $$

11. Expand the fractions $$\frac{1}{11}$$, $$\frac{1}{13}$$, $$\frac{2}{13}$$, $$\frac{3}{13}$$, $$\frac{1}{17}$$, $$\frac{2}{17}$$ into decimal fractions and determine the period.

    $$
    \begin{align*}
    \frac{1}{11} &= 0.\overline{09}\ldots \quad (\text{Period: } 2) \\
    \frac{1}{13} &= 0.\overline{076923}\ldots \quad (\text{Period: } 6) \\
    \frac{2}{13} &= 0.\overline{153846}\ldots \quad (\text{Period: } 6) \\
    \frac{3}{13} &= 0.\overline{230769}\ldots \quad (\text{Period: } 6) \\
    \frac{1}{17} &= 0.\overline{0588235294117647}\ldots \quad (\text{Period: } 16) \\
    \frac{2}{17} &= 0.\overline{0.1176470588235294}\ldots \quad (\text{Period: } 16)
    \end{align*}
    $$


11. The number 142857 has the property that multiplication with any one of the numbers 2, 3, 4, 5, or 6 produces only a cyclic permutation of its digits. Explain this property, using the expression of $$\frac{1}{7}$$ into a decimal fraction.
    
    $$
    \begin{align*}
    \frac{1}{7} &= 0.\overline{142857} \\
    2 \times \frac{1}{7} &= 0.\overline{285714} \\
    3 \times \frac{1}{7} &= 0.\overline{428571} \\
    4 \times \frac{1}{7} &= 0.\overline{571428} \\
    5 \times \frac{1}{7} &= 0.\overline{714285} \\
    6 \times \frac{1}{7} &= 0.\overline{857142}
    \end{align*}
    $$

13. Expand the rational numbers $$\frac{1}{11}$$, $$\frac{1}{13}$$, $$\frac{2}{13}$$, $$\frac{3}{13}$$, $$\frac{1}{17}$$, $$\frac{2}{17}$$ as decimals with base 5, 7, and 12.

    $$
    \begin{align*}
    \frac{1}{11} &= 0.\overline{09}\ldots \quad (\text{Period: } 2) \\
    \frac{1}{13} &= 0.\overline{076923}\ldots \quad (\text{Period: } 6) \\
    \frac{2}{13} &= 0.\overline{153846}\ldots \quad (\text{Period: } 6) \\
    \frac{3}{13} &= 0.\overline{230769}\ldots \quad (\text{Period: } 6) \\
    \frac{1}{17} &= 0.\overline{0588235294117647}\ldots \quad (\text{Period: } 16) \\
    \frac{2}{17} &= 0.\overline{0.1176470588235294}\ldots \quad (\text{Period: } 16)
    \end{align*}
    $$

15. Expand one third as a dyadic number.

16. Write $$.11212121 \cdots $$ as a fraction. Find the value of this symbol if it is meant in the systems with the bases 3 or 5.
    $$
    \begin{aligned}
    0.11212121\cdots &=  \frac{1}{10} + 10^{-3} \cdot 12(1 + 10^{-2} + 10^{-4}+\cdots)\\
                     &=  \frac{1}{10} + \frac{12}{1000} \times \frac{1}{1-10^{-2}}\\
                     &=  \frac{1}{10} + \frac{12}{1000} \times \frac{100}{99}\\
                     &=  \frac{111}{990}
    \end{aligned}
    $$

## The mathematical analysis of infinity
1. Show that the set of all positive and negative integers is denumerable. Show that the set of all positive and negative rational numbers is denumerable.
  
    The set of all natural numbers is denumerable, denoted as $$\mathbb{N}$$, and we define the set of all positive and negative integers as $$\mathbb{Z}$$, and this is an inifite set.

    To prove the set $$\mathbb{Z}$$ is denumerable, we need to show it is countable by finding the bijection: $$f: \mathbb{Z} \to \mathbb{N}$$ 

    $$
      f(n) =
    \begin{cases}
    3^n & n>0 \\
    7^{-n} & n \leq 0
    \end{cases}
    $$

    For every integers $$\mathbb{Z}$$ inside we could find a one to one mapping to $$\mathbb{N}$$, therefore the set $$\mathbb{Z}$$ is denumerable.


    For the set of all positive & negative rational numbers, all can be represented as $$\frac{b}{a}$$ where a and b are natural number. We can build this matrix by having a rows and b columns. the nagative rational numbers can be inserted as intermediate.

    $$
    \begin{aligned}
    \frac{1}{1}, -\frac{1}{1}, \frac{1}{2}, -\frac{1}{2}, \ldots\\
    \frac{2}{1}, -\frac{2}{1}, \frac{2}{2}, -\frac{2}{2}, \ldots\\
    \vdots\\
    \frac{n}{1}, -\frac{n}{1}, \frac{n}{2}, -\frac{n}{2}, \ldots\\
    \vdots\\
    \end{aligned}
    $$

    By using [Cantor’s Zig-Zag Method](https://human.libretexts.org/Bookshelves/Philosophy/Sets_Logic_Computation_(Zach)/01%3A_I-_Sets_Relations_Functions/1.04%3A_The_Size_of_Sets/1.4.03%3A_Cantors_Zig-Zag_Method), we can see this set is also countable, therefore it is denumerable. 

2. Show that the set $$S + T$$ (see p. 110) ia denumerable if S and T are denumerable sets. Show the same for the sum of three, four, or any number, n, of sets, and finally for a set composed of denumerably many denumerable sets.

    There exist bijections $$ f: \mathbb{N} \to S  $$ and $$ g: \mathbb{N} \to T $$.
    Define $$ h: \mathbb{N} \to S + T $$ by:

    $$
    h(n) = \begin{cases} 
    f\left(\frac{n}{2}\right) & \text{if } n \text{ is even} \\
    g\left(\frac{n-1}{2}\right) & \text{if } n \text{ is odd}
    \end{cases}
    $$

    h is a bijection, Therefore $$ S + T $$ is denumerable.

    Let $$ S_1, S_2, \ldots, S_n $$ be denumerable sets. To show $$ S_1 + S_2 + \cdots + S_n $$ is denumerable.

    There exist bijections $$ f_i: \mathbb{N} \to S_i $$  for  $$ i = 1, 2, \ldots, n $$.

    Define $$ h: \mathbb{N} \to S_1 + S_2 + \cdots + S_n $$ by:

    $$
    h(n) = 
    $$

    h is a bijection, so the sum of n denumerable sets is denumerable.

3. Show that any interval [A, B] of the number axis is equivalent to any other interval $$[C, Z]$$.

    Define a function $$f$$ to find bijection for end point: 

    $$
      f(A) = C, f(B) = D
    $$

    The function can be defined as to map $$[A,B]$$ to $$[C,D]$$: 

    $$
      f(x) = C + \frac{x-A}{B-A}\cdot (D-C) 
    $$

    From this we can find x to f(x) is 1 to 1 mapping (bijection).

    Q.E.D.


4. Prove that the same result holds for a denumerable set of points in the plane, replacing lengths of intervals by areas of squares.

    We can represent all of the points in a circle by $$\theta$$. Measure in radians, $$[0, 2\pi]$$.

    Assume the enumerable set of angles is given by,

    $$
    \begin{align*}
        \theta_1 &= 0.a_1b_1a_2a_3a_4 \ldots \\
        \theta_2 &= 0.b_1b_2b_3b_4 \ldots \\
        & \vdots \\
        \theta_n &= 0.n_1n_2n_3 \ldots
    \end{align*}

    $$


    Then we can construct a new angle $$\Theta_i$$ by using digits along the diagonal,
    $$\Theta_i = A_1b_2C_3 \ldots$$

    Which is also within $$[0, 2\pi]$$ and it contradicts the assumption.

5. If A contains n elements, where n is a positive integer, show that B, defined as above, contains $$2^n$$ elements. If A consists of the set of all positive integers, show that B is equivalent to the continuum of real numbers from 0 to 1, (Hint: Symbolize a subset of A in the first case by a finite and in the second case by an infinite sequence of the symbols 0 and 1



## Complex Numbers 
1. Express $$\frac{(1+i)(2+i)(3+i)}{(1-i)}$$ in the form $$a + bi$$.

    $$
    \begin{align*}
    \frac{(1+i)(2+i)(3+i)}{(1-i)} & = \frac{(1+2i+i^2)(2+i)(3+i)}{(1-i)(1+i)} \\
    & = \frac{(1+2i+i^2)(2+i)(3+i)}{1 - i^2} \\
    & = i(2+i)(3+i) \\
    & = (2i+i^2)(3+i) \\
    & = (-1+2i)(3+i) \\
    & = -3-i+6i+2i^2 \\
    & = -5+5i
    \end{align*}
    $$
    
2. Express $$\left( -\frac{1}{2} + i \frac{\sqrt{3}}{2} \right)^3$$ in the form $$a + bi$$.

    $$
    \begin{align*}
    \left(-\frac{1}{2} + i \frac{\sqrt{3}}{2}\right)^3 & = \left(-\frac{1}{2} + i \frac{\sqrt{3}}{2}\right)\left(-\frac{1}{2} + i \frac{\sqrt{3}}{2}\right)^2 \\
    & = \left(-\frac{1}{2} + i \frac{\sqrt{3}}{2}\right) \left(\frac{1}{4} + 2\cdot(-\frac{1}{2})\cdot(\frac{\sqrt{3}}{2})i + \frac{3}{4}i^2\right) \\
    & = \left(-\frac{1}{2} + i \frac{\sqrt{3}}{2}\right) \left(-\frac{1}{2} - \frac{\sqrt{3}}{2}i\right) \\
    & = \frac{1}{4} + \frac{\sqrt{3}}{4}i - \frac{\sqrt{3}}{4}i - \frac{3}{4}i^2\\
    & = 1 \\
    \end{align*}
    $$


3. Express in the form $$a + bi$$:
$$
\frac{1+i}{1-i}, \quad \frac{1+i}{2-i}, \quad \frac{1}{i^5}, \quad \frac{1}{(-2+i)(1-3i)}, \quad \frac{(4-5i)^2}{(2-3i)^2}
$$

    $$
      \begin{align*}
      \frac{1+i}{1-i}  & = \frac{(1+i)^2}{1^2-i^2} \\
      & = \frac{1+2i+i^2}{2} \\
      & = 1
      \end{align*}
    $$


    $$
      \begin{align*}
      \frac{1+i}{2-i} & = \frac{(1+i)(2+i)}{(2-i)(2+i)} \\
      & = \frac{2+i+2i+2^2}{4-i^2}\\
      & = \frac{1+3i}{5} \\
      & = \frac{1}{5} + \frac{3}{5}i
      \end{align*}
    $$


    $$
      \begin{align*}
      \frac{1}{i^5} & = \frac{1}{i^2\cdot i^2\cdot i} \\
      & = -i
      \end{align*}
    $$


    $$
      \begin{align*}
      \frac{1}{(-2+i)(1-3i)} & = \frac{1}{-2+6i+i-3i^2} \\
      & = \frac{1-7i}{(1+7i)(1-7i)} \\
      & = \frac{1-7i}{1-49i^2} \\
      & = \frac{1}{50} - \frac{7}{50}i\\
      \end{align*}
    $$


    $$
      \begin{align*}
      \frac{(4-5i)^2}{(2-3i)^2} & = \frac{16-40i+25i^2}{4-6i-6i+9i^2} \\
      & = \frac{-9-40i}{-5-12i} \\
      & = \frac{(-9-40i)(-5+12i)}{(-5-12i)(-5+12i)} \\
      & = \frac{45-108i+200i-480i^2}{144+25} \\
      & = \frac{525+92i}{169}
      \end{align*}
    $$
    
4. Calculate $$\sqrt{5 + 12i}$$. (Hint: Write $$\sqrt{5 + 12i} = x + yi$$, square, and equate real and imaginary parts.)

    $$
    \begin{align*}
        \sqrt{5 + 12i} &= x + yi \\
        5 + 12i &= x^2 + y^2 + 2xyi \\
        5 &= x^2 - y^2 \\
        12 &= 2xy \\
        x^2 - \left(\frac{6}{x}\right)^2 &= 5 \\
        x^2 - \frac{36}{x^2} &= 5 \implies x^4 - 36 = 5x^2 \\
        \text{substitute} x^2 = t \\
        t^2 - 5t - 36 &= 0 \\
        t &= -4 \quad \text{or} \quad t = 9 \\
        x &= \pm 3 \quad y = \pm 2
    \end{align*}
    $$

    Therefore,
    $$\sqrt{5 + 12i} = 3 + 2i \quad \text{or} \quad \sqrt{5 + 12i} = -3 - 2i$$


    
5. Prove this theorem that directly from the definition of multiplication of two complex numbers, $$z_1=x_1+y_1i$$ and $$z_2=x_2+y_2i$$. 

    Theorem: $$
    \begin{aligned}
    |z_1 \cdot z_2| = |z_1| \cdot |z_2|
    \end{aligned}
    $$. 

    $$
    \begin{aligned}
        |z_1 \cdot z_2| &= |(x_1 + y_1i) \cdot (x_2 + y_2i)| \\
        z_1 \cdot z_2 &= x_1 x_2 - y_1 y_2 + (x_1 y_2 + x_2 y_1)i \\
        |z_1 z_2| &= \sqrt{(x_1 x_2 - y_1 y_2)^2 + (x_1 y_2 + x_2 y_1)^2} \\
                  &= \sqrt{x_1^2 x_2^2 + x_1^2 y_2^2 + y_1^2 x_2^2 + y_1^2 y_2^2} \\
        |z_1| &= \sqrt{x_1^2 + y_1^2} \\
        |z_2| &= \sqrt{x_2^2 + y_2^2} \\
        |z_1| \cdot |z_2| &= \sqrt{x_1^2 + y_1^2} \cdot \sqrt{x_2^2 + y_2^2} \\
        &= \sqrt{(x_1^2 + y_1^2)(x_2^2 + y_2^2)} \\
        &= \sqrt{x_1^2 x_2^2 + x_1^2 y_2^2 + y_1^2 x_2^2 + y_1^2 y_2^2} \\
        \therefore |z_1 \cdot z_2| &= |z_1| \cdot |z_2|
    \end{aligned}
    $$

6. From the fact that the product of two real numbers is 0 only if one of the factors is 0, prove the corresponding theorem for complex numbers. (Hint: Use the two theorems just stated.)

    $$
    \begin{aligned}
    z_1 \cdot z_2 &= (x_1 + y_1 i) (x_2 + y_2 i)\\
    &= (x_1 x_2 - y_1 y_2) + (x_1 y_2 + x_2 y_1)i
    &= 0 
    \end{aligned}
    $$

    $$
    \begin{aligned}
    = \begin{cases} 
    x_1 x_2 - y_1 y_2 = 0 & \quad (1) \\
    x_1 y_2 + x_2 y_1 = 0 & \quad (2)
    \end{cases}
    \end{aligned}
    $$

    (1) implies that $$x_1 x_2 = y_1 y_2$$. Either $$x_1 = 0$$ or $$x_2 = 0$$. and for $$y_1 = 0$$ or $$y_2 = 0$$.

    (2) implies that $$x_1 y_2 = - x_2 y_1$$. Then $$x_1 = 0$$ or $$y_2 = 0$$. and for $$x_2 = 0$$ or $$y_1 = 0$$.

    Combine all of the situations together:

    Either $$x_1 = 0$$ and $$y_1 = 0$$ or $$x_2 = 0$$ and $$y_2 = 0 $$

7. When does the equality 
$$|z_1 + z_2| = |z_1| + |z_2|$$
 hold?

    $$
    \begin{aligned}
    |z_1 + z_2| &= |(x_1 + y_1i) + (x_2 + y_2i)| \\
                &= |(x_1 + x_2) + (y_1 + y_2)i| \\
                &= \sqrt{(x_1 + x_2)^2 + (y_1 + y_2)^2}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    |z_1| + |z_2| &= \sqrt{(x_1 + y_1)^2} + \sqrt{(x_2 + y_2)^2}
    \end{aligned}
    $$

    In order to have these 2 equality hold, it requires $$x_1=x_2=y_1=y_2$$, the intuition is that the sum of the other two sides of a triangle is equal to the hypotenuse if and only if it is an equilateral triangle.

8. Find the corresponding formulas for $$\sin 4\phi$$ and $$\cos 4\phi$$.

    $$
    (a + b i)^4 = a^4 + 4a^3b i + 6a^2b^2 +4ab^3 + b^4
    $$

    Obtaining:

    $$
    \begin{aligned}
    (\cos\phi + \sin\phi i)^4 &= \cos^4 \phi + 4 \cos^3 \phi \sin \phi i + 6\cos^2\phi\sin^2\phi i^2 + 4\cos \phi\sin^3\phi i^3 + \sin^4\phi i^4 \\
    &= \cos^4 \phi + \sin^4\phi - 6\cos^2\phi\sin^2\phi + (4 \cos^3 \phi \sin \phi - 4\cos \phi\sin^3\phi) i 
    \end{aligned}
    $$

    Therefore, 

    $$
    \begin{aligned}
    \cos 4\phi &= \cos^4\phi + (1-\cos^2\phi)^2 - 6\cos^2\phi(1-\cos^2\phi)\\
    \sin 4\phi &= 4(1-\sin^2\phi)^{\frac{3}{2}}\sin\phi - 4\sqrt{1-\sin^2\phi}\sin^3\phi\\
    \end{aligned}
    $$

9. Prove that for a point, $$z = \cos \phi + i \sin \phi$$, on the unit circle, $$\frac{1}{z} = \cos \phi - i \sin \phi$$.

    $$
    \begin{aligned}
    \frac{1}{z} &= \frac{1}{\cos \phi + i \sin \phi} \\
      &= \cos \phi - i \sin \phi
    \end{aligned}
    $$

    $$
    \begin{aligned}
    1 &= (\cos \phi - \sin \phi)(\cos \phi + \sin\phi) \\
    \end{aligned}
    $$


10. Prove without calculation that $$\frac{(a + bi)}{(a - bi)}$$ always has the absolute value 1.

    The expression we are interested in is 

    $$
    \frac{a + bi}{a - bi},
    $$

    which can be rewritten in terms of $$z$$ and conjugate $$\bar{z}$$:
    
    $$
    \frac{a + bi}{a - bi} = \frac{z}{\bar{z}}.
    $$

    To find the magnitude of this expression, we use the property of magnitudes for complex numbers:

    $$
    \left|\frac{z}{\bar{z}}\right| = \frac{|z|}{|\bar{z}|}.
    $$

    Since the modulo is the same, therefore it always has the solute value of 1 by calculating $$\frac{(a + bi)}{(a - bi)}$$.


11. If $$z_1$$ and $$z_2$$ are two complex numbers, prove that the angle of $$z_1 - z_2$$ is equal to the angle between the real axis and the vector pointing from $$z_2$$ to $$z_1$$.

    
    Let $$z_1 = x_1 + iy_1$$ and $$z_2 = x_2 + iy_2$$ be two complex number. In the complex plane, $$z_1$$ and $$z_2$$ can be represented as points $$(x_1, y_1)$$ and $$(x_2, y_2)$$, respectively.

    The difference $$z_1 - z_2$$ is given by:

    $$
    z_1 - z_2 = (x_1 - x_2) + i(y_1 - y_2).
    $$

    This difference represents the vector from $$z_2$$ to $$z_1$$ in the complex plane.

    To find the angle of $$z_1 - z_2$$ is given by $$\arg(z) = \theta$$, where:
    
    $$
    \arg(z_1 - z_2) = \tan^{-1} \left( \frac{y_1 - y_2}{x_1 - x_2} \right).
    $$


    Now, let's consider the vector pointing from $$z_2$$ to $$(z_1$$. In Cartesian coordinates, this vector is also:

    $$
    (x_1 - x_2, y_1 - y_2).
    $$

    The angle between this vector and the positive real axis (the x-axis) is given by the same expression:
    $$
    \theta = \tan^{-1} \left( \frac{y_1 - y_2}{x_1 - x_2} \right).
    $$

    Thus, the angle of the complex number $$z_1 - z_2$$ is exactly the angle between the real axis and the vector pointing from $$z_2$$ to $$z_1$$.



12. Interpret the angle of the complex number $$\frac{(z_1 - z_2)}{(z_1 - z_3)}$$ in the triangle formed by the points $$z_1$$, $$z_2$$, and $$z_3$$.

    $$z_1 - z_2$$ represents the complex number corresponding to the vector from $$z_2$$ to $$z_1$$ and $$z_1 - z_3$$ represents the complex number corresponding to the vector from $$z_3$$ to $$z_1$$.

    Dividing two complex numbers $$\frac{z_1 - z_2}{z_1 - z_3}$$ gives a new complex number whose magnitude is the ratio of the magnitudes of the two complex numbers and whose argument (angle) is the difference of their arguments. Let $$\theta_{12} = \arg(z_1 - z_2)$$, which is the angle that the vector from $$z_2$$ to $$z_1$$ makes with the positive real axis. Let $$\theta_{13} = \arg(z_1 - z_3)$$, which is the angle that the vector from $$z_3$$ to $$z_1$$ makes with the positive real axis.

    The argument of the quotient $$\frac{(z_1 - z_2)}{(z_1 - z_3)}$$ is $$\theta_{12} - \theta_{13}$$.

    In geometric terms:

    - If you start from the vector $$\overline{z_1z_3}$$ and rotate counterclockwise by an angle $$\theta_{12} - \theta_{13}$$, you will align with the vector $$\overline{z_1z_2}$$.

    - Thus, the complex number $$\frac{(z_1 - z_2)}{(z_1 - z_3)}$$ gives a complex number whose argument represents the oriented angle between the directed line segments from $$z_1$$ to $$z_3$$ and from $$z_1$$ to $$z_2$$.


13. Prove that the quotient of two complex numbers with the same angle is real.

    If two complex numbers $$ z_1 $$ and $$ z_2 $$ have the same angle, then the argument (angle) of $$ z_1 $$ is equal to the argument of $$ z_2 $$. We can express these complex numbers in polar form:

    $$
    z_1 = \rho _1 e^{i\theta}
    $$

    $$
    z_2 = \rho _2  e^{i\theta}
    $$

    where $$ \rho _1 $$ and $$ \rho _2  $$ are the magnitudes of $$ z_1 $$ and $$ z_2 $$, respectively, and $$ \theta $$ is their common angle.


    The quotient of $$ z_1 $$ and $$ z_2$$ is given by:

    $$
    \begin{aligned}
    \frac{z_1}{z_2} &= \frac{\rho _1 e^{i\theta}}{\rho _2 e^{i\theta}} \\
                    &= \frac{\rho _1}{\rho _2} e^0 \\
                    &= \frac{\rho _1}{\rho _2}
    \end{aligned}
    $$

    Q.E.D.


14. Prove that if for four complex numbers $$z_1, z_2, z_3, z_4$$ the angles of $$\frac{z_3 - z_1}{z_3 - z_2}$$ and $$\frac{z_4 - z_1}{z_4 - z_2}$$ are the same, then the four numbers lie on a circle or on a straight line, and conversely.

    The solution is adapted from: [math exchange](https://math.stackexchange.com/posts/805047/edit)

    First of all, based on the prove on exercise 12, 

    $$\arg\left(\frac{z_4-z_1}{z_4-z_2}\right)$$

    represents the angle $$\angle Z_2 Z_4 Z_1$$.  Similarly

    $$\arg\left(\frac{z_3-z_1}{z_3-z_2}\right)$$

    represents the angle $$\angle Z_2 Z_3 Z_1$$.  
    
    This can be seen as 4 points to be [concyclic](http://en.wikipedia.org/wiki/Inscribed_angle_theorem#Theorem)

    The $$A$$ and $$B$$ in the wikipedia graphic are your $$z_1$$ and $$z_2$$.

    If the 4 lines lies in a straight line then the angle is 0, which is a special case. 

    Q.E.D.

15. Prove that four points $$z_1, z_2, z_3, z_4$$ lie on a circle or on a straight line if and only if 
$$\frac{z_3 - z_1}{z_3 - z_2} = \frac{z_4 - z_1}{z_4 - z_2}$$

    Proved above. 


16. Find the 6th roots of 1.

    $$
    x^6 = 1
    $$

    Based on De Moivre's theorem, for unit circle:

    $$
    z^n = (\cos \phi + i \sin \phi)^n = \cos(n \phi) + i \sin(n \phi)
    $$

    $$
    z^6 = 1 = \cos 0 + i \sin 0
    $$


    $$
    \begin{cases}
    \cos n \phi = 1 \\
    \sin n \phi = 0
    \end{cases}
    \Rightarrow \phi = \frac{2k\pi}{n} = \frac{k\pi}{3}, 
    k \in \{1, 2, 3, 4, 5, 6\}
    $$

    $$
    z = 
    \begin{cases}
    \cos \frac{\pi}{3} + i \sin \frac{\pi}{3} = \frac{1}{2} + i \frac{\sqrt{3}}{2} & k=1 \\
    \cos \frac{2\pi}{3} + i \sin \frac{2\pi}{3} = -\frac{1}{2} + i \frac{\sqrt{3}}{2} & k=2 \\
    \cos \pi + i \sin \pi = -1 & k=3 \\
    \cos \frac{4\pi}{3} + i \sin \frac{4\pi}{3} = -\frac{1}{2} - i \frac{\sqrt{3}}{2} & k=4 \\
    \cos \frac{5\pi}{3} + i \sin \frac{5\pi}{3} = \frac{1}{2} - i \frac{\sqrt{3}}{2} & k=5 \\
    \cos 2\pi + i \sin 2\pi = 1 & k=6 \\
    \end{cases}
    $$


17. Find $$(1 + i)^{11}$$.
    
    $$
    1+i = \sqrt{2} (\cos \frac{\pi}{4} + i \sin \frac{\pi}{4})
    $$

    $$
    \begin{aligned}
    (1+i)^{11} &= (\sqrt{2})^{11} \left[ \cos \frac{11\pi}{4} + i \sin \frac{11\pi}{4} \right] \\
    &= 32 \sqrt{2} \left[ \cos \frac{3\pi}{4} + i \sin \frac{3\pi}{4} \right] \\
    &= 32 \sqrt{2} \left[ -\frac{1}{\sqrt{2}} + i \frac{1}{\sqrt{2}} \right] \\ 
    &= -32 + 32i
    \end{aligned}
    $$

    

18. Find all the different values of $$\sqrt[3]{1 + i}$$, $$\sqrt[3]{7 - 4i}$$, $$\sqrt[3]{i}$$, $$\sqrt[3]{-i}$$.

    (1).

    $$
    1+i = \sqrt{2} (\cos \frac{\pi}{4} + i \sin \frac{\pi}{4})
    $$

    $$
    \sqrt{1+i} = \sqrt[4]{2} (\cos\frac{\pi}{8} + i \sin \frac{\pi}{8})
    $$

    (2).

    $$
    \sqrt[3]{7-4i} = \sqrt[6]{65} \{\cos [\tan^{-1}(\frac{-4}{7})] + i \sin [\tan^{-1}(\frac{-4}{7})]\}
    $$

    (3).

    $$
    i = \cos \phi + i \sin \phi \quad \phi = \frac{\pi}{2} + 2k\pi
    $$

    $$
    i^{1/3} = \cos \left( \frac{\pi}{6} + \frac{2k\pi}{3} \right) + i \sin \left( \frac{\pi}{6} + \frac{2k\pi}{3} \right), \quad k = 0, 1, 2
    $$

    $$
    \sqrt[3]{i} = \frac{i}{2} + \frac{\sqrt{3}}{2} \quad \text{or} \quad -i \quad \text{or} \quad \frac{i}{2} - \frac{\sqrt{3}}{2}
    $$

    (4).

    $$
    -i = \cos \phi + i \sin \phi \quad \phi = -\frac{\pi}{2} + 2k\pi, \quad k = 0, 1, 2, 3, 4
    $$

    $$
    -i^{1/5} = \cos \left( -\frac{\pi}{10} + \frac{2k\pi}{5} \right) + i \sin \left( -\frac{\pi}{10} + \frac{2k\pi}{5} \right)
    $$

19. Calculate $$\frac{1}{2i} (i^7 - i^{-7})$$.  

    $$
    i^7 = i^4 \cdot i^3 = (i^2)^2 \cdot i^3 = i^3 = -i
    $$

    $$
    i^{-7} = (-i)^7 = (-i)^4\cdot(-i)^3 = (-i)^3 = i
    $$

    Therefore 

    $$
    \frac{1}{2i} (-i - i) = \frac{1}{2i}(-2i)=-1
    $$

<!-- ## Supplement: The Algebra of Sets 
1.  Find a corresponding formula for $$p(A + B + C + D)$$ and apply it to the case of four digits. The corresponding probability is $$\frac{1}{2} = 0.6250$$. -->