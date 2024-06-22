---
giscus_comments: true
layout: post
title: "What is Mathematics: Solution Chapter 1"
date: "2024-01-29"
categories: 
  - "general science"
toc:
  sidebar: true
---

### Before the solutions :) 
The solution presented on the blog is my personal solutions for the exercises in the book 'What is Mathematics: An Elementary Approach To Ideas And Methods' by Herbert Robbins and Richard Courant,  please leave a comment if you spot any mistakes in the solution or calculations. Thanks in advance! 

## Chapter 1: The Natural Numbers 

### 1. Calculation with Integers 
1. Set up the addition and multiplication tables in the duodecimal system and work some examples of the same sort.

    The duodecimal system (also known as base 12 or dozenal) is the number system with a base of twelve.


    $$
        \begin{aligned} & \text {Table 1.1. Addition table of Duodecimal }\\ & \begin{array}{c|cccccccccccc}
         & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B \\
        \hline
        1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & 10 \\
        2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & 10 & 11 \\
        3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & 10 & 11 & 12 \\
        4 & 5 & 6 & 7 & 8 & 9 & A & B & 10 & 11 & 12 & 13 \\
        5 & 6 & 7 & 8 & 9 & A & B & 10 & 11 & 12 & 13 & 14 \\
        6 & 7 & 8 & 9 & A & B & 10 & 11 & 12 & 13 & 14 & 15 \\
        7 & 8 & 9 & A & B & 10 & 11 & 12 & 13 & 14 & 15 & 16 \\
        8 & 9 & A & B & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 \\
        9 & A & B & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 \\
        A & B & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 \\
        B & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 1A \\
        \end{array}
        \end{aligned}
    $$
    
    
    $$
        \begin{aligned} & \text{Table 1.2. Multiplication Table} \\\
        & \begin{array}{c|cccccccccccc}
        & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B \\
        \hline
        1 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B \\
        2 & 2 & 4 & 6 & 8 & A & 10 & 12 & 14 & 16 & 18 & 1A \\
        3 & 3 & 6 & 9 & 10 & 13 & 16 & 19 & 20 & 23 & 26 & 29 \\
        4 & 4 & 8 & 10 & 14 & 18 & 20 & 24 & 28 & 30 & 34 & 38 \\
        5 & 5 & A & 15 & 18 & 21 & 26 & 2B & 34 & 39 & 42 & 47 \\
        6 & 6 & 10 & 16 & 20 & 26 & 30 & 36 & 40 & 46 & 50 & 56 \\
        7 & 7 & 12 & 19 & 24 & 2B & 36 & 41 & 48 & 53 & 5A & 65 \\
        8 & 8 & 14 & 20 & 28 & 34 & 40 & 48 & 54 & 60 & 68 & 74 \\
        9 & 9 & 16 & 23 & 30 & 39 & 46 & 53 & 60 & 69 & 76 & 83 \\
        A & A & 18 & 26 & 34 & 42 & 50 & 5A & 68 & 76 & 84 & 92 \\
        B & B & 1A & 29 & 38 & 47 & 56 & 65 & 74 & 83 & 92 & A1 \\
        \end{array}
        \end{aligned}
    $$

2. Express 'thirty' and 'one hundred and thirty-three’ in the systems with the bases 5, 7, 11, 12.

    $$\\
        \begin{aligned}
        & \text{base 5:} & \quad 110, \quad 1013 \\
        & \text{base 7:} & \quad 42, \quad 245 \\
        & \text{base 11:} & \quad 28, \quad 10A \\
        & \text{base 12:} & \quad 26, \quad B1 \\
        \end{aligned}
    \\$$

