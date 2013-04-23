---
layout: post
title: "convolution"
tldr: "simple explanation of convolution"
tags: [cs, convolution, image processing]
---

[1]: www.songho.ca/dsp/convolution/convolution.html
[2]: www.songho.ca/dsp/convolution/convolution2d_separable.html
[3]: https://www.cs.duke.edu/courses/spring03/cps296.1/handouts/Image%20Processing.pdf

### Convolution 1D ###
How do you convolve two functions?  
h(n) = f(n)\*g(n) = \int_{k = -\infty}^{\infty} f(k) \cdot g(n-k)

Imagine you have f(x) and g(x) overlayed on a graph. 
To do a convolution, g(n-k) becomes g(-(k-n)) which means flip g horizontally (because -k) and shift it to the right by n units.
Then take the sum of values of the product of the two functions for the whole domain of the two functions.  

In the discrete case, this boils down to convolving two vectors. 

h\[n\] = f\[n\]\*g\[n\] = \sum_{k = -\infty}^{\infty} f\[k\] \cdot g\[n-k\]

Taking the discrete analogy of the above description, be aware of two things
* consider the vector as a probability mass function
* but make sure it is in line with your indexing. 
* If it's zero index, then flipping one of them means that you have one overlap at k=0

\[1 2 3\] * \[1 0 -1\] = 

    |   |   | 1 | 2 | 3 |
    | -1| 0 | 1 |   |   |

h\[0\] = 1

    |   | 1 | 2 | 3 |
    | -1| 0 | 1 | |

h\[1\] = 0+2=2

    | 1 | 2 | 3 |
    | -1| 0 | 1 |

h\[2\] = -1+0+3 = 2

    | 1 | 2 | 3 |   |
    |   | -1| 0 | 1 |

h\[3\] = -2+0 = -2

    | 1 | 2 | 3  |   |   |
    |   |   | -1 | 0 | 1 |

h\[4\] = -3

	    1  2  3  
	    1  0 -1  
	    --------
	    -1 -2 -3
	 1 2 3
	 ---------
	 1 2 2 -2 -3

### Convolution 2D ###
f\[i,j\]\*g\[i,j\] =   

The idea for 2d convolution is similar, you have to flip the g matrix vertically and horizontally so that in the classic 3 x 3 matrix case, it looks like

	 = = =  
	| | | |  
	 = = =  
	| | | |  
	 = = = = =  
	| | | | | |  
	 = = = = =   
	    | | | |  
	     = = =  
	    | | | |  
	     = = =  

So you just shift it left and right for the other entries of the convolution matrix

### Applications ###

[4]: http://en.wikipedia.org/wiki/Kernel_%28image_processing%29
[5]: http://beej.us/blog/data/convolution-image-processing/

An interesting application is convolving images with kernels for [different][4] [effects][5]. Another interesting application is to convolve with the matrix \[-1 0 1\] which gives the derivatives. [Source][3]

References: 
* [Concise website with examples][1]
* [Separable convolutions][2]

