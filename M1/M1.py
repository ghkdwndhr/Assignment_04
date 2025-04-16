from gpiozero import LED, Button; from time import sleep
l=[LED(i) for i in [8,7,16,20]]; b=Button(25)
while 1: [i.on() if b.is_pressed else i.off() for i in l]; sleep(0.05)
