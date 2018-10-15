import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

data = np.loadtxt('crash.txt')

train_set = data[0::2]
test_set = data[1::2]

def basis_functions(X, L):
    w = np.empty(L+1)
    for x in X:
        p = np.empty(L+1)
        for order in range(L+1):
            p[order] = x ** (order)
        w = np.vstack((w, p))
    return w[1:]

x = train_set[:,0]
t = train_set[:,1]
t = t.reshape((-1,1))
test_x = test_set[:,0]
test_t = test_set[:,1].reshape((-1,1))
# z = np.polyfit(x, t, 3)

x_plot = list(range(1,21))
y_train = []
y_test = []
for L in range(1,21):

    phi_train = basis_functions(x, L)
    w = np.linalg.solve(phi_train.T.dot(phi_train), phi_train.T.dot(t))

    E_train = t - phi_train.dot(w)
    E_train = E_train ** 2
    RMS_train = np.sqrt(E_train.sum()/x.shape[0])

    phi_test = basis_functions(test_x, L)
    E_test = test_t - phi_test.dot(w)
    E_test = E_test ** 2
    RMS_test = np.sqrt(E_test.sum()/test_x.shape[0])

    y_train.append(RMS_train)
    y_test.append(RMS_test)

# plt.plot(x_plot, y_train)
# plt.plot(x_plot, y_test)
# plt.show()

phi_train = basis_functions(x, 15)
w = np.linalg.solve(phi_train.T.dot(phi_train), phi_train.T.dot(t))
pred_train = phi_train.dot(w)
phi_test = basis_functions(test_x, 15)
pred_test = phi_test.dot(w)

plt.scatter(x, t, c='red')
plt.scatter(test_x,test_t, c='green')
plt.plot(x, pred_train)
plt.plot(test_x, pred_test, c='purple')
plt.show()