---
title: "MIT 15.S12 Blockchain and Money Note (Lec 4)"
date: "2021-06-12"
categories: 
  - "未分类"
---

Study Questions:

1. What is the Byzantine Generals problem? How does proof-of-work and mining in Bitcoin address it? More generally how does blockchain technology address it?
2. What other consensus protocols are there? What are some of the tradeoffs of alternative consensus algorithms – proof-of-work, proof-of- stake, etc.?
3. How do economic incentives work within blockchain technology to maintain decentralised ledgers and avoid double spending? What are the incentives of consensus protocols and mining?

Discussion:

1. Timestamped append-open log blockchain that keep the block unfeasible to be cracked, but there is a way that if you control the power of the internet, or say capturing part of the Internet, you fork the blockchain. What Satoshi Nakamoto (中本聪) answered in an exchanged e-mail was that as long as the captured internet is less than 50% of the majority of the whole internet, after certain amount of time, people will realise they're in the wrong chain and all of the people will stop investing power to mining in that specific internet-controlled area.

**Byzantine Generals Problem:**

The term takes its name from an [allegory](https://en.wikipedia.org/wiki/Allegory), the "Byzantine Generals Problem",[\[2\]](https://en.wikipedia.org/wiki/Byzantine_fault#cite_note-2) developed to describe a situation in which, in order to avoid catastrophic failure of the system, the system's actors must agree on a concerted strategy, but some of these actors are unreliable.

\----- From Wikipedia

**Proof-of-work:**

[![](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-12-at-09.03.44.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-12-at-09.03.44.png)

One of the reason for bitcoin to design it as to find the leading zeros hash is to make the mining difficult and make the verification easy. When mining it you could only brute-force change the nonce and hashing it over and over again until you find the correct leading-zeros hash, but by verifying it you need only a small hash function.

**Blockchain – Consensus:**

1. Supports the longest chain

Bitcoin Mining Evolution:

[![](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-12-at-09.33.22.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-12-at-09.33.22.png)

The mining pool started in 2010 in order to smooth out the revenue.
