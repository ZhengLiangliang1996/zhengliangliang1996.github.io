---
giscus_comments: true
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

<div class="problem" markdown="1">
**Problem 1.** That the cross-ratio of four points remains unchanged by a *parallel* projection follows from elementary properties of similar triangles. The proof is left to the reader as an exercise.

<figure class="tikz-figure">
{% include figures/cross-ratio-projection.svg %}
<figcaption>Invariance of cross-ratio under parallel projection.</figcaption>
</figure>
</div>

<div class="solution" markdown="1">
**Solution.**

#### Setting

The projecting lines $$AA'$$, $$BB'$$, $$CC'$$, $$DD'$$ are parallel — that is what it means for the centre of projection to lie at infinity. Neither $$l$$ nor $$l'$$ is parallel to them, or the projection would not be defined. Let $$\theta$$ be the angle between $$l$$ and that common direction and $$\theta'$$ the angle for $$l'$$; both lie in $$(0^\circ,90^\circ]$$, so $$\sin\theta>0$$ and $$\sin\theta'>0$$.

#### The construction

A line perpendicular to one projecting line is perpendicular to all four. Draw it through $$A$$: it meets $$BB'$$, $$CC'$$, $$DD'$$ at $$O$$, $$O'$$, $$O''$$. Draw it through $$A'$$: it meets them at $$P$$, $$P'$$, $$P''$$.

<figure class="tikz-figure">
{% include figures/cross-ratio-construction.svg %}
<figcaption>One perpendicular through A and one through A', each cutting the three other projecting lines. Corresponding segments on the two perpendiculars are equal, because they are cut off by the same pairs of parallel lines.</figcaption>
</figure>

#### Step 1: the two perpendiculars carry equal segments

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

#### Step 2: three similar right triangles on each side

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

#### Step 3: the sines cancel

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

</div>

<div class="problem" markdown="1">
**Problem 2.**

1) Given two lines together with a projective correspondence between their points, prove one can shift one line by a parallel displacement into such a position that the given correspondence is obtained by a simple projection. *(Hint: bring a pair of corresponding points of the two lines into coincidence.)*

2) On the basis of the preceding result, show that if the points of two lines $$l$$ and $$l'$$ are coördinated by any finite succession of projections onto various intermediate lines, using arbitrary centers of projection, the same result can be obtained by only *two* projections.
</div>

<div class="solution" markdown="1">
**Solution.**

### Part 1

Let $$\varphi \colon l \to l'$$ be the given projective correspondence, so $$\varphi$$ is a bijection that preserves the cross-ratio of any four points. Fix a point $$A$$ on $$l$$ and let $$A' = \varphi(A)$$.

**Step 1 (the parallel displacement).** Translate $$l'$$ by the vector $$v = A - A'$$, obtaining the line $$l'' = l' + v$$, and define

$$
\varphi'' \colon l \to l'', \qquad \varphi''(X) = \varphi(X) + v.
$$

<figure class="svg-figure">
{% include figures/parallel_slide_creates_perspectivity.svg %}
</figure>



