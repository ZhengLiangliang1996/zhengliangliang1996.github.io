---
giscus_comments: true
tikzjax: true
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


5. If two segments of lengths $$1$$ and $$a$$ are given, give actual constructions for $$1 + \alpha + \alpha^2$$, $$(1+\alpha)/(1-\alpha)$$, $$\alpha^3$$.

    $$5.1$$: To construct $$1 + a + a^2$$, first let's assume $$\alpha>1$$ first construct 1 as OA, then extend from A to B with length $$\alpha$$, therefore we have $$1+\alpha$$.

    the next is to construct $$\alpha^2$$. We first construct a right triangle OCD, where angle OCD is right angle, OC is 1, and OD is $$\alpha$$, and then extend OC to OA, the length of OA is $$\alpha$$, then construct a line from A that is perpendicular to OA, exten OD and the line will intersect with previouly contsructed line on point B. then obviously we have $$\triangle OCD \sim \triangle OAB$$.
          
    Therefore we can eaisly have the ratio equation that is $$\frac{OC}{OA}=\frac{OD}{OB}$$, where we can see OB is $$\alpha^2$$, using compass we then can construct another extension on the basis of $$1+\alpha$$ and get $$1 + a + a^2$$.
    
    $$5.2$$: To construct $$(1+\alpha)/(1-\alpha)$$, first let's assume $$0<\alpha<1$$construct $$1+\alpha$$, using the same way as described in 5.1, and then construct $$1-\alpha$$ by constructing unit length 1 OA and OB with length $$\alpha$$, then we can get $$1-\alpha$$

    Then we construct right triangle, first one side is $$OB=1+\alpha$$, and another side OA with length $$1-\alpha$$ which is perpendicular to AB, then we construct OC which is $$1$$, from point C construct a line CD that is parallel to CD. then we can get $$\triangle OAB \sim \triangle OCD$$.

    Therefore we can eaisly have the ratio equation that is $$\frac{OD}{OB}=\frac{OC}{OA}$$, which we can gete $$\frac{OD}{1+\alpha}=\frac{1}{1-\alpha}$$, then we can get OD is $$(1+\alpha)/(1-\alpha)$$.

    $$5.3$$: To construct $$\alpha^3$$, construct $$\alpha^2$$ by using the step in 5.1 and then construct $$\alpha^3$$ by using the same way using triangle similarity $$\triangle OCD \sim \triangle OAB$$.

6.  The lines $$x + \sqrt{2}y - 1 = 0$$, $$2x - y + \sqrt{2} = 0$$, have coefficients in the field $$ a + b\sqrt{2} $$.
Calculate the coordinates of their point of intersection, and verify that these have the form $$ a + b\sqrt{2} $$. Join points $$(1, \sqrt{2})$$ and $$(\sqrt{2}, 1 - \sqrt{2})$$ by a line $$ ax + by + c = 0 $$, and verify that the coefficients are of the form $$ a + b\sqrt{2} $$. Same with respect to field $$ p + q\sqrt{k} $$ for the lines $$ \sqrt{(1+\sqrt{2})x} + \sqrt{2} y = 1 $$, $$(1+\sqrt{2})x - y = 1 - \sqrt{1+\sqrt{2}} $$, and the points $$ (\sqrt{2}, -1) $$, $$(1+\sqrt{2}, \sqrt{1+\sqrt{2}})$$ respectively.

    To find intersection:
    
    $$
      \begin{cases}
          x + \sqrt{2}y - 1 &= 0 \\
          2x - y + \sqrt{2} &= 0
      \end{cases}
    $$
    
      Easily get:

    $$
      \begin{cases}
          x &= \frac{7}{7} - \frac{3}{7} \sqrt{2} \\
          y &= \frac{2}{7} + \frac{3}{7} \sqrt{2}
      \end{cases}
    $$

    And they are both in the filed of $$ a + b\sqrt{2} $$.
      
    Join 2 points $$(1, \sqrt{2})$$ and $$(\sqrt{2}, 1-\sqrt{2})$$, The line is $$ ax + b = y $$. Then we can have: 

    $$
      \begin{cases}
          a + b &= \sqrt{2} \\
          \sqrt{2} a + b &= 1 - \sqrt{2}
      \end{cases}
    $$

    Easily get:

    $$
      \begin{align*}
          a &= -3 + \sqrt{2} \\
          b &= 3 + \sqrt{2}
      \end{align*}
    $$
    
    And they are both in the form of $$ a + b\sqrt{2} $$.
      
    To find intersection of:

    $$
      \begin{cases}
          (1 + \sqrt{2})x + \sqrt{2} y &= 1 \\
          (1 + \sqrt{2})x - y &= 1 - (1 + \sqrt{2})
      \end{cases}
    $$

    Say $$k=1+\sqrt{2}$$

    $$
      \begin{cases}
          \sqrt{(k-1)x+1} + \sqrt{2}y &= 1 \\
          kx-y&=1-\sqrt{k}
      \end{cases}
    $$

      Then we can get 

    $$
      \begin{cases}
          x &= \\
          y &= 
      \end{cases}
    $$

    Which are in the form of $$p+q\sqrt{k}$$

    Join $$(\sqrt{2}, -1)$$, $$(1+\sqrt{2}, \sqrt{1+\sqrt{2}})$$, with $$ k = 1+\sqrt{2} $$:

    $$
      \begin{cases}
          \sqrt{2} a + b &= -1 \\
          k a + b &= \sqrt{2} k
      \end{cases}
    $$

      Say $$ k=1+\sqrt{2}$$ Easily get:

    $$
      \begin{cases}
          a &= \frac{-1 - \sqrt{k}}{\sqrt{2} - k} \\
          b &= \frac{-1  \sqrt{k}}{\sqrt{2} - k}\sqrt{2}+1
      \end{cases}
    $$

      which is of the form $$ p + q\sqrt{k} $$.