3. What do the symbols 11111 and 21212 mean in these systems.

    $$\\
        \begin{aligned}
        &\text{Converting } 11111 \text{ from various bases to decimal:} \\
        &\text{Base 5:} \\
        &11111_5 = 1 \cdot 5^4 + 1 \cdot 5^3 + 1 \cdot 5^2 + 1 \cdot 5^1 + 1 \cdot 5^0 \\
        &11111_5 = 1 \cdot 625 + 1 \cdot 125 + 1 \cdot 25 + 1 \cdot 5 + 1 \cdot 1 = 625 + 125 + 25 + 5 + 1 = 781 \\[10pt]
        &\text{Base 7:} \\
        &11111_7 = 1 \cdot 7^4 + 1 \cdot 7^3 + 1 \cdot 7^2 + 1 \cdot 7^1 + 1 \cdot 7^0 \\
        &11111_7 = 1 \cdot 2401 + 1 \cdot 343 + 1 \cdot 49 + 1 \cdot 7 + 1 \cdot 1 = 2401 + 343 + 49 + 7 + 1 = 2801 \\[10pt]
        &\text{Base 11:} \\
        &11111_{11} = 1 \cdot 11^4 + 1 \cdot 11^3 + 1 \cdot 11^2 + 1 \cdot 11^1 + 1 \cdot 11^0 \\
        &11111_{11} = 1 \cdot 14641 + 1 \cdot 1331 + 1 \cdot 121 + 1 \cdot 11 + 1 \cdot 1 = 14641 + 1331 + 121 + 11 + 1 = 16105 \\[10pt]
        &\text{Base 12:} \\
        &11111_{12} = 1 \cdot 12^4 + 1 \cdot 12^3 + 1 \cdot 12^2 + 1 \cdot 12^1 + 1 \cdot 12^0 \\
        &11111_{12} = 1 \cdot 20736 + 1 \cdot 1728 + 1 \cdot 144 + 1 \cdot 12 + 1 \cdot 1 = 20736 + 1728 + 144 + 12 + 1 = 22621 \\[20pt]
        &\text{Converting } 21212 \text{ from various bases to decimal:} \\
        &\text{Base 5:} \\
        &21212_5 = 2 \cdot 5^4 + 1 \cdot 5^3 + 2 \cdot 5^2 + 1 \cdot 5^1 + 2 \cdot 5^0 \\
        &21212_5 = 2 \cdot 625 + 1 \cdot 125 + 2 \cdot 25 + 1 \cdot 5 + 2 \cdot 1 = 1250 + 125 + 50 + 5 + 2 = 1432 \\[10pt]
        &\text{Base 7:} \\
        &21212_7 = 2 \cdot 7^4 + 1 \cdot 7^3 + 2 \cdot 7^2 + 1 \cdot 7^1 + 2 \cdot 7^0 \\
        &21212_7 = 2 \cdot 2401 + 1 \cdot 343 + 2 \cdot 49 + 1 \cdot 7 + 2 \cdot 1 = 4802 + 343 + 98 + 7 + 2 = 5252 \\[10pt]
        &\text{Base 11:} \\
        &21212_{11} = 2 \cdot 11^4 + 1 \cdot 11^3 + 2 \cdot 11^2 + 1 \cdot 11^1 + 2 \cdot 11^0 \\
        &21212_{11} = 2 \cdot 14641 + 1 \cdot 1331 + 2 \cdot 121 + 1 \cdot 11 + 2 \cdot 1 = 29282 + 1331 + 242 + 11 + 2 = 30868 \\[10pt]
        &\text{Base 12:} \\
        &21212_{12} = 2 \cdot 12^4 + 1 \cdot 12^3 + 2 \cdot 12^2 + 1 \cdot 12^1 + 2 \cdot 12^0 \\
        &21212_{12} = 2 \cdot 20736 + 1 \cdot 1728 + 2 \cdot 144 + 1 \cdot 12 + 2 \cdot 1 = 41472 + 1728 + 288 + 12 + 2 = 43502 \\[20pt]
        \end{aligned}
    \\$$


    $$\\
        \begin{aligned}
        &\text{Summary of conversions:} \\[10pt]
        &\begin{array}{|c|c|c|}
        \hline
        \text{Number} & \text{Base} & \text{Decimal Equivalent} \\
        \hline
        11111 & 5 & 781 \\
        11111 & 7 & 2801 \\
        11111 & 11 & 16105 \\
        11111 & 12 & 22621 \\
        \hline
        21212 & 5 & 1432 \\
        21212 & 7 & 5252 \\
        21212 & 11 & 30868 \\
        21212 & 12 & 43502 \\
        \hline
        \end{array}
        \end{aligned}
    $$\\
    

