---
title: "MIT 15.S12 Blockchain and Money Note (Lec 5)"
date: "2021-06-21"
categories: 
  - "未分类"
---

Study Questions:

1. How does Bitcoin record transactions? What is unspent transaction output (UTXO)? What is script code embedded in each Bitcoin transaction and how flexible a programming language is it?
2. As many design features pre-date Bitcoin, what was the novel innovation of Santoshi Nakamoto?
3. Who is Satoshi Nakamoto? (Only kidding a bit.)

l**ock time**: It's a protection mechanism that ensure the transaction time can only happen within this specific time span. It simply works kind of like condition on time.

**Transaction Format**

[![](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-21-at-18.41.53.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-21-at-18.41.53.png)

[![](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-21-at-18.45.15.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/06/screenshot-2021-06-21-at-18.45.15.png)

**Why the transaction fee is not regulated (fixed) ?** Market gives you the best price for a transaction fee. this is also how free market works.

**Unspent Transaction Output (UTXO)**

Set (Bitcoin transaction outputs that have not been spent at a given time)

1. Contains All Currently Unspent Transaction Outputs
2. Speeds up Transaction Validation Process
3. Stored using a LevelDB database in Bitcoin Core called ‘chainstate’

These UTXO data are stored in a distributed nodes, some wallet might be able save the UTXO data but not all the node.

There is only 1 transaction output, which is the spent output, the unspent transaction output is actually not an transaction output conceptually.

**Bitcoin Script: A programming code used for transaction**

Bitcoin Script **(Not Turing Complete)**  
Programing Code used for Transactions  
• Stack-based Code, with no Loops (not Turing-complete)  
• Provides a Flexible Set of Instructions for Transaction Validation and  
Signature Authentication  
• Most Common Script Types in UTXO:  
• Transaction sent to Hash of Bitcoin Address – ‘Pay-to-PubkeyHash’ (81%)  
• Transaction sent to Hash of Conditional Script – ‘Pay-to-ScriptHash’ (18%)  
• Transaction subject to Multiple Signatures – ‘M of N Multisig’ (0.7%)  
• Transaction sent to Bitcoin Address – ‘Pay-to-Pubkey’ (0.1%)  
(Source: Perez-Sola, Delgado-Segura, et al.)

Hal Finney might be Satoshi Nakamoto because he was an early [bitcoin](https://en.wikipedia.org/wiki/Bitcoin) contributor and received the first bitcoin transaction from bitcoin's creator [Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto).
