import matplotlib.pyplot as plot
import math
import numpy as np
f1=float(input("enter the frequency"))
f2=float(input("enter the frequency"))
fr=float(input("enter the input"))
p=float(input("enter the phase in radians"))
p1=float(input("enter the phase in radians"))
a=input("enter amplitude")
a1=input("enter amplitude")
t=np.arange(0,10,0.01)
x=np.sin((2*np.pi*f1*t/fr)+p)
x1=np.sin((2*np.pi*f2*t/fr)+p1)
y=x+x1
plot.subplot(311)
plot.plot(t,x)
plot.subplot(312)
plot.plot(t,x1)
plot.subplot(313)
plot.plot(t,y)
plot.show()

