---
giscus_comments: true
layout: post
title: "What is Mathematics: Solution Chapter 3"
date: "2024-07-08"
categories: 
  - "math"
toc:
  sidebar: true
---

## Before the solutions :) 
The solution presented on the blog is my personal solutions for the exercises in the book 'What is Mathematics: An Elementary Approach To Ideas And Methods' by Herbert Robbins and Richard Courant,  please leave a comment if you spot any mistakes or you have questions on the solution. Thanks in advance! 

## Fundamental Geometrical and Algebra 
1. Since $$2^n \rightarrow \infty $$, prove as a consequence that 
$$
\sqrt{2 + \sqrt{2 + \sqrt{2 + \cdots + \sqrt{2}}}}
$$
(with $$ n $$ square roots) converges to 2 as $$ n \rightarrow \infty $$.

    $$
    \begin{align*}
    x &= \sqrt{2 + \sqrt{2 + \sqrt{2 + \cdots}}} \\
    x^2 &= 2 + \sqrt{2 + \sqrt{2 + \sqrt{2 + \cdots}}} \\
    x^2 &= 2 + x
    \end{align*}
    $$

    And we can get x = 2.


2. Show that every field contains all the rational numbers at least. (Hint: If $$a \neq 0$$ is a number in the field $$F$$ , then $$a/a = 1$$ belongs to F , and from 1 we can obtain any rational number by rational operations.)



3. Ex: From $$p=1+\sqrt{2}, q=2-\sqrt{2}, r=-3+\sqrt{2}$$ obtain the numbers
$$
\frac{p}{q}, \quad p^2, \quad (p-p^2)\frac{q}{r}, \quad \frac{p+qr}{p-r}, \quad \frac{p+r}{q+pr}
$$
in the form $$a+b\sqrt{2}$$.


    $$
    \begin{aligned}
    \frac{p}{q} &= \frac{1+\sqrt{2}}{2-\sqrt{2}} \\
    &= \frac{(1+\sqrt{2})(2+\sqrt{2})}{(2-\sqrt{2})(2+\sqrt{2})} \\
    &= \frac{2+2\sqrt{2}+\sqrt{2}+2}{4-2} \\
    &= \frac{4+3\sqrt{2}}{2} \\
    &= 2 + \frac{3\sqrt{2}}{2}
    \end{aligned}
    $$


    $$
    \begin{aligned}
    p + p^2 &= (1+\sqrt{2}) + (1+\sqrt{2})^2 \\ 
    &= (1+\sqrt{2} + 1 + 2\sqrt{2} + 2) \\
    &= 4 + 3\sqrt{2}
    \end{aligned}
    $$


    $$
    \begin{aligned}
    (p-p^2)\frac{q}{r} &= \left[(1+\sqrt{2}) - (1+\sqrt{2})^2\right]\frac{2-\sqrt{2}}{-3+\sqrt{2}} \\
    &= \left[1+\sqrt{2} - (1+2\sqrt{2} + 2)\right]\frac{(2-\sqrt{2})(\sqrt{2}+3)}{(-3+\sqrt{2})(\sqrt{2}+3)} \\
    &= \left[-2-\sqrt{2}\right]\frac{2\sqrt{2}+6-2+3\sqrt{2}}{2-9} \\
    &= \left[-2-\sqrt{2}\right]\frac{4-\sqrt{2}}{-7} \\
    &= \frac{6}{7} + \frac{2\sqrt{2}}{7}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    \frac{pqr}{1+r^2} 
    &= \frac{(1+\sqrt{2})(2-\sqrt{2})(-3+\sqrt{2})}{1+(-3+\sqrt{2})^2} \\
    &= \frac{\sqrt{2}(-3+\sqrt{2})}{1+9-6\sqrt{2}+2} \\
    &= \frac{2-3\sqrt{2}}{12-6\sqrt{2}} \\
    &= \frac{(2-3\sqrt{2})(12+6\sqrt{2})}{(12-6\sqrt{2})(12+6\sqrt{2})} \\
    &= \frac{24+12\sqrt{2}-36\sqrt{2}-36}{144-72} \\
    &= \frac{-12-24\sqrt{2}}{72} \\
    &= -\frac{1}{6}-\frac{1}{3}\sqrt{2} \\ 
    \end{aligned}
    $$

    $$
    \begin{aligned}
    \frac{p+qp}{q+pr^2} 
    &= \frac{(1+\sqrt{2})+(2-\sqrt{2})(-3+\sqrt{2})}{(2-\sqrt{2})+(1+\sqrt{2})(-3+\sqrt{2})^2} \\
    &= \frac{(1+\sqrt{2})+(-6+2\sqrt{2}+3\sqrt{2}-2)}{(2-\sqrt{2})+(1+\sqrt{2})(11-6\sqrt{2})} \\
    &= \frac{-7+6\sqrt{2}}{(2-\sqrt{2})+(5\sqrt{2}-1)}\\
    &= \frac{-7+6\sqrt{2}}{1+4\sqrt{2}} \\
    &= \frac{(-7+6\sqrt{2})(1-4\sqrt{2})}{(1+4\sqrt{2})(1-4\sqrt{2})} \\
    &= \frac{-7+28\sqrt{2}+6\sqrt{2}-48}{1-32} \\
    &= \frac{-55+34\sqrt{2}}{-31} \\
    &= \frac{55}{31}-\frac{34}{31}\sqrt{2}\\
    \end{aligned}
    $$

