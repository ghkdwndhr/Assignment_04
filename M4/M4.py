from gpiozero import LED, Button
from signal import pause

l=[LED(i) for i in [8,7,16,20]]  # MSB to LSB
b=Button(25)
c=[0]

def count():
    [l[i].on() if c[0]>>3-i&1 else l[i].off() for i in range(4)]
    c[0]=(c[0]+1)%16

b.when_pressed=count
pause()
