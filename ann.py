# -*- coding: utf-8 -*-
"""ANN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ubg3umpogBpNMRzynF5jA_aljDwBuQe4
"""

# first neural network with keras tutorial

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# load the dataset
path = "wheat_model.png.csv"
rr = open(path, "r")
def divide(st, d):
    li = []
    st += d
    while len(st) > 0:
        n = st.index(d)
        we = st[:n]
        if we != "":
            li.append(we)
        st = st[n+len(d):]
    return li

li = divide(str(rr.read()), "\n")
le = []
for k in li:
  le.append(divide(k, ","))
print(le)

def convertfloat(li):
    ll = []
    for k in li:
        ll.append(float(k))
    return ll

data = le[1:]
X = []
y = []
t = []
for u in data:
  lli = convertfloat(u)
  X.append(lli[2:])
  y.append([lli[1]])
  t.append(lli[0])
print(X)
print(y)

# define the keras model
model = Sequential()
model.add(Dense(32, input_dim=5, activation='relu', use_bias=True))
model.add(Dense(32, activation='relu', use_bias=True))
model.add(Dense(32, activation='relu', use_bias=True))
model.add(Dense(1, activation='linear', use_bias=True))
# compile the keras model
model.compile(loss='mean_squared_error', optimizer='Adam')
# fit the keras model on the dataset
model.fit(X, y, epochs=1000, batch_size=45)
# evaluate the keras model

#Predict

print(t)
real = []
pred = []
for i in range(len(t)):
  real.append(y[i][0])
  
  n = model.predict([X[i]])[0][0]
  pred.append(n)

print(real)
print(pred)

print(len(t))
import matplotlib.pyplot as plt

plt.plot(t, real, t, pred)

plt.show()

inp = [0,0,0,0,0]
n = model.predict([inp])[0][0]
print(n)

model.save("modelnn.h5")

