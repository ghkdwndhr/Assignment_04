from gpiozero import LED, Button
from signal import pause

l=[LED(i) for i in [8,7,16,20]]; b=Button(25); s=[0]
def t(): [i.on() if not s[0] else i.off() for i in l]; s[0]^=1
b.when_pressed=t
pause()
