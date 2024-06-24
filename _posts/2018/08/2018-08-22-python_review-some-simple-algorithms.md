---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Python_review &amp; Some simple algorithms"
date: "2018-08-22"
categories: 
  - "dl-ml-python"
---

Life is short, I use python

Today, I'm gonna review some basics of python.

- **List can be mix types** 

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_094806.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **List Slicing**

numers = [0, 1, 2, 3, 4, 5, 6]       list[start:end]

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_095130.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **Tuple**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_095316.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **Dictionary**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_095407.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **Some loops we may ignore**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_095519.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **shape of array in numpy you might be confused!**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_095646.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **axis in numpy (important!!!!) & keepdims** 

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_095839.jpg" alt="screenshot" width="80%" height="auto">
</p>

**difference between axis = 1 and axis = 0:**
```python
 1 # -*- coding: utf-8 -*-
 2 """
 3 Created on Wed Aug 22 08:51:33 2018
 4 
 5 @author: zhengstars
 6 """
 7 import numpy as np
 8 # can be done by recursive
 9 def test():
10     x = np.array([[1, 2],[3, 4]])
11     print(np.max(x, axis = 1))
12     print(np.max(x, axis = 0))
13     
14     print(np.max(x, axis = 1, keepdims = True))
15     print(np.max(x, axis = 0, keepdims = True))
16         
17 def main():
18     test()
19     
20 if __name__ == '__main__':
21     main()

```

output :

[2 4] [3 4] [[2] [4]] [[3 4]]

Which means that when we use axis = 1 , then the operation will go according to the column(cross column), and axis = 0 will go cross rows. and keepdims will keep the dimension after this operation, default option is false(output as scalar)

- **Element-wise operation and dot product (对应元素相称与矩阵乘法的区别)**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_101023.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **indexing**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_101556.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **Broadcasting**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_101719.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **Some tips**

format: [func(x) for x in some_list]

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_101904.jpg" alt="screenshot" width="80%" height="auto">
</p>

we will use this format in the following **Some simple algorithms** part

- **Debugging Tips & Anaconda & Virtualenv:**

Unsure of what you can do with an object? Use **_type()_** and **_dir()_**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_102155.jpg" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/08/2018-08-22_102216.jpg" alt="screenshot" width="80%" height="auto">
</p>

- **Some simple algorithms**
```python
 1 # -*- coding: utf-8 -*-
 2 """
 3 Created on Wed Aug 22 08:51:33 2018
 4 
 5 @author: 
 6 """
 7 
 8 def QuickSort(arr):
 9    if len(arr) <= 1:
10         return arr
11     pivot = arr[len(arr) // 2]
12     left = [x for x in arr if x < pivot]
13     middle = [x for x in arr if x == pivot]
14     right = [x for x in arr if x > pivot]
15     return QuickSort(left) + middle + QuickSort(right)
16 
17 def main():
18     print(QuickSort([4,52,4,51,3,7,23,6,7,2]))
19 
20 if __name__ == '__main__':
21     main()
```

This a very simple Quick sort, as you can see that in this QuickSort function, we can simply get the result of left middle right in the [x for x in arr if x <=>] operation. and array can be concatenated by simply using '+' operation.

print(QuickSort([4, 52, 4, 51, 3, 7, 23, 6, 7, 2]))
```python
 1 # -*- coding: utf-8 -*-
 2 """
 3 Created on Wed Aug 22 08:51:33 2018
 4 
 5 @author: 
 6 """
 7 
 8 # can be done by recursive
 9 def QuickSort(arr):
10     if len(arr) <= 1:
11         return arr
12     pivot = arr[len(arr) // 2]
13     left = [x for x in arr if x < pivot]
14     middle = [x for x in arr if x == pivot]
15     right = [x for x in arr if x > pivot]
16     return QuickSort(left) + middle + QuickSort(right)
17 
18 # 2 for loops
19 def SelectionSort(arr):
20     for i in range(0,len(arr)):
21         min = i
22         for j in range(i+1,len(arr)): # smallest on the very right side
23             if arr[min] > arr[j]:
24                 min = j
25         arr[min],arr[i] = arr[i],arr[min]
26     return arr
27 
28 # merge Sort
29 def merge(a, b):  # conquer
30     C = []
31     while len(a) != 0 and len(b) != 0:
32         if a[0] < b[0]:
33             C.append(a[0])
34             a.remove(a[0])
35         else:
36             C.append(b[0])
37             b.remove(b[0])
38     
39     if len(a) == 0:
40         C += b
41     else:
42         C += a
43     return C
44 
45 def mergesort(arr):
46     if len(arr) == 0 or len(arr) == 1:
47         return arr
48     else:
49         middle = len(arr) // 2
50         a = mergesort(arr[:middle])  #divide
51         b = mergesort(arr[middle:])
52         arr = merge(a,b)
53     return arr
54         
55 def main():
56     print(QuickSort([4, 52, 4, 51, 3, 7, 23, 6, 7, 2]))
57     print(QuickSort([4, 52, 4, 51, 3, 7, 23, 6, 7, 2]))
58     print(mergesort([4, 52, 4, 51, 3, 7, 23, 6, 7, 2]))
59 if __name__ == '__main__':
60     main()
```

Above code I add the selection sort and merge sort,which are very simple compared to other programming language, and easy to understand.
