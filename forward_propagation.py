import numpy as np

# logistic
def logistic(x):
    return 1/(1+np.exp(-x))

# forward prop
def forwardprop(w1,w2,x):
    '''
    w1 are the weights between input and hidden layer
    w2 are the weights between hidden and output layer
    x is a column vector for a single data point
    '''
    a0 = np.insert(x,0,1)  # insert bias unit at input layer
    z1 = w1.dot(a0)        # calculate input to hidden layer
    a1 = logistic(z1)      # calculate output from hidden layer
    a1 = np.insert(a1,0,1) # insert bias unit
    z2 = w2.dot(a1)        # calculate input to output layer
    a2 = logistic(z2)      # calculate output of neural network
    return a2

# set inputs
X = np.array([[0,0],[0,1],[1,0],[1,1]]).transpose()
m = X.shape[1]

# network architecture
nin = X.shape[0]
nhid = 2
nout = 1

# randomize the weights
# input to hidden
w1 = (np.sqrt(6)/np.sqrt(nhid+nin+1))*2*(np.random.rand(nhid,nin+1)-0.5)
# hidden to output
w2 = (np.sqrt(6)/np.sqrt(nhid+1+nout))*2*(np.random.rand(nout,nhid+1)-0.5)

# initialize the activity matrix
a2 = np.zeros(m)

for i in range(0,m):
    a2[i] = forwardprop(w1,w2,X[:,i])
    print a2[i]
