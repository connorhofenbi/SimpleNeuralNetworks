import math
import numpy as np

#x is the actual matrix the sigmoid is applied to
#isDer is if youre taking the derivative of the sigmoid
def sigmoid(x, isDer = False) :
    if isDer:
        return x*(1-x)
    return 1/(1+np.exp(-x))


x = np.array([[0,1,1],
             [1,0,1],
             [1,0,0],
             [0,0,1]])

#If you dont notice it, y is the mode of each row
y = np.array([1,1,0,0])

#initing the weights for each layer
weightsLayerOne = np.random.rand(3,4)
weightsLayerTwo = np.random.rand(4,1)

#train over 1000 cycles
for i in xrange(1000):

    #feeding forward
    layer1 = sigmoid(np.dot(x, weightsLayerOne))
    out = sigmoid(np.dot(layer1, weightsLayerTwo))

    #back propogation
    #error = y - output
    back1_delta = (y-out)*sigmoid(out,True)
    print(back1_delta)
    back2_error = np.dot(weightsLayerTwo.T, back1_delta)
    back2_delta = back2_error*sigmoid(layer1 ,True)

    #update weights by the slope of the loss
    weightsLayerOne += np.dot(x.T, back2_delta)
    weightsLayerTwo += np.dot(layer1.T , back1_delta)

print "output "
print out