4. Form the addition and multiplication tables for the bases 5, 11, 13.

    $$
    \begin{aligned} & \text{Table 1.3. Addition Table of Base 5} \\
    & \begin{array}{c|ccccc}
        & 0 & 1 & 2 & 3 & 4 \\
    \hline
    0 & 0 & 1 & 2 & 3 & 4 \\
    1 & 1 & 2 & 3 & 4 & 10 \\
    2 & 2 & 3 & 4 & 10 & 11 \\
    3 & 3 & 4 & 10 & 11 & 12 \\
    4 & 4 & 10 & 11 & 12 & 13 \\
    \end{array}
    \end{aligned}

    \begin{aligned} & \text{Table 1.4. Multiplication Table of Base 5} \\
    & \begin{array}{c|ccccc}
    & 0 & 1 & 2 & 3 & 4 \\
    \hline
    0 & 0 & 0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 2 & 3 & 4 \\
    2 & 0 & 2 & 4 & 11 & 13 \\
    3 & 0 & 3 & 11 & 14 & 22 \\
    4 & 0 & 4 & 13 & 22 & 31 \\
    \end{array}
    \end{aligned}

    $$


    $$\\
        \begin{aligned} 
        & \text{Table 1.5. Addition Table: Base 11} \\
        & \begin{array}{c|ccccccccccc}
        & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A \\
        \hline
        0 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A \\
        1 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & 10 \\
        2 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & 10 & 11 \\
        3 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & 10 & 11 & 12 \\
        4 & 4 & 5 & 6 & 7 & 8 & 9 & A & 10 & 11 & 12 & 13 \\
        5 & 5 & 6 & 7 & 8 & 9 & A & 10 & 11 & 12 & 13 & 14 \\
        6 & 6 & 7 & 8 & 9 & A & 10 & 11 & 12 & 13 & 14 & 15 \\
        7 & 7 & 8 & 9 & A & 10 & 11 & 12 & 13 & 14 & 15 & 16 \\
        8 & 8 & 9 & A & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 \\
        9 & 9 & A & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 \\
        A & A & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 \\
        \end{array}
        \end{aligned}
    \\$$

    $$\\
        \begin{aligned} 
        & \text{Table 1.6. Multiplication Table: Base 11} \\
        & \begin{array}{c|ccccccccccc}
        & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A \\
        \hline
        0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
        1 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A \\
        2 & 0 & 2 & 4 & 6 & 8 & A & 11 & 13 & 15 & 17 & 19 \\
        3 & 0 & 3 & 6 & 9 & 11 & 14 & 17 & 1A & 22 & 25 & 28 \\
        4 & 0 & 4 & 8 & 11 & 15 & 19 & 22 & 26 & 2A & 33 & 37 \\
        5 & 0 & 5 & A & 14 & 19 & 23 & 28 & 32 & 37 & 41 & 46 \\
        6 & 0 & 6 & 11 & 17 & 22 & 28 & 33 & 39 & 44 & 4A & 55 \\
        7 & 0 & 7 & 13 & 1A & 26 & 32 & 39 & 45 & 51 & 58 & 64 \\
        8 & 0 & 8 & 15 & 22 & 2A & 37 & 44 & 51 & 59 & 66 & 73 \\
        9 & 0 & 9 & 17 & 25 & 33 & 41 & 4A & 58 & 66 & 74 & 82 \\
        A & 0 & A & 19 & 28 & 37 & 46 & 55 & 64 & 73 & 82 & 91 \\

        \end{array}
        \end{aligned}
    \\$$


    $$\\
        \begin{aligned} 
        & \text{Table 1.7. Addition Table: Base 13} \\
        & \begin{array}{c|ccccccccccccc}
        & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C \\
        \hline
        0 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C \\
        1 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C & 10 \\
        2 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C & 10 & 11 \\
        3 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C & 10 & 11 & 12 \\
        4 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C & 10 & 11 & 12 & 13 \\
        5 & 5 & 6 & 7 & 8 & 9 & A & B & C & 10 & 11 & 12 & 13 & 14 \\
        6 & 6 & 7 & 8 & 9 & A & B & C & 10 & 11 & 12 & 13 & 14 & 15 \\
        7 & 7 & 8 & 9 & A & B & C & 10 & 11 & 12 & 13 & 14 & 15 & 16 \\
        8 & 8 & 9 & A & B & C & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 \\
        9 & 9 & A & B & C & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 \\
        A & A & B & C & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 \\
        B & B & C & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 1A \\
        C & C & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 1A & 1B \\
        \end{array}
        \end{aligned}
    \\$$


    $$\\
        \begin{aligned} 
        & \text{Table 1.8. Multiplication Table: Base 13} \\
        & \begin{array}{c|ccccccccccccc}
        & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C \\
        \hline
        0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
        1 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C \\
        2 & 0 & 2 & 4 & 6 & 8 & A & C & 11 & 13 & 15 & 17 & 19 & 1B \\
        3 & 0 & 3 & 6 & 9 & C & 12 & 15 & 18 & 1B & 21 & 24 & 27 & 2A \\
        4 & 0 & 4 & 8 & C & 13 & 17 & 1B & 22 & 26 & 2A & 31 & 35 & 39 \\
        5 & 0 & 5 & A & 12 & 17 & 1C & 24 & 29 & 31 & 36 & 3B & 43 & 48 \\
        6 & 0 & 6 & C & 15 & 1B & 24 & 2A & 33 & 39 & 42 & 48 & 51 & 57 \\
        7 & 0 & 7 & 11 & 18 & 22 & 29 & 33 & 3A & 44 & 4B & 55 & 5C & 66 \\
        8 & 0 & 8 & 13 & 1B & 26 & 31 & 39 & 44 & 4C & 57 & 62 & 6A & 75 \\
        9 & 0 & 9 & 15 & 21 & 2A & 36 & 42 & 4B & 57 & 63 & 6C & 78 & 84 \\
        A & 0 & A & 17 & 24 & 31 & 3B & 48 & 55 & 62 & 6C & 79 & 86 & 93 \\
        B & 0 & B & 19 & 27 & 35 & 43 & 51 & 5C & 6A & 78 & 86 & 94 & A2 \\
        C & 0 & C & 1B & 2A & 39 & 48 & 57 & 66 & 75 & 84 & 93 & A2 & B1 \\
        \end{array}
        \end{aligned}
    \\$$

5. Exercise: Consider the question of representing integers with the base $a$. In order to name the integers in this system we need words for the digits $$0, 1, \ldots, a - 1$$ and for the various powers of $$a$$: $$a, a^1, a^2, \ldots$$. How many different number words are needed to name all numbers from zero to one thousand, for $$a = 2, 3, 4, 5, \ldots, 15$$? Which base requires the fewest? (Examples: If $$a = 10$$, we need ten words for the digits, plus words for $$10, 100,$$ and $$1000$$, making a total of 13. For $$a = 20$$, we need twenty words for the digits, plus words for $$20$$ and $400$, making a total of 22. If $$a = 100$$, we need 100 plus 1.)
    
    From the description we can easily get the following count by listsing them.

    $$
        \begin{aligned}
        a = 10 & : \quad 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10^1,  10^2, 10^3\\
        a = 11 & : \quad 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, 11^1, 11^2 \\
        a = 20 & : \quad 0, \ldots, R,S, 20^1, 20^2
        \end{aligned}
    $$

    It can be eaily derived that the number of words x needed to name all numbers from 0 to 1000 is number number of a + the maximum power of a that is less or equal to 1000. for 10 that is 3 in $$10^3$$ because $$10^3\leq1000$$.Therefore we can have the formula: 

    $$
        x = a + \lfloor\frac{\log 1000}{\log a}\rfloor
    $$


    {% include figure.liquid loading="eager" path="assets/img/20140616.png.jpg" class="img-fluid rounded z-depth-1" %}


    This shows that 4 uses the fewest words.

### 2. The Infinite of number system, mathematical induction.

Exercise: Prove by mathematical induction

1. $$\frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\cdots+\frac{1}{n(n+1)}=\frac{n}{n+1}$$ . 

    Base Case: For $$n = 1$$,

    $$\frac{1}{1 \cdot 2} = \frac{1}{2}$$

    So, the base case holds.

    Inductive Step: Assume the statement is true for some arbitrary positive integer $$ k $$, i.e.,

    $$\frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \cdots + \frac{1}{k(k+1)} = \frac{k}{k+1}.$$

    Now, we prove it for $$k+1$$:

    $$\frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \cdots + \frac{1}{k(k+1)} + \frac{1}{(k+1)((k+1)+1)} = \frac{k}{k+1} + \frac{1}{(k+1)(k+2)}.
    $$

    To simplify the right-hand side:
    
    $$\begin{aligned}\frac{k}{k+1} + \frac{1}{(k+1)(k+2)} &= \frac{k(k+2) + 1}{(k+1)(k+2)}\\ &= \frac{k^2 + 2k + 1}{(k+1)(k+2)}\\ &= \frac{(k+1)^2}{(k+1)(k+2)}\\ &= \frac{k+1}{k+2}.\end{aligned}$$

    Q.E.D.

