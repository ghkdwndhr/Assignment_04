from gpiozero import LED; from time import sleep
l=[LED(i) for i in [8,7,16]]
while 1: [([x.off() for x in l],[l[j].on() for j in range(3) if i>>2-j&1],sleep(1)) for i in range(8)]
