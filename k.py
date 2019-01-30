import matplotlib.pyplot as plot
import math
import numpy as np
f1=float(input("enter the frequency"))
f2=float(input("enter the frequency"))
fr=float(input("enter the input"))
p=math.pi
p1=0
a=input("enter amplitude")
a1=input("enter amplitude")
t=np.arange(0,0.1,0.0001)
x=np.sin(2*np.pi*f1*t/fr)
x1=np.sin(2*np.pi*f2*t/fr)
y=x+x1
plot.subplot(311)
plot.plot(t,x)
plot.subplot(312)
plot.plot(t,x1)
plot.subplot(313)
plot.plot(t,y)
plot.show()

