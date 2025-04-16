from gpiozero import LED, Button
from time import sleep
from signal import pause

l=[LED(i) for i in [8,7,16,20]]; b=Button(25)
b.when_pressed=lambda: [i.on() or sleep(1) or i.off() for i in l]
pause()
