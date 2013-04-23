---
layout: post
title: "interview"
tldr: "more interview questions"
tags: [cs, interview, algorithms]
---

Q0. Given numbers arranged as two sorted arrays A and B, find the k-th smallest number in them. E.g., if A = \[1, 3, 5\], B = \[2, 3, 4\], k = 5, return 4.

```python
def findk(A,B,k):
    A_i = 0
    B_i = 0
    for i in range(1,k+1) [1... k]
        if A_i >= length(A):
            B_i = B_i + 1
            isA = false
        else if B_i >= length(B):
            A_i = A_i + 1   
            isA = true      
        else if A[A_i] <= B[B_i]:
            A_i = A_i +1
            isA = true
        else:
            B_i = B_i + 1
            isA = false
    if isA:
        return A[A_i-1]
    else 
        return B[B_i-1]
```

Test cases:

    k = 1 A[0] < B[0] ; A_i = 1, isA is true
    k =2  A[1] >B[0] ; B_i = 1, isA is false
    k = 3 A[1] == B[1]; A_i = 2, isA is true
    A = [1,2,3], B = [4,5,6], k = 5;

Q1. Given a sorted binary tree and a pointer to one of the nodes in the tree, find the next largest number in the tree.

       9
     4    14
    1 5 11  16
       10 12

if you have right subtree, then find smallest element in right subtree
if you don't have right subtree, then find the parent of the first node (also considering yourself) that is a left child.

```python
def find_next(ele):
    if ele.rchild:
        node iter = ele.rchild
        while iter.lchild:
            iter = iter.lchild
        return iter
    else:
        node iter = ele
        if not iter.parent:
            return null
        while iter.parent.lchild != iter:
                iter = iter.parent
                if not iter.parent
                    return null
        return iter.parent
```

Node n = smallest node in the tree
while (n != null)
 n = find_next(n)
 
Q2. Given an array A of length n containing positive integers, compute an array B of length n, where B\[i\] = (A\[0\] * A\[1\] * … * A\[n-1\] ) / A\[i\]. Assume that divide operation is not available.

```python
def mult_array(A):  
    Af = list()  
    Af[1] = A[0]  
    Af[0] = 1  
    Ab = list()      
    Ab[n-2] = A[n-1]  
    Ab[n-1] = 1  
    for i in [2... n-1]:  
        Af[i] = Af[i-1]*A[i-1]  
    for j in [n-3 .... 0]:  
        Ab[j] = Ab[j+1]*A[j+1]  
    for i in [0 ... n-1]:
        B[i] = Af[i]*Ab[i] 
```

Test Case:

    B[i] = A[0] * A[1] * ... A[i-1]
    B[1] = A[0]
    B[n-2] = A[n-1]  
    B[i] = A[n-1] * A[n-2] ... A[i+1]  

Example:

    A = 1 2 3  
    B = [6 3 2]  
    Af[1] = 1  
    Af[2] = 1*2 = 2  
    Ab[1] = 3  
    Ab[0] = 3*2 = 6  
    B[0] = 1*6=6  
    B[1] = 3  
    B[2] = 2  

Q3 : Given two arrays a and b, find all pairs of elements (a1,b1) such that a1 belongs to Array A and b1 belongs to Array B whose sum a1+b1 = k (any integer).

O(n) using hashmap  
O(n log n) by first sorting them but doesn't require additional memory.