2. $$\frac{1}{2}+\frac{2}{2^n}+\frac{3}{2^n}+\cdots+\frac{n}{2^n}=2-\frac{n+2}{2^n}$$.

    Base Case: For $$n = 1$$,

    $$
    \frac{1}{2} = 2 - \frac{1+2}{2^1} = 2 - \frac{3}{2} = \frac{1}{2}.
    $$
    
    So, the base case holds.

    Inductive Step:Assume the statement is true for some arbitrary positive integer $$ k $$ sum denoted as $A_k$
    
    $$
    A_k = \frac{1}{2} + \frac{2}{2^2} + \frac{3}{2^2} + \cdots + \frac{k}{2^2} = 2 - \frac{k+2}{2^k}.
    $$

    Then for sum of $$A_{k+1}$$ is: 

    $$
        \begin{aligned}
            A_{k+1} &= 2 - \frac{k+2}{2^k} + \frac{k+1}{2^{k+1}} \\
            &= 2 - \frac{2k+4}{2^{k+1}} + \frac{k+1}{2^{k+1}} \\
            &= 2 - \frac{k+3}{2^{k+1}}
        \end{aligned}
    $$

    Q.E.D.

3. $$1+2 q+3 q^2+\cdots+n q^{n-1}=\frac{1-(n+1) q^n+n q^{n+1}}{(1-q)^2}$$.

    Base Case: $$ n = 1 $$

    $$
    \frac{1 - 2q + q^2}{(1-q)^2} = \frac{(1-q)^2}{(1-q)^2} = 1.
    $$

    Inductive Step:

    Assume the identity holds for some arbitrary $$ n = k $$:

    $$\\
    1 + 2q + 3q^2 + \cdots + kq^{k-1} = \frac{1 - (k+1)q^k + kq^{k+1}}{(1-q)^2}.
    \\$$

    Now, we need to show it holds for $$ n = k + 1 $$:

    $$\\
    1 + 2q + 3q^2 + \cdots + (k+1)q^k = \frac{1 - ((k+1)+1)q^{k+1} + (k+1)q^{k+2}}{(1-q)^2}.
    \\$$

    To prove this, consider the sum up to $$ k+1 $$:

    $$\\
    1 + 2q + 3q^2 + \cdots + (k+1)q^k = \left( 1 + 2q + 3q^2 + \cdots + kq^{k-1} \right) + (k+1)q^k.
    \\$$

    Using the induction hypothesis:

    $$\\
    1 + 2q + 3q^2 + \cdots + kq^{k-1} = \frac{1 - (k+1)q^k + kq^{k+1}}{(1-q)^2}.
    \\$$

    Therefore,

    $$\\
    \begin{aligned}
    1 + 2q + 3q^2 + \cdots + (k+1)q^k &= \frac{1 - (k+1)q^k + kq^{k+1}}{(1-q)^2} + (k+1)q^k \\
        &=  \frac{1 - (k+1)q^k + kq^{k+1} + (k+1)q^k (1-q)^2}{(1-q)^2} \\
        &= \frac{1 - (k+2) q^{k+1} + (k+1) q^{k+2}}{(1 - q)^2}
    \end{aligned}
    \\$$

    Q.E.D.

4. $$(1+q)\left(1+q^2\right)\left(1+q^4\right) \cdots\left(1+q^{2^n}\right)=\frac{1-q^{2^{n+1}}}{1-q}$$.
    
    Base Case: For $$n=1$$.

    $$
        \begin{aligned}
            (1+q)(1+q^2) &= \frac{1 - q^4}{1 - q} \\
            1 + q^2 + q + q^3 &= \frac{1 - q^4}{1 - q} \\
            (1 + q^2 + q + q^3)(1-q) &= 1-q^4
        \end{aligned}
    $$

    Simpily the left term we have $$1-q^4 = 1-q^4$$. therefore $$n=1$$ is true.

    Assume for n case is correct, for n+1 case: 
    $$
        \begin{aligned}
        (1+q)\left(1+q^2\right)\left(1+q^4\right) \cdots\left(1+q^{2^n}\right)(1+q^{2{n+1}}) 
        &= \frac{1-q^{2^{n+1}}}{1-q}(1+q^{2^{n+1}})\\
        &= \frac{1-q^{2^{n+2}}}{1-q}
        \end{aligned}
    $$

    Q.E.D.

Find sum of the following: 

5. $$\frac{1}{1+x^2}+\frac{1}{\left(1+x^2\right)^2}+\cdots+\frac{1}{\left(1+x^2\right)^n}$$.

    Denote  $$S_n$$ be the sum

    \begin{equation}
    \label{sum_5_1}
    S_n = \frac{1}{1+x^2}+\frac{1}{\left(1+x^2\right)^2}+\cdots+\frac{1}{\left(1+x^2\right)^n}
    \end{equation}

    Construct another sum
    \begin{equation}
    \label{sum_5_2}
    \frac{1}{1+x^2}S_n = \frac{1}{\left(1+x^2\right)^2}+\cdots+\frac{1}{\left(1+x^2\right)^n}+\frac{1}{\left(1+x^2\right)^{n+1}}
    \end{equation}

    By using \eqref{sum_5_1} - \eqref{sum_5_2} we can have 

    $$
    \begin{aligned}
    S_n - \frac{1}{1+x^2}S_n &= \frac{1}{\left(1+x^2\right)}-\frac{1}{\left(1+x^2\right)^{n+1}} \\
    \frac{(1+x^2)S_n-S_n}{1+x^2} &=\frac{1}{\left(1+x^2\right)}-\frac{1}{\left(1+x^2\right)^{n+1}} \\
    \frac{x^2}{1+x^2}S_n &=\frac{1}{\left(1+x^2\right)}-\frac{1}{\left(1+x^2\right)^{n+1}} \\
    Sn &=\frac{1}{x^2} -  \frac{1}{\left(1+x^2\right)^{n}x^2}
    \end{aligned}
    $$

    Thus the sum is:

    $$S_n = \frac{1}{x^2} \left(1 - \frac{1}{(1+x^2)^n}\right)$$

