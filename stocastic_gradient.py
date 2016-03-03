import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# logistic function
def logistic(x):
    return 1/(1+np.exp(-x))

# this is the derivative of logistic with respect to x
def dlogistic(x):
    u = logistic(x)
    return u*(1-u)

# forward propagation step for a single data point
def forwardprop(w1,w2,x):
    a0 = np.insert(x,0,1)  # insert bias unit
    z1 = w1.dot(a0)        # calculate input to hidden layer
    a1 = logistic(z1)      # calculate output from hidden layer
    a1 = np.insert(a1,0,1) # insert bias unit
    z2 = w2.dot(a1)        # calculate input to output layer
    a2 = logistic(z2)      # calculate output of neural network
    return a2,z2,a1,z1,a0

# backprop
def backwardprop(y,a2,a1,a0,z1,w2,nout,nhid):
    d2 = a2 - y
    dw2 = np.outer(d2,a1)
    v2 = np.reshape(w2[:,1:],(nout,nhid))
    d1 = v2.transpose().dot(d2)*dlogistic(z1)
    dw1 = np.outer(d1,a0)
    return dw1,dw2

# batch forward propagation
def batchforwardprop(x,w1,w2):
    m = x.shape[1]
    n = x.shape[0]
    h = w1.shape[0]
    a0 = np.reshape(np.append(np.ones(m),x),(n+1,m))
    z1 = w1.dot(a0)
    a1 = logistic(z1)
    a1 = np.reshape(np.append(np.ones(m),a1),(h+1,m))
    a2 = logistic(w2.dot(a1))
    return a2

# cost function
def costfunction(y,a):
    return -y*np.log(a)-(1-y)*np.log(1-a)

# learn
def learn(Nsteps,eta,X,y,w1,w2):
    m = X.shape[1]
    nout = w2.shape[0]
    nhid = w1.shape[0]
    for i in range(0,Nsteps):
        order = np.random.permutation(m) # get random ordering of data points
        cost = 0
        for j in range(0,m):
            idx = order[j]
            a2,z2,a1,z1,a0 = forwardprop(w1,w2,X[:,idx])
            dw1,dw2 = backwardprop(y[idx],a2,a1,a0,z1,w2,nout,nhid)
            w1 -= eta*dw1
            w2 -= eta*dw2
            cost += costfunction(y[idx],a2)
        if i%500==0:
            print 'iteration %d:, cost = %.6f'%(i,cost[0])
    return w1,w2

# plot the output
def plotoutput(x,y,w1,w2):
    m = x.shape[1]
    xmin = x.min()
    xmax = x.max()
    xr = xmax-xmin
    ngrid = 13
    xl=np.linspace(xmin-xr*0.1,xmax+xr*0.1,ngrid)
    [X1,X2]=np.meshgrid(xl,xl)
    A=batchforwardprop(np.array([X1.flatten(), X2.flatten()]),w1,w2)
    A = np.resize(A,(ngrid,ngrid))
    fig = pl.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X1, X2, A, rstride=1, cstride=1, linewidth=0.5, cmap=cm.autumn, antialiased=False)
    for i in range(0,m):
        ax.plot([x[0,i],x[0,i]],[x[1,i],x[1,i]],[0,y[i]],'k')
        ax.plot([x[0,i]],[x[1,i]],[y[i]],'og',markersize=10)
    pl.setp(ax,xlabel='X1', ylabel='X2')
    pl.show()

### Feel free to adjust code below this

# the data
X = np.array([[0,0],[0,1],[1,0],[1,1]]).transpose()
y = np.array([0, 1, 1, 0])

# weights
nin = X.shape[0]
nhid = 2
nout = 1
np.random.seed(8981100442)
w1 = (np.sqrt(6)/np.sqrt(nhid+nin+1))*2*(np.random.rand(nhid,nin+1)-0.5)
w2 = (np.sqrt(6)/np.sqrt(nhid+1+nout))*2*(np.random.rand(nout,nhid+1)-0.5)

# learn
w1,w2=learn(200,10,X,y,w1,w2)
batchforwardprop(X,w1,w2) # batchforwardprop calculates forward prop for all data at once.
plotoutput(X,y,w1,w2) # plots the output of the neural network along with the data points