A translation is itself a parallel projection — it carries each point of $$l'$$ to a point of $$l''$$ along the fixed direction $$v$$ — so by Problem 1 it preserves cross-ratio; composed with $$\varphi$$, which preserves cross-ratio by hypothesis, $$\varphi''$$ is again a projective correspondence. By construction $$\varphi''(A) = A' + (A - A') = A$$, so $$A$$ lies on both $$l$$ and $$l''$$ and is a *self-corresponding* point: it is exactly the intersection point $$l \cap l''$$.

**Step 2 (the candidate projection).** Choose two further points $$B, C$$ on $$l$$ and write $$B'' = \varphi''(B)$$, $$C'' = \varphi''(C)$$. Let

$$
O = BB'' \cap CC'',
$$

and let $$\psi \colon l \to l''$$ be the simple projection with center $$O$$. Then $$\psi(B) = B''$$ and $$\psi(C) = C''$$, since $$O$$ lies on the lines $$BB''$$ and $$CC''$$ by definition. Moreover $$\psi(A) = A$$, because the ray $$OA$$ meets $$l''$$ at $$A$$ itself ($$A \in l''$$). So $$\varphi''$$ and $$\psi$$ agree at the three points $$A, B, C$$.

**Step 3 (agreement at three points forces agreement everywhere).** Let $$X$$ be an arbitrary point of $$l$$. Both maps preserve cross-ratio — $$\varphi''$$ by Step 1, and $$\psi$$ because a simple projection preserves cross-ratio (the theorem of Fig. 75/76 in the book). Hence

$$
(A, B'' ; C'', \varphi''(X)) = (A,B;C,X) = (A, B'' ; C'', \psi(X)).
$$

But the cross-ratio $$(A, B''; C'', \cdot)$$, with the three distinct points $$A, B'', C''$$ fixed, is an injective function of its fourth argument: in a coordinate $$t$$ on $$l''$$ it is a fractional linear function with nonvanishing determinant, hence invertible. Therefore

$$
\varphi''(X) = \psi(X) \quad \text{for every } X \in l,
$$

so after the displacement the correspondence *is* the simple projection from $$O$$. $$\mathrm{Q.E.D.}$$


### Part 2

**Setup.** Suppose the correspondence $$\Phi \colon l \to l'$$ is built from a chain of simple projections through intermediate lines

$$
l = m_0 \;\longrightarrow\; m_1 \;\longrightarrow\; \cdots \;\longrightarrow\; m_n = l', \qquad \Phi = \pi_n \circ \cdots \circ \pi_1,
$$

where each $$\pi_i \colon m_{i-1} \to m_i$$ is a simple projection from some center $$O_i$$ (an ordinary point, or a point at infinity if $$\pi_i$$ happens to be a parallel projection).

**Step 1 ($$\Phi$$ is a projective correspondence).** Each $$\pi_i$$ preserves the cross-ratio of any four points — this is the theorem for a simple projection with an ordinary center, of which Problem 1 is the limiting case where the center recedes to infinity. A composition of cross-ratio-preserving bijections again preserves cross-ratio, so $$\Phi$$ itself preserves the cross-ratio of every four points of $$l$$: it is a projective correspondence between $$l$$ and $$l'$$, exactly the kind of map to which Part 1 applies — regardless of how many intermediate steps $$n$$ it took to build.

**Step 2 (reduce to one projection plus one displacement).** Apply Part 1 to $$\Phi$$: there is a vector $$v$$ such that, writing $$l'' = l' + v$$ and

$$
\Phi'' \colon l \to l'', \qquad \Phi''(X) = \Phi(X) + v,
$$

the map $$\Phi''$$ coincides with a simple projection $$\psi \colon l \to l''$$ centered at some point $$O$$.

**Step 3 (the displacement is itself a projection).** As noted in Part 1, translating a line by a vector is exactly a parallel projection — a simple projection with center at infinity. So

$$
\tau \colon l' \to l'', \qquad \tau(Y) = Y + v,
$$

is a simple projection, with center at infinity in the direction of $$v$$, and its inverse

$$
\tau^{-1} \colon l'' \to l', \qquad \tau^{-1}(Z) = Z - v,
$$

is likewise a simple projection, the parallel projection in the direction $$-v$$.

**Conclusion.** For every $$X \in l$$,

$$
\Phi(X) = \Phi''(X) - v = \psi(X) - v = \tau^{-1}\big(\psi(X)\big),
$$

so

$$
\Phi = \tau^{-1} \circ \psi.
$$

That is, $$\Phi$$ is realized by first projecting $$l$$ onto $$l''$$ from the ordinary center $$O$$, then projecting $$l''$$ onto $$l'$$ by the parallel projection in direction $$-v$$ — two projections in all, no matter how many projections $$n$$ were used in the original chain. $$\mathrm{Q.E.D.}$$

</div>

<div class="problem" markdown="1">
**Problem 3** Given a segment $$AB$$ and a region $$R$$ blocking the line to the right of $$B$$, continue the line $$AB$$ beyond $$R$$ using the straightedge alone, without the straightedge ever crossing $$R$$.
</div>

<div class="solution" markdown="1">
**Solution.**

**Construction.**
1. Choose $$C, C'$$ on segment $$AB$$, both between the midpoint and $$B$$, close enough to the midpoint that (by the formula above) their conjugates will clear $$R$$.
2. Choose an auxiliary point $$E$$ above the line, and draw $$EA$$, $$EB$$, $$EC$$, $$EC'$$ — all within the region left of $$R$$.
3. Quadrilateral for $$C$$: mark $$G$$ on $$EC$$; let $$F = AG \cap EB$$ and $$I = BG \cap EA$$; the line $$IF$$, extended down to the base line, lands at $$D$$, the harmonic conjugate of $$C$$. By placing $$E$$ high and $$G$$ suitably, the line $$IF$$ descends to $$D$$ passing **above** $$R$$.
4. Repeat with $$C'$$ (the same $$E$$ may be reused, with a point $$G'$$ on $$EC'$$), obtaining $$D'$$ beyond $$R$$.
5. Draw the line $$D'D$$ and extend it to the right: this is the continuation of $$AB$$.


<figure class="svg-figure">
{% include figures/extending_line_past_obstacle.svg %}
</figure>

</div>

<div class="problem" markdown="1">
**Problem 4.** What is the cross-ratio of four lines $$l_1, l_2, l_3, l_4$$ if they are parallel? What is the cross-ratio if $$l_4$$ is the line at infinity?
</div>

<div class="solution" markdown="1">
**Solution.**

### Part 1: four parallel lines

Four parallel lines form a pencil whose center is a point at infinity — the common "point" all four pass through is the ideal point of their shared direction. The cross-ratio of a pencil is defined as the cross-ratio of the four points in which any transversal cuts it, so let a transversal $$t$$ meet the lines in $$A_1, A_2, A_3, A_4$$ and define

$$
(l_1, l_2; l_3, l_4) = (A_1, A_2; A_3, A_4) = \frac{A_1A_3 / A_3A_2}{A_1A_4 / A_4A_2}.
$$

<figure class="svg-figure">
{% include figures/parallel_lines_cross_ratio.svg %}
</figure>

**This is well defined** — the transversal doesn't matter — precisely by Problem 1: if a second transversal $$t'$$ cuts the lines in $$B_1, B_2, B_3, B_4$$, then the correspondence $$A_i \mapsto B_i$$ *is* a parallel projection from $$t$$ to $$t'$$ (its projecting rays are the four given lines themselves, which are parallel), and Problem 1 says parallel projection preserves cross-ratio. So $$(A_1,A_2;A_3,A_4) = (B_1,B_2;B_3,B_4)$$.

In particular one may take the transversal **perpendicular** to the four lines. Writing $$h_1, h_2, h_3, h_4$$ for signed positions of the lines along that common perpendicular,

$$
(l_1, l_2; l_3, l_4) = \frac{(h_3 - h_1)/(h_2 - h_3)}{(h_4 - h_1)/(h_2 - h_4)}:
$$

the cross-ratio of four parallel lines is the cross-ratio of their (signed) mutual distances. This is the limiting form of the $$\sin$$-formula for a pencil with ordinary center: as the center recedes to infinity, the sines of the angles at the center become proportional to the distances between the lines.

### Part 2: $$l_4$$ the line at infinity

For the four lines to form a pencil, $$l_1, l_2, l_3, l_4$$ must share a common point. The line at infinity passes through every ideal point, so the shared point is the ideal point of $$l_1, l_2, l_3$$ — that is, $$l_1, l_2, l_3$$ are parallel to one another, and $$l_4 = l_\infty$$ completes their pencil.

Cut with a transversal $$t$$: it meets $$l_1, l_2, l_3$$ at $$A_1, A_2, A_3$$, and it meets $$l_\infty$$ at its own point at infinity, $$A_4 = \infty$$. In the cross-ratio the factor involving $$A_4$$ tends to $$1$$:

$$
(l_1, l_2; l_3, l_\infty) = \lim_{A_4 \to \infty} \frac{A_1A_3 / A_3A_2}{A_1A_4 / A_4A_2} = \frac{A_1A_3}{A_3A_2} = \frac{h_3 - h_1}{h_2 - h_3},
$$

the **simple ratio** in which $$l_3$$ divides the strip between $$l_1$$ and $$l_2$$, measured by distances.
</div>