6. $$1+\frac{x}{1+x^2}+\frac{x^2}{\left(1+x^2\right)^2}+\cdots+\frac{x^n}{\left(1+x^2\right)^n}$$.

    we denote the sum by $$ S_{n+1} $$.
    \begin{equation}
    \label{sum_6_1}
    1+\frac{x}{1+x^2}+\frac{x^2}{\left(1+x^2\right)^2}+\cdots+\frac{x^n}{\left(1+x^2\right)^n}
    \end{equation}

    Construct another sum $$\frac{x}{1+x^2}S_{n+1}$$. 
    \begin{equation}
    \label{sum_6_2}
    \begin{aligned}
    1+\frac{x}{1+x^2}+\frac{x^2}{\left(1+x^2\right)^2}+\cdots+\frac{x^n}{\left(1+x^2\right)^n}
    \end{aligned}
    \end{equation}

    By using \eqref{sum_6_1} - \eqref{sum_6_2} we can have 

    $$
    \begin{aligned}
    S_{n+1} - \frac{x}{1+x^2}S_{n+1} &= 1 -\frac{x^n}{\left(1+x^2\right)^{n+1}} \\
    \frac{1+x^2-x}{1+x^2}S_{n+1} &= 1 -\frac{x^n}{\left(1+x^2\right)^{n+1}}  \\
    S_{n+1} &= \frac{1+x^2}{1+x^2-x} - \frac{x^n}{\left(1+x^2\right)^{n+1}}\frac{1+x^2}{1+x^2-x}     \\
    S_{n+1} &= \frac{\left(1+x^2\right)^{n+1}}{(1+x^2-x)(\left(1+x^2\right)^{n})} - \frac{x^{n+1}}{(1+x^2-x)(\left(1+x^2\right)^{n})}
    \end{aligned}
    $$

    Thus, the sum of the series is:

    $$
    S_{n+1} = \frac{\left(1+x^2\right)^{n+1}-x^{n+1}}{(1+x^2-x)(\left(1+x^2\right)^{n})}
    $$


7. $$\frac{x^2-y^2}{x^2+y^2}+\left(\frac{x^2-y^2}{x^2+y^2}\right)^2+\cdots+\left(\frac{x^2-y^2}{x^2+y^2}\right)^n$$.

    The common ratio of the geometric progression is $$q = \frac{x^2-y^2}{x^2+y^2}$$

    Based on the formula of summation for geometric sequence:

    $$
        S_n = a_1\frac{1-q^n}{1-q}
    $$

    By substituting $$q = \frac{x^2-y^2}{x^2+y^2}$$, we can have 

    $$
        S_n = \frac{x^2-y^2}{x^2+y^2}\frac{1-(\frac{x^2-y^2}{x^2+y^2})^n}{1-\frac{x^2-y^2}{x^2+y^2}} \\
    $$



Using formulas (4) and (5) in the book to prove:

8. $$1^2+3^2+\cdots+(2n+1)^2=\frac{(n+1)(2n+1)(2n+3)}{3}$$.
   
   What we've already known: $$1^2+2^2+\cdots+n^2=\frac{n(n+1)(2n+1)}{6}$$.

   If $$S_n$$ is the original progression, notice that each base is odd, we can construct it by using $$2n+1$$ terms and subtract it with the progress where each base is even. 
    
    $$
        \begin{aligned}
        Sn &= [1^2+2^2+\cdots+(2n+1)^2=] - (2^2+4^2+6^2+\cdots+(2n)^2) \\
           &= \frac{(2n+1)(2n+2)(4n+3)}{6} - 2^2[1^2+2^2+\cdots+(n)^2] \\
           &= \frac{(2n+1)(2n+2)(4n+3)}{6} - \frac{4n(n+1)(2n+1)}{3} \\
           &= \frac{(2n+1)(2n+2)(4n+3)}{6} - \frac{2n(2n+2)(2n+1)}{6} \\
           &= \frac{(2n+1)(2n+2)[(4n+3)-2n]}{6}\\
           &= \frac{(n+1)(2n+1)(2n+3)}{3}
        \end{aligned}
    $$

9. $$1^3+3^3+\cdots+(2 n+1)^2=(n+1)^2\left(2 n^2+4 n+1\right)$$.

    Using the same trick as above.

    Known: $$(1^3+2^3+3^3+\cdots+n^3)=[\frac{n(n+1)}{2}]^2$$

    If $$ S_n $$ is the original progression:

    $$
        \begin{aligned}
        S_n &= \left[ 1^3 + 2^3 + \ldots + (2n+1)^3 \right] - \left[ 2^3 + 4^3 + \ldots + (2n)^3 \right]\\
            &= \left[ \frac{(2n+1)(2n+2)}{2} \right]^2 - 2^3 \left[ \frac{n(n+1)}{2} \right]^2\\
            &= \frac{(2n+1)^2 (2n+2)^2}{4} - 2^3 \cdot \frac{n^2 (n+1)^2}{4}\\
            &= (4n^4 + 12n^3 + 13n^2 + 6n + 1) - (2n^4 + 4n^3 + 2n^2)\\
            &= 2n^4 + 8n^3 + 11n^2 + 6n + 1 \\
            &= (n+1)^2\left(2 n^2+4 n+1\right)
        \end{aligned}
    $$

