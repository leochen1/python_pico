from machine import Timer, Pin

led = Pin("LED", Pin.OUT)

def callback1(t):
    print("1")
    led.on()

def callback2(t):
    print("2")
    led.off()

def callback3(t):
    print("3")
    t.deinit()


time1 = Timer()
time1.init(freq=1, callback=callback1)

time2 = Timer()
time2.init(period=2000, callback=callback2)
    
time3 = Timer()
time3.init(period=2000, callback=callback3)







