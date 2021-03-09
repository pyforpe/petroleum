# IPR Straight line curve
import math
import matplotlib

global x

def select():
    while 1==1:
        select = int(input("Steady state flow rate calculation, press :1 \nStraightline IPR, press :2 \nVogels IPR, press :3 \nComposite IPR, press :4 "))
        if int(select) in range(1,5):
            break
        print("please select number from 1 to 4")
    return select

val = select()

# Steady state flow rate calculation
if val == 1:
    k = float(input("Enter Permeability(md)"))
    h = float(input("Enter height (ft)"))
    p1 = float(input("Reservoir or static pressure(Pe) in psi"))
    p2 = float(input("Wellbore flowing Pressure(Pwf) in psi"))
    u = float(input("enter viscosity"))
    re = float(input("Reservoir Radius(ft)"))
    rw = float(input("wellbore radius(ft)"))
    b = float(input("enter FVF of Oil in bbl/SCF"))
    Q = (0.00708*k*h*(p1-p2))/(u*b*math.log(re/rw))
    print(str(Q) +" STB/Day")
    

# Straightline IPR
if val == 2:
    p1 = float(input("Reservoir or static pressure(Pe) in psi"))
    p2 = float(input("Wellbore flowing Pressure(Pwf) in psi"))
    q = float(input("Flow rate in STB/Day"))
    j = q/(p1-p2)
    pwf = []
    Q = []
    for i in range(0,int(p1),50):
        pwf.append(i)
        q2 = j*(p1-i)
        Q.append(q2)
    
    matplotlib.pyplot.plot(Q,pwf)
    matplotlib.pyplot.xlabel("flow rate (STB/Day)")
    matplotlib.pyplot.ylabel("bottomhole flowing pressure (psi)")


# Vogels IPR
if val == 3:
    p1 = float(input("Reservoir or static pressure(Pe) in psi"))
    p2 = float(input("Wellbore flowing Pressure(Pwf) in psi"))
    q = float(input("Flow rate in STB/Day"))
    
    qmax = q / (1 - 0.2*(p2/p1) - 0.8*((p2/p1)**2) )
    pwf = []
    Q = []
    for i in range(0,int(p1),50):
        pwf.append(i)
        q2 = qmax * (1 - 0.2*(i/p1) -0.8*((i/p1)**2))
        Q.append(q2)
    
    matplotlib.pyplot.plot(Q,pwf)
    matplotlib.pyplot.xlabel("flow rate (STB/Day)")
    matplotlib.pyplot.ylabel("bottomhole flowing pressure (psi)")


#Composit IPR
if val == 4:
    p1 = float(input("Reservoir or static pressure(Pe) in psi"))
    p2 = float(input("Wellbore flowing Pressure(Pwf) in psi"))
    pb = float(input("Buuble point pressure in psi"))
    q = float(input("Flow rate when pressure is above Pb in STB/Day"))
    j = q/(p1-p2)
    pwf = []
    Q = []
    for i in range(0,int(p1),50):
        pwf.append(i)
        if i >= pb :
            q2 = j*(p1-i)
        else:
            q2 = j*(p1 - pb) + ((j*pb)/1.8) * (1 - 0.2*(i/pb) -0.8*((i/pb)**2))
        Q.append(q2)
    
    matplotlib.pyplot.plot(Q,pwf)
    matplotlib.pyplot.xlabel("flow rate (STB/Day)")
    matplotlib.pyplot.ylabel("bottomhole flowing pressure (psi)")