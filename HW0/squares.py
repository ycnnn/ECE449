import numpy 
import torch


## You only need to complete the two functions.
def numpy_squares(k):
    x = numpy.power(numpy.arange(1,k + 1,1),2)
    return x

def torch_squares(k):
    x = torch.square(torch.arange(1, k+1))
    return x

x = torch_squares(10)
