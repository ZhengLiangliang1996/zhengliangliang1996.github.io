---
giscus_comments: true
tikzjax: true
layout: post
title: "What is Mathematics: Solution Chapter 4"
date: "2025-04-08"
categories: 
  - "math"
toc:
  sidebar: true
---

## Before the solutions :) 
The solution presented on the blog is my personal solutions for the exercises in the book 'What is Mathematics: An Elementary Approach To Ideas And Methods' by Herbert Robbins and Richard Courant,  please leave a comment if you spot any mistakes or you have questions on the solution. Thanks in advance! 

## Projective Geometry 

That the cross-ratio of four points remains unchanged by a *parallel* projection follows from elementary properties of similar triangles. The proof is left to the reader as an exercise.

<figure class="tikz-figure">
<script type="text/tikz">
\begin{tikzpicture}[scale=1.75, line width=0.7pt,
                    dot/.style={circle,fill=black,inner sep=0pt,minimum size=3pt},
                    foot/.style={circle,fill=red,inner sep=0pt,minimum size=3pt},
                    perp/.style={red,dashed,line width=0.9pt}]
  % the two transversals, which just fail to meet inside the picture
  \draw (1.815,3.30) -- (-0.3025,-0.55);
  \draw (1.960,3.30) -- (5.0400,-0.55);
  \node[below left] at (-0.3025,-0.55) {$l$};
  \node[below right] at (5.04,-0.55) {$l'$};
  % the four parallel rays of the projection, all bound for infinity
  \draw[->] (1.65,3) -- (5.6,3);
  \draw[->] (1.10,2) -- (5.6,2);
  \draw[->] (0.55,1) -- (5.6,1);
  \draw[->] (0.00,0) -- (5.6,0);
  % the four points on l and their four images on l'
  \node[dot,label=above left:$A$] at (1.65,3) {};
  \node[dot,label=above left:$B$] at (1.10,2) {};
  \node[dot,label=above left:$C$] at (0.55,1) {};
  \node[dot,label=above left:$D$] at (0.00,0) {};
  \node[dot,label=above right:$A'$] at (2.20,3) {};
  \node[dot,label=above right:$B'$] at (3.00,2) {};
  \node[dot,label=above right:$C'$] at (3.80,1) {};
  \node[dot,label=above right:$D'$] at (4.60,0) {};
  % brace gathering the rays at their common point at infinity
  \draw (5.85,3.25) .. controls (6.2,3.25) and (5.95,2.05) .. (6.3,1.5)
                    .. controls (5.95,0.95) and (6.2,-0.25) .. (5.85,-0.25);
  \node[right] at (6.4,1.5) {$\infty$};
\end{tikzpicture}
</script>
<figcaption>Invariance of cross-ratio under parallel projection.</figcaption>
</figure>

**Solution.**

### Setting

The projecting lines $$AA'$$, $$BB'$$, $$CC'$$, $$DD'$$ are parallel — that is what it means for the centre of projection to lie at infinity. Neither $$l$$ nor $$l'$$ is parallel to them, or the projection would not be defined. Let $$\theta$$ be the angle between $$l$$ and that common direction and $$\theta'$$ the angle for $$l'$$; both lie in $$(0^\circ,90^\circ]$$, so $$\sin\theta>0$$ and $$\sin\theta'>0$$.

### The construction

A line perpendicular to one projecting line is perpendicular to all four. Draw it through $$A$$: it meets $$BB'$$, $$CC'$$, $$DD'$$ at $$O$$, $$O'$$, $$O''$$. Draw it through $$A'$$: it meets them at $$P$$, $$P'$$, $$P''$$.

<figure class="tikz-figure">
<script type="text/tikz">
\begin{tikzpicture}[scale=1.75, line width=0.7pt,
                    dot/.style={circle,fill=black,inner sep=0pt,minimum size=3pt},
                    foot/.style={circle,fill=red,inner sep=0pt,minimum size=3pt},
                    perp/.style={red,dashed,line width=0.9pt}]
  % the two transversals, which just fail to meet inside the picture
  \draw (1.815,3.30) -- (-0.3025,-0.55);
  \draw (1.960,3.30) -- (5.0400,-0.55);
  \node[below left] at (-0.3025,-0.55) {$l$};
  \node[below right] at (5.04,-0.55) {$l'$};
  % the four parallel rays of the projection, all bound for infinity
  \draw[->] (1.65,3) -- (5.6,3);
  \draw[->] (1.10,2) -- (5.6,2);
  \draw[->] (0.55,1) -- (5.6,1);
  \draw[->] (0.00,0) -- (5.6,0);
  % the two perpendiculars, one through A and one through A'
  \draw[perp] (1.65,3) -- (1.65,0);
  \draw[perp] (2.20,3) -- (2.20,0);
  \node[foot] at (1.65,2) {};
  \node[foot] at (1.65,1) {};
  \node[foot] at (1.65,0) {};
  \node[foot] at (2.20,2) {};
  \node[foot] at (2.20,1) {};
  \node[foot] at (2.20,0) {};
  \node[red,above left] at (1.65,2) {$O$};
  \node[red,above left] at (1.65,1) {$O'$};
  \node[red,above left] at (1.65,0) {$O''$};
  \node[red,above right] at (2.20,2) {$P$};
  \node[red,above right] at (2.20,1) {$P'$};
  \node[red,above right] at (2.20,0) {$P''$};
  % the angle each transversal makes with the direction of projection
  \draw (0.55,0) arc (0:61.2:0.55);
  \node at (0.675,0.39) {$\theta$};
  \draw (4.256,0.429) arc (128.7:180:0.55);
  \node at (3.881,0.351) {$\theta'$};
  % the four points on l and their four images on l'
  \node[dot,label=above left:$A$] at (1.65,3) {};
  \node[dot,label=above left:$B$] at (1.10,2) {};
  \node[dot,label=above left:$C$] at (0.55,1) {};
  \node[dot,label=above left:$D$] at (0.00,0) {};
  \node[dot,label=above right:$A'$] at (2.20,3) {};
  \node[dot,label=above right:$B'$] at (3.00,2) {};
  \node[dot,label=above right:$C'$] at (3.80,1) {};
  \node[dot,label=above right:$D'$] at (4.60,0) {};
  % brace gathering the rays at their common point at infinity
  \draw (5.85,3.25) .. controls (6.2,3.25) and (5.95,2.05) .. (6.3,1.5)
                    .. controls (5.95,0.95) and (6.2,-0.25) .. (5.85,-0.25);
  \node[right] at (6.4,1.5) {$\infty$};
\end{tikzpicture}
</script>
<figcaption>One perpendicular through A and one through A', each cutting the three other projecting lines. Corresponding segments on the two perpendiculars are equal, because they are cut off by the same pairs of parallel lines.</figcaption>
</figure>

### Step 1: the two perpendiculars carry equal segments

$$
\begin{aligned}
AO   &= A'P, \\
AO'  &= A'P', \\
AO'' &= A'P'' .
\end{aligned}
$$

Indeed $$AA'\parallel BB'$$, and the two are distinct: were $$A$$ on $$BB'$$, then $$A$$ and $$B$$ would both lie on $$BB'$$ and on $$l$$, forcing $$l=BB'$$ and making $$l$$ parallel to the projection. Distinct parallels are everywhere equidistant, so every point of $$AA'$$ — in particular $$A$$ and $$A'$$ — is that one distance from $$BB'$$, and those distances are $$AO$$ and $$A'P$$. The pairs $$(AA',CC')$$ and $$(AA',DD')$$ give the other two lines. Subtracting:

$$
\begin{aligned}
OO'  &= AO'  - AO = A'P'  - A'P = PP' , \\
OO'' &= AO'' - AO = A'P'' - A'P = PP'' .
\end{aligned}
$$

### Step 2: three similar right triangles on each side

$$ABO$$, $$ACO'$$, $$ADO''$$ are right-angled at $$O$$, $$O'$$, $$O''$$, with hypotenuse along $$l$$ and one leg along a projecting line; so each carries the angle $$\theta$$ at $$B$$, $$C$$, $$D$$ — or its supplement, which has the same sine. Reading off the opposite leg:

$$
\begin{aligned}
AO   &= AB\,\sin\theta, \\
AO'  &= AC\,\sin\theta, \\
AO'' &= AD\,\sin\theta .
\end{aligned}
$$

The triangles $$A'B'P$$, $$A'C'P'$$, $$A'D'P''$$ stand the same way against $$l'$$:

$$
\begin{aligned}
A'P   &= A'B'\,\sin\theta', \\
A'P'  &= A'C'\,\sin\theta', \\
A'P'' &= A'D'\,\sin\theta' .
\end{aligned}
$$

### Step 3: the sines cancel

The points lie on $$l$$ in the order $$A,B,C,D$$ and the feet in the order $$A,O,O',O''$$, so $$CB=AC-AB$$ and $$DB=AD-AB$$. Subtracting inside Step 2 therefore removes $$\sin\theta$$:

$$
\begin{aligned}
\frac{AC}{CB} &= \frac{AC}{AC-AB} = \frac{AO'}{AO'-AO} = \frac{AO'}{OO'} , \\[6pt]
\frac{AD}{DB} &= \frac{AD}{AD-AB} = \frac{AO''}{AO''-AO} = \frac{AO''}{OO''} ,
\end{aligned}
$$

and the same computation on $$l'$$ removes $$\sin\theta'$$:

$$
\begin{aligned}
\frac{A'C'}{C'B'} &= \frac{A'P'}{PP'} , \\[6pt]
\frac{A'D'}{D'B'} &= \frac{A'P''}{PP''} .
\end{aligned}
$$

### Conclusion

Step 1 matches these right-hand sides in pairs, so

$$
\begin{aligned}
\frac{AC}{CB} &= \frac{A'C'}{C'B'}, \\[6pt]
\frac{AD}{DB} &= \frac{A'D'}{D'B'} ,
\end{aligned}
$$

and dividing,

$$
(A,B;C,D) = \frac{AC/CB}{AD/DB} = \frac{A'C'/C'B'}{A'D'/D'B'} = (A',B';C',D') .
\tag*{$\mathrm{Q.E.D.}$}
$$