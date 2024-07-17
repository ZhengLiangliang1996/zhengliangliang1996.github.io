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


2. Show that every field contains all the rational numbers at least. (Hint: If $$a \neq 0$$ is a number in the field $$F$$ , then $$a/a = 1$$ belongs to F , and from 1 we can obtain any rational number by rational operations.)


3. Ex: From $$p=1+\sqrt{2}, q=2-\sqrt{2}, r=-3+\sqrt{2}$$ obtain the numbers
$$
\frac{p}{q}, \quad p^2, \quad (p-p^2)\frac{q}{r}, \quad \frac{p+qr}{p-r}, \quad \frac{p+r}{q+pr}
$$
in the form $$a+b\sqrt{2}$$.

    $$
    \frac{p}{q} = \frac{1+\sqrt{2}}{2-\sqrt{2}} = \frac{(1+\sqrt{2})(2+\sqrt{2})}{(2-\sqrt{2})(2+\sqrt{2})} = \frac{2+2\sqrt{2}+\sqrt{2}+2}{4-2} = \frac{4+3\sqrt{2}}{2} = 2 + \frac{3\sqrt{2}}{2}
    $$

    $$
    p + p^2 = (1+\sqrt{2}) + (1+\sqrt{2})^2 = (1+\sqrt{2} + 1 + 2\sqrt{2} + 2) = 4 + 3\sqrt{2}
    $$

    $$
    (p-p^2)\frac{q}{r} = \left[(1+\sqrt{2}) - (1+\sqrt{2})^2\right]\frac{2-\sqrt{2}}{-3+\sqrt{2}}
    $$

    $$
    = \left[1+\sqrt{2} - (1+2\sqrt{2} + 2)\right]\frac{2-\sqrt{2}}{-3+\sqrt{2}} = \left[-2-\sqrt{2}\right]\frac{2-\sqrt{2}}{-3+\sqrt{2}}
    $$

    $$
    = \frac{(-2-\sqrt{2})(2-\sqrt{2})}{(-3+\sqrt{2})^2} = \frac{(-2)(2) + (-2)(-\sqrt{2}) + (-\sqrt{2})(2) + (-\sqrt{2})(-\sqrt{2})}{9 - 6\sqrt{2} + 2} = \frac{-4 - 2\sqrt{2} - 2\sqrt{2} + 2}{-7}
    $$

    $$
    = \frac{-4\sqrt{2}}{-7} = \frac{4\sqrt{2}}{7}
    $$

4.  Represent 
    $$
    \frac{\sqrt{k}^3 \cdot \sqrt{1+\sqrt{k}} - \sqrt{k} \cdot \sqrt{1-\sqrt{k}}}{(\sqrt{k})^3 - 3}
    $$
    in the form $$p+q\sqrt{k}$$.

    $$
    \frac{\sqrt{k^3} \left( 1+\sqrt{k} - (1-\sqrt{k}) \right)}{(\sqrt{k})^3 - 3}
    = \frac{\sqrt{k^3} \cdot 2\sqrt{k}}{\sqrt{k^3} - 3}
    = \frac{2k^2 \sqrt{k}}{k^3 - 3}
    = \frac{2 \sqrt{k^3}}{k^3 - 3}
    = \frac{2 \sqrt{k}}{k - \frac{3}{k^2}}
    = \frac{2 \sqrt{k}}{k - \frac{3}{k^2}}
    = \frac{2 \sqrt{k}}{k - \frac{3}{k^2}}
    = \frac{2 \sqrt{k}}{k - \frac{3}{k^2}}
    $$

5. If two segments of lengths $l$ and $a$ are given, give actual constructions for $$1 + a + a^2$$, $$1 + a + a^2 + a^3$$, $$(1+a)^2$$, and $$(1-a)^2$$, $$a^3$$.

    <script type="text/tikz">
    \begin{tikzpicture}
        \draw[thick] (0,0) node[left] {$O$} -- (4,0) node[right] {$A$} -- (3,2) node[above] {$B$} -- cycle;
        \draw[dashed] (0,0) -- (2.5,1) node[above] {$D$} -- (4,0);
        \node at (2.5,1) {$a$};
        \node at (3.5,1) {$1$};
        \node at (1.25,0.5) {$a$};
    \end{tikzpicture}
    </script>
  


## Constructible Number and Number Fields 

