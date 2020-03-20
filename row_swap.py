
'''swap row0 and row4'''
import numpy
A = numpy.arange(25).reshape(5,5)
A[[0,4],:] = A[[4,0],:]
print(A)