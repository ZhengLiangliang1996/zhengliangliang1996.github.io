---
giscus_comments: true
layout: post
title: "TEST B — CH4 figures only, no math"
date: "2025-04-08"
permalink: /test/ch4-figonly/
categories:
  - "math"
toc:
  sidebar: true
sitemap: false
nav: false
---

<!--
  BISECT PAGE B — delete this file once the iPhone reload bug is diagnosed.
  The two inline tikz-figure SVGs from the CH4 post, with every display-math
  block removed so MathJax has nothing to typeset. Front matter matches CH4.

  If THIS page reloads itself on iPhone -> the inline SVG (or the
  .tikz-figure CSS applied to it) is the cause.
  If THIS page is stable -> the SVG is innocent, look at MathJax.
-->

## Figures only

No math on this page. Both inline SVGs from the CH4 post are below, wrapped in
the same `figure.tikz-figure` markup and styled by the same rules in
`_sass/_tikzjax.scss`.

### Figure 1

<figure class="tikz-figure">
{% include figures/cross-ratio-projection.svg %}
<figcaption>Invariance of cross-ratio under parallel projection.</figcaption>
</figure>

### Figure 2

<figure class="tikz-figure">
{% include figures/cross-ratio-construction.svg %}
<figcaption>One perpendicular through A and one through A', each cutting the three other projecting lines. Corresponding segments on the two perpendiculars are equal, because they are cut off by the same pairs of parallel lines.</figcaption>
</figure>

### Scroll padding

Filler so the page scrolls roughly like the real post, since the reload is
often triggered by scrolling rather than by initial load.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium
doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore
veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam
voluptatem quia voluptas sit aspernatur aut odit aut fugit.

Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur,
adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et
dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis
nostrum exercitationem ullam corporis suscipit laboriosam.