7.  Let $$F$$ be the field $$ p + q\sqrt{2 + \sqrt{2}}$$, where p and q are of the form $$ a + b\sqrt{2}$$, a, b rational. Represent $$\frac{1 + \sqrt{2 + \sqrt{2}}}{2 - 3\sqrt{2 + \sqrt{2}}}$$ in this form.


    Say $$ k = 2 + \sqrt{2} $$, we can get:

    $$
    \frac{1 + \sqrt{k}}{2 - 3k}
    $$

    Rewriting:

    $$
    \frac{(1 + \sqrt{k})}{(2 - 3\sqrt{k})}
    $$

    Multiplying numerator and denominator by $$ (2 + 3\sqrt{k}) $$:

    $$
    \frac{(1 + \sqrt{k})(2 + 3\sqrt{k})}{(2 - 3\sqrt{k})(2 + 3\sqrt{k})}
    $$

    Expanding:

    $$
    \frac{2 + 5\sqrt{k} + 3k}{4 - 9k}
    $$

    $$
    = \frac{2 + 3k}{4 - 9k} + \frac{5}{4 - 9k} \cdot \sqrt{k}
    $$

    Therefore it is the form of field $$p+q\sqrt{2+\sqrt{2}}$$


8. Consider the circle with radius $$2\sqrt{2}$$ about the origin, and the line joining the points $$ (\frac{1}{2}, 0) $$, $$ (4\sqrt{2}, \frac{\sqrt{2}}{2}) $$. Find the field $$ F' $$ determined by the coordinates of intersection of the circle and the line. Do the same with respect to the intersection of the given circle with the circle with radius $$ \frac{\sqrt{2}}{2} $$ and center $$ (0, 2\sqrt{2}) $$.

    $$8.1$$: Say the line is $$ ax + b = y $$,

    $$
    \begin{cases}
    \frac{1}{2} a + b = 0, \\
    4\sqrt{2} a + b = \frac{\sqrt{2}}{2}.
    \end{cases}
    $$

    Easily get the equation of the line,

    $$
    \left( \frac{32}{127} + \frac{2\sqrt{2}}{127} \right) x - \frac{16}{127} - \frac{\sqrt{2}}{127} = y. \quad 
    $$

    The equation of the circle is

    $$
    x^2 + y^2 = 8.
    $$

    With (1) and (2), we get

    $$
    x^2 + \left[ \left( \frac{32}{127} + \frac{2\sqrt{2}}{127} \right) x - \frac{16}{127} - \frac{\sqrt{2}}{127} \right]^2 = 8.
    $$

    By calculating it we can get: 

    $$
    \begin{cases}
      x_1 &= \frac{548 + 64 \sqrt{2} - \sqrt{2501773094 - 19209248 \sqrt{2}}}{18257}\\
      y_1 &= (-16/2318639 - \sqrt{2}/2318639) (17161 - 128 \sqrt{2} + 2 \sqrt{2501773094 - 19209248 \sqrt{2}}) \\
      x_2 &= \frac{548 + 64 \sqrt{2} - \sqrt{2501773094 - 19209248 \sqrt{2}}}{18257} \\
      y_2 &= (16/2318639 + \sqrt{2}/2318639) (-17161 + 128 \sqrt{2} + 2 \sqrt{2501773094 - 19209248 \sqrt{2}}) \\
    \end{cases}
    $$

    Therefore the field extension F is needed to accommodate these two values is 
    
    $$F = \mathbb{Q}(\sqrt{2}, \sqrt{2501773094 - 19209248 \sqrt{2}})$$

    $$ y $$ can be gained by the coefficient with $$\sqrt{2}$$ therefore $$y$$ is also in the same filed $$ F $$. 

    $$8.2$$: For the circle with radius $$ \frac{\sqrt{2}}{2} $$ and center $$ (0, 2\sqrt{2}) $$. 

    $$
    \begin{cases}
      C_1 &= x^2 + y^2 = 8 \\
      C_2 &= x^2 + (y-2\sqrt{2})^2 = \frac{1}{2}
    \end{cases}
    $$

    Therefore we can get: 

    $$
    \begin{cases}
      x_1 &= \frac{-3 \sqrt{\frac{7}{2}}}{8} \\
      y_1 &= \frac{31}{8 \sqrt{2}}\\
      x_2 &= \frac{3 \sqrt{\frac{7}{2}}}{8} \\
      y_1 &= \frac{31}{8 \sqrt{2}}
    \end{cases}
    $$

    The field is $$F = \mathbb{Q}(\sqrt{2}, \sqrt{7})$$
    