4.  Represent 
    $$
    (\sqrt{k})^3 , \frac{1+(\sqrt{k})^2}{1+\sqrt{k}} , \frac{\sqrt{2}\sqrt{k}+\frac{1}{\sqrt{2}}}{(\sqrt{k})^3-3}, \frac{(1+\sqrt{k})(2-\sqrt{k})(\sqrt{2}+\frac{1}{\sqrt{k}})}{1+\sqrt{2}k}
    $$
    in the form $$p+q\sqrt{k}$$.

    $$
    (\sqrt{k})^3 = k\sqrt{k}
    $$

    $$
    \begin{aligned}
    \frac{1+(\sqrt{k})^2}{1+\sqrt{k}} &= \frac{(1+k)(1-\sqrt{k})}{(1+\sqrt{k})(1-\sqrt{k})} \\
    &= \frac{1+\sqrt{k}+k-k\sqrt{k}}{1-k}  \\
    &= \frac{1+k}{1-k} - \frac{1+k}{1-k}\sqrt{k}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    \frac{\sqrt{2}\sqrt{k}+\frac{1}{\sqrt{2}}}{(\sqrt{k})^3-3} &= \frac{(\sqrt{2}\sqrt{k} + \frac{\sqrt{2}}{2})(k \sqrt{k} + 3)}{(k \sqrt{k} - 3)(k \sqrt{k} + 3)} \\
    &= \frac{k^2\sqrt{2} + 3\sqrt{2} \sqrt{k} + \frac{\sqrt{2}}{2} k \sqrt{k} + 2 \frac{\sqrt{2}}{2}}{k^3 - 9} \\
    &= \frac{k^2\sqrt{2}}{k^3 - 9} +  \frac{3\sqrt{2} + \frac{\sqrt{2}}{2} k}{k^3 - 9}\sqrt{k}
    \end{aligned}
    $$

    $$
    \begin{aligned}
    \frac{(1+\sqrt{k})(2-\sqrt{k})(\sqrt{2}+\frac{1}{\sqrt{k}})}{1+\sqrt{2}k} &= \frac{(2 - \sqrt{k}+ \sqrt{2k} - \sqrt{k})(\sqrt{2} + \frac{1}{\sqrt{k}})}{1 + \sqrt{2k}} \\
    &= \frac{2 \sqrt{2} + \frac{2 \sqrt{k}}{k}  + 2 \sqrt{k} - 1 + 2\sqrt{k} + \sqrt{2} - \sqrt{2}k - \sqrt{k}}{1 + \sqrt{2k}} \\
    &= \frac{2 \sqrt{2} + \sqrt{k} - \sqrt{2}k - 1}{1 + \sqrt{2}k} + \frac{\frac{2}{k}-\sqrt{2}+1}{1+\sqrt{2}k}\sqrt{k}

    \end{aligned}
    $$


5. If two segments of lengths $l$ and $a$ are given, give actual constructions for $$1 + a + a^2$$, $$1 + a + a^2 + a^3$$, $$(1+a)^2$$, and $$(1-a)^2$$, $$a^3$$.

  
## Constructible Number and Number Fields 