10. Prove the same results directly by mathematical induction.

    To prove $$1^3+3^3+\cdots+(2n+1)^3=\frac{(n+1)(2n+1)(2n+3)}{3}$$.

    Base Case: 
    
    $$
    S_1 = \frac{2 \times 3 \times 5}{3} = 10 \quad \text{True.}
    $$

    Assume $$S_n$$ holds

    $$
    S_n = \frac{(n+1)(2n+1)(2n+3)}{3}
    $$

    For $$S_{n+1}$$

    $$
    \begin{aligned}
    S_{n+1} &= \frac{(n+1)(2n+1)(2n+3)}{3} + (2n+3)^2 \\
    &= \frac{(2n+3)\left[(n+1)(2n+1)+3(2n+3)\right]}{3} \\
    &= \frac{(2n+3)\left[2n^2 + n + 2n + 1 + 6n + 9\right]}{3} \\
    &= \frac{(2n+3)(n+2)(2n+5)}{3} 
    \end{aligned}
    $$

    Q.E.D.


    To prove $$1^2+3^2+\cdots+(2 n+1)^2=(n+1)^2\left(2 n^2+4 n+1\right)$$.

    Base Case: 

    $$
    S_1 = 2^2 (2 + 4 + 1) = 28 \quad \text{True}
    $$

    Assume $$S_n$$ holds

    $$
    S_n = (n+1)^2 (2n^2 + 4n + 1)
    $$

    For $$S_{n+1}$$

    $$
    \begin{aligned}
    S_{n+1} &= (n+1)^2 (2n^2 + 4n + 1) + (2n+1)^3 \\
    &= (n+1)^2 (2n^2 + 4n + 1) + (2n+1)^3\\
    &= (2n^4 + 8n^3 + 12n^2 + 6n + 1)\\
    &= 2n^4 + 8n^3 + 11n^2 + 6n + 1 + (8n^3 + 12n^2 + 6n + 1)\\
    &= 2n^4 + 16n^3 + 23n^2 + 12n + 1\\
    &= \frac{2n^4 + 16n^3 + 23n^2 + 12n + 1}{n^2 + 4n + 4}\\
    \end{aligned}
    $$