9. Verify that, starting with the rational field, the side of the regular $$2^m$$-gon is a constructible number, with $$n = m - 1$$. Determine the sequence of extension fields. Do the same for the numbers:
    $$
      \begin{align*}
          &\sqrt{1+ \sqrt{2}+ \sqrt{3} + \sqrt{5}}, \\
          &\frac{(\sqrt{5} + 11)}{(1+\sqrt{7-\sqrt{3}})} \\
          &(\sqrt{2} + 3)(\sqrt[3]{2} + \sqrt{1+\sqrt{2+\sqrt{5}}} + \sqrt{3-\sqrt{7}})
      \end{align*}
    $$


      The side of a regular $$2^m$$-gon is given as:
    $$
      \begin{equation*}
          2^n \cdot \sqrt{2+\sqrt{2+\sqrt{2+\dots+\sqrt{2}}}}
      \end{equation*}
    $$

    where there are $$n$$ square roots.

    Starting with the rational field $F_0$, let $k_0 = 2$, obtaining:
    $$
    \begin{equation*}
        F_1 = 2 + \sqrt{2}.
    \end{equation*}
    $$
    Similarly, setting $$k_1 = \sqrt{2 + \sqrt{2}}$$, we obtain $$F_2$$, and continuing this process iteratively $n$ times, we reach the desired expression.

    Since $$2^n$$ is inside the field $F_n$ by a product of $2$, the number is constructible.


    Let $$F_0$$ denote the rational field.
    $$
    \begin{align*}
        &F_0: \text{rational numbers}, \\
        &k_0 = 2 \Rightarrow F_1 = 1 + \sqrt{2}, \\
        &k_1 = \sqrt{3} \Rightarrow F_2 = 1 + \sqrt{2} + \sqrt{3}, \\
        &k_2 = 3 \Rightarrow F_3 = 1 + \sqrt{2} + \sqrt{3} + \sqrt{5}.
    \end{align*}
    $$

    Thus, continuing this extension process, we obtain a constructible number.

    Find the equations with rational coefficients for:
    $$
    \begin{cases}
        x &= \sqrt{2} + \sqrt{3} \\
        x &= \sqrt{2} + \sqrt{3}\\
        x &= \frac{1}{\sqrt{5} + \sqrt{3}} \\
    \end{cases}
    $$

    For example, considering $$x = \sqrt{2} + \sqrt{3}$$:

    $$
    \begin{equation*}
        x^2 = 2 + 2\sqrt{6} + 3 = 5 + 2\sqrt{6}.
    \end{equation*}
    $$

    Squaring again:
    $$
    \begin{equation*}
        (x^2 - 5)^2 = 24 \Rightarrow x^4 - 10x^2 + 25 = 24.
    \end{equation*}
    $$

    Rearrange:
    $$
    \begin{equation*}
        x^4 - 10x^2 + 1 = 0.
    \end{equation*}
    $$


10. To prove the theorem for $$x$$ in a field $F_k$ with arbitrary $$k$$, we use induction. The goal is to show $$x$$satisfies an equation of degree $$2^k$$ with coefficients in $$F_k$$. The statement for $$k=l$$ completes the proof.


## Constructible Number and Number Fields 

