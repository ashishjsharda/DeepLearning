import theano
from theano import tensor
a=tensor.dscalar()
b=tensor.dscalar()
rem=a-b
print(rem)
func=theano.function([a,b],rem)
assert 10 == func(20,10)