### 3. The prime numbers 
1. Exercise: Carry out this construction starting with $$p_1 = 2$$, $$p_2$$= 3 and find 5 more primes
    The construction of proving that prime numbers are infinite is as followed: 
    
    $$
        A = p_1p_2\ldots p_n + 1
    $$

    Based on this constrction, the next 5 primes is 

    $$
    \begin{aligned}
        p_3 &= p_1p_2 + 1 = 7 \\
        p_4 &= p_1p_2p_3 + 1 = 43 \\
        p_5 &= p_1p_2p_3p_4 + 1 = 1807\\
        p_6 &= p_1p_2p_3p_4p_5 + 1 = 3263443 \\ 
        p_7 &= p_1p_2p_3p_4p_5p_6 + 1 = 10650056950807
    \end{aligned}
    $$

    side note: This is the famous [Sylvester's sequence](https://en.wikipedia.org/wiki/Sylvester%27s_sequence)

2. Exercise: In order to find all the divisors of any number a we need only decompose a into a product

    $$a = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_r^{\alpha_r},$$

    where the $$p$$'s are distinct primes, each raised to a certain power. All the divisors of $a$ are the numbers

    $$b = p_1^{\beta_1} p_2^{\beta_2} \cdots p_r^{\beta_r},$$

    where the $$\beta$$'s are any integers satisfying the inequalities

    $$0 \leq \beta_1 \leq \alpha_1, \quad 0 \leq \beta_2 \leq \alpha_2, \quad \cdots, \quad 0 \leq \beta_r \leq \alpha_r.$$

    Prove this statement. As a consequence, show that the number of different divisors of $$a$$ (including the divisors $$a$$ and 1) is given by the product

    $$(\alpha_1 + 1)(\alpha_2 + 1) \cdots (\alpha_r + 1).$$

    For example,

    $$144 = 2^4 \cdot 3^2$$

    has $$5 \cdot 3$$ divisors. They are 1, 2, 4, 8, 16, 3, 6, 12, 24, 48, 9, 18, 36, 72, 144.


    Proof: 

    For the form of b that is divisors of a, every prime $$p_i$$ in a must appear in b with an exponent that is less than or equal to the exponent in a. 
    For example: $$b_1 = p_1^1$$ is a divisor where $$\beta_1$$ is 1 and the rest are 0
    
    Hence, $$0 \leq \beta_i \leq \alpha_i$$.

    To find the total number of distinct divisors, we need to count all possible combinations of the exponents $$\beta_i$$ where $$0 \leq \beta_i \leq \alpha_i$$.

    For each prime $$p_i$$, the exponent $$\beta_i$$ can take any integer value from 0 to $$\alpha_i$$. This gives $$\alpha_i + 1$$ possible values (including 0).

    Since the exponents are independent for different primes, the total number of distinct divisors is the product of the number of choices for each $$\beta_i$$:

    $$
    (\alpha_1 + 1)(\alpha_2 + 1) \cdots (\alpha_r + 1).
    $$

3. Prove the corresponding theorem for the progression $$6n+5$$ that there are infinitely number of primes inside.

    Assume there are only infinit amount of prime numbers inside $$6n+5$$

    Any prime greater than 2 is odd. And all of the odds greater than 2 can be described by
    
    $$
        6n+3, 6n+5, 6n+7
    $$

    Furthermore, the product of 2 numbers of the form $$6n+3$$ and $$6n+7$$ are again of that form
    
    $$
        \begin{aligned}
        (6a+3)(6b+3) = 36ab + 18a + 18b + 9 = 6(6ab+3a+3b+1) + 3
        \end{aligned}
    $$
    $$
        \begin{aligned}
        (6a+7)(6b+7) = 36ab + 42a + 42b + 49 = 6(6ab+7a+7b+7) + 7
        \end{aligned}
    $$

    Construct N where:
    $$
        N = 6(p_1p_2\cdots p_n) - 1 = 6(p_1\cdots p_n - 1) + 5 
    $$

    None of the product from $$p_1$$ to $$p_n$$ could be N's factor since it always remains with 1

    And the factor can not be $$6n+3$$ or $$6n+7$$ because the product of them is still the form of themselves.

    So it can only be 6n+5, which contractdicts with the assumption, therefore there are infinit number of primes inside it.s

    Related proof:  [Dirichlet's theorem](https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions). if gcd(a, b) = 1 in the progression $$an+b$$, then there are infinite number of prime numbers inside. 

### 4. Congruences 
0. Find a similar rule for divisibility by 13.

    For congruences modulo 13 we have: 

    $$
    \begin{aligned}
    10^0 &\equiv 1 \pmod{13} \\
    10^1 &\equiv 10 \pmod{13} \\ 
    10^2 &\equiv 100 \equiv 100 - 7 \cdot 13 \equiv 100 - 91 \equiv 9 \pmod{13}\\ 
    10^3 &\equiv 10 \cdot 10^2 \equiv 10 \cdot 9 \equiv 90 \equiv 90 - 7 \cdot 13 \equiv 90 - 91 \equiv -1 \equiv 12 \pmod{13}\\
    10^4 &\equiv 10 \cdot 10^3 \equiv 10 \cdot 12 \equiv 120 \equiv 120 - 9 \cdot 13 \equiv 120 - 117 \equiv 3 \pmod{13} \\
    10^5 &\equiv 10 \cdot 10^4 \equiv 10 \cdot 3 \equiv 30 \equiv 30 - 2 \cdot 13 \equiv 30 - 26 \equiv 4 \pmod{13} \\
    10^6 &\equiv 10 \cdot 10^5 \equiv 10 \cdot 4 \equiv 40 \equiv 40 - 3 \cdot 13 \equiv 40 - 39 \equiv 1 \pmod{13} \\
    \end{aligned}
    $$

    the successive remainders then repeat,
    for the expression 
    
    $$
        z = a_0 + a_110 + a2_10^2 + \cdots + a_n10^n 
    $$

    z is divisible by 13 if the following expression is divisible by 13.

    $$
        r = a_0 + 10a_1 + 9a_2 + 12a_3 + 3a_4 + 4a_5 + a_6 + \cdots
    $$

0. Show that the following law of cancellation holds for congruences with respect to a prime modulus: If $$ab \equiv ac$$ and $$a\not\equiv0$$, then $$b \equiv c$$.

    Using law of subtraction:

    $$
    \begin{aligned}
    ab-ac \equiv 0 \pmod{p} \\
    a(b-c) \equiv 0 \pmod{p}
    \end{aligned}
    $$

    By applying the law 7 stated in the book, since $$a\not\equiv0 \pmod{p}$$, therefore 

    $$(b-c) \equiv 0 \pmod{p}$$
    
    which leads to 

    $$b 
    \begin{aligned}
    \equiv c \pmod{p}
    \end{aligned}
    $$.

    Q.E.D.

1. To what number between 0 and 6 inclusive is the product $$11\times 18\times 2322\times 13\times 19$$ congruent modulo 7?
    By computing the smaller congruences from the factors in the product.

    $$
    \begin{aligned}
        11 \equiv 4 \pmod{7} \\
        18 \equiv 4 \pmod{7} \\ 
        2322 \equiv 5 \pmod{7} \\
        13 \equiv 6 \pmod{7} \\
        19 \equiv 5 \pmod{7} \\
    \end{aligned}
    $$

    Then we have $$11\times 18\times 2322\times 13\times 19 \equiv 4\times 4\times 5\times 6\times 5 \pmod{7}$$

    $$
    \begin{aligned}
    4\times 4 \equiv 2 \pmod{7} \\
    5\times 6 \equiv 2 \pmod{7} \\
    \end{aligned}
    $$

    Therefore we have $$2\times 2 \times 5 \equiv 6\pmod{7}$$, 6 the congruence of the product.

2. To what number between 0 and 12 inclusive is $$3\cdot7\cdot11\cdot17\cdot19\cdot23\cdot29\cdot113$$ congruent modulo 13?
    By computing the smaller congruences from the factors in the product.

    $$
        \begin{aligned}
        17 \equiv 4 \pmod{13} \\
        19 \equiv 6 \pmod{13} \\ 
        23 \equiv 10 \pmod{13} \\
        29 \equiv 3 \pmod{13} \\
        113 \equiv 9 \pmod{13} \\
        \end{aligned}
    $$

    To furthur make it smaller 

    $$
        \begin{aligned}
        3\times 7 \equiv 8 \pmod{13} \\
        11\times 4 \equiv 5 \pmod{13} \\
        6\times 10 \equiv 8 \pmod{13} \\
        3\times 9 \equiv 1 \pmod{13} \\
        \end{aligned}
    $$


    Therefore we have $$9\times 8 \times 5 \times 8 \equiv 8 \pmod{13}$$, 8 is the congruence of the product.


3. To what number between 0 and 4 inclusive is the sum $$1 + 2 + 2^2 +\cdots +2^{19} $$ congruent modulo 5?

    We can observe from the following that the form 1,2,4,3 is repeated for the congruence in each term.

    $$
        \begin{aligned}
        1 \equiv 1 \pmod{5} \\
        2 \equiv 2 \pmod{7} \\ 
        2^2 \equiv 4 \pmod{5} \\
        2^3 \equiv 3 \pmod{5} \\
        2^4 \equiv 1 \pmod{5} \\
        2^5 \equiv 2 \pmod{5} \\
        \cdots 
        \end{aligned}
    $$

    Therefore the original sum can be rewritten as: 

    $$1 + 2 + 4 + 3 + \cdots  $$

    There are 20 terms inside, for every 4 terms $$1+2+4+3 \equiv 0 \pod{5}$$, so the congrence is 0.

4. Show by similar computation that 

    $$
    \begin{align*}
    2^8 &\equiv 1 \pmod{17}; \\
    3^8 &\equiv -1 \pmod{17}; \\
    3^{14} &\equiv \pmod{29}; \\
    2^{14} &\equiv -1 \pmod{29}; \\
    4^{14} &\equiv 1 \pmod{29}; \\
    5^{14} &\equiv 1 \pmod{29}\\
    \end{align*}
    $$

    $$
        \begin{aligned}
        2^8 &\equiv 2^4 \cdot 2^4 \equiv (-1)\cdot(-1) \equiv 1 \pmod{17} \\
        3^8 &\equiv 3^4 \cdot 3^4 \cdot (-4)\cdot(-4) \equiv -1 \pmod{17} \\
        3^{14} &\equiv 3^4 \cdot 3^4 \cdot 3^4 \cdot 3^2 \equiv (-6) \cdot (-6) \cdot(-6) \cdot(9) \\
               &\equiv 7 \cdot 9 \cdot (-6)  \equiv -1 \pmod{29} \\
        2^{14} &\equiv 2^5 \cdot 2^5 \cdot 2^4 \equiv 3 \cdot 3 \cdot 16 \equiv 28 \equiv -1 \pmod{29} \\
        4^{14} &\equiv 4^3 \cdot 4^3 \cdot 4^3 \cdot 4^3 \cdot 4^2 \equiv 6 \cdot 6 \cdot 6 \cdot 6 \cdot 16 \equiv 1  \pmod{29} \\
        5^{14} &\equiv 5^2 \cdot 5^4 \cdot 5^8 \equiv 4 \cdot 16 \dot 24 \equiv 1 \pmod{29} \\
        \end{aligned}
    $$

5. Check Fermat's theorem for p = 5, 7, 11, 17, and 23 with different values of a.

    For a = 3 

    $$
        \begin{aligned}
        3^4 &\equiv 3^2 \cdot 3^2 \equiv 9 \cdot 9 \equiv 4 \cdot 4 \equiv 1 \pmod{5} \\
        3^6 &\equiv 3^2 \cdot 3^2 \cdot 3^2 \equiv 2 \cdot 2\cdot 2 \equiv 1 \pmod{7} \\
        3^{10} &\equiv 3^2 \cdot 3^4 \cdot 3^4 \equiv 9 \cdot 4 \cdot 4 \equiv 1 \pmod{11} \\
        3^{16} &\equiv 3^4 \cdot 3^4 \cdot 3^4 \cdot 3^4 \equiv 13^4 \equiv 1 \pmod{17}\\
        3^{22} &\equiv 3^8 \cdot 3^8 \cdot 3^4 \cdot 3^2 \equiv (-6) \cdot (-6) \cdot 12 \cdot 9 \equiv 1 \pmod{23}\\
        \end{aligned}
    $$

6. Prove the general theorem: The smallest positive integer e for which $$a^e \equiv 1 \pmod{p}$$ must be a divisor of p-1. (Hint: Divide p — 1 by e, obtaining:

    $$
        p-1 = ke + r
    $$

    where $$0 < r < e$$, and use the fact that $$a^{p-1} \equiv a^e \equiv 1 \pmod{p}$$ )

    Proof: 
    Based on Fermat's Little theorem, we have 
    $$
    a^{p-1} \equiv 1 \pmod{p}
    $$

    Dividing p-1 by e and obtain: 

    $$
    p-1 = ke + r
    $$

    where k is the quotient, r is the remainder, $$0 \leq r < e $$.

    Substitute it in the Fermat's Little theorem

    $$
    a^{p-1} = a^{ke + r} \equiv 1 \pmod{p}
    $$

    Simplify using the fact that $$ a^e \equiv 1 \pmod{p}$$ :

    $$
    (a^e)^k \equiv 1^k \equiv 1 \pmod{p}
    $$

    Therefore,

    $$
    a^{ke + r} \equiv 1 \cdot a^r \equiv a^r \pmod{p}
    $$
    
    And this implies 

    $$
    a^r \equiv 1 \pmod{p}
    $$

    r can only be 0 because e  is defined as the smallest positive integer for which $$0 \leq r < e$$

    Therefore,  r  must be 0, meaning:

    $$
    p-1 = ke
    $$

    Q.E.D.


### 5. Pythegorean Numbers and Fermat's Last Theorem 

1. $$6^2 = 36 \equiv 13 pmod{23}$$. Is 23 a quadratic residue (mod 13)?

2. 2. We have seen that $$ x^2 \equiv (p - x)^2 \pmod{p} $$. Show that these are the only congruences among the numbers $$ 1^2, 2^2, 3^2, \ldots, (p - 1)^2 $$.


### 6. The Euclidean Algorithm 

1. *Bxercite: Prove the last statement

10. Exercise : Find the continued fraction developments of

11. Solve the Diophantine equations (a) 3x — \y = 29. (b)llx 4* 12 y = 58. (c) 153s - 34 y = 51