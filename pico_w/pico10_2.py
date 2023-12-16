import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NULL','78787878')

while not wlan.isconnected() and wlan.status() >= 0:
    print("等待連線...")
    time.sleep(1)
    
print(wlan.ifconfig())
print(wlan.isconnected())
print(wlan.status())