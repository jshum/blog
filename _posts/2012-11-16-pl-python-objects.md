---
layout: post
title: "python objects"
---

### python objects in our language
constructors in our method are all done like this

Node() desugars into (Node.__init__(self)), with self bounded to an instance of the object.
In our language, we do this in several steps:

Let !instance = (VObject (Instance) (Generic) (Instance attributes of Node)
 in
	(CApp (CMethodCall 'Node '__init__ (list 'self)) 
		!instance) 

python retardedness
int(4) actually calls int.__int__(4)

instead of 
int.__init__(4)

because, the init method actually calls the __int__ method
int.__init__(self) = int.__int__()

### recursion
How to have recursion in definitions!!!
let F = dummy func
	in
	let !F = (desugar body) ;;thus any mention of F inside body will have ref.
		in
		(begin (set! F !F) F)

### Class having an attribute class referring to itself
Using recursion, if we do
CObject (Class) (Generic) (CAttribute 'this (CName ClassName)
			   CAttribute 'name (CStr "ClassName"))
then after recursion this will actually point to itself now

### built in objects/primitive operations

Built in objects are injectd into the store in the order dependent on class hierarchy
Primitive operations have to call racket functions because it has to depend on racket stuff

### Shouldn't add VName to our CVals

can't use a Vname:

def f()
	class C:
		pass
	return C()

a = f()
# class C not in environment, because we dump the env from functionDef





